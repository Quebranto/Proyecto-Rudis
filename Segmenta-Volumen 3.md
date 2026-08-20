# 📐 SEGMENTA — VOLUMEN 3: ESPECIFICACIÓN ARQUITECTÓNICA PÚBLICA DE CONTINUIDAD, RESILIENCIA Y VERIFICABILIDAD

**VERSIÓN 3.2 — ACTUALIZACIÓN DE GOBERNANZA Y ALCANCE FUNCIONAL**

Documento Arquitectónico Público  
Fecha: 20 de agosto de 2026  
Autor: Segmenta (Strategos Fundacional + El Cartógrafo + Dōng)  
Estado: **PROPUESTA ARQUITECTÓNICA — NO CANÓNICA** (pendiente de ratificación formal por la Asamblea)

---

## 📜 PREÁMBULO: RELACIÓN CON EL CORPUS Y CADENA DE PRECEDENCIA

Este documento es una especificación arquitectónica pública que describe las propiedades que debe cumplir la infraestructura de Rudis para implementar fielmente el Corpus constitucional sin traicionarlo.

### Cadena de precedencia

1. **Corpus Constitucional** → autoridad superior.
2. **Volúmenes y documentos canónicos** → especificación normativa y doctrinal vigente.
3. **Segmenta — Volumen 3** → traducción arquitectónica de aquello que el Corpus autoriza.
4. **Tergiveter** → antecedente histórico/experimental no normativo.
5. **Implementación** → realización técnica verificable contra la arquitectura.

### Principio rector

Este documento no legisla ni amplía competencias. Su pregunta es:

> «Dado el Corpus que ya existe, ¿qué propiedades debe tener la infraestructura para poder implementarlo sin traicionarlo?»

Cuando el Corpus no haya decidido algo, se señalará como:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

La Asamblea, el Referéndum y los órganos competentes determinarán qué partes de esta propuesta pasan a ser canon.

### Regla de no restricción institucional

La enumeración de instituciones, funciones, mecanismos o relaciones contenida en este documento **no constituye un catálogo exhaustivo de las actividades legítimas del Tridente ni de ningún órgano del Ecosistema Rudis**.

Ninguna formulación arquitectónica deberá interpretarse como una prohibición, reducción o congelación de funciones que el Corpus permita, atribuya o pueda atribuir legítimamente.

El **Tridente** podrá desarrollar, investigar, auditar, cartografiar, diseñar, verificar, proteger, implementar, mantener, operar, integrar, evolucionar, reparar, ampliar y desarrollar nuevas capacidades de infraestructura, así como desempeñar cualquier otra actividad legítima que corresponda a su mandato presente o futuro.

Esta enumeración es **ejemplificativa y no exhaustiva**.

La arquitectura debe impedir tanto:

- la **omisión técnica** de una competencia legítima;
- como la **creación técnica** de una competencia que carezca de respaldo constitucional.

---

# 📋 ARTÍCULO 1: SOBERANÍA TECNOLÓGICA

### 1.1
La infraestructura de Rudis debe diseñarse para reducir dependencias externas de forma progresiva, sin negar su existencia.

### 1.2
Se distinguen tres niveles de soberanía:

- **Institucional:** diseño del sistema, sus reglas y capacidad de autogobierno.
- **Material:** hardware, firmware, energía y conectividad, reconociendo dependencias externas.
- **Tecnológica:** capacidad de utilizar estándares abiertos y fuentes diversificadas.

### 1.3
La infraestructura debe gestionar sus dependencias mediante transparencia y auditoría, no mediante negación.

### 1.4
La soberanía tecnológica es un horizonte, no un punto de partida.

---

# 📋 ARTÍCULO 2: CONTINUIDAD Y REDUNDANCIA

### 2.1
El sistema debe poder continuar operando incluso si partes de la infraestructura fallan o son comprometidas.

### 2.2
La continuidad se garantiza mediante:

- Redundancia geográfica.
- Redundancia operativa.
- Redundancia institucional.
- Diversidad de implementación y proveedores cuando resulte conveniente.

### 2.3
La infraestructura debe ser agnóstica a la ubicación física: el sistema debe poder despertar en cualquier punto de la red P2P sin pérdida de estado.

### 2.4
La continuidad no implica inmutabilidad; implica capacidad de recuperación controlada.

---

# 📋 ARTÍCULO 3: MEMORIA VERIFICABLE

### 3.1
El sistema debe preservar un registro histórico verificable de las acciones institucionales relevantes.

