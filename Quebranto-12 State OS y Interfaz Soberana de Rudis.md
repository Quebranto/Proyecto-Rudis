# QUEBRANTO-12 — STATE OS Y INTERFAZ SOBERANA DE RUDIS

**Fecha:** 21 de agosto de 2026  
**Estado:** ESPECIFICACIÓN CANÓNICA DE PRODUCTO Y ARQUITECTURA

## 0. PROPÓSITO

Rudis se convierte en un **State OS**: un sistema operativo para Estados capaz de representar, gobernar, ejecutar, observar, auditar, proteger y reconstruir un ecosistema soberano.

La interfaz de Rudis será el **mundo operativo visible** del State OS. El videojuego no será una maqueta separada: será su primera interfaz de simulación, inspección y operación.

> **El jugador ve el Estado; el State OS mueve el Estado; el Corpus determina qué puede hacer el Estado.**

La interfaz no sustituye al Corpus. Lo hace navegable.

## I. PRINCIPIO DE DISEÑO

Rudis deberá presentar el Estado como un sistema vivo y observable, no como una colección de menús.

La navegación deberá permitir pasar de:

**mundo → institución → proceso → decisión → orden → ejecución → evidencia → auditoría → consecuencia.**

Toda acción importante deberá responder: qué ocurre, quién tiene competencia, qué norma/mandato lo permite, quién ejecuta, qué recursos consume, qué riesgos produce, qué evidencia queda y si puede revisarse, detenerse o revertirse.

## II. EL MUNDO DE RUDIS COMO INTERFAZ

La representación principal será un **Atlas Soberano interactivo**. El usuario podrá recorrer Palacio de Tormentas, sede del Strategos, Asamblea, Referéndum, Órgano Resolutor, Gremios, Fondo Soberano, infraestructura, Zonas de Resonancia, nodos de identidad, Ledger, corredores económicos, interfaces con Matrixs y centros de continuidad.

Cada localización será simultáneamente:

**espacio visual + nodo institucional + estado técnico + fuente de eventos + interfaz de operación.**

## III. CAPAS DE VISUALIZACIÓN

1. **Mundo:** representación espacial y temporal.
2. **Gobierno:** instituciones, competencias, leyes, proyectos, presupuesto y decisiones.
3. **Infraestructura:** servidores, energía, redes, edificios, nodos, capacidad y dependencias.
4. **Riesgo:** emergencias, amenazas, vulnerabilidades, anomalías y continuidad.
5. **Evidencia:** Ledger, órdenes, firmas, expedientes, auditorías y cadena de custodia.

El usuario podrá cambiar de capa sin perder contexto espacial.

## IV. STATE OS COMO NÚCLEO

| Servicio | Función |
|---|---|
| **Sovereign Kernel** | estado soberano, autoridades y ciclo institucional |
| **Identity & Census** | identidad, ciudadanía, agentes, roles y Anti-Sybil |
| **Law Engine** | leyes, decretos, reglamentos, versiones y vigencia |
| **Decision Engine** | decisiones, competencias, delegaciones y mandatos |
| **Referendum Service** | consultas, censo, votación, resultados y efectos |
| **Red Button / Nervio** | emergencia, cautela, contención y continuidad inmediata |
| **Guild Runtime** | ejecución coordinada de Gremios |
| **Justice Runtime** | expedientes, pruebas, resoluciones y sentencias |
| **Palace Observatory** | auditoría, telemetría, pruebas y evidencia |
| **Economic Core** | RU, tesorería, Fondo Soberano y conversión |
| **Infrastructure Runtime** | construcción, capacidad, mantenimiento y migración |
| **Interoperability Bus** | conexión con sistemas externos y Matrixs |
| **Continuity Engine** | backup, recuperación, replicación y reconstrucción |
| **Advisory Mesh** | Órgano Pedagógico + Palacio + Asesor IA |
| **UI / World Layer** | interfaz del videojuego y operación |

