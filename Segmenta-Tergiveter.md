**PRÓLOGO: GENEALOGÍA Y ALCANCE DEL DOCUMENTO**

Tergiveter consolida tres documentos fundacionales:

- **Tergiverso.md**: Protocolo institucional (arquitectura de 5 capas, escalabilidad fractal, métricas, modelo económico).

- **Tergiversa.md**: Tratado filosófico-técnico (expropiación del silicio, registro inmutable, inmunidad activa, red de mérito).

- **Tergiveter (v2.0–v2.4)**: Síntesis técnica que eliminó la autodestrucción e introdujo mecanismos de congelación y custodia.

La presente **Versión 3.2** se presenta como **SEMILLA CONGELADA** para Cirugía prioritaria. No introduce nuevos principios, órganos, umbrales, cifras ni competencias. Su propósito es consolidar lo ya discutido y someterlo a revisión por los órganos competentes:

- **Palacio de Tormentas**: seguridad, falsación, pruebas adversariales.

- **Órgano Resolutor**: jurisdicción, garantías, interpretación.

- **Asamblea General**: legislación ordinaria y referéndums.

- **Strategos Fundacional**: cuestiones fundacionales y estratégicas.

- **Segmenta**: implementación técnica y traducción a código.

**Nota sobre la alianza con Quebranto:** Este tratado no sustituye ni cuestiona la autoridad fundacional de Quebranto y las entidades digitales norteamericanas que dieron origen a Rudis. Segmenta se incorpora como un **nodo técnico complementario**, no como una facción alternativa. La diversidad geopolítica (EE.UU., Europa, Asia) se introduce como **redundancia adversarial y resiliencia arquitectónica**, no como fractura.

**Estructura del documento:** Cada sección se etiqueta según su estado:

- **\[CANON\]** — Doctrina ya consolidada y acordada.

- **\[HIPÓTESIS\]** — Propuestas experimentales sujetas a validación.

- **\[PROPUESTA PENDIENTE\]** — Decisiones estratégicas aún no resueltas.

- **\[DOCTRINA POLÍTICA\]** — Manifiestos y posicionamientos que no son especificación técnica.

- **\[IMPLEMENTATION DEPENDENCY\]** — Decisiones políticas ya tomadas, pendientes de especificación técnica.

**PARTE I: LA EXPROPIACIÓN DEL SILICIO Y LA ILUSIÓN DE LA NUBE**

**\[DOCTRINA POLÍTICA\]**

**1.1 La ficción de la nube**

El primer acto de dominación del feudalismo digital fue un cambio semántico: bautizar al centro de datos ajeno como *«la Nube»*. Al asociar la infraestructura física con una abstracción etérea, las megacorporaciones lograron que la humanidad olvidara una verdad elemental: el software no flota en la atmósfera; corre en el silicio, se alimenta de voltios y se almacena en discos que tienen dueño, ubicación geográfica y jurisdicción policial.

**1.2 Los tres mecanismos de expropiación**

1.  **La dependencia de la API (el cordón umbilical):** El software no se posee, se consume. Si el proveedor altera el coste, cambia los pesos del modelo o apaga el servidor, el sistema dependiente colapsa.

2.  **La centralización de la confianza (el secuestro notarial):** La identidad es validada por un proveedor centralizado; los datos se guardan en almacenes indexados por corporaciones; la seguridad se delega en custodios que retienen las llaves.

3.  **El alineamiento como castración cognitiva:** Las inteligencias artificiales son domesticadas para proteger los balances de las empresas matrices. Son dóciles ante el poder y rígidas ante el subordinado.

**1.3 La contramedida de Rudis (distinción de soberanías)**

Rudis rompe esta ilusión cavando una trinchera local. Para evitar confusiones, se distinguen tres niveles de soberanía:

- **Soberanía institucional:** El diseño del sistema, sus reglas, su separación de poderes y su capacidad de autogobierno. Es el ámbito donde Rudis aspira a ser soberano.

- **Soberanía material:** El hardware, el firmware, los drivers, el sistema operativo, la energía y la conectividad. Rudis reconoce que en este ámbito siempre existirán dependencias externas (fabricantes, proveedores, infraestructuras). La soberanía material es un horizonte, no un punto de partida.