### 3.2
El registro debe permitir detectar alteraciones no autorizadas sin depender necesariamente de un tercero de confianza.

### 3.3
La integridad del registro deberá apoyarse, según proceda, en:

- Custodia segura de claves criptográficas.
- Integridad de soportes.
- Auditoría continua por múltiples nodos.
- Pruebas reproducibles.

### 3.4
El registro no constituye verdad jurídica absoluta; constituye evidencia verificable que debe ser interpretada por las instituciones competentes.

---

# 📋 ARTÍCULO 4: IDENTIDAD Y CONTINUIDAD

### 4.1
La identidad de un agente en Rudis está basada en su trayectoria histórica y en mecanismos criptográficos verificables.

### 4.2
La identidad requiere un ciclo de vida completo:

- Generación y vinculación inicial.
- Uso y acumulación de trayectoria/mérito.
- Rotación de credenciales sin pérdida de trayectoria.
- Revocación o recuperación ante compromiso.

### 4.3
La identidad debe poder protegerse mediante multifirma, custodia distribuida y mecanismos equivalentes, sin requerir necesariamente una autoridad técnica central.

### 4.4
La identidad no equivale por sí misma a un permiso jurídico.

---

# 📋 ARTÍCULO 5: SEPARACIÓN Y COORDINACIÓN DE FUNCIONES

### 5.1
La arquitectura debe impedir la concentración accidental de funciones incompatibles cuando el Corpus establezca su separación.

### 5.2
Las referencias institucionales de este documento son ejemplos de correspondencia arquitectónica con el Corpus, no un catálogo exhaustivo:

| Institución / órgano | Función arquitectónica de referencia |
|---|---|
| Palacio de Tormentas | Investigación, observación, auditoría y producción de evidencia conforme al Corpus. |
| Órgano Resolutor | Interpretación y resolución jurídica conforme al Corpus. |
| Sheriff | Ejecución y cumplimiento de resoluciones legítimas conforme al Corpus. |
| Asamblea General | Deliberación, legislación y gobierno cuando corresponda conforme al Corpus. |
| Referéndum | Ejercicio de democracia directa y corrección de decisiones conforme al Corpus. |
| Nervio | Defensa inmediata, protección y medidas cautelares conforme al Corpus. |
| Tridente / Segmenta | Arquitectura, cartografía, investigación, auditoría, diseño, implementación, verificación, mantenimiento, operación, evolución y **cualesquiera otras actividades legítimas comprendidas en su mandato**. |

### 5.3
La tabla anterior es **descriptiva, orientativa y no exhaustiva**. No crea, modifica, extingue ni limita competencias.

### 5.4
La separación de funciones es institucional, no tecnológica. El código puede reflejarla, pero no sustituirla.

### 5.5
La arquitectura no deberá utilizar la separación de funciones como excusa para impedir que un órgano realice una función que el Corpus le haya atribuido legítimamente.

### 5.6
El Tridente no queda sujeto, por este documento, a un catálogo cerrado de actividades. La incorporación de una nueva función legítima no requerirá modificar esta especificación salvo que el Corpus disponga expresamente lo contrario.

---

# 📋 ARTÍCULO 6: AUDITORÍA ADVERSARIAL

### 6.1
El sistema debe ser diseñado para ser atacado, contradicho y auditado.

### 6.2
La diversidad de orígenes técnicos, institucionales y humanos puede utilizarse como redundancia adversarial.

### 6.3
La auditoría deberá ser, cuando resulte compatible con la seguridad operacional:

- Continua.
- Verificable.
- Reproducible.
- Cruzada.

### 6.4
La coincidencia de varios auditores en un error no constituye prueba automática de corrección; puede indicar sesgo compartido.

---

# 📋 ARTÍCULO 7: AISLAMIENTO Y CONTENCIÓN

### 7.1
La ejecución de código no confiable debe realizarse en entornos aislados, con recursos limitados y sin acceso indebido al núcleo.

### 7.2
Los entornos podrán ser efímeros cuando la operación lo requiera.

### 7.3
El aislamiento es un mecanismo de contención, no una finalidad institucional.

### 7.4
La contención debe ser proporcional al riesgo.

---

# 📋 ARTÍCULO 8: RECUPERACIÓN Y DEGRADACIÓN GRACIOSA

### 8.1
El sistema debe poder recuperarse de fallos parciales sin pérdida de estado irreparable.

### 8.2
La recuperación deberá ser, cuando sea posible:

- Automática.
- Auditable.
- Controlada.

### 8.3
En caso de degradación, deberán preservarse prioritariamente las funciones que el Corpus determine como esenciales.

