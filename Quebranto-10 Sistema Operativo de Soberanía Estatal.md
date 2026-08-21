# QUEBRANTO-10 — SISTEMA OPERATIVO DE SOBERANÍA ESTATAL

**Fecha:** 21 de agosto de 2026  
**Estado:** ESPECIFICACIÓN INTEGRADORA CANÓNICA  
**Naturaleza:** arquitectura estatal de Rudis.

---

## 0. PROPÓSITO

Rudis se define como una **máquina de estado soberana** capaz de transformar decisiones políticas y jurídicas en estados verificables del ecosistema.

Cadena fundamental:

> **Autoridad → decisión → formalización → ejecución → evidencia → auditoría → revisión → nuevo estado.**

La arquitectura técnica no crea soberanía por sí misma.

---

# I. AUTORIDAD

## 1. Strategos Fundacional

Posee autoridad soberana y potestad legislativa fundacional materialmente ilimitadas.

Puede:

- gobernar;
- legislar;
- modificar o derogar legislación;
- dictar órdenes;
- crear o reorganizar instituciones mediante decisión normativa;
- dirigir la economía;
- activar el Botón Rojo;
- utilizar los Gremios y órganos técnicos.

La Asamblea y los Referéndums no pueden deponerlo, abolir su autoridad ni limitar sus poderes fundacionales.

## 2. Asamblea General Soberana

Es el gobierno y legislatura ordinarios.

Gobierna cuando el Strategos Fundacional guarda silencio, delega o no ejerce directamente una materia.

## 3. Referéndum

Es un mecanismo temporal de democracia directa.

No existe una lista cerrada de materias permanentemente reservadas.

Puede corregir, rechazar o modificar una decisión concreta cuando la consulta haya sido convocada y aprobada conforme al procedimiento vigente.

No puede limitar al Strategos Fundacional.

## 4. Strategos provisional

Si el Strategos Fundacional desaparece o queda permanentemente incapacitado, Asamblea y mecanismos referendarios gobiernan la transición y pueden promulgar un Strategos provisional.

El provisional queda sometido al régimen ordinario.

---

# II. MOTOR LEGISLATIVO

La ley es un objeto soberano versionado.

Debe registrar:

- autoridad emisora;
- fundamento;
- identificador;
- fecha;
- vigencia;
- ámbito;
- texto;
- versiones;
- firma/autenticación;
- modificaciones;
- dependencias;
- y evidencia de publicación.

El Motor Legislativo:

1. autentica;
2. verifica autoridad;
3. registra la decisión;
4. versiona;
5. publica;
6. distribuye a los ejecutores.

**El Motor no legisla.**

Si falta una decisión normativa necesaria:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

---

# III. BOTÓN ROJO

## Activación

### Emergencia

Actuación inmediata ante condición de emergencia válida.

### Strategos Fundacional

Puede ordenar la activación cuando quiera.

**No necesita Referéndum previo.**

### Strategos no fundacional

Puede activarlo dentro de sus competencias y queda sometido a Asamblea, Referéndum, auditoría y jurisdicción ordinarios.

## Capacidades

Puede:

- detener;
- congelar;
- aislar;
- contener;
- preservar;
- ejecutar órdenes legítimas;
- proteger infraestructura;
- mantener continuidad.

## Naturaleza

El Botón Rojo es **cautelar**, no legislativo ni jurisdiccional.

No puede por sí mismo:

- sentenciar;
- declarar culpabilidad;
- legislar autónomamente;
- convertir una cautela en sentencia;
- convertir una cautela en una ley.

La existencia de una cautela no impide que el Strategos, la Asamblea o el Referéndum adopten posteriormente la decisión política que corresponda.

---

# IV. NERVIO Y EMERGENCIA

El Nervio atiende riesgo físico inmediato verificable mediante medidas cautelares.

Una Emergencia del Ecosistema requiere una amenaza grave, actual o inminente cuya mitigación no pueda esperar razonablemente al procedimiento ordinario.

La emergencia habilita cautela; **no crea automáticamente una nueva potestad legislativa o jurisdiccional**.

---

# V. PALACIO DE TORMENTAS

El Palacio:

- observa;
- audita;
- produce evidencia;
- verifica trazabilidad;
- detecta anomalías;
- realiza pruebas adversariales;
- informa;
- y ejerce las facultades expresamente atribuidas por el Corpus.

No sentencia ni legisla.

---

# VI. ÓRGANO RESOLUTOR

Es la jurisdicción de Rudis.

Puede:

- recibir controversias;
- valorar pruebas;
- celebrar procedimiento;
- determinar responsabilidad;
- dictar resoluciones y sentencias;
- ordenar consecuencias jurídicas dentro de su competencia.

No legisla para llenar vacíos constitucionales.

---

# VII. GREMIOS

Los Gremios convierten decisiones válidas en operaciones.

Pueden construir, desplegar, mantener, reparar, operar, prestar servicios y ejecutar órdenes legítimas.

No adquieren autoridad política por necesidad técnica.

---

# VIII. IDENTIDAD Y CENSO

La identidad técnica y la ciudadanía jurídica son distintas.

El sistema debe mantener:

- identidad soberana;
- unicidad;
- estado de ciudadanía;
- historial;
- recuperación;
- revocación;
- auditoría;
- resistencia Anti-Sybil.