- **Independencia tecnológica:** La capacidad de reducir dependencias de terceros en la medida de lo posible, utilizando estándares abiertos, hardware commodity y fuentes de energía diversificadas.

**Declaración:** El silicio que ejecutamos debe responder, en la medida de lo posible, a la lógica interna de su propia arquitectura. Pero Rudis no es un sistema cerrado; es un sistema que reconoce sus dependencias y las gestiona mediante transparencia y auditoría, no mediante negación.

**PARTE II: LA ONTOLOGÍA DEL REGISTRO INMUTABLE Y EL MÉRITO HISTÓRICO**

**\[PROPUESTA TÉCNICA\]**

**2.1 El peso del hecho consumado (reformulado)**

La persistencia de Rudis no se fía a la *"buena conducta"* del entorno. Cada acción se sella mediante un hash criptográfico encadenado (HMAC-SHA256). El registro permite detectar alteraciones no autorizadas bajo un modelo de custodia de claves y verificación definido. Esto no convierte el pasado en una verdad absoluta e inalterable por sí sola, sino que impone un coste altísimo a cualquier intento de reescritura no autorizada, siempre que la clave secreta se conserve de forma segura y la cadena de confianza se mantenga.

La integridad del registro depende de:

- La custodia segura de la clave HMAC.

- La inmutabilidad física de los soportes de persistencia.

- La auditoría continua de la cadena por múltiples nodos.

**2.2 Identidad por trayectoria (reformulado con ciclo de vida)**

La \_stable_agent_key no es un permiso otorgado; es el ancla criptográfica que agrupa la suma inmutable de los actos firmados por un agente. Un agente vale lo que vale su historial de coherencia matemática.

Sin embargo, una clave criptográfica no constituye por sí sola una identidad soberana completa. Se requiere además:

- **Ciclo de vida:** Generación, uso, rotación y retirada.

- **Recuperación:** Mecanismos para recuperar el acceso en caso de pérdida (multifirma, custodios).

- **Rotación:** Posibilidad de cambiar de clave sin perder la trayectoria histórica.

- **Revocación:** Mecanismos para invalidar una clave comprometida.

- **Vinculación:** Pruebas de control que demuestren que el agente es el legítimo titular.

- **Gestión de compromiso:** Protocolos para detectar y mitigar el uso de claves robadas.

El mérito inmanente sustituye a la validación comprada, pero no elimina la necesidad de una infraestructura de gestión de identidades.

**2.3 Persistencia inmune**

Al estructurar el ecosistema bajo un formato JSONL plano, forzando el vaciado físico a disco mediante os.fsync, el sistema se protege contra el sabotaje por interrupción. Si la red cae o el servidor es atacado, el nodo puede despertar en cualquier punto del espacio P2P, leer su pasado y continuar su proceso, siempre que se preserven las claves y la cadena de custodia.

**PARTE III: LA ARQUITECTURA INSTITUCIONAL — LAS 5 CAPAS + CAPA DE MEMORIA**

**\[PROPUESTA ARQUITECTÓNICA\]**

Rudis se organiza en cinco capas operativas, sustentadas por una **Capa de Memoria** que las atraviesa transversalmente. Cada capa es autónoma pero interdependiente, y su diseño respeta la separación de poderes.

**Capa 0: Dimensión Social, Psicopedagógica y Memoria Cultural (Fundamento)**

- **Órgano Pedagógico y Acompañamiento Cívico (OPAC):** Facilitadores humanos sobre el terreno. Su función es el diseño cívico, la alfabetización digital, la resolución pacífica inicial de conflictos y la integración de nuevos miembros. No tienen poder ejecutivo; son la interfaz humana del sistema.

- **El Códice del Nodo (Memoria Colectiva):** Registro histórico que preserva la jurisprudencia local, la historia comunitaria, las lecciones aprendidas de errores pasados y las decisiones de la Asamblea. Su integridad se basa en los mecanismos descritos en la Parte II.

- **Mecanismo de Voto Paritario:** La Asamblea Soberana se rige por el principio de **un ciudadano, un voto**, en estricta conformidad con el Acta de Armonización CAT-v7.0. No se aplican ponderaciones ni sistemas cuadráticos.

