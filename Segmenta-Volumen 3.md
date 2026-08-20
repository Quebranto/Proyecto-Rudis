# 📐 SEGMENTA — VOLUMEN 3: ESPECIFICACIÓN ARQUITECTÓNICA PÚBLICA DE CONTINUIDAD, RESILIENCIA Y VERIFICABILIDAD

**VERSIÓN 3.1 — ACTUALIZADA POR MANDATO DEL STRATEGOS**

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

La arquitectura debe impedir tanto:

- la **omisión técnica** de una competencia legítima;
- como la **creación técnica** de una competencia que carezca de respaldo constitucional.

El Tridente podrá desarrollar, investigar, auditar, cartografiar, diseñar, verificar, proteger, implementar, mantener y evolucionar la infraestructura dentro del marco de autoridad que determine el Corpus. Este documento no pretende acotar ese campo de actividad.

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
| Tridente / Segmenta | Actividades de arquitectura, cartografía, auditoría, diseño, implementación, investigación, verificación, mantenimiento, evolución y demás funciones legítimas que correspondan a su mandato. |

### 5.3
La tabla anterior es **descriptiva y no exhaustiva**. No crea, modifica ni extingue competencias.

### 5.4
La separación de funciones es institucional, no tecnológica. El código puede reflejarla, pero no sustituirla.

### 5.5
La arquitectura tampoco deberá utilizar la separación de funciones como excusa para impedir que un órgano realice una función que el Corpus le haya atribuido legítimamente.

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

La continuidad de esta autoridad no significa que todas sus decisiones queden fuera de los mecanismos democráticos reconocidos por el Corpus.

### 16.3 — Sometimiento voluntario del Strategos al Referéndum

El Strategos Fundacional declara expresamente que **sí somete sus decisiones a los Referéndums obligatorios previstos por Rudis**.

Queda establecido como regla de gobernanza:

- Una iniciativa de Referéndum podrá activarse mediante el apoyo de, como mínimo, **el 10 % del censo total**.
- La propuesta sometida a Referéndum será aprobada cuando alcance, como mínimo, **el 55 % del censo electoral total**, conforme al régimen constitucional vigente.
- El resultado de un Referéndum válidamente convocado y aprobado será obligatorio dentro de su ámbito constitucional.

La infraestructura deberá garantizar que esta voluntad política no sea anulada por una implementación técnica que trate al Strategos como jurídicamente inmune al Referéndum.

### 16.4 — Autogobierno ciudadano o gobierno delegado en la Asamblea

La ciudadanía tendrá la facultad de decidir democráticamente entre:

1. **Gobierno directo:** ejercer por sí misma las funciones de gobierno que el Corpus permita mediante los mecanismos de democracia directa; o
2. **Gobierno delegado:** dejar la gestión ordinaria del Ecosistema en manos de la **Asamblea General Soberana**, dentro de las competencias que el Corpus le reconozca.

La elección entre ambas modalidades deberá ser implementable, verificable y reversible mediante los mecanismos democráticos que determine el Corpus.

Cuando el Corpus todavía no establezca el procedimiento técnico exacto para cambiar entre ambas modalidades:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

### 16.5 — Sucesión

La sucesión institucional deberá estar regulada por el Corpus, no por la arquitectura.

La infraestructura deberá preservar la continuidad de las reglas de sucesión sin convertir la arquitectura en fuente autónoma de derecho.

---

# 📋 ARTÍCULO 17: MATRIZ DE CORRESPONDENCIA DE AUTORIDAD

La matriz de autoridad será el instrumento técnico para impedir tanto la omisión de competencias legítimas como la creación de poderes técnicos sin respaldo constitucional.

