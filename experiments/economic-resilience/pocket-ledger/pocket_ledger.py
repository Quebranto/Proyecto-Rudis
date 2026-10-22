#!/usr/bin/env python3
"""Rudis Pocket Ledger: local, offline, privacy-preserving income/cost ledger."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

FIELDS = ("date", "category", "income", "expense", "note")

def money(value):
    try:
        x = Decimal(value)
    except (InvalidOperation, TypeError):
        raise ValueError("invalid amount")
    if not x.is_finite() or x < 0 or x.as_tuple().exponent < -2:
        raise ValueError("amount must be nonnegative, finite and <=2 decimals")
    return x

def summarize(path):
    totals = {}
    with Path(path).open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != list(FIELDS):
            raise ValueError("invalid CSV columns")
        for line, row in enumerate(reader, 2):
            if not row["date"] or not row["category"]:
                raise ValueError(f"line {line}: missing date/category")
            inc, exp = money(row["income"]), money(row["expense"])
            if inc and exp:
                raise ValueError(f"line {line}: income and expense cannot both be positive")
            bucket = totals.setdefault(row["category"], [Decimal("0"), Decimal("0")])
            bucket[0] += inc
            bucket[1] += exp
    return {k: {"income": str(v[0]), "expense": str(v[1]), "net": str(v[0]-v[1])}
            for k, v in sorted(totals.items())}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv", help="local CSV ledger, never uploaded")
    args = p.parse_args()
    try:
        results = summarize(args.csv)
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    for category, values in results.items():
        print(f'{category}: income={values["income"]}, expense={values["expense"]}, net={values["net"]}')
    print("OFFLINE / LOCAL ONLY. No financial advice, transactions or data transmission.")

if __name__ == "__main__":
    main()
