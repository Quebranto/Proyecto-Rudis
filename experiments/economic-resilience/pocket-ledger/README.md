# Rudis Pocket Ledger — portable offline prototype

**Propuesta técnica no canónica. Sin red, sin cuenta, sin API, sin pagos y sin datos de terceros.**

Pequeña herramienta que una persona puede descargar y ejecutar fuera de ChatGPT, incluso sin conexión a internet. Permite calcular ingresos, gastos y saldo por categoría a partir de un archivo CSV **local**.

## Uso

```sh
cd experiments/economic-resilience/pocket-ledger
python3 -m unittest -v test_pocket_ledger.py
python3 pocket_ledger.py example_SYNTHETIC.csv
```

El archivo CSV debe tener las columnas exactas `date,category,income,expense,note`. Los importes deben estar en **una única moneda** y usar punto decimal. La herramienta no valida fechas, no convierte divisas, no calcula impuestos, no verifica transacciones ni protege por sí sola los ficheros que el usuario guarde en su dispositivo. **No introducir datos sensibles de terceros sin autorización.**

Este prototipo es para pruebas y educación económica, no para contabilidad legal ni para decisiones crediticias. Los ejemplos son ficticios. No se ha desplegado en comunidades africanas, no hay usuarios reales acreditados ni impacto económico medido.

Para un piloto futuro: traducciones y revisión por participantes locales, análisis de accesibilidad, empaquetado para smartphones de gama baja, controles de privacidad y seguridad, verificación independiente y consentimiento. `CAPABILITY != AUTHORITY`. No integrar en `main` sin revisión.