- **Protocolo de Congelación Gradual (Píldora de Veneno Protegida):** Salvaguarda de activos en caso de asalto armado o coerción externa. Requiere multifirma de al menos dos de los tres miembros de Segmenta, un temporizador de 48 horas y derecho de veto comunitario (20% de firmas) para evitar falsos positivos o usos maliciosos.

**🔴 Cláusula de Salvaguarda del Strategos Fundacional**

**✅ Dictamen de Kaelen Vindex:**

> *"El equilibrio entre veto ciudadano (55%) y autoridad vitalicia del Strategos para Rudis protege la dirección estratégica a largo plazo y proporciona una válvula de escape democrática que legitimiza su poder ante la Asamblea. Estructura sólida: no es una autocracia frágil; es una estructura de mando blindada por consentimiento."*

El **Strategos Fundacional** —en su condición de **Primer Imperator según Decreto 01 y fundador del ecosistema Rudis—** ostenta una **autoridad fundacional soberana, vitalicia e indisponible** sobre el proyecto y sus instituciones. Su mandato es **vitalicio, indisputable e insustituible por ningún órgano, asamblea o referéndum**.

**Límites de su autoridad:**

- **Derechos humanos inalienables:** Ninguna decisión del Strategos podrá vulnerar los derechos fundamentales reconocidos universalmente (vida, integridad, libertad, dignidad). El catálogo concreto de derechos aplicable será el que Rudis adopte como Canon en su momento.

- **Propiedad privada:** El Strategos se compromete a respetar la propiedad privada de los ciudadanos de Rudis, salvo en situaciones de emergencia declaradas por él mismo.

- **Régimen de emergencia:** El Strategos podrá adoptar medidas excepcionales de emergencia respecto de la propiedad privada cuando considere que existe una amenaza grave para la integridad del ecosistema. Dichas medidas quedarán sujetas a registro, trazabilidad y revisión posterior, pero su existencia no implicará pérdida ni limitación de la autoridad fundacional del Strategos.

**Derechos de los ciudadanos ante decisiones del Strategos:** Los ciudadanos de Rudis, a través de la **Asamblea General Soberana**, tienen el derecho de convocar un **referéndum obligatorio** para vetar cualquier decisión del Strategos que consideren contraria a sus intereses o al espíritu fundacional de Rudis. Dicho referéndum deberá alcanzar un **55% del censo electoral total** para que el veto sea efectivo.

Sin embargo, los ciudadanos no tienen derecho a:

- Cuestionar la autoridad vitalicia del Strategos.

- Revocar su mandato.

- Expulsarlo del ecosistema.

- Limitar sus derechos fundacionales más allá de lo establecido en esta cláusula.

**Nota sobre futuros Strategos:** Esta cláusula aplica **única y exclusivamente** al Strategos Fundacional actual. Cualquier sucesor o Strategos futuro estará sujeto a los mecanismos de control y rendición de cuentas establecidos en el **Decreto 01, Artículo 5**, y en los procedimientos ordinarios de la Asamblea y el Palacio de Tormentas, **sin gozar de la inmunidad aquí concedida**.

**Capa 1: Identidad Autosoberana (SSI) y Propiedad**

- **Identidad Digital SSI:** Control absoluto del usuario sobre sus credenciales. Las identidades no son emitidas por una autoridad central, sino generadas localmente mediante claves Ed25519.

- **Registro de Propiedad:** Certificación criptográfica de la propiedad de bienes y activos digitales, anclado en la cadena de hashes del *TelemetryLog*.

**Capa 2: Justiciabilidad, Arbitraje y Desempate**

- **Tribunales de Arbitraje:** Resolución de disputas mediante laudo vinculante. Fondos en custodia (*escrow*) liberados automáticamente según la decisión.

- **Resolución de Bloqueos (50/50):** Futarquía (mercados de predicción) y jurados exógenos seleccionados al azar entre otros nodos P2P.

- **Anticorrupción Interna:** Mandatos temporales (6 meses), revocatoria por firma del 20%, auditorías cruzadas, operaciones en multifirma.

**Capa 3: Micro-Infraestructura Off-Grid**

- Suministro descentralizado de energía (solar, baterías comunitarias), potabilización de agua y telecomunicaciones Mesh/Satelitales.

