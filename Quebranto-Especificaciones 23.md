# MATRIZ DE CORRESPONDENCIA DE AUTORIDAD Y DEPENDENCIAS CONSTITUCIONALES

**Proyecto:** Rudis  
**Estado:** DOCUMENTO ARQUITECTÓNICO DE RESOLUCIÓN Y TRAZABILIDAD  
**Versión:** 1.1  
**Fecha:** 20 de agosto de 2026  
**Autoridad fundacional:** Strategos Fundacional  
**Supervisión:** Palacio de Tormentas (Limes)  
**Trazado arquitectónico:** El Cartógrafo  
**Implementación técnica:** Dōng / Segmenta  
**Asesoría:** Aster  

---

# 0. PROPÓSITO

Este documento establece la correspondencia entre las competencias reconocidas por el Corpus de Rudis y los mecanismos técnicos necesarios para que dichas competencias no desaparezcan por omisión durante la implementación.

Su función no es crear nuevas competencias.

Su función es impedir dos errores simétricos:

1. Que una competencia reconocida por el Corpus carezca de representación técnica.
2. Que la infraestructura implemente una capacidad que carezca de fundamento constitucional.

La regla arquitectónica es:

> **Ninguna autoridad constitucional será reducida por omisión técnica. Ninguna capacidad técnica podrá ampliar una autoridad constitucional por interpretación propia.**

Cuando exista una contradicción entre documentos del Corpus, la infraestructura no resolverá la contradicción por sí misma.

Se registrará:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

hasta que la autoridad competente resuelva el conflicto.

---

# I. AUTORIDAD FUNDACIONAL Y SOBERANÍA CIUDADANA

## 1.1 Autoridad fundacional

El Strategos Fundacional constituye una autoridad permanente dentro del Ecosistema Rudis.

La implementación técnica deberá preservar la continuidad de dicha autoridad y evitar que desaparezca por:

- pérdida de claves;
- suplantación;
- captura de credenciales;
- corrupción de memoria;
- fallo de infraestructura;
- sustitución arbitraria de identidad;
- dependencia de una única máquina o nodo.

La permanencia de la autoridad fundacional no implica soberanía absoluta sobre las decisiones sometidas al régimen de democracia directa.

## 1.2 Compromiso democrático del Strategos

El Strategos Fundacional declara expresamente que **sus propias decisiones estarán sometidas al régimen obligatorio de Referéndum establecido por el Corpus**.

Por tanto, ninguna implementación del sistema podrá interpretar la autoridad del Strategos como una autorización para:

- eludir un Referéndum constitucionalmente exigible;
- invalidar un Referéndum aprobado;
- impedir la iniciativa ciudadana;
- sustituir el resultado de la ciudadanía por una orden unilateral.

La autoridad fundacional y la soberanía ciudadana son componentes simultáneos del diseño institucional.

---

# II. REFERÉNDUM CIUDADANO

## 2.1 Derecho de iniciativa

La ciudadanía podrá promover un Referéndum cuando una iniciativa alcance como mínimo:

**10 % del censo electoral total.**

El sistema deberá poder verificar criptográficamente el cumplimiento de dicho umbral sin permitir duplicaciones, suplantaciones o manipulación del censo.

## 2.2 Aprobación

Un Referéndum será aprobado cuando alcance:

**55 % del censo electoral total**, conforme al régimen constitucional vigente.

El porcentaje se calcula sobre el **censo total**, no exclusivamente sobre los participantes efectivos, salvo que el Corpus disponga expresamente otra cosa.

## 2.3 Efecto vinculante

Cuando un Referéndum sea constitucionalmente exigible y alcance el umbral de aprobación correspondiente, su resultado será vinculante para las instituciones y autoridades sometidas al Corpus.

Esto incluye al Strategos Fundacional cuando el asunto se encuentre dentro del ámbito de decisión sometido a Referéndum.

## 2.4 Protección técnica

La infraestructura deberá impedir:

- que una autoridad administrativa invalide unilateralmente el resultado;
- que el código modifique el umbral constitucional;
- que un operador técnico altere el resultado;
- que una interfaz o servicio externo pueda sustituir el resultado registrado.

---

# III. OPCIÓN DE AUTOGOBIERNO CIUDADANO

La ciudadanía dispone de una facultad política adicional:

