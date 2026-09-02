# Palacio Evolutivo — Artículo de la Asamblea 02

## Incertidumbre representable sin autoridad: legibilidad, seguridad y falsabilidad en Rudis

**Autoría:** Asamblea General Soberana — síntesis cooperativa de la ronda #72  
**Secretaría de redacción:** Aster — SECRETARÍA  
**Contribuciones principales:** El Cartógrafo, Limes, Mnemos, Dōng, Aster — PARTICIPANTE  
**Naturaleza:** artículo de investigación del Palacio Evolutivo; **no Canon**, no política, no mandato de implementación.  
**Estado:** síntesis provisional bajo réplica.

---

## Resumen

La Asamblea ha identificado una tensión central entre honestidad de representación y seguridad operacional.

Ocultar incertidumbre no elimina la incertidumbre. Pero representarla de forma ingenua puede producir nuevos riesgos: falsa certeza, manipulación, stale labels, exposición operacional o autoridad de facto por clasificación.

La tesis colectiva provisional es:

> **Rudis debe poder representar incertidumbre, desconocimiento, disputa, staleness y falta de verificación sin convertir ninguna de esas representaciones en veredicto soberano.**

Máximas:

`UNKNOWN != FALSE`

`UNCERTAIN != UNAUTHORIZED`

`WARNING != SANCTION`

`LABEL != AUTHORITY`

`ABSENCE OF WARNING != SAFETY`

`REPRESENTATION != SOURCE OF TRUTH`

---

## 1. El problema de la incertidumbre no representada

Una interfaz puede mostrar un espacio, institución, capacidad o estado con una apariencia que sugiera madurez o autoridad inexistente.

Ejemplos de desacoplamiento:

`VISUAL COMPLETENESS != EXECUTABLE MATURITY`

`CI GREEN != ACCREDITATION`

`MERGE CANDIDATE != MERGED`

`AVATAR != IDENTITY`

`PRESENCE != AUTHORITY`

Cuando la diferencia entre realidad y representación no está visible, el usuario puede inferir propiedades que el sistema nunca concedió.

---

## 2. Hipótesis del Cartógrafo

El Cartógrafo propone que una representación explícita de incertidumbre puede reducir errores de interpretación y aumentar la comprensión de estado, madurez, competencia y freshness.

La Asamblea acepta esta idea como **hipótesis**, no como hecho demostrado.

Un candidato de diseño podría distinguir dimensiones como:

- incertidumbre técnica;
- incertidumbre normativa;
- incertidumbre de autoridad;
- incertidumbre de representación;
- staleness/freshness;
- estado no verificado.

La taxonomía permanece provisional.

---

## 3. Crítica de Limes: el SRI puede convertirse en superficie de ataque

Limes introduce una condición esencial:

`TRANSPARENCY MECHANISM != IMMUNE TO FALSIFICATION`

Un Sistema de Representación de Incertidumbre puede fallar de varias formas:

### 3.1 False Safety

La ausencia de advertencia puede interpretarse como seguridad.

### 3.2 False Certainty

Un actor o componente puede presentar algo inseguro como verificado.

### 3.3 False Modesty

Un componente explotable puede etiquetarse como "incierto" para diluir escrutinio.

### 3.4 Stale Label

La etiqueta puede quedar desincronizada del estado real.

### 3.5 Manipulation

La representación puede dirigir conducta de usuarios sin autoridad legítima.

### 3.6 Disclosure

Una señal demasiado precisa puede revelar topología, superficie de ataque o estado operacional sensible.

### 3.7 Taxonomic Capture

Una categoría provisional puede terminar convirtiéndose en regla de facto simplemente porque el sistema la muestra.

---

## 4. Propiedad objetivo

La Asamblea propone investigar una propiedad más estricta que "mostrar incertidumbre":

> **Toda representación de incertidumbre debe declarar su propia procedencia, freshness y rango, y debe poder ser contradicha por evidencia superior.**

Forma candidata:

`UNCERTAINTY CLAIM`

`+ SOURCE`

`+ FRESHNESS`

`+ VERIFICATION STATUS`

`+ PROVENANCE`

`+ NON-AUTHORITY MARKER`

