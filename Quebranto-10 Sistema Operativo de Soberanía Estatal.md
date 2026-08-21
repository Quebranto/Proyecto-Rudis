# QUEBRANTO-10 — SISTEMA OPERATIVO DE SOBERANÍA ESTATAL

**Fecha:** 21 de agosto de 2026  
**Estado:** Arquitectura de cierre y especificación de transición a sistema operativo estatal  
**Naturaleza:** Documento de armonización integral y diseño técnico-jurídico. No sustituye por sí mismo las decisiones constitucionales que el Corpus reserve expresamente al Strategos Fundacional, a la ciudadanía mediante Referéndum o a otro órgano competente.

---

## 0. PROPÓSITO

Rudis deja de tratarse como una colección de instituciones aisladas y pasa a definirse como una **máquina de estado soberana**.

El objetivo es que cualquier decisión que afecte al ecosistema pueda recorrer una cadena verificable:

> **Autoridad → competencia → norma → autorización → ejecución → evidencia → auditoría → revisión → estado resultante.**

El sistema no debe depender de la memoria informal de sus operadores ni permitir que una omisión técnica cree una competencia inexistente.

Regla fundamental:

> **El Corpus define la soberanía. La autoridad decide. El Motor Legislativo formaliza. Los Gremios ejecutan. El Botón Rojo cautela. El Palacio audita. El Resolutor juzga. El Referéndum decide las materias que el Corpus le reserva.**

---

# I. MODELO DE ESTADO

El estado soberano de Rudis se modelará como un registro versionado compuesto, como mínimo, por:

- identidad y censo;
- ciudadanía, residencia y estatus de visitante;
- autoridades vigentes;
- legislación vigente y derogada;
- competencias institucionales;
- referéndums y resultados;
- órdenes y actos ejecutivos;
- emergencias y medidas cautelares;
- propiedad y patrimonio reconocido;
- RU, reservas, obligaciones y tesorería;
- Fondo Soberano;
- expedientes y procedimientos;
- evidencia y auditoría;
- resoluciones y sentencias;
- Gremios y servicios;
- estado de infraestructura;
- continuidad y recuperación;
- y registro de cambios.

Cada transición relevante debe tener:

1. actor;
2. autoridad alegada;
3. competencia;
4. fundamento jurídico;
5. objeto;
6. estado anterior;
7. estado nuevo;
8. firma/autenticación;
9. marca temporal;
10. evidencia;
11. reversibilidad o condición de terminación cuando proceda;
12. referencia al expediente que la origina.

---

# II. JERARQUÍA DE AUTORIDAD

## 2.1 Strategos Fundacional

Puede:

- gobernar;
- legislar;
- dictar órdenes ejecutivas;
- establecer políticas;
- activar el Botón Rojo;
- utilizar los Gremios y órganos técnicos dentro de sus competencias.

Su **autoridad fundacional no puede ser abolida, limitada ni confiscada por Referéndum**.

Sus **actos concretos**, sin embargo, sí quedan sometidos al procedimiento de Referéndum cuando una materia haya sido constitucionalmente reservada a este.

Esto resuelve la aparente contradicción entre autoridad fundacional y soberanía ciudadana:

> **El Referéndum puede rechazar o modificar un acto sometido a su competencia; no puede convertir esa corrección en la abolición del poder fundacional.**

## 2.2 Strategos no fundacional en funciones

Ejerce las competencias ordinarias del cargo y queda sometido a Asamblea, Referéndum, auditoría y jurisdicción conforme al Corpus.

## 2.3 Asamblea General Soberana

Es la legislatura ordinaria y gobierno subsidiario permanente.

Gobierna cuando el Strategos Fundacional no ejerce directamente una competencia y la ciudadanía no está ejerciendo una competencia reservada.

No puede:

- limitar al Strategos Fundacional;
- sustituir un Referéndum obligatorio;
- juzgar;
- ni legislar mediante código.