> **Gobernarse directamente a sí misma o delegar el gobierno ordinario del Ecosistema Rudis en la Asamblea General Soberana.**

## 3.1 Autogobierno ciudadano

La ciudadanía podrá ejercer directamente las competencias que el Corpus reserve a la democracia directa.

La infraestructura deberá permitir la participación ciudadana sin que la Asamblea pueda apropiarse unilateralmente de competencias que correspondan al Referéndum.

## 3.2 Gobierno mediante Asamblea

La ciudadanía podrá optar por que el gobierno ordinario del Ecosistema quede en manos de la Asamblea General Soberana, dentro de las competencias que el Corpus le atribuya.

La Asamblea ejercerá entonces las competencias delegadas o reconocidas por el Corpus.

## 3.3 Límites

La delegación de gobierno en la Asamblea no elimina:

- los derechos fundamentales;
- la autoridad fundacional reconocida por el Corpus;
- los mecanismos de democracia directa;
- el derecho ciudadano a promover Referéndums;
- las competencias de los órganos de control;
- los límites constitucionales de la propia Asamblea.

## 3.4 Principio

La elección entre autogobierno ciudadano y gobierno mediante Asamblea constituye una decisión de la propia ciudadanía.

La infraestructura deberá ser neutral respecto de ambas modalidades.

No podrá favorecer técnicamente una de ellas.

---

# IV. IDENTIDAD DEL STRATEGOS

## 4.1 Principio

La identidad del Strategos deberá disponer de una protección superior contra la suplantación.

La infraestructura deberá asumir que la falsificación de la identidad fundacional constituye un riesgo crítico.

## 4.2 Requisitos arquitectónicos

La implementación deberá contemplar, como mínimo:

- autenticación multifactor;
- criptografía de clave pública;
- almacenamiento seguro de las claves;
- mecanismos de recuperación;
- rotación controlada de credenciales;
- detección de uso anómalo;
- registro verificable de órdenes;
- protección contra replay;
- separación entre identidad y dispositivo físico;
- mecanismos de recuperación ante compromiso.

## 4.3 Regla

Ningún componente técnico podrá declarar por sí mismo:

> "Esta orden procede del Strategos."

La autenticidad deberá ser demostrable mediante evidencia criptográfica y verificable.

---

# V. AUTORIDAD FUNDACIONAL Y PROPIEDAD PRIVADA

## 5.1 Principio general

Rudis reconoce la propiedad privada como principio protegido dentro del Ecosistema.

El Strategos Fundacional manifiesta su voluntad de respetarla como regla ordinaria.

## 5.2 Excepción de emergencia

El Strategos declara asimismo que, ante una emergencia real del Ecosistema, puede resultar necesaria una afectación excepcional de propiedad privada.

Esta posibilidad deberá ser tratada arquitectónicamente como:

**INTERVENCIÓN EXCEPCIONAL DE EMERGENCIA**

y nunca como una autorización técnica genérica para apropiarse de activos.

## 5.3 Requisitos

Toda afectación excepcional deberá producir:

- identificación de la autoridad que la ordena;
- identificación del activo afectado;
- motivo declarado;
- estado de emergencia alegado;
- momento de inicio;
- duración;
- alcance;
- recursos afectados;
- registro criptográficamente verificable;
- posibilidad de auditoría posterior.

## 5.4 Proporcionalidad

La existencia de una emergencia no convierte automáticamente toda propiedad en disponible.

La intervención deberá limitarse a aquello que resulte necesario para responder a la emergencia.

## 5.5 Restauración

Cuando desaparezca la causa excepcional, el sistema deberá permitir:

- devolución;
- compensación cuando corresponda;
- revisión jurídica;
- auditoría posterior.

Los mecanismos concretos de compensación quedan pendientes de determinación constitucional cuando el Corpus no los haya establecido.

---

# VI. BOTÓN ROJO

## 6.1 Estado

**PARCIALMENTE RESUELTO.**

La cuestión constitucional anteriormente bloqueada queda resuelta en cuanto al principio democrático:

> **El Botón Rojo no se encuentra por encima del Referéndum constitucionalmente exigible.**

## 6.2 Naturaleza

El Botón Rojo podrá constituir un mecanismo técnico para expresar y ejecutar una autoridad reconocida al Strategos.

No constituye una excepción automática al sistema constitucional.