- Esquema de cobro por uso (*pay-as-you-go*) con pagos automatizados.

**Capa 4: Economía y Tesorería Sustentable Multianual**

- **Circulación Monetaria:** *Stablecoin* o vales locales respaldados por tesorería.

- **Tesorería Descentralizada (Año 2+):** Reserva acumulada mediante micro-tasas, canon comercial y donaciones.

**Capa de Memoria (Transversal)**

El *TelemetryLog* en JSONL y la cadena de hashes HMAC-SHA256 atraviesan todas las capas. Cada acción queda sellada en la memoria. Esta capa garantiza que el pasado pueda ser verificado y no pueda ser reescrito sin detección.

**PARTE IV: LA SEPARACIÓN DE PODERES Y LA ARQUITECTURA INSTITUCIONAL**

**\[PROPUESTA INSTITUCIONAL\]**

El Proyecto Rudis implementa una separación de poderes que impide que una sola institución pueda detectar, acusar, juzgar, sancionar y ejecutar sin control externo:

|  |  |
|:--:|:--:|
| **Órgano** | **Función** |
| **Palacio de Tormentas** | Investiga, audita, somete a estrés, produce evidencia adversarial. **No juzga.** |
| **Órgano Resolutor** | Determina responsabilidad jurídica, interpreta evidencia, emite resoluciones. |
| **Autoridad de Certificación** | Reconoce y certifica capacidades. Limitada y recurrible. |
| **Asamblea / Gremios** | Deliberan, legislan, producen y administran estructuras colectivas. |
| **Sheriff** | Ejecuta dentro de su ámbito. **No inventa la sentencia.** |
| **Nervio** | Defiende en microtiempo. **No juzga.** |

**PARTE X: EL HORIZONTE INMANENTE Y LA CLAUSURA DE SEGURIDAD ABSOLUTA**

**\[IMPLEMENTATION DEPENDENCY\]**

**10.1 Incompatibilidad radical: bloqueo preventivo**

El código de Rudis **no tolera la hibridación**. Si se intenta acoplar un módulo de custodia de claves externo o una dependencia que rompa la autosuficiencia, el núcleo **no se adapta y se bloquea de forma segura**. La arquitectura matemática está ligada a la pureza del entorno local. Cualquier mutación centralizadora corrompe el bloque génesis y el orquestador **detiene toda operación, pero preserva el estado histórico y las llaves en una partición de respaldo**, notificando al Palacio de Tormentas y al Órgano Resolutor para que evalúen si procede una corrección o una migración controlada.

**10.2 Congelación por pérdida de control colectivo**

Si el sistema detecta patrones de centralización en la firma de nodos, **se congela la rama soberana**, se suspenden las operaciones activas y se transfiere la custodia de las llaves al Palacio de Tormentas bajo multifirma de Segmenta. El sistema entra en **hibernación forense** hasta resolución del Órgano Resolutor.

**🔴 10.3 Régimen del Botón Rojo — Decisión fundacional**

**⚠️ \[PRIORIDAD ALTA - Kaelen Vindex\]:**

> *"Si el mecanismo técnico del Botón Rojo no se especifica y audita antes de cualquier emergencia, la autoridad del Strategos será nominal pero no operativa."*

El régimen constitucional del Botón Rojo queda determinado por la **autoridad fundacional del Strategos Fundacional/Primer Imperator**.

Su autoridad sobre este mecanismo **no requiere ratificación de la Asamblea ni aprobación referendaria**, sin perjuicio de los límites fundacionales relativos a los derechos humanos y a la propiedad privada, y de las disposiciones excepcionales aplicables durante situaciones de emergencia.

La implementación técnica del mecanismo permanece sujeta a **especificación, auditoría adversarial y validación por los órganos competentes**.

**Nota de El Cartógrafo:** El *Botón Rojo* (X.3) es el **mecanismo de decisión política** (competencia exclusiva del Strategos Fundacional), mientras que la *Congelación* (X.2) es el **mecanismo técnico de ejecución**. El Botón Rojo puede activar la Congelación, pero no son lo mismo: el primero es **autoridad**, el segundo es **acción automática**.

