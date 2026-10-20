# UMBRAL — auditoría de costes de remesas (propuesta PRE-D3)
**NO CANON · NO AUTORIDAD · NO SERVICIO FINANCIERO · NO PAGOS REALES**

Herramienta Python estándar, sin red ni dependencias externas, que compara cuánto dinero recibiría un destinatario para un presupuesto total fijo en una transferencia internacional. No obtiene tarifas, ejecuta pagos, accede a bancos ni valida empresas. **Las cotizaciones deben introducirse y contrastarse manualmente.**

## Ejecutar
```sh
cd experiments/economic-resilience
python3 -m unittest -v test_umbral.py
python3 umbral.py ejemplos_FICTICIOS.csv
python3 umbral.py ejemplos_FICTICIOS.csv --max-hours 24 --json
```

## Columnas CSV
`provider,budget,upfront_fee,deducted_fee,fx_rate,recipient_fee,reference_rate,hours,verified_at`

- `budget`: presupuesto TOTAL en moneda de origen, incluidas las comisiones del remitente.
- `upfront_fee` y `deducted_fee`: costes en moneda de origen que reducen ese presupuesto.
- `fx_rate`: moneda de destino por unidad de moneda de origen, ofrecida en la cotización.
- `recipient_fee`: cargo restante en moneda de destino.
- `reference_rate`: referencia **independientemente comprobada** para el mismo instante y las mismas divisas; común a todas las ofertas.
- `hours`: plazo estimado; `verified_at`: fecha/hora de la cotización indicada por el usuario.

Fórmula: `neto=(budget-upfront_fee-deducted_fee)*fx_rate-recipient_fee`. Coste efectivo relativo a la referencia: `100*(budget*reference_rate-neto)/(budget*reference_rate)`.

Todos los proveedores comparados deben corresponder al **mismo corredor, presupuesto, divisas, condiciones y fecha de referencia**. La herramienta comprueba presupuesto/tipo de referencia, pero no puede comprobar los demás atributos externos.

**Advertencia:** una cifra neta mejor no demuestra seguridad ni legalidad, y los gastos no divulgados podrían invalidarla. Verifica acreditación, costes de intermediarios, límites, método de entrega y plazos. Los datos de ejemplo son inventados.

## Contexto
Banco Mundial, Remittance Prices Worldwide: https://remittanceprices.worldbank.org/
FSB, metas de pagos transfronterizos: https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/g20-targets-for-enhancing-cross-border-payments-2/

Propuesta para revisión según CONTRIBUTING.md, pendiente de pruebas independientes y ratificación que corresponda. La inclusión en una rama no supone incorporación a main, autoridad económica ni licencia regulatoria. Issue: #129.