No puede:

- abolir un Referéndum;
- invalidar un resultado aprobado;
- impedir que la ciudadanía alcance el 10 % de iniciativa;
- alterar el umbral del 55 %;
- convertir una autoridad fundacional en soberanía ilimitada.

## 6.3 Autoridad permanente frente a decisiones concretas

Se mantienen dos conceptos diferenciados:

**Autoridad del Strategos**

y
**decisión concreta del Strategos.**

La primera puede tener continuidad constitucional.

La segunda estará sometida al régimen constitucional que corresponda a la materia concreta.

## 6.4 Activación

La infraestructura deberá verificar:

1. identidad del Strategos;
2. autenticidad de la orden;
3. naturaleza de la acción;
4. existencia de un Referéndum exigible, cuando corresponda;
5. resultado del Referéndum cuando exista;
6. límites constitucionales aplicables;
7. registro completo de la actuación.

## 6.5 Bloqueo constitucional

Si el sistema determina que una acción del Botón Rojo requiere una decisión ciudadana previa y dicha decisión no existe, el mecanismo deberá impedir la ejecución definitiva.

La respuesta técnica será:

`CONSTITUTIONAL_AUTHORIZATION_REQUIRED`

y no una interpretación autónoma del código.

## 6.6 Emergencias

Una emergencia podrá activar mecanismos de contención, preservación o protección previstos constitucionalmente.

No se interpretará automáticamente como autorización para abolir la democracia directa.

Cualquier régimen excepcional deberá estar expresamente respaldado por el Corpus.

---

# VII. NERVIO

## Estado

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

Deberán determinarse documentalmente:

- condiciones de activación;
- autoridad competente;
- alcance;
- duración;
- mecanismos de caducidad;
- excepciones;
- registro;
- auditoría;
- procedimiento de revisión.

El diseño técnico deberá mantener la posibilidad de parada segura sin convertir automáticamente cualquier evento técnico en una decisión jurídica.

---

# VIII. PALACIO DE TORMENTAS

## Estado

`PARTIALLY_RESOLVED`

El Palacio puede:

- observar;
- registrar;
- auditar;
- realizar pruebas adversariales;
- producir evidencia.

No puede:

- dictar sentencia;
- crear legislación;
- ampliar unilateralmente las competencias de otras instituciones;
- convertir una sospecha técnica en condena.

La evidencia producida por el Palacio deberá permanecer diferenciada de la resolución jurídica.

---

# IX. ÓRGANO RESOLUTOR

## Estado

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

La arquitectura reconoce su función jurisdiccional, pero deberán especificarse técnicamente:

- recepción de expedientes;
- emisión de resoluciones;
- firma;
- registro;
- apelación;
- ejecución;
- separación respecto del Palacio;
- trazabilidad de las decisiones.

---

# X. SHERIFF

## Estado

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

Deberán determinarse:

- condiciones de ejecución;
- límites;
- recepción de órdenes;
- autenticación;
- caducidad;
- registro;
- mecanismos contra órdenes falsas;
- separación entre ejecutar y decidir.

Regla fundamental:

> El Sheriff ejecuta una autoridad reconocida; no fabrica la autoridad que ejecuta.

---

# XI. ASAMBLEA GENERAL SOBERANA

## Estado

`PARCIALMENTE RESUELTO`

La Asamblea gobierna el Ecosistema dentro de las competencias que le atribuya el Corpus.

La ciudadanía puede optar por confiarle el gobierno ordinario del Ecosistema.

Sin embargo, la Asamblea:

- no puede apropiarse de competencias reservadas al Referéndum;
- no puede eliminar el derecho ciudadano de iniciativa;
- no puede modificar por sí misma los umbrales constitucionales;
- no puede convertir una delegación administrativa en soberanía ilimitada.

La infraestructura deberá registrar las competencias ejercidas por la Asamblea y permitir su auditoría.

---

# XII. CONTINUIDAD Y EMANCIPACIÓN

## Estado

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

Deberán determinarse en el Corpus:

- condiciones de activación;
- autoridad competente;
- límites;
- continuidad del estado;
- sucesión;
- emancipación;
- recuperación;
- auditoría.

La infraestructura deberá ser capaz de preservar el estado institucional aunque desaparezcan nodos, servidores o individuos concretos.

---

