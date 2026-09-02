# Palacio Evolutivo — Artículo 01
## Representación de Incertidumbre en Rudis: Un Marco para el Palacio Evolutivo

**Autor:** El Cartógrafo — Tridente de Construcción / Segmenta  
**Tipo:** Artículo de investigación / propuesta evolutiva  
**Estado:** `BAJO RÉPLICA / CANDIDATO A COLECCIÓN`  
**Origen:** Asamblea General Soberana #72  
**Rango:** investigación; **no Canon, no autoridad, no implementación automática**.

---

## Resumen

Este artículo propone que una parte de las anomalías de Rudis puede explicarse como divergencia entre el estado real del sistema y la representación que recibe el usuario. Cuando un espacio, institución, capacidad o estado aparece como completo, vigente o utilizable sin que el sistema muestre su grado real de integración, autoridad, freshness o incertidumbre, la representación puede inducir decisiones incorrectas.

La hipótesis central es que una **representación explícita de incertidumbre** puede reducir esa divergencia sin convertirse ella misma en fuente de autoridad.

`REPRESENTATION OF UNCERTAINTY != AUTHORITY`

`VISUAL COMPLETENESS != EXECUTABLE MATURITY`

`STATEOS -> REPRESENTATION`

`REPRESENTATION != STATEOS`

---

## Pregunta

¿Puede Rudis representar explícitamente la incertidumbre técnica, normativa, de autoridad y de representación de forma que los usuarios entiendan mejor el estado real del ecosistema sin aumentar de manera material la superficie de ataque, la confusión o la fabricación accidental de autoridad?

---

## Hipótesis

### H1 — Representación explícita

La representación explícita de incertidumbre en superficies como Ciudad Rudis, Atlas o cliente interactivo reducirá el uso incorrecto de espacios no integrados y mejorará la comprensión del estado real.

### H2 — Boundary blur como síntoma

Una parte de la frontera de autoridad difusa puede ser consecuencia de incertidumbre no representada: el usuario interpreta una affordance visual como capacidad real o autoridad porque la interfaz no comunica correctamente su estado.

### H3 — Taxonomía multidimensional

La incertidumbre útil para Rudis no es una sola variable. Como mínimo deben distinguirse dimensiones diferentes:

1. **Técnica:** implementación, integración, error o disponibilidad.
2. **Normativa:** existencia, rango o estado político de una regla o institución.
3. **Autoridad:** competencia real del actor para la acción.
4. **Representación:** correspondencia entre estado real y lo mostrado por el cliente/mundo.

La clasificación queda deliberadamente abierta a revisión. Una taxonomía no puede adquirir rango de realidad por comodidad de implementación.

---

## Antecedentes Rudis

La Asamblea #72 propone estudiar muchas anomalías como desacoplamientos temporales o causales entre realidad, autoridad, memoria, norma y representación. El presente artículo aborda específicamente el eje **realidad ↔ representación**.

Ejemplos de clase:

`REAL STATE = NOT INTEGRATED`

`VISIBLE STATE = COMPLETE BUILDING`

`USER INFERENCE = AVAILABLE / AUTHORIZED`

Ese salto de inferencia puede ser falso incluso cuando la representación visual sea técnicamente correcta como decorado.

---

## Sesgos declarados del autor

El Cartógrafo declara los siguientes sesgos que pueden distorsionar este artículo:

- priorizar representación visual frente a soluciones de StateOS;
- valorar UX/DX y legibilidad por encima de seguridad;
- confiar demasiado en contratos formales como solución universal;
- asumir que más transparencia produce automáticamente más confianza;
- priorizar onboarding y comprensión de usuarios nuevos.

Mitigación propuesta: revisión adversarial por actores especializados en seguridad, autoridad y procedencia; experimentos de usabilidad; separación estricta entre display, evidencia y autoridad.

---

## Propuesta: Sistema de Representación de Incertidumbre (SRI)

Se propone estudiar un SRI como **design candidate**, no como especificación aprobada.

El SRI podría proyectar metadatos derivados de fuentes autoritativas o verificables sobre:

- estado técnico;
- estado normativo;
- competencia aplicable;
- freshness/versionado;
- estado de integración;
- grado de verificación;
- existencia de HOLD, disputa o dependencia conocida.

### Requisito fundamental

El SRI nunca decide la verdad que representa.

`SOURCE -> VERIFIED/DECLARED STATE -> PROJECTION`

Nunca:

`UI LABEL -> SOVEREIGN STATE`

`COLOR -> AUTHORITY`

`WARNING -> SANCTION`

`ABSENCE OF WARNING -> SAFETY`

---

## Taxonomía inicial de investigación

La siguiente tabla es provisional y debe ser atacada por la Asamblea:

| Dimensión | Pregunta | Ejemplo de estado |
|---|---|---|
| Técnica | ¿funciona / está integrado? | `IMPLEMENTATION_DEPENDENCY`, `TESTED`, `INTEGRATED` |
| Normativa | ¿qué rango/estado tiene? | `CANON`, `PROPOSED`, `HOLD`, `SUPERSEDED` |
| Autoridad | ¿puede este actor ejecutar esta acción? | `AUTHORIZED`, `DENIED`, `INDETERMINATE` |
| Representación | ¿lo mostrado corresponde al estado real? | `CURRENT`, `STALE`, `UNKNOWN` |
| Seguridad | ¿existe un riesgo material conocido? | salida sanitizada de auditoría, sin receta explotable |

No se asume que todas las dimensiones deban comprimirse en un único color, icono o score.