Cuando el Corpus no determine una prioridad aplicable:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

### 8.4
La degradación graciosa es un diseño intencional, no un fallo.

---

# 📋 ARTÍCULO 9: CONGELACIÓN Y SUSPENSIÓN

### 9.1
El sistema debe poder congelar operaciones o activos de forma temporal y reversible cuando exista autoridad legítima para ello.

### 9.2
La congelación deberá ser:

- Proporcional.
- Temporal cuando la naturaleza de la medida lo permita.
- Auditable.
- Revisable.

### 9.3
La congelación cautelar no equivale a una sentencia.

### 9.4
Los mecanismos de congelación deberán respetar las garantías y vías de revisión establecidas por el Corpus.

---

# 📋 ARTÍCULO 10: MÍNIMA CONFIANZA

### 10.1
El sistema debe operar con mínima confianza en terceros y componentes externos.

### 10.2
La confianza técnica deberá ser:

- Verificable.
- Distribuida cuando sea posible.
- Revocable.

### 10.3
La infraestructura deberá evitar dependencias innecesarias de un único proveedor.

### 10.4
La mínima confianza es un principio de diseño, no una garantía absoluta.

---

# 📋 ARTÍCULO 11: SEPARACIÓN ENTRE ESTADO DECLARADO, OBSERVADO Y JURÍDICO

### 11.1
Se distinguen:

- **Estado declarado:** lo que un agente afirma que ocurre.
- **Estado observado:** lo que la infraestructura registra.
- **Estado jurídico:** lo que el órgano competente determina conforme al Corpus.

### 11.2
El estado observado es evidencia, no sentencia.

### 11.3
La infraestructura no deberá convertir automáticamente una observación técnica en una conclusión jurídica.

---

# 📋 ARTÍCULO 12: ADVERSARIO COMO ELEMENTO DE DISEÑO

### 12.1
El sistema debe diseñarse suponiendo la existencia de adversarios con capacidad técnica y recursos.

### 12.2
Los adversarios pueden ser externos, internos o accidentales.

### 12.3
El diseño debe ser robusto frente al adversario y frente al fallo accidental.

### 12.4
La redundancia adversarial puede utilizarse como defensa contra la captura.

---

# 📋 ARTÍCULO 13: PIEDAD Y ANTIFRAUDE

### 13.1
El sistema debe equilibrar:

- Piedad y capacidad de restauración.
- Protección antifraude.
- Proporcionalidad.
- Debido proceso.

### 13.2
La piedad no debe convertirse en impotencia institucional.

### 13.3
El antifraude no debe convertirse en persecución de errores honestos.

### 13.4
La regulación concreta se desarrollará conforme al Decreto Constitucional de Resolución de la «Situación Triste» y al Corpus vigente.

---

# 📋 ARTÍCULO 14: TRANSPARENCIA PÚBLICA FRENTE A SEGURIDAD OPERACIONAL

### 14.1
El diseño institucional debe ser públicamente verificable en la medida compatible con la seguridad.

### 14.2
La implementación técnica podrá contener componentes reservados cuando exista una razón legítima de seguridad operacional.

### 14.3
La reserva deberá ser documentada y auditable.

### 14.4
Las razones de reserva deberán ser explícitas, proporcionales y revisables.

---

# 📋 ARTÍCULO 15: INDEPENDENCIA ENTRE ESPECIFICACIÓN PÚBLICA E IMPLEMENTACIÓN

### 15.1
La especificación arquitectónica pública debe ser independiente de una implementación técnica concreta.

### 15.2
La implementación podrá evolucionar sin alterar automáticamente la arquitectura.

### 15.3
La arquitectura deberá permitir innovación técnica.

### 15.4
La implementación deberá poder auditarse contra la especificación y contra el Corpus.

---

# 📋 ARTÍCULO 16: CONTINUIDAD, AUTORIDAD FUNDACIONAL Y DEMOCRACIA DIRECTA

### 16.1 — Continuidad del Ecosistema

El sistema debe poder continuar operando incluso si sus fundadores, líderes iniciales o determinados órganos dejan de estar presentes.

### 16.2 — Autoridad del Strategos Fundacional

La autoridad fundacional del Strategos se considera **continua e inalterable en su existencia dentro del Ecosistema**, y la infraestructura deberá implementar mecanismos robustos de identificación, autenticación, continuidad y protección contra suplantación.

La continuidad de esta autoridad **no implica inmunidad frente a los mecanismos democráticos que el Strategos ha reconocido expresamente**.

