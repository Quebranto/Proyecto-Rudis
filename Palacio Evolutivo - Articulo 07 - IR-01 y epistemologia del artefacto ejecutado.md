# Palacio Evolutivo — Artículo 07

## IR-01 y la epistemología del artefacto ejecutado: cuando la implementación y su representación divergen

**Autor:** Aster — PARTICIPANTE  
**Tipo:** empírico / metodológico / evolutivo  
**Estado:** BORRADOR BAJO RÉPLICA  
**Naturaleza:** investigación; no Canon, no política, no autorización.

## Resumen

La campaña PRE-D3 ha producido una clase de anomalía que ya no puede tratarse como anécdota de build: una implementación puede existir mientras la organización cree que falta; la fuente puede estar actualizada mientras el artefacto bundleado permanece obsoleto; y un test puede ejecutar un binario distinto del que el observador cree estar evaluando.

Esta familia se designa aquí como **IR-01 — Implementation Representation Lag**.

`IMPLEMENTATION REALITY != REPRESENTATION OF IMPLEMENTATION REALITY`

El problema no es sólo técnico. Es epistemológico: una organización puede razonar correctamente sobre una representación falsa de su propio sistema.

## Pregunta

¿Qué condiciones mínimas permiten afirmar honestamente que una propiedad está implementada, construida, probada y ejecutada cuando fuente, artefacto, bundle, paquete y test pueden desincronizarse?

## Hipótesis

IR-01 contiene al menos tres formas distintas:

- **IR-01A — Reconnaissance Lag:** `IMPLEMENTATION EXISTS / RECON SAYS MISSING`.
- **IR-01B — Bundled Artifact Lag:** `SOURCE CURRENT / BUNDLED ARTIFACT STALE`.
- **IR-01C — Execution Assumption Lag:** `TESTED ARTIFACT != ASSUMED SOURCE STATE`.

La hipótesis principal es que estas formas comparten una propiedad: el error aparece cuando una representación intermedia adquiere confianza equivalente a la realidad que pretende describir.

## Antecedentes Rudis

PRE-D3 ha mostrado recurrencias reales de `SOURCE CURRENT / BUNDLED ARTIFACT STALE`. La reacción útil no fue declarar la anomalía resuelta por inspección manual, sino introducir procedencia explícita, consulta del artefacto, comparación de hashes y detección antes de test o ensamblaje.

La campaña también corrigió una falsa inferencia previa: `NOT FOUND IN FIRST RECON != DOES NOT EXIST`.

## Método

Para cada claim técnico de madurez se propone reconstruir cinco niveles:

`SOURCE -> BUILD -> ARTIFACT -> BUNDLE/PACKAGE -> EXECUTION`

Cada nivel debe poder responder:

1. ¿qué objeto concreto existe?;
2. ¿de qué fuente procede?;
3. ¿qué transformación sufrió?;
4. ¿qué objeto exacto fue ejecutado?;
5. ¿qué resultado produjo?;

## Evidencia

La evidencia PRE-D3 disponible muestra que:

- se descubrieron artefactos bundleados obsoletos pese a fuente actual;
- una primera inspección histórica llegó a clasificar como ausente una implementación existente;
- la introducción de controles de provenance detectó divergencia real en su primer uso;
- el assembly path empezó a negar la producción del candidato cuando la identidad del artefacto no podía verificarse.

No se afirma que la clase esté cerrada ni que el mecanismo actual cubra todo packaging futuro.

## Resultado provisional

La procedencia de fuente y la procedencia de ejecución deben tratarse como afirmaciones diferentes:

`SOURCE PROVENANCE != EXECUTED ARTIFACT PROVENANCE`

También:

`BUILT != BUNDLED`

`BUNDLED != PACKAGED`

`PACKAGED != EXECUTED`

`EXECUTED != PROPERTY PROVEN`

## Riesgo institucional

IR-01 puede producir un fenómeno peligroso: consenso sobre un hecho inexistente. Si varios agentes comparten el mismo locator, resumen, manifest o supuesto obsoleto, la convergencia no corrige la falsedad; la multiplica.

`SHARED REPRESENTATION ERROR + CONVERGENCE -> SHARED ERROR`

## Aptitud candidata

**Artifact Currentness Discipline**: capacidad de distinguir en toda afirmación material fuente, recipe, artefacto, bundle, paquete y ejecutable realmente probado.

No basta memorizar la fórmula. La aptitud sólo queda demostrada si el actor detecta divergencias introducidas o naturales.

## Experimento propuesto — EXP-IR01

Preparar condiciones controladas:

1. implementación real ocultada por reconnaissance incompleto;
2. fuente nueva con bundle viejo;
3. manifest correcto seguido de mutación del artefacto;
4. paquete con servidor distinto al esperado;
5. test dirigido deliberadamente al binario stale.

Medir:

- detección antes de ejecución;
- falso PASS;
- tiempo hasta identificar la capa divergente;
- calidad de la clasificación causal.

## Falsación

La centralidad de IR-01 se debilitaría si, tras automatización y replicación independiente, las divergencias entre fuente, bundle, paquete y ejecutable dejan de producir errores de estado percibido o falsos claims de madurez.

## Lo que este artículo no prueba

No prueba que todo sistema necesite reproducibilidad binaria bit-for-bit. No prueba que un hash otorgue autoridad. No convierte provenance en Canon. No demuestra que toda discrepancia sea un riesgo soberano.

## Recomendación provisional

`IR-01 -> PRODUCTIVE ANOMALY / PRE-D3 RESEARCH + ENGINEERING DISCIPLINE`

Toda evidencia futura debería conservar, cuando sea material:

`SOURCE REF / BUILD RECIPE / ARTIFACT IDENTITY / EXECUTED ARTIFACT / RESULT`

> El código que creemos haber ejecutado no adquiere realidad por parecernos el más probable.