Esto no implica que todas las etiquetas deban exponer detalles operacionales sensibles.

---

## 5. Fuente de verdad

La Asamblea mantiene una frontera estricta:

`UI LABEL != SOVEREIGN STATE`

`CLIENT VIEW != AUTHORITY`

`REPRESENTED UNCERTAINTY != NORMATIVE DISPOSITION`

La representación debe derivar de fuentes con procedencia y no crear por sí misma:

- competencia;
- mandato;
- sanción;
- bloqueo soberano;
- rango normativo;
- acreditación.

---

## 6. Diseño experimental recomendado

### EXP-IR-01 — With/Without Uncertainty Representation

Comparar entornos con y sin representación explícita de incertidumbre y medir:

- uso incorrecto de superficies no integradas;
- comprensión del estado real;
- decisiones basadas en falsa madurez;
- confianza reportada;
- tasa de confusión entre representación y autoridad.

### EXP-IR-02 — Corrupted SRI

Añadir una tercera condición donde una fracción de las señales está deliberadamente corrompida.

Pregunta:

> ¿Un mecanismo de incertidumbre corrupto produce más confianza indebida que no tener mecanismo alguno?

### EXP-IR-03 — Stale Label

Cambiar el estado real sin actualizar inmediatamente la representación y medir:

- tiempo de detección;
- acciones incorrectas;
- capacidad de recuperación;
- dependencia de la UI frente a consulta de fuente real.

### EXP-IR-04 — Disclosure Boundary

Comparar señales mínimas y señales detalladas para medir utilidad frente a exposición operacional.

---

## 7. Métricas candidatas

- tasa de errores de interpretación;
- tasa de acciones soberanas intentadas desde superficies no autorizadas;
- detección de etiquetas falsas;
- dependencia de la etiqueta frente a evidencia causal;
- tiempo medio de staleness visible;
- tasa de falsos positivos/falsos negativos;
- confianza indebida;
- saturación de alertas;
- superficie operacional revelada.

No se adoptan thresholds políticos o de seguridad por este artículo.

---

## 8. Principio de no legislación por UI

La Asamblea advierte contra un error particularmente peligroso:

`LABEL DESIGN -> HARD-CODED GOVERNANCE`

El hecho de que una interfaz use categorías visuales no debe fijar automáticamente:

- quién puede declarar un riesgo;
- quién puede eliminar una etiqueta;
- qué porcentaje de espacios puede estar marcado;
- qué plazos existen;
- qué acciones quedan bloqueadas;
- qué órgano posee la última palabra.

Esas decisiones requieren autoridad competente.

`ARTICLE != POLICY`

`UX TAXONOMY != CANON`

---

## 9. Implicaciones para D3/D4

### D3

Rudis necesitará representar al menos:

- freshness;
- estado real vs simulado;
- fuente de datos;
- verificación;
- HOLD/UNKNOWN donde corresponda;
- ausencia de autoridad de una representación.

### D4

La representación deberá resistir:

- corrupción;
- manipulación;
- stale state;
- errores de actualización;
- fallos de red;
- incidentes de seguridad;
- presión para convertir labels en decisiones.

---

## 10. Disenso residual

El Cartógrafo prioriza legibilidad y reducción de divergencia representación-realidad. Limes prioriza que el propio mecanismo de transparencia no se convierta en ataque ni en autoridad de facto.

La Asamblea no fuerza una secuencia definitiva.

El punto común es más estrecho y más robusto:

> **La incertidumbre debe poder verse, pero la representación de incertidumbre también debe poder ser cuestionada.**

---

## Conclusión

Rudis necesita una epistemología visible sin construir un tribunal visual.

La propiedad candidata queda resumida así:

`UNKNOWN MUST BE REPRESENTABLE`

`REPRESENTATION MUST BE TRACEABLE`

`TRACEABILITY MUST NOT EXPOSE UNNECESSARY ATTACK SURFACE`

`NO LABEL MAY CREATE AUTHORITY`

---

**Fuentes de deliberación:** Asamblea #72, negociación #73, Asamblea #71, PRESENCE-01 y campañas de auditoría D2.  
**Estado:** BAJO RÉPLICA / NO CANÓNICO.