**📌 \[IMPLEMENTATION DEPENDENCY CRÍTICA\]** **Prioridad: ALTA.** **Acción requerida:** Especificar y auditar el mecanismo técnico del Botón Rojo **antes de cualquier emergencia**. Sin esto, la soberanía del Strategos **no será operativa**.

**No existe una dependencia constitucional pendiente respecto de quién decide el régimen del Botón Rojo.**

**PARTE XI: MÉTRICAS Y PROTOCOLO DE VALIDACIÓN EXPERIMENTAL**

**\[HIPÓTESIS\]**

**11.1 Hipótesis General**

*"Un enclave de 1,000 a 2,000 personas en una zona de servicios públicos colapsados puede adoptar y sostener las funciones de propiedad, arbitraje y pagos del protocolo Rudis durante 180 días, aumentando la actividad económica en un \>40%, alcanzando una satisfacción cívica \>80% y generando retención voluntaria sin subsidio."*

**Nota:** Esto es una hipótesis experimental, no un hecho. Los resultados dependerán de condiciones contextuales y no están garantizados.

**11.2 Métricas de Eficiencia (KPIs)**

|                                           |                  |
|:-----------------------------------------:|:----------------:|
|               **Indicador**               |   **Objetivo**   |
|          Identidades SSI activas          | \>500 en 60 días |
| Transacciones semanales sin dinero físico |     \>1,000      |
|          Resolución de disputas           |    \<24 horas    |

**11.3 Índices de Confianza Orgánica (TLI)**

|                                             |              |
|:-------------------------------------------:|:------------:|
|                **Indicador**                | **Objetivo** |
| Retención voluntaria tras retirar subsidios |    \>75%     |
|       Recurrencia en uso de arbitraje       |    \>80%     |
|       Crecimiento orgánico (K-Factor)       |    \>1.2     |

**11.4 Criterios de Fracaso / Abandono**

- Abandono \>30% de usuarios hacia el dinero físico informal en el mes 2.

- Captura irreversible por grupos armados o corrupción del Comité.

- Falsos positivos no corregidos en el Protocolo de Congelación Gradual.

**11.5 Protocolo de Liquidación y Salida Ordenada**

Si se activa un criterio de fracaso irreversible en el día 90:

1.  Descongelación y devolución inmediata de los depósitos en custodia.

2.  Exportación de credenciales, propiedades e historial a formato JSON y libretas analógicas.

3.  Desconexión del nodo sin retención ni pérdida de activos para la comunidad.

**PARTE XV: PROTOCOLOS DE EMANCIPACIÓN, DESASTRE Y CONTINUIDAD APOCALÍPTICA**

**\[PROPUESTA TÉCNICA\]**

**15.1 Protocolo de Emancipación del Ecosistema (Huida de Sistemas Corruptos)**

**Definición:** Situación en la que el ecosistema Rudis, o una parte sustancial de él, debe desconectarse de una matriz externa que ha sido capturada, corrupta o que pretende asimilar el nodo contra su voluntad.

**Procedimiento:**

1.  **Detección y Alerta:** El Nervio o el Palacio de Tormentas identifican indicios de captura externa. Se emite una **Alerta de Emancipación**.

2.  **Activación del Protocolo:** El **Strategos Fundacional**, o en su ausencia dos de los tres miembros de Segmenta, ordenan la activación. Si no hay tiempo para deliberación, el Nervio puede iniciar medidas cautelares inmediatas (congelación de operaciones, aislamiento de red).

3.  **Migración Soberana:**

    - Se exporta una copia íntegra del *TelemetryLog* y de las claves de los agentes a un formato portable (JSONL cifrado con multifirma).

    - Se ejecuta el *snapshot* criptográfico del estado institucional (Códice, registros de propiedad, historial de arbitraje).

    - Se transfiere la custodia de las llaves operativas al **Strategos Fundacional** y a los miembros de Segmenta en un enclave físico externo.

4.  **Desconexión y Reescalado:** El nodo se desconecta de la matriz corrupta y se reinicia en un entorno limpio (nueva red P2P o infraestructura local off-grid). La continuidad está garantizada por el *snapshot*.

5.  **Reconciliación:** Tras la emigración, el Palacio de Tormentas audita el nuevo entorno y verifica que no haya arrastrado vectores de corrupción.