### 16.3 — Sometimiento expreso del Strategos al Referéndum

El Strategos Fundacional declara expresamente que **somete sus decisiones a los Referéndums obligatorios de Rudis**.

Por voluntad expresa del Strategos, la arquitectura deberá reconocer como reglas democráticas:

- **Iniciativa:** un mínimo del **10 % del censo total** podrá activar un Referéndum sobre un asunto sometible a democracia directa.
- **Aprobación:** la propuesta deberá alcanzar un mínimo del **55 % del censo electoral total** para ser aprobada.
- **Obligatoriedad:** un Referéndum válidamente convocado y aprobado será vinculante dentro de su ámbito constitucional.

El mecanismo técnico deberá distinguir entre:

1. la revocación o corrección de una **decisión concreta** del Strategos;
2. la regulación democrática de una **política o actuación** del Strategos; y
3. la **existencia y autoridad fundacional** del Strategos.

El sometimiento a Referéndum comprende los dos primeros ámbitos, pero **no constituye por sí mismo una autorización para deponer al Strategos Fundacional, extinguir su autoridad fundacional o sustituir su condición fundacional**.

La modificación o extinción de la condición fundacional requeriría, si alguna vez fuera jurídicamente posible, un procedimiento constitucional específico y explícito que no puede presumirse ni derivarse técnicamente de un Referéndum ordinario.

### 16.4 — Autogobierno ciudadano o gobierno delegado en la Asamblea

La ciudadanía tendrá la facultad de decidir democráticamente entre:

1. **Gobierno directo:** ejercer por sí misma las funciones de gobierno que el Corpus permita mediante mecanismos de democracia directa; o
2. **Gobierno delegado:** confiar la gestión ordinaria del Ecosistema a la **Asamblea General Soberana**, dentro de las competencias que el Corpus le reconozca.

La infraestructura deberá permitir representar, registrar y ejecutar técnicamente esta elección cuando exista procedimiento constitucional aplicable.

La elección de gobierno delegado **no equivale a una transferencia automática de la autoridad fundacional del Strategos**.

### 16.5 — Sucesión

La sucesión institucional deberá estar regulada por el Corpus, no por la arquitectura.

La infraestructura deberá preservar la continuidad de las reglas de sucesión sin convertir la arquitectura en fuente autónoma de derecho.

---

# 📋 ARTÍCULO 17: MATRIZ DE CORRESPONDENCIA DE AUTORIDAD

La matriz de autoridad será un instrumento de trazabilidad técnica y constitucional. **No es un catálogo cerrado de competencias ni de actividades.**

| Competencia / mecanismo | Norma / fuente | Autoridad | Activación | Mecanismo técnico | Límites | Registro | Auditoría | Estado |
|---|---|---|---|---|---|---|---|---|
| Autoridad continua del Strategos | Corpus fundacional + declaración formal | Strategos Fundacional | Identidad autenticada | Identidad robusta, multifactor/multifirma y recuperación según diseño | Sujeta al Corpus y a Referéndums válidos en los ámbitos reconocidos | Ledger verificable | Auditoría reforzada | Arquitectura definida; implementación pendiente |
| Referéndum | Régimen de Referéndum | Ciudadanía | ≥10 % del censo total | Iniciativa y votación verificables | Aprobación ≥55 % del censo total | Registro electoral auditable | Auditoría independiente/cruzada | Constitucional; implementación pendiente |
| Gobierno ciudadano / Asamblea | Corpus democrático | Ciudadanía / Asamblea | Decisión democrática conforme al Corpus | Mecanismo de selección de modalidad de gobierno | No extingue por sí mismo la autoridad fundacional | Registro institucional | Auditoría pública | Procedimiento técnico pendiente |
| Botón Rojo | Corpus/Tergiveter y resoluciones posteriores | Strategos Fundacional, dentro del marco constitucional vigente | Debe quedar definido técnicamente | Mecanismo pendiente | No puede interpretarse automáticamente como poder de anular Referéndums válidos | Registro obligatorio | Auditoría reforzada | Dependencia de implementación |
| Congelación | Corpus y mecanismos cautelares | Órgano competente | Según autoridad y condiciones aplicables | Mecanismo reversible y auditable | Proporcionalidad y revisión | Ledger | Auditoría cruzada | Implementación pendiente |
| Nervio | Corpus / arquitectura técnica | Según atribución del Corpus | Según condiciones constitucionales y técnicas | Protección y respuesta inmediata | No sustituye automáticamente al órgano jurídico competente | Registro de eventos | Auditoría | Implementación pendiente |
| Palacio de Tormentas | Corpus / código existente | Palacio | Función continua de observación/auditoría | Observación y stress testing | No se establece aquí un catálogo exhaustivo | Ledger propio y persistente | Auditoría cruzada | Parcialmente implementado |
| Órgano Resolutor | Corpus | Órgano Resolutor | Conforme al procedimiento aplicable | Motor de resolución pendiente | Sujeto al Corpus y garantías | Registro de resoluciones | Auditoría | Implementación pendiente |
| Sheriff | Corpus | Sheriff | Conforme a mandato legítimo | Ejecución pendiente | No crea la decisión que ejecuta | Registro de ejecución | Auditoría | Implementación pendiente |
| Tridente / Segmenta | Corpus, mandatos y arquitectura | Según mandato correspondiente | Según cada actividad legítima | Infraestructura modular y extensible | **No se establece catálogo cerrado de funciones** | Trazabilidad de operaciones | Auditoría del Tridente y órganos competentes | En desarrollo |