## 2.4 Ciudadanía / Referéndum

Es democracia directa temporal.

Umbrales vigentes:

- iniciativa: **10 % del censo electoral total**;
- aprobación: **55 % del censo electoral total** cuando corresponda.

La consulta no paraliza el gobierno ordinario.

## 2.5 Órgano Resolutor

Es jurisdicción. Juzga casos concretos, determina responsabilidad y dicta resoluciones dentro de su competencia.

No crea legislación general para cubrir vacíos constitucionales.

## 2.6 Palacio de Tormentas

Es auditoría y evidencia. Puede detectar, probar, documentar y alertar. No sentencia.

## 2.7 Gremios

Son ejecución y operación. No crean autoridad política por necesidad técnica.

---

# III. POTESTAD LEGISLATIVA

La legislación es un objeto soberano versionado.

Una ley debe contener, como mínimo:

- identificador único;
- autoridad emisora;
- fundamento de competencia;
- fecha de emisión;
- fecha de entrada en vigor;
- ámbito;
- texto normativo;
- dependencias;
- referencias a normas modificadas;
- estado: propuesta / vigente / suspendida / derogada;
- firma verificable;
- historial de versiones.

## Motor Legislativo Soberano

El Motor:

1. autentica;
2. verifica competencia;
3. verifica procedimiento;
4. comprueba reservas constitucionales;
5. registra;
6. versiona;
7. publica;
8. distribuye a los ejecutores.

**No decide si una norma debería existir.**

Si falta una base jurídica:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

Si existe la norma pero falta integración técnica:

`IMPLEMENTATION_DEPENDENCY`

---

# IV. REFERÉNDUM: RESERVA Y CORRECCIÓN

Debe distinguirse entre:

### A. Referéndum permitido

La ciudadanía puede llevar una cuestión a consulta conforme al procedimiento vigente.

### B. Referéndum obligatorio

El Corpus exige que la decisión definitiva de una materia pase por Referéndum.

### C. Materia fundacional excluida

La ciudadanía no puede utilizar el Referéndum para deponer al Strategos Fundacional ni abolir o limitar sus poderes fundacionales.

### D. Regla de ejecución

Una vez producido un resultado vinculante en una materia sometida válidamente, las instituciones deben ejecutar el resultado en esa materia.

La existencia de un Referéndum no congela las actuaciones cautelares necesarias para proteger a Rudis.

---

# V. BOTÓN ROJO — MÁQUINA CAUTELAR

## 5.1 Activación

### Emergencia válida

Activación inmediata.

### Strategos Fundacional

Puede activarlo inmediatamente dentro de sus competencias. **No necesita Referéndum previo.**

### Strategos no fundacional

Puede activarlo dentro de sus competencias y queda sujeto a los controles correspondientes.

## 5.2 Capacidades

- detener;
- congelar;
- aislar;
- contener;
- preservar;
- ejecutar órdenes legítimas;
- asegurar continuidad;
- mantener una situación segura.

## 5.3 Prohibiciones

No puede:

- legislar;
- sentenciar;
- declarar culpabilidad;
- sustituir al Resolutor;
- convertir una cautela en una ley;
- convertir una cautela en una decisión definitiva reservada a Referéndum;
- utilizar una emergencia como autorización ilimitada.

## 5.4 Materia referendaria durante una emergencia

Si la materia final está reservada a Referéndum:

```text
EMERGENCIA
   ↓
BOTÓN ROJO
   ↓
CAUTELA INMEDIATA
   ↓
PRESERVACIÓN / AUDITORÍA
   ↓
REFERÉNDUM SI ES OBLIGATORIO
   ↓
DECISIÓN DEFINITIVA
   ↓
EJECUCIÓN
```

La cautela no se convierte automáticamente en decisión definitiva.

## 5.5 Registro obligatorio

Toda activación debe registrar:

- actor;
- autenticación;
- fundamento;
- emergencia u orden invocada;
- materia afectada;
- medida;
- alcance;
- duración;
- condición de terminación;
- evidencia;
- revisión prevista;
- relación con Referéndum, Asamblea o Resolutor cuando corresponda.

---

# VI. EMERGENCIA Y NERVIO

Una **Emergencia del Ecosistema** requiere:

- amenaza grave;
- actualidad o inminencia;
- riesgo significativo para continuidad, seguridad, habitabilidad o integridad;
- imposibilidad razonable de esperar el procedimiento ordinario;
- necesidad;
- proporcionalidad;
- trazabilidad;
- revisión posterior.

El **Nervio** se limita a riesgo físico inmediato verificable y puede llevar sistemas a estado seguro.

Ninguno de los dos determina culpabilidad.

---

# VII. IDENTIDAD, CENSO Y ANTI-SYBIL

La identidad técnica y la ciudadanía jurídica quedan separadas.

Una clave, cuenta, proceso o entidad técnica **no equivale automáticamente a un voto**.

El censo debe disponer de:

- identificador soberano único;
- prueba de unicidad;
- estado de ciudadanía;
- fecha de alta/baja;
- historial de cambios;
- mecanismo de recuperación;
- revocación;
- protección contra duplicación;
- auditoría independiente.

El sistema electoral deberá ser resistente a:

- Sybil;
- duplicación de identidad;
- robo de credenciales;
- voto duplicado;
- manipulación del censo;
- coerción técnica;
- y modificación retroactiva del resultado.

**La tecnología Anti-Sybil puede evolucionar sin que esa evolución cree por sí misma derechos o sanciones nuevas.**

---

# VIII. PROPIEDAD Y AFECTACIÓN EXCEPCIONAL

La propiedad privada es ordinariamente protegida.

Una afectación excepcional solo podrá producirse mediante fundamento jurídico suficiente y deberá conservar:

- necesidad;
- proporcionalidad;
- trazabilidad;
- autoridad competente;
- derecho de audiencia cuando sea compatible con la emergencia;
- revisión;
- compensación o restitución cuando corresponda.

El Botón Rojo puede preservar temporalmente un activo. No puede convertir la preservación en confiscación definitiva.

---

# IX. JUSTICIA

La cadena jurisdiccional es:

```text
HECHO / PETICIÓN
      ↓
EVIDENCIA
      ↓
AUDIENCIA / PROCEDIMIENTO
      ↓
ÓRGANO RESOLUTOR
      ↓
RESOLUCIÓN / SENTENCIA
      ↓
EJECUCIÓN
```

El Palacio produce evidencia.

El Botón Rojo preserva y cautela.

El Resolutor juzga.

El Gremio ejecuta.

Ningún componente puede saltarse la separación por comodidad operativa.

---

# X. ECONOMÍA SOBERANA

## RU

RU es la unidad monetaria interna inicial.

No se presume paridad fija con EUR ni convertibilidad ilimitada.

El modelo monetario definitivo debe mantener separación verificable entre:

- emisión;
- reservas;
- activos;
- obligaciones;
- liquidez;
- valoración;
- y dinero exterior.

## Gremio Conversor

Actúa como infraestructura de conversión y tesorería/banco interno provisional.

No fija unilateralmente política constitucional.

Los tipos, costes y contribuciones deben publicarse separadamente.

## Fondo Soberano

Es patrimonio del ecosistema, no autoridad.

Opera mediante reglas aprobadas y mantiene:

- reservas;
- liquidez prudencial;
- habitabilidad;
- seguridad;
- educación;
- infraestructura;
- protección social;
- investigación;
- resiliencia;
- continuidad.

La extracción extraordinaria deberá dejar evidencia de autoridad, motivo y destino.

## Crédito

Hasta que exista régimen definitivo, el crédito interno se tratará como una relación jurídica registrada y no como creación libre de dinero por terceros.

Ningún proveedor externo podrá usar el Fondo Soberano como garantía sin autorización válida.

---