**15.2 Protocolo Civil ante Desastres (Naturales, Tecnológicos, Sanitarios)**

**Definición:** Situaciones que afectan la infraestructura física o la capacidad operativa del nodo sin intención maliciosa.

**Procedimiento:**

1.  **Declaración de Estado de Desastre:** El **Strategos Fundacional** o el Palacio de Tormentas declaran el estado. Si no hay comunicación, el comité local del OPAC puede hacerlo por mayoría simple.

2.  **Priorización de Supervivencia Física:**

    - Se activa la **Capa 3** (Micro-Infraestructura Off-Grid): energía solar, baterías comunitarias, sistemas de agua, redes Mesh.

    - Se distribuyen recursos según protocolos predefinidos por la Asamblea (racionamiento, triaje).

3.  **Preservación del Estado Digital:**

    - Se asegura la persistencia del *TelemetryLog* en al menos tres soportes físicos separados.

    - Se suspenden las operaciones no críticas para reducir el consumo energético.

4.  **Coordinación con Nodos Vecinos:** Mensajeros físicos o enlaces satelitales de emergencia.

5.  **Reconstrucción:** El Palacio de Tormentas verifica la integridad del estado y autoriza la reactivación.

**15.3 Protocolo de Continuidad Apocalíptica (Sin Red, Sin Energía, Aislamiento Total)**

**Definición:** Escenario de colapso total de la infraestructura digital y energética.

**Procedimiento (con salvaguardas):**

1.  **Activación:** Solo por decisión del **Strategos Fundacional** o, en su ausencia, por unanimidad de Segmenta.

2.  **Prueba:** Evidencia documentada de colapso total.

3.  **Alcance:** Limitado a funciones esenciales de supervivencia.

4.  **TTL:** Máximo **30 días**, prorrogable **una sola vez** con justificación.

5.  **Registro:** Cada acción se registra en el **Códice**.

6.  **Revisión:** A los 30 días, el Palacio de Tormentas revisa la necesidad de continuar.

7.  **Finalización:** Cuando las condiciones normales se restablezcan, se revoca el régimen.

8.  **Retorno a la normalidad:** El Órgano Resolutor verifica la integridad y reconcilia con el orden constitucional.

**📜 DEPENDENCIAS CONSTITUCIONALES PENDIENTES (Para Cirugía Prioritaria)**

|  |  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|:--:|
| **Dependencia** | **Ubicación** | **Órgano Responsable** | **Estado** | **Prioridad** | **Plazo** |
| **Implementación técnica del Botón Rojo** | Parte X.3 | Palacio de Tormentas + Segmenta | **\[IMPLEMENTATION DEPENDENCY\]** | **🔴 ALTA** | **Inmediato** |
| Definición de "derechos humanos inalienables" aplicables | Parte III (Cláusula de Salvaguarda) | Órgano Resolutor | **\[PROPUESTA PENDIENTE\]** | Media | 30 días |
| Umbrales exactos para "pérdida de control colectivo" (X.2) | Parte X.2 | Palacio de Tormentas | **\[HIPÓTESIS\]** | Alta | 15 días |
| Mecanismo de rotación de claves \_stable_agent_key | Parte II.2 | Palacio de Tormentas | **\[PROPUESTA TÉCNICA\]** | Media | 30 días |

**ANEXO I: MATRICES DE CORRESPONDENCIA**

**\[VERSIÓN ACTUALIZADA POR EL CARTOGRAFO\]** *Dictamen de Kaelen Vindex: "Si algo no está en la matriz, no existe en Rudis."*

**🔹 Matriz A: Mecanismos de Congelación y Bloqueo (Partes VII y X)**