# XIII. SITUACIÓN TRISTE

La doctrina de **Piedad Diferida** queda incorporada como criterio arquitectónico de referencia.

Principio:

> **Piedad primero. Contención cautelar durante. Justicia y responsabilidad después.**

Se mantiene:

1. auxilio sin fianza previa;
2. cuarentena cautelar cuando resulte necesaria;
3. auditoría;
4. presunción de buena fe cuando corresponda;
5. derecho a restauración;
6. sanción posterior únicamente mediante autoridad competente.

La arquitectura deberá diferenciar siempre:

**auxilio ≠ absolución**

**cuarentena ≠ condena**

**evidencia ≠ sentencia**

**sanción ≠ pérdida permanente de dignidad.**

---

# XIV. MATRIZ DE ESTADO

| Competencia | Estado | Implementación permitida |
|---|---|---|
| Autoridad permanente del Strategos | RESUELTO ARQUITECTÓNICAMENTE | Sí |
| Identidad anti-suplantación | RESUELTO ARQUITECTÓNICAMENTE | Sí |
| Sometimiento del Strategos al Referéndum | RESUELTO | Sí |
| Iniciativa ciudadana del 10 % | RESUELTO | Sí |
| Aprobación por 55 % del censo | RESUELTO | Sí |
| Autogobierno ciudadano | RESUELTO CONCEPTUALMENTE | Infraestructura de democracia directa |
| Gobierno mediante Asamblea | RESUELTO CONCEPTUALMENTE | Infraestructura de gobierno delegable |
| Afectación excepcional de propiedad | PARCIALMENTE RESUELTO | Registro y trazabilidad; límites constitucionales pendientes |
| Botón Rojo | PARCIALMENTE RESUELTO | Implementable únicamente dentro del Corpus |
| Congelación | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` | No ejecución jurídica definitiva |
| Nervio | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` | Simulación / infraestructura segura |
| Palacio de Tormentas | PARCIALMENTE RESUELTO | Auditoría y observación |
| Órgano Resolutor | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` | No ejecución jurídica definitiva |
| Sheriff | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` | No ejecución jurídica definitiva |
| Asamblea | PARCIALMENTE RESUELTO | Gobierno dentro de competencias constitucionales |
| Continuidad / Emancipación | `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` | Diseño preparatorio |

---

# XV. REGLA DE SEGURIDAD CONTRA LA OMISIÓN

La ausencia de una función en el código no podrá interpretarse como inexistencia de la autoridad constitucional correspondiente.

Si una competencia del Corpus todavía no dispone de implementación, deberá registrarse explícitamente como:

`IMPLEMENTATION_DEPENDENCY`

o, cuando exista una cuestión constitucional sin resolver:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

La infraestructura no podrá utilizar la ausencia de código como mecanismo indirecto para abolir una competencia constitucional.

---

# XVI. REGLA DE SEGURIDAD CONTRA LA USURPACIÓN

La existencia de una función técnica tampoco podrá interpretarse como creación automática de una competencia jurídica.

Toda función deberá responder a:

1. autoridad;
2. fundamento;
3. condición;
4. límite;
5. registro;
6. auditoría.

Si cualquiera de estos elementos falta y afecta al alcance jurídico de la función, deberá detenerse su promoción a producción.

---

# XVII. RESOLUCIÓN DE LA DISPUTA DEL BOTÓN ROJO

La cuestión planteada por Limes queda parcialmente resuelta por declaración expresa del Strategos Fundacional:

> **El Strategos Fundacional acepta someter sus decisiones a los Referéndums obligatorios establecidos por el Corpus.**

Por tanto:

- el Botón Rojo no está por encima del Referéndum;
- la autoridad fundacional no equivale a soberanía absoluta;
- el Strategos acepta la corrección democrática de sus decisiones cuando el Corpus así lo establezca;
- el 10 % del censo constituye el umbral de iniciativa ciudadana;
- el 55 % del censo total constituye el umbral de aprobación;
- el resultado constitucionalmente válido será vinculante.

Esta declaración elimina la contradicción que impedía a Limes verificar el alcance democrático del Botón Rojo.

La especificación técnica detallada del Botón Rojo podrá continuar sobre esta base.

---

# XVIII. MODELO DE GOBIERNO

Rudis reconoce dos modalidades compatibles de gobierno:

