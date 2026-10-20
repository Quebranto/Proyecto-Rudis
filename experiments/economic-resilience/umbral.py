#!/usr/bin/env python3
"""UMBRAL — comparación local de cotizaciones de remesas; no ejecuta pagos."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
import json

FIELDS = ("provider", "budget", "upfront_fee", "deducted_fee", "fx_rate",
          "recipient_fee", "reference_rate", "hours", "verified_at")

def number(value, field):
    try:
        x = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field}: no es un número válido")
    if not x.is_finite():
        raise ValueError(f"{field}: debe ser finito")
    return x

def calculate(row):
    missing = [k for k in FIELDS if not str(row.get(k, "")).strip()]
    if missing:
        raise ValueError("Faltan campos: " + ", ".join(missing))
    numbers = {k: number(row[k], k) for k in FIELDS if k not in ("provider", "verified_at")}
    b, u, d = (numbers[k] for k in ("budget", "upfront_fee", "deducted_fee"))
    fx, ref, fee = (numbers[k] for k in ("fx_rate", "reference_rate", "recipient_fee"))
    if b <= 0 or fx <= 0 or ref <= 0:
        raise ValueError("Presupuesto y tipos de cambio deben ser positivos")
    if min(u, d, fee, numbers["hours"]) < 0 or u + d > b:
        raise ValueError("Comisiones/plazo inválidos o superiores al presupuesto")
    net = (b - u - d) * fx - fee
    if net < 0:
        raise ValueError("Comisión del destinatario superior al importe")
    theoretical = b * ref
    return {"provider": row["provider"], "budget": b, "reference_rate": ref,
            "received": net, "cost_pct": 100 * (theoretical - net) / theoretical,
            "hours": numbers["hours"], "verified_at": row["verified_at"]}

def compare(path, max_hours=None):
    with open(path, newline="", encoding="utf-8-sig") as f:
        records = list(csv.DictReader(f))
    if not records:
        raise ValueError("CSV vacío")
    quotes = []
    for line, row in enumerate(records, 2):
        try:
            quotes.append(calculate(row))
        except ValueError as e:
            raise ValueError(f"Fila {line}: {e}") from e
    if len({q["budget"] for q in quotes}) != 1:
        raise ValueError("Los presupuestos deben ser idénticos")
    if len({q["reference_rate"] for q in quotes}) != 1:
        raise ValueError("El tipo de referencia debe ser idéntico")
    if max_hours is not None:
        quotes = [q for q in quotes if q["hours"] <= max_hours]
    return sorted(quotes, key=lambda x: x["received"], reverse=True)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv")
    p.add_argument("--max-hours")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    try:
        hours = number(args.max_hours, "max-hours") if args.max_hours else None
        if hours is not None and hours < 0:
            raise ValueError("El plazo no puede ser negativo")
        quotes = compare(args.csv, hours)
        if not quotes:
            raise ValueError("Sin cotizaciones válidas para ese plazo")
    except (OSError, ValueError) as e:
        p.error(str(e))
    rows = [{"provider": q["provider"], "net_received": str(q["received"].quantize(Decimal("0.01"))),
             "cost_pct": str(q["cost_pct"].quantize(Decimal("0.01"))),
             "hours": str(q["hours"]), "verified_at": q["verified_at"]} for q in quotes]
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        for row in rows:
            print(f'{row["provider"]}: neto={row["net_received"]}, coste={row["cost_pct"]}%, plazo={row["hours"]}h; fecha={row["verified_at"]}')
        if len(quotes) > 1:
            print(f'Brecha mejor-peor: {quotes[0]["received"]-quotes[-1]["received"]:.2f} unidades de moneda de destino')
        print("Aviso: datos suministrados por el usuario; verifica precios, licencias y seguridad antes de pagar.")

if __name__ == "__main__":
    main()