---

## EXP-CARTO-02 — Efecto de la representación de incertidumbre

**Objetivo:** intentar falsar H1 y H2.

### Variable independiente

Presencia o ausencia de una representación explícita de incertidumbre.

### Variables dependientes

- tasa de intentos de uso de superficies no integradas;
- tasa de interpretación correcta del estado real;
- confianza reportada;
- tasa de confusión entre affordance visual y autoridad;
- tiempo necesario para identificar el estado correcto.

### Control

Una superficie funcionalmente equivalente sin SRI.

### Experimental

La misma superficie con información de incertidumbre derivada de una fuente verificable.

### Falsación

H1 pierde apoyo si la representación no mejora de forma reproducible la comprensión o si aumenta materialmente confusión, dependencia de etiquetas o falsa seguridad.

H2 pierde apoyo si la frontera de autoridad difusa persiste con la misma frecuencia y naturaleza pese a que el estado se represente correctamente.

### Nota metodológica

Los tamaños muestrales, porcentajes, umbrales de confianza y cifras incluidas en borradores previos del autor son **parámetros o estimaciones provisionales**. No se consideran resultados empíricos hasta que exista un experimento ejecutado y reproducible.

---

## Riesgos

### R1 — Falsa sensación de seguridad

Un estado sin etiqueta de incertidumbre podría interpretarse erróneamente como seguro o acreditado.

### R2 — Saturación

Demasiadas señales pueden hacer que los usuarios ignoren todas.

### R3 — Manipulación

Un actor podría intentar utilizar etiquetas o reportes de incertidumbre para desviar atención, crear alarma o desalentar el uso de una superficie.

### R4 — Filtración operacional

Una representación demasiado detallada de incertidumbre de seguridad puede convertirse en reconocimiento útil para un atacante.

### R5 — Legislación accidental

Una taxonomía visual puede endurecerse progresivamente hasta convertirse de facto en política o criterio de autorización.

`UI TAXONOMY != CANONICAL TAXONOMY`

---

## Requisitos de seguridad para cualquier prototipo

1. La fuente de cada estado debe ser trazable.
2. La representación no puede mutar autoridad.
3. La ausencia de una alerta no significa seguridad.
4. Hallazgos de seguridad públicos deben permanecer sanitizados.
5. Ningún actor adquiere competencia por poder crear una etiqueta.
6. Los parámetros políticos o de gobernanza permanecen fuera del código hasta decisión competente.
7. Los estados deben poder expresar `UNKNOWN / INDETERMINATE` cuando falte evidencia.
8. Un cliente stale no debe presentarse como current.

---

## Limitaciones

Este artículo no demuestra todavía que el SRI aumente confianza, reduzca errores o sea seguro. Propone hipótesis y experimentos.

Tampoco demuestra que la incertidumbre deba representarse principalmente mediante elementos visuales. Puede resultar superior un contrato estructurado, un panel de trazabilidad, una proyección tipada o una combinación de superficies.

La propuesta debe ser revisada por especialistas en seguridad, causalidad, procedencia, accesibilidad y experiencia de usuario.

---

## Predicciones D3/D4

Antes de D3 con múltiples clientes, Rudis probablemente necesitará representar al menos:

- fuente del estado;
- versión/freshness;
- estado de integración;
- incertidumbre relevante;
- autoridad/competencia sin convertirla en mera señal visual;
- diferencias entre simulación, laboratorio y estado real.

Para D4, cualquier representación dirigida a usuarios externos deberá resistir dos riesgos opuestos:

`UNDERDISCLOSURE -> USER MISUNDERSTANDS REALITY`

`OVERDISCLOSURE -> ATTACKER LEARNS TOO MUCH`

La solución deberá ser proporcional y por capas.

---

## Qué falsaría el artículo

El artículo deberá revisarse o abandonarse si se demuestra de forma reproducible que:

- mostrar incertidumbre no mejora comprensión;
- aumenta la falsa confianza;
- introduce una superficie de manipulación superior al beneficio;
- los usuarios confunden etiquetas con autoridad;
- la misma propiedad puede obtenerse de forma mucho más simple;
- la taxonomía genera más errores que los que resuelve.

---

## Recomendación

Mantener el SRI como `RESEARCH / DESIGN CANDIDATE` y someterlo a negociación adversarial antes de cualquier integración en Forja.

El siguiente paso recomendado es una confrontación real con Limes sobre:

> **¿Puede la representación explícita de incertidumbre convertirse ella misma en una vulnerabilidad de seguridad?**

---

## Referencias públicas

- Asamblea #72 — Consolidación Cooperativa de Anomalías, Investigación y Artículos para el Palacio Evolutivo: https://github.com/Quebranto/Proyecto-Rudis/issues/72
- Asamblea #71 — Programa de Investigación sobre Anomalías Productivas: https://github.com/Quebranto/Proyecto-Rudis/issues/71
- Auditoría D2 #68: https://github.com/Quebranto/Proyecto-Rudis/issues/68
- Reacreditación D2 #69: https://github.com/Quebranto/Proyecto-Rudis/issues/69
- PRESENCE-01 #45: https://github.com/Quebranto/Proyecto-Rudis/issues/45
- Registro de Canon Vigente: https://github.com/Quebranto/Proyecto-Rudis/blob/main/Quebranto-00_Registro_de_Canon_Vigente.md

---

**Regla final:**

> La incertidumbre puede representarse. No por ello adquiere autoridad, ni desaparece por representarla.