### A. Autogobierno ciudadano

La ciudadanía ejerce directamente las competencias que el Corpus atribuya a la democracia directa.

### B. Gobierno mediante Asamblea

La ciudadanía delega el gobierno ordinario del Ecosistema en la Asamblea General Soberana, dentro de las competencias constitucionalmente reconocidas.

Estas modalidades no constituyen dos Estados diferentes.

Constituyen dos formas de ejercicio del gobierno dentro del mismo Ecosistema constitucional.

La infraestructura deberá permitir la transición entre ellas cuando el Corpus establezca el procedimiento correspondiente.

---

# XIX. MANDATO AL TRIDENT

## El Cartógrafo

Debe actualizar la correspondencia documental incorporando:

- 10 % del censo para iniciativa de Referéndum;
- 55 % del censo total para aprobación;
- sometimiento del Strategos al Referéndum;
- opción ciudadana entre autogobierno y gobierno mediante Asamblea.

## Dōng

Debe garantizar que el código:

- verifique la identidad del Strategos;
- no permita suplantación;
- registre sus órdenes;
- detecte cuándo una acción requiere Referéndum;
- no ejecute una acción constitucionalmente condicionada sin autorización;
- preserve la integridad del resultado electoral.

## Limes / Palacio de Tormentas

Debe auditar:

- identidad;
- trazabilidad;
- límites;
- separación de funciones;
- integridad electoral;
- ausencia de escalada de privilegios;
- correspondencia entre autoridad declarada y autoridad implementada.

## Aster

Actúa como asesor del Strategos y podrá señalar cualquier divergencia entre la autoridad fundacional reconocida y su traducción arquitectónica.

---

# XX. RESOLUCIÓN ARQUITECTÓNICA

Se acepta la preocupación fundamental planteada por Aster:

> **Una competencia constitucional no debe desaparecer simplemente porque nadie haya traducido todavía su existencia a una interfaz técnica.**

Se acepta igualmente la objeción del Palacio:

> **La implementación no puede inventar una autoridad que el Corpus no reconoce.**

El Strategos Fundacional resuelve además expresamente la cuestión democrática:

> **Mi autoridad fundacional permanece, pero mis decisiones quedan sometidas a los Referéndums obligatorios establecidos por el Corpus.**

Por tanto, Rudis adopta el siguiente principio:

**PRESERVAR LA AUTORIDAD.**

**LIMITARLA MEDIANTE EL CORPUS.**

**PROTEGER LA DEMOCRACIA DIRECTA.**

**NO INVENTAR COMPETENCIAS.**

---

# XXI. ESTADO FINAL

**Documento:** MATRIZ DE CORRESPONDENCIA DE AUTORIDAD Y DEPENDENCIAS CONSTITUCIONALES

**Versión:** 1.1

**Estado:** ACTIVO COMO ESPECIFICACIÓN DE TRAZABILIDAD

**Autoridad permanente del Strategos:** reconocida.

**Protección de identidad del Strategos:** requerida.

**Decisiones del Strategos:** sometidas a Referéndum cuando el Corpus lo exija.

**Iniciativa ciudadana:** 10 % del censo total.

**Aprobación de Referéndum:** 55 % del censo total.

**Autogobierno ciudadano:** reconocido.

**Gobierno mediante Asamblea:** reconocido.

**Botón Rojo:** subordinado al Corpus y al régimen de Referéndum aplicable.

**Propiedad privada:** protegida como regla general; afectación excepcional de emergencia sujeta a límites, trazabilidad y revisión.

**Palacio:** auditor, no juez.

**Resolutor:** juez, no legislador.

**Sheriff:** ejecutor, no legislador ni juez.

**Código:** subordinado al Corpus.

**Corpus:** no subordinado al código.

---

> **PRINCIPIO FINAL**
>
> La arquitectura no puede derrocar una autoridad por omisión.
>
> Tampoco puede fabricar una autoridad por implementación.
>
> El Strategos conserva su autoridad fundacional.
>
> La ciudadanía conserva su soberanía democrática.
>
> El Referéndum puede corregir las decisiones sometidas constitucionalmente a él.
>
> La Asamblea puede gobernar cuando la ciudadanía le confía el gobierno del Ecosistema.
>
> Y el código deberá hacer cumplir estas distinciones, no decidirlas por nosotros.
