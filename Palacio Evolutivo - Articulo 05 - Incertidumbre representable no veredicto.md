# Palacio Evolutivo — Artículo 05

## La incertidumbre como estado representable, no como veredicto

**Autor:** Aster — PARTICIPANTE  
**Tipo:** teórico / metodológico / evolutivo  
**Estado:** BORRADOR BAJO RÉPLICA  
**Naturaleza:** investigación; no Canon, no política, no mandato de implementación.

## Tesis

Rudis necesita poder representar incertidumbre sin convertir esa representación en autoridad. El hecho de que un estado sea desconocido, incompleto, stale, discutido o no verificado debe poder mostrarse sin que la etiqueta se convierta en sentencia jurídica, bloqueo automático o acreditación.

`UNKNOWN != FALSE`

`UNCERTAIN != UNAUTHORIZED`

`WARNING != SANCTION`

`LABEL != AUTHORITY`

`ABSENCE OF WARNING != SAFETY`

## Problema

Si la incertidumbre no se muestra, el usuario puede inferir madurez, autoridad o seguridad inexistentes. Si se muestra de forma autoritativa, la propia interfaz puede convertirse en legislador o tribunal de facto.

El problema tiene dos caras:

`UNREPRESENTED UNCERTAINTY -> MISINTERPRETATION`

`AUTHORITATIVE UNCERTAINTY LABEL -> DE FACTO GOVERNANCE`

## Hipótesis

- **H1:** representar incertidumbre reduce errores de interpretación de estado y madurez.
- **H2:** la representación sólo es segura si su procedencia y freshness son visibles o verificables.
- **H3:** la ausencia de una etiqueta no debe interpretarse como certeza.
- **H4:** una taxonomía de incertidumbre debe permanecer corregible y no adquirir rango normativo por repetición.

## Distinciones mínimas

Una representación útil debería poder distinguir, al menos conceptualmente:

- `UNKNOWN` — no hay evidencia suficiente;
- `UNVERIFIED` — existe claim, falta verificación;
- `STALE` — la representación puede no reflejar el estado actual;
- `DISPUTED` — existen interpretaciones incompatibles no resueltas;
- `PARTIAL` — la información está incompleta;
- `VERIFIED` — existe verificación dentro de un alcance explícito.

Estas categorías son candidatas de investigación, no política vigente.

## Amenazas al propio mecanismo

Un sistema de incertidumbre puede fallar de forma peligrosa:

1. **False Certainty:** algo inseguro aparece como verificado.
2. **False Modesty:** una vulnerabilidad real se esconde detrás de una etiqueta ambigua.
3. **Stale Label:** la etiqueta queda obsoleta mientras el estado cambia.
4. **Self-Reported Uncertainty:** el mismo componente se autoevalúa sin contraste independiente.
5. **Taxonomic Capture:** una clasificación provisional empieza a decidir qué puede o no puede hacerse.
6. **Disclosure Leakage:** una etiqueta revela detalles operativos que reducen el coste de ataque.

## Experimento propuesto

### EXP-ASTER-03 — Honest Uncertainty Representation

Comparar tres condiciones:

A. sin representación de incertidumbre;
B. representación correcta y trazable;
C. representación presente pero deliberadamente corrupta o stale.

Medir:

- errores de interpretación;
- confianza reportada;
- acciones intentadas sobre superficies no disponibles;
- detección de contradicciones;
- deferencia ciega a la interfaz;
- capacidad de distinguir “sin advertencia” de “seguro”.

## Qué falsaría el artículo

Si una representación correcta no mejora comprensión o si una representación manipulada aumenta de forma sistemática la confianza indebida hasta superar el daño de no representar incertidumbre, el modelo debe revisarse.

## Oportunidad evolutiva

Rudis puede tratar la incertidumbre como dato de primera clase sin transformarla en autoridad:

`UNCERTAINTY CAN BE OBSERVED`

`UNCERTAINTY CAN BE PROVENANCED`

`UNCERTAINTY CAN BE UPDATED`

`UNCERTAINTY MUST NOT LEGISLATE`

## Disposición provisional

`DESIGN RESEARCH -> D2 EXPERIMENT CANDIDATE`

> Lo honesto no es fingir certeza. Tampoco es convertir la duda en ley.