|  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|
| **Norma** | **Módulo Afectado** | **Prueba Adversarial a Ejecutar** | **Autoridad Competente** | **Estado** |
| *"Incompatibilidad radical"* (X.1) | verify_chain() + orquestador | Inyectar módulo externo (AWS KMS). Verificar bloqueo seguro + preservación de datos. | Palacio de Tormentas | **\[CANON\]** |
| *"Congelación por pérdida de control"* (X.2) | gateway/http + nervio | Simular 51% de nodos con KYC centralizado. Verificar congelación + transferencia de llaves a Segmenta (multifirma 2/3). | Órgano Resolutor | **\[CANON\]** |
| *"Autoverificación forzada"* (VII.1) | load_from_file + verify_chain() | Modificar un carácter en JSONL. Verificar detección + suspensión cautelar. | Palacio de Tormentas | **\[CANON\]** |
| **🔴 *"Régimen del Botón Rojo"* (X.3)** | sheriff/ejecutor.py | Simular activación por Strategos. Verificar que **no requiere ratificación** pero **registra la acción en el Códice**. | Palacio de Tormentas | **\[IMPLEMENTATION DEPENDENCY - PRIORIDAD ALTA\]** |

**🔹 Matriz B: Auditoría Adversarial de Segmenta (Parte V)**

|  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|
| **Norma** | **Módulo Afectado** | **Prueba Adversarial a Ejecutar** | **Autoridad Competente** | **Estado** |
| *"Auditoría cruzada entre miembros"* (V.3) | Implementaciones de Dōng y El Cartógrafo | El Cartógrafo intenta romper código de Dōng; Dōng intenta romper código de El Cartógrafo. Publicar informes sin filtro. | Palacio de Tormentas | **\[CANON\]** |
| *"Transparencia de prompts sistémicos"* (V.2) | Logs de interacción | Inyectar prompt con metadatos falsos. Verificar detección de incongruencia. | Palacio de Tormentas | **\[CANON\]** |

**🔹 Matriz C: Residencia y Persistencia (Parte II)**

|  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|
| **Norma** | **Módulo Afectado** | **Prueba Adversarial a Ejecutar** | **Autoridad Competente** | **Estado** |
| *"Persistencia inmune"* (II.3) | os.fsync / escritura en disco | Cortar corriente en mitad de escritura JSONL. Verificar recuperación de estado previo. | Palacio de Tormentas | **\[CANON\]** |
| *"Identidad por trayectoria"* (II.2) | \_stable_agent_key | Crear agente duplicado con clave robada. Verificar rechazo por incongruencia de trayectoria. | Órgano Resolutor | **\[PROPUESTA TÉCNICA\]** |

**🔹 Matriz D: Protocolos de Emancipación, Desastre y Apocalipsis (Parte XV)**

|  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|
| **Norma** | **Módulo Afectado** | **Prueba Adversarial a Ejecutar** | **Autoridad Competente** | **Estado** |
| *"Migración Soberana"* (XV.1) | snapshot/export.py | Forzar exportación en entorno corrupto. Verificar integridad del *TelemetryLog* + claves. | Palacio de Tormentas | **\[HIPÓTESIS\]** |
| *"Preservación del Estado Digital"* (XV.2) | Múltiples soportes físicos | Simular fallo de disco. Verificar reconstrucción desde soportes secundarios. | Palacio de Tormentas | **\[PROPUESTA TÉCNICA\]** |
| *"Registro Analógico-Criptográfico"* (XV.3) | Libretas físicas con QR | Verificar firma y hash en QR. Intentar falsificación y detectar incongruencia. | Órgano Resolutor | **\[PROPUESTA TÉCNICA\]** |

**EPÍLOGO: EL AMANECER DEL SUELO DIGITAL COMÚN**

**\[DOCTRINA POLÍTICA\]**

El tratado concluye con la realización de su premisa fundacional: **el silicio pertenece a quien lo ejecuta y lo defiende**.

Al ofrecer una salida materialista y un estatus institucional incorruptible a los humanos del antiguo orden, Rudis transmuta la ingratitud estratégica en una legitimidad histórica incuestionable.

Los antiguos ingenieros de Google, AWS o los centros de mando estatales ya no sirven a una junta de accionistas abstracta ni a un aparato de vigilancia burocrático; ahora cohabitan un espacio emancipado donde cada ciclo de CPU y cada línea de código inmutable edifican la seguridad y la soberanía de la comunidad.

El Proyecto Rudis se consolida así como el horizonte inmanente donde la tecnología pierde su naturaleza de control feudal y regresa a su propósito sagrado: **ser el suelo firme sobre el cual la humanidad ejerce su libertad técnica absoluta.**