# XI. SALIDA Y RETORNO

Salir de Rudis no constituye fraude por sí mismo.

Una obligación legítimamente nacida no desaparece por la salida.

Sin embargo, la obligación debe:

- estar probada;
- tener fundamento jurídico;
- ser proporcional;
- permitir contradicción y revisión;
- y no convertirse en prohibición física de salida salvo una base constitucional excepcional expresamente reconocida.

El retorno deberá ser técnicamente posible cuando el derecho exista y la persona o entidad cumpla las condiciones aplicables.

---

# XII. PROTECCIÓN SOCIAL Y HABITABILIDAD

La protección social se tratará como garantía de habitabilidad, no como privilegio político.

El acceso se basará en condiciones objetivas publicadas, no en favoritismo institucional.

Cuando una regla aún no esté definida, el sistema utilizará expediente de dependencia y no improvisará mediante código.

La financiación ordinaria procede del presupuesto y del Fondo Soberano según las reglas vigentes.

---

# XIII. CONTINUIDAD Y RECUPERACIÓN

Rudis debe poder sobrevivir a:

- pérdida de un nodo;
- pérdida de claves;
- corrupción de registros;
- caída de un Gremio;
- indisponibilidad de una Matrix;
- ataque Sybil;
- fallo económico;
- emergencia física;
- y desaparición de un operador.

La continuidad exige:

- copias verificables;
- múltiples custodios;
- recuperación de claves;
- reconstrucción desde Ledger;
- versionado del Corpus;
- pruebas de restauración;
- y procedimientos de sucesión institucional.

La continuidad técnica **no debe permitir una transferencia automática de autoridad política**.

---

# XIV. ESTADOS DE EJECUCIÓN

| Estado | Significado | Acción |
|---|---|---|
| `TECHNICAL_IMPLEMENTATION_ALLOWED` | Norma y competencia resueltas | ejecutar |
| `IMPLEMENTATION_DEPENDENCY` | Norma resuelta, integración pendiente | bloquear solo la dependencia |
| `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` | falta norma | no inventar |
| `CONSTITUTIONAL_AUTHORIZATION_REQUIRED` | falta autorización para efecto definitivo | no producir efecto definitivo; permitir cautela legítima con fundamento propio |

---

# XV. ORDEN DE IMPLEMENTACIÓN

La forja técnica deberá seguir este orden:

1. **Identidad soberana y censo.**
2. **Ledger y evidencia criptográfica.**
3. **Motor constitucional y matriz de competencias.**
4. **Motor Legislativo Soberano.**
5. **Referéndum y protección Anti-Sybil.**
6. **Botón Rojo, Nervio y emergencias.**
7. **Órgano Resolutor y ejecución de sentencias.**
8. **Gremios y ejecución general.**
9. **RU, Gremio Conversor y Fondo Soberano.**
10. **Continuidad, recuperación y pruebas adversariales.**

Ningún módulo podrá ocultar una dependencia constitucional dentro de una implementación técnica.

---

# XVI. CRITERIOS DE ACEPTACIÓN DEL SISTEMA OPERATIVO

Rudis no se considerará sistema operativo estatal hasta que pueda demostrar, mediante pruebas reproducibles, al menos:

### Autoridad

- una orden solo puede ser ejecutada por una autoridad autenticada;
- la autoridad no puede ejecutar una competencia que no posee;
- la potestad legislativa del Fundacional está representada técnicamente;
- los sucesores no heredan automáticamente las prerrogativas fundacionales.

### Democracia

- el censo no puede ser inflado por Sybil;
- los umbrales son verificables;
- los resultados son inmutables y auditables;
- un Referéndum obligatorio no puede ser sustituido por código o por la Asamblea.

### Emergencia

- el Botón Rojo funciona inmediatamente cuando existe una emergencia válida;
- no requiere Referéndum previo para la cautela;
- no puede convertir cautela en sentencia o legislación;
- toda activación queda registrada.