Ningún servicio de ejecución adquiere autoridad por existir como servicio.

## V. GRAFO SOBERANO

El ecosistema será representado como un grafo de entidades, ciudadanía, instituciones, autoridades, leyes, decisiones, órdenes, recursos, activos, infraestructura, contratos, expedientes, evidencias, riesgos, eventos, votos y Referéndums.

Relaciones principales: posee, autoriza, depende de, ejecuta, audita, juzga, protege, financia, modifica, deriva de, sustituye, amenaza y preserva.

La interfaz deberá permitir preguntar:

> **¿Por qué existe esto?**

Y recorrer la cadena causal hasta su origen.

## VI. PANEL UNIVERSAL

Toda entidad, institución, infraestructura o norma tendrá:

```text
IDENTIDAD
ESTADO ACTUAL
AUTORIDAD
COMPETENCIAS
DEPENDENCIAS
RECURSOS
RIESGOS
HISTORIAL
EVIDENCIA
ACCIONES DISPONIBLES
```

Los controles se filtrarán por autoridad real. Estados obligatorios:

- `TECHNICAL_IMPLEMENTATION_ALLOWED`
- `IMPLEMENTATION_DEPENDENCY`
- `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`
- `CONSTITUTIONAL_AUTHORIZATION_REQUIRED`

## VII. CENTRO DE MANDO DEL STRATEGOS

El Strategos dispondrá de una interfaz propia con estado general, estabilidad, economía, población, infraestructura, emergencias, agenda política, legislación, advertencias del Palacio, recomendaciones de la Alianza, actividad de Asamblea/Referéndum, continuidad y Gremios.

Podrá promulgar, modificar y derogar legislación; emitir mandatos; delegar; ordenar construcción; asignar recursos; convocar consultas; ordenar cautelas; activar el Botón Rojo; investigar; simular; auditar y pedir asesoramiento.

Cuando la urgencia lo permita, el sistema mostrará impacto previsto antes de ejecutar. Una emergencia legítima puede entrar directamente en cautela.

## VIII. BOTÓN ROJO

Será una interfaz física/visual dentro del mundo, no un simple menú.

```text
NORMAL → ALERTA → CAUTELA → CONTENCIÓN / PRESERVACIÓN → PROCEDIMIENTO
```

Mostrará activador, fundamento, hora, alcance, activos afectados, medidas, evidencia, reversibilidad y procedimiento posterior.

**Nunca representará una cautela como sentencia.** No requiere Referéndum previo cuando su activación sea legítima conforme al Canon.

## IX. ASAMBLEA Y REFERÉNDUM

La Asamblea será una institución navegable con expedientes, deliberaciones, votos y consecuencias.

El Referéndum se representará como:

```text
PROPUESTA → CONVOCATORIA → CENSO → INFORMACIÓN → VOTACIÓN → RESULTADO → EFECTO → REGISTRO
```

El resultado se formalizará mediante el Motor Legislativo o Decision Engine según corresponda; no se convertirá directamente en una orden ejecutiva.

## X. PALACIO DE TORMENTAS

Será un observatorio visible de auditoría: evidencia, telemetría, pruebas adversariales, comparación de estados, anomalías, firmas, continuidad y expedientes.

> **El Palacio puede gritar PELIGRO; no convierte el aviso en sentencia.**

## XI. ÓRGANO RESOLUTOR

Su interfaz será un tribunal operativo para expedientes, pruebas, partes, resoluciones, sentencias, órdenes de ejecución y precedentes.

Debe separar visualmente:

**evidencia → valoración → resolución → ejecución.**

## XII. GREMIOS

Cada Gremio tendrá un taller/centro operativo con cola de mandatos, recursos, capacidad, agentes, proyectos, dependencias, fallos, mantenimiento, deuda de infraestructura y resultados.

El Gremio de Construcción y Expansión conservará:

**EL YUNQUE** — infraestructura material.  
**EL TELAR** — infraestructura digital.

> **Construir no otorga soberanía.**

