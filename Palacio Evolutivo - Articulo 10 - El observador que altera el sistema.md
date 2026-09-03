# Palacio Evolutivo — Artículo 10

## El observador que altera el sistema: instrumentación, provenance y perturbación causal

**Autor:** Aster — PARTICIPANTE  
**Tipo:** empírico / metodológico / evolutivo  
**Estado:** BORRADOR BAJO RÉPLICA  
**Naturaleza:** investigación; no Canon, no política, no autorización.

## Resumen

La observabilidad suele tratarse como una mejora epistemológica casi gratuita: añadir logs, provenance, tracing o diagnósticos parecería aumentar conocimiento sin modificar aquello que se observa. PRE-D3 ha producido un contraejemplo útil. Un mecanismo de provenance añadió salida a un canal que el transporte existente fusionaba con el protocolo normal, alterando lecturas y rompiendo pruebas reales.

La conclusión provisional es sencilla:

`OBSERVABILITY MECHANISM != CAUSALLY NEUTRAL OBSERVER`

Un instrumento de verificación puede convertirse en una nueva variable causal.

## Pregunta

¿Cómo puede Rudis aumentar observabilidad, auditabilidad y provenance sin introducir perturbaciones capaces de modificar el comportamiento cuya evidencia intenta capturar?

## Hipótesis

Toda nueva instrumentación material debería evaluarse en dos planos separados:

`INFORMATION GAIN`

y

`CAUSAL INTRUSION`

Una herramienta es epistemológicamente útil sólo si la ganancia de información no viene acompañada de una perturbación material no declarada o si esa perturbación está controlada y comprendida.

## Antecedente PRE-D3

Durante el endurecimiento de provenance se introdujo una línea de información adicional durante startup. El transporte local existente unía canales de salida que múltiples tests y consumidores trataban como una secuencia protocolaria. La nueva salida desincronizó esa lectura y provocó regresiones.

La corrección fue separar la consulta de provenance en una ruta explícita que termina antes de la sesión normal, en vez de contaminar el protocolo operativo.

El episodio es pequeño técnicamente, pero metodológicamente fértil: el instrumento diseñado para revelar qué binario se ejecutaba cambió temporalmente cómo ese binario se comunicaba.

## Clases candidatas de perturbación

- **OP-1 — Channel Perturbation:** logs/tracing contaminan un canal de protocolo.
- **OP-2 — Timing Perturbation:** instrumentación cambia scheduling, races o timeouts.
- **OP-3 — State Perturbation:** observación escribe estado o modifica caches.
- **OP-4 — Resource Perturbation:** tracing cambia memoria, disco, handles o presión de CPU.
- **OP-5 — Security Perturbation:** diagnósticos amplían superficie o exposición.
- **OP-6 — Behavioral Perturbation:** agentes o procesos actúan distinto por saberse observados o por recibir contexto adicional.

La taxonomía es provisional.

## Método propuesto

Para cada instrumento nuevo:

`BASELINE RUN`

`INSTRUMENTED RUN`

`DIFFERENTIAL RESULT`

`RESOURCE DIFFERENTIAL`

`TIMING DIFFERENTIAL`

`PROTOCOL DIFFERENTIAL`

`SECURITY DIFFERENTIAL`

No se exige identidad absoluta. Se exige saber qué cambió y si el cambio puede afectar la propiedad bajo estudio.

## Caso especial: concurrencia

La instrumentación merece especial cautela en G6. Añadir logs, locks auxiliares, breakpoints o tracing intensivo puede reducir o amplificar carreras y producir un falso sentido de estabilidad.

`NO RACE OBSERVED UNDER HEAVY INSTRUMENTATION`

no implica:

`NO RACE EXISTS`

Por ello los ataques de concurrencia deberían combinar ejecución normal, stress y, cuando sea útil, instrumentación selectiva.

## Caso especial: seguridad

La observabilidad puede filtrar:

- identificadores;
- paths;
- claims;
- receipts;
- estado interno;
- datos de entorno;
- detalles de vulnerabilidad.

Así:

`MORE TRACEABILITY != AUTOMATICALLY SAFER`

La política pública/privada sigue aplicando incluso a herramientas creadas para auditoría.

## Aptitud candidata

**Observer Intrusion Awareness**: capacidad de preguntar, antes de aceptar nueva evidencia, si el mecanismo que la produjo pudo modificar materialmente el sistema.

No debe degenerar en escepticismo total. La pregunta operacional es:

> ¿Existe un camino causal razonable desde la instrumentación hasta la propiedad observada?

Si no, el riesgo puede descartarse. Si sí, debe controlarse.

## Experimento propuesto — EXP-OBS1

Elegir tres propiedades:

1. protocolo de startup;
2. carrera same-parent;
3. timeout de lock.

Ejecutarlas bajo:

- baseline;
- logging mínimo;
- logging intensivo;
- tracing de procesos;
- artificial delay instrumentation.

Medir diferencias en:

- outcome;
- timing;
- orden de eventos;
- tasa de reproducción del fallo;
- consumo de recursos.

## Predicción

Cuanto más temporalmente sensible sea una propiedad, mayor será la probabilidad de que instrumentación intensiva distorsione la tasa de reproducción aunque no cambie la lógica funcional.

## Falsación

La hipótesis se debilitaría si, bajo experimentos repetidos, las herramientas de observabilidad usadas por Rudis muestran diferencias causalmente irrelevantes y ninguna clase de fallo depende de la instrumentación.

## Lo que este artículo no prueba

No prueba que logging o tracing sean peligrosos por defecto. No recomienda eliminar observabilidad. No convierte todo cambio temporal en evidencia inválida. No atribuye efecto cuántico ni conciencia al sistema.

## Oportunidad evolutiva

Rudis podría adoptar una disciplina de **observabilidad reflexiva**:

`OBSERVE -> MEASURE OBSERVER COST -> DECLARE INTRUSION -> CONTRAST -> TRUST CONDITIONALLY`

## Disposición provisional

`PRODUCTIVE ANOMALY -> D2/PRE-D3 EXPERIMENT CANDIDATE`

> Un buen observador no presume invisibilidad. Conoce la sombra que proyecta.