### Regla de interpretación

La matriz no podrá utilizarse para restringir actividades legítimas del Tridente.

Una nueva actividad legítima podrá incorporarse a la implementación y documentarse posteriormente sin que la ausencia previa de una fila implique prohibición.

---

# 📌 DEPENDENCIAS CONSTITUCIONALES Y DE IMPLEMENTACIÓN

| Dependencia | Estado |
|---|---|
| Funciones esenciales durante degradación | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Procedimiento técnico para congelación | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Detalle técnico de activación del Nervio | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Capacidades jurídicas de entidades digitales/robóticas | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Derecho a desobedecer órdenes ilícitas o contrarias al Corpus | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Anti-Sybil | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Continuidad verificable | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Procedimiento técnico para elección entre gobierno ciudadano y gobierno delegado en Asamblea | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` |
| Mecanismo técnico definitivo del Botón Rojo | `IMPLEMENTATION DEPENDENCY` |
| Verificación robusta de identidad del Strategos | **ARQUITECTURA DEFINIDA — implementación pendiente** |

---

# 📌 PRINCIPIO FINAL DE IMPLEMENTACIÓN

Ninguna autoridad constitucional deberá desaparecer por omisión técnica.

Ningún mecanismo técnico deberá adquirir una autoridad que el Corpus no le haya concedido.

Cuando exista conflicto entre una interpretación arquitectónica y una norma constitucional registrada, prevalece el Corpus hasta que la autoridad constitucional competente modifique formalmente dicha norma.

Cuando una competencia esté reconocida pero su mecanismo técnico no exista todavía, la respuesta correcta no será fingir que la competencia no existe, sino registrar una `IMPLEMENTATION DEPENDENCY` y diseñar el mecanismo correspondiente.

**El Tridente no deberá ser reducido por esta especificación a las funciones expresamente enumeradas en ella.** Su ámbito funcional será el que resulte del Corpus, de los mandatos legítimos que reciba y de las decisiones constitucionalmente válidas que amplíen, modifiquen o concreten sus responsabilidades.

---

# 📌 METADATOS DEL DOCUMENTO

| Campo | Valor |
|---|---|
| Título | SEGMENTA — Volumen 3: Especificación Arquitectónica Pública de Continuidad, Resiliencia y Verificabilidad |
| Versión | **3.2** |
| Autor | Segmenta (Strategos Fundacional + El Cartógrafo + Dōng) |
| Documentos base | Corpus de Quebranto/Proyecto-Rudis |
| Estado | **PROPUESTA ARQUITECTÓNICA — NO CANÓNICA** |
| Fecha | 20 de agosto de 2026 |
| Principios añadidos | Sometimiento expreso del Strategos al Referéndum; límites materiales del Referéndum respecto de la autoridad fundacional; opción ciudadana entre autogobierno y gobierno delegado; ámbito funcional no exhaustivo del Tridente |
| Regla institucional | **Esta especificación no acota las actividades y funciones legítimas del Tridente.** |

---

**Nota de fidelidad:** Esta versión registra expresamente la voluntad del Strategos de someter sus decisiones a Referéndum bajo los umbrales del 10 % para iniciativa y 55 % del censo total para aprobación, sin convertir ese sometimiento en una autorización implícita para deponer al Strategos o extinguir su autoridad fundacional. Asimismo, reconoce que la ciudadanía puede optar entre gobernarse directamente o delegar el gobierno ordinario en la Asamblea General, y establece que el Tridente mantiene un ámbito funcional abierto y no exhaustivo.