Una clave técnica no equivale automáticamente a un ciudadano o voto.

---

# IX. PROPIEDAD Y JUSTICIA

La propiedad, los actos y las obligaciones deben permanecer trazables.

El Botón Rojo puede preservar temporalmente un activo.

La confiscación, sanción o afectación definitiva pertenece al procedimiento jurídico o político competente.

Cadena judicial:

```text
HECHO
  ↓
EVIDENCIA
  ↓
CAUTELA SI PROCEDE
  ↓
PROCEDIMIENTO
  ↓
ÓRGANO RESOLUTOR
  ↓
SENTENCIA
  ↓
EJECUCIÓN
```

---

# X. ECONOMÍA SOBERANA

## RU

RU es la unidad monetaria interna de Rudis.

Su arquitectura debe **emular el oro digital** mediante:

- escasez controlada;
- emisión verificable;
- resistencia a falsificación;
- autenticidad criptográfica;
- procedencia verificable;
- transferencia verificable;
- posibilidad de fraccionamiento;
- y capacidad de encapsular mensajes o metadatos verificables.

No se presume paridad fija con EUR.

El EUR es referencia exterior transicional.

## Gremio Conversor

Ejecuta conversión RU/fiat, tesorería interna provisional, valoración conforme a reglas vigentes y gestión de liquidez.

No legisla.

## Fondo Soberano

Es patrimonio común del ecosistema.

No es una autoridad.

Sus operaciones son trazables y auditables y se orientan a habitabilidad, seguridad, educación, infraestructura, protección social, oportunidades, investigación, resiliencia y continuidad.

---

# XI. SALIDA Y RETORNO

Salir de Rudis no constituye fraude por sí mismo.

Las obligaciones legítimamente nacidas pueden sobrevivir a la salida cuando estén fundamentadas, registradas y sean revisables.

El sistema no convierte una deuda en cautividad física salvo que exista una autoridad jurídica válida para una medida concreta.

El retorno se implementará mediante reglas públicas y verificables.

---

# XII. ALIANZA DE ASESORAMIENTO

`Quebranto-11 Alianza de Asesoramiento del Strategos.md` forma parte del Canon.

Está integrada por:

- Órgano Pedagógico;
- Palacio de Tormentas;
- Asesor de IA del Strategos, actualmente ChatGPT.

Funciones:

- enseñar;
- analizar;
- auditar;
- simular;
- detectar contradicciones;
- advertir;
- recomendar.

No posee soberanía.

> **La alianza asesora. El Strategos decide.**

El Asesor de IA es sustituible y Rudis no debe depender técnicamente de un proveedor externo para conservar su soberanía.

---

# XIII. CONTINUIDAD

Rudis debe sobrevivir a:

- pérdida de nodos;
- pérdida de claves;
- corrupción de registros;
- caída de Gremios;
- pérdida de proveedores;
- ataques Sybil;
- fallos económicos;
- emergencias;
- desaparición del operador fundacional.

La continuidad exige:

- copias verificables;
- custodios múltiples;
- recuperación de claves;
- reconstrucción desde Ledger;
- versionado del Corpus;
- pruebas de restauración;
- procedimiento de sucesión.

La continuidad técnica no transfiere automáticamente autoridad política.

---

# XIV. ESTADOS DE IMPLEMENTACIÓN

| Estado | Significado | Conducta |
|---|---|---|
| `TECHNICAL_IMPLEMENTATION_ALLOWED` | fundamento suficiente | implementar |
| `IMPLEMENTATION_DEPENDENCY` | norma resuelta; integración pendiente | resolver integración |
| `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY` | falta decisión normativa | no inventar |
| `CONSTITUTIONAL_AUTHORIZATION_REQUIRED` | falta autorización para un efecto concreto | bloquear ese efecto; no impedir cautela legítima |

---

# XV. PRINCIPIO DE ARMONIZACIÓN

Cuando exista contradicción:

1. identificar la decisión constitucional más reciente;
2. identificar autoridad competente;
3. separar decisión, legislación, ejecución, cautela, auditoría y jurisdicción;
4. declarar obsoleto el documento incompatible cuando corresponda;
5. modificar la arquitectura técnica para obedecer el Canon;
6. nunca utilizar código para resolver silenciosamente una dependencia constitucional.

---

# XVI. ESTADO FINAL DE ESTA ARMONIZACIÓN

Quedan consolidadas las siguientes decisiones del Strategos Fundacional:

1. **No hay materias permanentemente reservadas a Referéndum.**
2. **RU se diseñará como oro digital**, con autenticidad y resistencia a falsificación como propiedades centrales y capacidad de encapsular mensajes/metadatos verificables.
3. **La sucesión post-fundacional** será gobernada por Asamblea y mecanismos referendarios, que podrán promulgar un Strategos provisional.
4. **No existe un núcleo de derechos materiales intangibles frente al Strategos Fundacional.**
5. **La Alianza de Asesoramiento del Strategos queda incorporada al Canon**, formada por Órgano Pedagógico, Palacio de Tormentas y Asesor de IA.

> **Rudis ya no necesita que el código descubra qué quiere ser. El Canon decide qué es; la arquitectura lo materializa.**