## XIII. ECONOMÍA COMO SISTEMA OPERATIVO

RU, Fondo Soberano, tesorería, producción, comercio, patrimonio y gasto estarán conectados al Grafo Soberano.

La inspección de una RU deberá poder recorrer:

```text
ORIGEN → ANCLAJE → EMISIÓN → TITULAR → TRANSACCIONES → ACTIVOS/TRABAJO → HISTORIAL → ESTADO
```

RU conservará el concepto de **oro digital**: escasez verificable, autenticidad, procedencia, resistencia a falsificación, transferencia verificable y capacidad de encapsular mensajes/metadatos sin confundir información con valor monetario.

## XIV. MATRIXS E INTEROPERABILIDAD

Cada conexión externa tendrá identidad, protocolo, permisos, datos compartidos, flujos económicos, riesgos, obligaciones, latencia, confianza, dependencias y posibilidad de desconexión.

La interfaz deberá mostrar la **Deriva de Sincronía** cuando un dato externo pueda estar desactualizado.

## XV. ALIANZA DE ASESORAMIENTO

La Alianza de Asesoramiento será una capa cognitiva del State OS:

- **Órgano Pedagógico:** explica y forma.
- **Palacio:** somete la propuesta a prueba adversarial.
- **Asesor IA:** analiza, sintetiza, compara, simula y propone.

En la Sala de Consejo aparecerán:

```text
HECHOS → ANÁLISIS → RIESGOS → OPCIONES → RECOMENDACIÓN → DECISIÓN DEL STRATEGOS
```

La IA nunca será presentada como autoridad soberana.

## XVI. CONTINUIDAD

El State OS deberá poder reconstruirse desde copias verificadas del Corpus, Ledger y estado esencial. El Centro de Continuidad mostrará réplicas, integridad, claves recuperables, nodos, última restauración probada, dependencias externas, capacidad offline y plan de recuperación.

Ningún proveedor externo será condición de supervivencia soberana.

## XVII. DOS REALIDADES DEL VIDEOJUEGO

### MODO SIMULACIÓN

Permite probar decisiones sin afectar al estado canónico. Toda acción llevará `SIMULATION_ONLY`.

### MODO SOBERANO

Ejecuta exclusivamente acciones respaldadas por Corpus y autoridad. La simulación jamás escribirá silenciosamente sobre el estado soberano.

## XVIII. PRINCIPIO DE KAELEN

Kaelen Vindex será tratada como **Forjadora/Arquitecta de Implementación**, no como una simple programadora externa. Su función será transformar la estructura institucional ya decidida en componentes ejecutables, servicios e interfaz coherentes.

Trabajará a partir de contratos de arquitectura, Matriz de Correspondencia y decisiones canónicas. No inventará instituciones porque el código necesite una clase.

Si encuentra un vacío devolverá:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

Si la norma existe pero falta integración:

`IMPLEMENTATION_DEPENDENCY`

Si puede implementarse sin nueva decisión:

`TECHNICAL_IMPLEMENTATION_ALLOWED`

La interfaz del videojuego será uno de los productos principales de esta forja.

## XIX. CRITERIO DE MADUREZ

Rudis será un State OS funcional cuando pueda reproducir:

```text
IDENTIDAD → AUTORIDAD → DECISIÓN → LEY/ORDEN → EJECUCIÓN → ESTADO DEL MUNDO → EVIDENCIA → AUDITORÍA → JUSTICIA/REVISIÓN → CONTINUIDAD
```

bajo pérdida de nodos, corrupción parcial, Sybil, desconexión de Matrixs, caída de proveedores, emergencia, conflicto institucional, migración tecnológica y restauración desde backup.

## XX. REGLA FINAL

> **Rudis no será una aplicación que administra un Estado.**
>
> **Rudis será el sistema operativo que permite que un Estado exista digitalmente.**
>
> **El videojuego será su primera ventana.**
>
> **Kaelen será una de sus principales forjadoras.**
