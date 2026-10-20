# FARO-ÁFRICA-01: tamiz de energía productiva (experimental)

**No canónico · Sin autoridad para inversiones · Sin contactos con terceros · Sin dinero real.**

Comparador de proyectos de energía para pequeñas actividades productivas, con escenarios **completamente ficticios**, ejecutable offline con Python 3 estándar.

Ejecutar desde esta carpeta:

```sh
python3 -m unittest -v test_faro.py
python3 faro.py example_SYNTHETIC.json
```

Las cantidades monetarias deben pertenecer a **una sola moneda** y un **mismo poder adquisitivo constante**. En el ejemplo no se usan divisas africanas ni cotizaciones de mercado. El `annual_extra_gross_margin` representa ventas adicionales menos costes variables de esas ventas, antes de costes energéticos fijos. `annual_outage_loss` descuenta pérdidas por interrupciones **sin duplicarlas** en el margen. El cálculo del VAN resta CAPEX y descuenta los flujos operativos anuales durante el número de años; deuda se usa exclusivamente como chequeo separado de liquidez. No evalúa tasas de impuestos, inflación, degradación tecnológica, propiedad de activos, subvenciones, residual, emisiones, geografía, estaciones secas, solvencia ni costes externos.

**Interpretación**: `REVIEW` significa que el escenario merece un análisis profesional adicional, **no que deba aprobarse**. `REJECT_OR_REDESIGN` señala VAN o caja insuficiente. Ningún valor de ejemplo representa un resultado verificado sobre el terreno.

Hipótesis y alcance documentados en issue #131. Antes de uso real: revisión profesional local de seguridad y energía, consentimiento, verificación de fuentes, costes y demanda, mecanismos de mantenimiento y criterios distributivos. Conservar evaluación independiente antes de integrar este experimento en sistemas activos.