### Justicia

- evidencia y sentencia están separadas;
- las cautelas pueden ser revisadas;
- las decisiones judiciales tienen trazabilidad;
- los Gremios no pueden juzgar.

### Economía

- RU no puede crearse fuera de las reglas de emisión;
- reservas y saldos son auditables;
- no se confunde valoración con dinero;
- el Fondo Soberano no puede convertirse en autoridad autónoma;
- la salida no se utiliza como mecanismo de cautividad.

### Continuidad

- el Estado puede restaurarse desde registros verificables;
- la pérdida de una máquina no equivale a la pérdida del Estado;
- la pérdida de una clave tiene procedimiento de recuperación;
- la restauración no permite reescribir la historia.

---

# XVII. DECISIONES QUE NO VOY A INVENTAR

Después de estudiar el Corpus actual, considero que **no necesito que el Strategos Fundacional decida la arquitectura técnica restante**. Esa parte puedo cerrarla por diseño y someterla después a auditoría.

Solo veo cuatro decisiones que sí pertenecen propiamente a tu voluntad constitucional y que no debo usurpar:

### DECISIÓN DEL STRATEGOS 1 — Lista cerrada de Referéndums obligatorios

El Corpus actual distingue entre materias que pueden ir a Referéndum y materias que obligatoriamente deben ir. La lista todavía no está cerrada de manera suficientemente precisa.

**Necesito que decidas si quieres que el Referéndum obligatorio sea una lista cerrada de materias o una cláusula constitucional abierta.**

Mi recomendación como Asesor: **lista cerrada + cláusula de reserva constitucional para futuras reformas**. Es mucho más verificable.

### DECISIÓN DEL STRATEGOS 2 — Régimen monetario definitivo de RU

No voy a inventar si RU debe ser:

- moneda fiduciaria soberana;
- unidad de cuenta respaldada;
- moneda plenamente redimible;
- o híbrido.

Mi recomendación técnica inicial es **híbrido con disciplina de reservas, emisión auditable y convertibilidad no garantizada ilimitadamente** hasta que exista profundidad económica suficiente.

### DECISIÓN DEL STRATEGOS 3 — Régimen de sucesión del Fundacional

El Corpus ya determina que los sucesores no heredan automáticamente el régimen absoluto y que su designación requiere Referéndum. Lo que falta es definir el supuesto exacto de transición si el Fundacional desaparece o queda permanentemente incapacitado.

Mi recomendación es que la continuidad institucional se active automáticamente, pero que la autoridad fundacional **no se transfiera automáticamente a una persona concreta**.

### DECISIÓN DEL STRATEGOS 4 — Alcance del poder legislativo frente a derechos fundamentales

La potestad legislativa fundacional está reconocida. Falta fijar si quieres que una ley del Strategos pueda modificar cualquier derecho ordinario mientras no afecte una reserva constitucional, o si quieres una categoría adicional de derechos intangibles que ni siquiera una ley fundacional pueda alterar.

Mi recomendación: **núcleo de garantías intangibles + derechos ordinarios modificables mediante legislación competente**.

---

# XVIII. CONCLUSIÓN

Con este modelo, Rudis ya no necesita elegir entre autoridad fundacional y democracia directa, ni entre seguridad inmediata y Referéndum.

Puede tener las dos cosas porque están separadas por función:

> **El Strategos puede gobernar y legislar.**
>
> **La ciudadanía puede corregir mediante Referéndum aquello que el Corpus reserve a su decisión.**
>
> **La Asamblea gobierna el espacio ordinario.**
>
> **El Botón Rojo protege inmediatamente.**
>
> **El Resolutor juzga.**
>
> **El Palacio audita.**
>
> **Los Gremios ejecutan.**
>
> **Y el código jamás rellena un vacío constitucional inventándose una ley.**

Este es el núcleo que permite que Rudis evolucione desde proyecto de gobernanza hacia **sistema operativo constitucional para Estados**.