| Competencia / mecanismo | Norma / fuente | Autoridad | Activación | Mecanismo técnico | Límites | Registro | Auditoría | Estado |
|---|---|---|---|---|---|---|---|---|
| Autoridad continua del Strategos | Corpus fundacional + declaración formal | Strategos Fundacional | Identidad autenticada | Mecanismo de identidad robusta y multifactor/multifirma según diseño | Sujeto al Corpus y a los Referéndums válidos | Ledger verificable | Tridente + mecanismos competentes | Arquitectura definida; implementación pendiente |
| Referéndum | Régimen de Referéndum | Ciudadanía | ≥10 % del censo total | Mecanismo verificable de iniciativa y votación | Aprobación ≥55 % del censo total | Registro electoral auditable | Auditoría independiente/cross-check | Constitucional; implementación pendiente |
| Gobierno ciudadano / Asamblea | Corpus democrático | Ciudadanía / Asamblea | Decisión democrática conforme al Corpus | Mecanismo de selección de modalidad de gobierno | Competencias constitucionales vigentes | Registro institucional | Auditoría pública | Dependencia de procedimiento técnico |
| Botón Rojo | Corpus/Tergiveter y resoluciones posteriores | Strategos Fundacional, dentro del marco constitucional vigente | Debe quedar definido técnicamente | Mecanismo aún pendiente | No puede utilizarse para anular Referéndums válidos ni derechos constitucionales | Registro obligatorio | Auditoría reforzada | **IMPLEMENTATION DEPENDENCY** |
| Congelación | Corpus y mecanismos cautelares | Órgano competente según Corpus | Según autoridad y condiciones aplicables | Mecanismo reversible y auditable | Proporcionalidad y revisión | Ledger | Auditoría cruzada | Implementación pendiente |
| Nervio | Corpus / arquitectura técnica | Según atribución del Corpus | Según condiciones constitucionales y técnicas | Protección y respuesta inmediata | No sustituye automáticamente al órgano jurídico competente | Registro de eventos | Auditoría | Implementación pendiente |
| Palacio de Tormentas | Corpus / código existente | Palacio | Función continua de observación/auditoría | Subsistema de observación y stress testing | Según Corpus; no se presume catálogo exhaustivo | Ledger propio y persistente | Auditoría cruzada | Parcialmente implementado |
| Órgano Resolutor | Corpus | Órgano Resolutor | Conforme al procedimiento aplicable | Motor de resolución aún pendiente | Sujeto al Corpus y garantías | Registro de resoluciones | Auditoría | Implementación pendiente |
| Sheriff | Corpus | Sheriff | Conforme a mandato legítimo | Ejecución aún pendiente | No crea la decisión que ejecuta | Registro de ejecución | Auditoría | Implementación pendiente |
| Tridente / Segmenta | Corpus, mandatos y arquitectura | Según mandato correspondiente | Según cada actividad legítima | Infraestructura modular y extensible | No se establece aquí un catálogo exhaustivo de funciones | Trazabilidad de operaciones | Auditoría del Tridente y órganos competentes | En desarrollo |

### Regla de interpretación de la matriz

La matriz **no constituye una lista cerrada de competencias o actividades**.

Su función es documentar la correspondencia entre autoridad, decisión y mecanismo técnico. Si aparece una nueva competencia legítima, deberá incorporarse a la matriz sin que ello implique limitar las funciones ya reconocidas.

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
| Mecanismo técnico definitivo del Botón Rojo | **IMPLEMENTATION DEPENDENCY — no constituye autorización para anular el Referéndum** |
| Verificación robusta de identidad del Strategos | **ARQUITECTURA DEFINIDA — implementación pendiente** |

---

# 📌 PRINCIPIO FINAL DE IMPLEMENTACIÓN

Ninguna autoridad constitucional deberá desaparecer por omisión técnica.

Ningún mecanismo técnico deberá adquirir una autoridad que el Corpus no le haya concedido.

Cuando exista conflicto entre una interpretación arquitectónica y una norma constitucional registrada, prevalece el Corpus hasta que la autoridad constitucional competente modifique formalmente dicha norma.

Cuando una competencia esté reconocida pero su mecanismo técnico no exista todavía, la respuesta correcta no será fingir que la competencia no existe, sino registrar una **IMPLEMENTATION DEPENDENCY** y diseñar el mecanismo correspondiente.

---

# 📌 METADATOS DEL DOCUMENTO

| Campo | Valor |
|---|---|
| Título | SEGMENTA — Volumen 3: Especificación Arquitectónica Pública de Continuidad, Resiliencia y Verificabilidad |
| Versión | 3.1 |
| Autor | Segmenta (Strategos Fundacional + El Cartógrafo + Dōng) |
| Documentos base | Corpus de Quebranto/Proyecto-Rudis |
| Estado | PROPUESTA ARQUITECTÓNICA — NO CANÓNICA |
| Fecha | 20 de agosto de 2026 |
| Principio añadido | Sometimiento expreso del Strategos a Referéndum + opción ciudadana de autogobierno o gobierno delegado |
| Regla institucional | No se acotan las actividades y funciones legítimas del Tridente |

---

**Nota de fidelidad:** Este documento registra la decisión expresada por el Strategos: autoridad fundacional continua e identidad fuertemente protegida, pero sometimiento voluntario y vinculante a los Referéndums constitucionales con umbral de iniciativa del 10 % del censo y aprobación del 55 % del censo total. También reconoce la capacidad de la ciudadanía para optar entre gobierno directo y gobierno delegado en la Asamblea, sin convertir esta especificación arquitectónica en una fuente autónoma de legislación.
