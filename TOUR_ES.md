# 🌐 Proyecto Rudis — Tour guiado

**Idioma / Language:** **Español** · [English](./TOUR_EN.md)

> **Bienvenido a Rudis. No necesitas leer todo el Corpus para entender qué estamos construyendo.**

Este recorrido está pensado para una primera visita. La idea no es enseñarte toda la arquitectura, sino darte suficiente contexto para que puedas decidir si quieres profundizar después.

Puedes seguir dos rutas:

- 👁️ **Visitante — 8–10 minutos:** entiende el problema, la arquitectura, qué podría sentirse distinto al usar Rudis y cuáles son sus límites actuales.
- 💼 **Inversor / Socio estratégico — 12–15 minutos:** entiende la tesis, qué puede financiarse, qué evidencia importa y dónde termina la inversión y empieza la soberanía del proyecto.

Si quieres imaginar cómo sería entrar, participar y volver a Rudis como usuario, después del tour continúa por [Vivir Rudis](./VIVIR_RUDIS_ES.md).

---

# 👁️ Tour para visitantes

## Parada 1 — ¿Qué problema intenta resolver Rudis?

Rudis es un proyecto experimental de **arquitectura constitucional, sistemas distribuidos e infraestructura institucional**.

Su punto de partida es una intuición muy cotidiana: que un sistema diga “esto es así” no significa que tenga autoridad para hacerlo verdad.

Piensa en un agente de IA que puede enviar dinero, modificar una cuenta o actuar sobre infraestructura. Puede tener la capacidad técnica para hacerlo y aun así no tener permiso legítimo. O piensa en una aplicación que muestra que alguien sigue teniendo un cargo porque conserva un dato antiguo, aunque ese cargo ya haya sido revocado. El sistema representa un estado, pero esa representación puede estar desactualizada, ser incompleta o carecer de autoridad.

Rudis intenta impedir que esas confusiones se vuelvan normales.

Su principio central es:

> **Una representación del estado no adquiere autoridad sobre la realidad simplemente por afirmar que la representa.**

Las fórmulas compactas que verás en Rudis son resúmenes de esa idea, no sustitutos de la explicación:

```text
CAPACIDAD != AUTORIDAD
IDENTIDAD != COMPETENCIA
REPRESENTACIÓN != AUTORIDAD
```

En lenguaje simple: **poder hacer algo, ser quien dices ser o aparecer correctamente en una interfaz no demuestra por sí solo que tengas derecho a producir una consecuencia.**

## Parada 2 — ¿Qué se está construyendo?

Rudis tiene tres superficies principales.

**StateOS** es la arquitectura de estado institucional. Su función es conservar una cadena causal entre quién actúa, qué claim presenta, qué competencia debe demostrar, qué regla se aplica, qué mandato autoriza la ejecución, qué efecto ocurre y qué evidencia queda después.

**RAL — Rudis Authority Layer** se concentra especialmente en el momento peligroso: cuando una intención está a punto de convertirse en una acción real. Su pregunta no es “¿puede el agente llamar a esta herramienta?”, sino “¿puede demostrar que está autorizado a producir este efecto ahora?”.

**Rudis Habitat** es la forma habitable de ese estado institucional. Puede expresarse mediante web, móvil, entornos inmersivos, agentes o APIs, pero ninguna de esas ventanas debería convertirse en la fuente soberana de verdad sólo por ser la interfaz desde la que miras.

Una forma compacta de verlo es:

```text
UN ESTADO INSTITUCIONAL CAUSAL
-> MUCHAS REPRESENTACIONES LEGÍTIMAS
```

Por ejemplo: una decisión puede verse desde una app móvil, una interfaz web o un entorno 3D. Las tres pueden mostrarla, pero ninguna debería poder inventarla.

## Parada 3 — ¿Qué hace distinta a la arquitectura?

Rudis insiste mucho en separar conceptos que el software convencional suele mezclar.

**Autenticación y autorización no son lo mismo.** Puedes demostrar quién eres y seguir sin tener permiso para una acción concreta.

**Una firma válida no demuestra autoridad vigente.** La firma puede ser auténtica y, aun así, pertenecer a un mandato ya revocado o expirado.

**Recuperar estado no significa recuperar autoridad.** Reiniciar un sistema y restaurar un snapshot antiguo no debería resucitar permisos muertos.

**Un resumen no sustituye la fuente.** Una Asamblea puede usar una síntesis para orientarse, pero la síntesis no debe borrar votos, disenso o evidencia primaria.

**El código no legisla.** Si falta una decisión política o constitucional, la implementación no debe inventarla para que el programa compile.

Por eso aparecen invariantes como:

```text
AUTENTICACIÓN != AUTORIZACIÓN
FIRMA VÁLIDA != AUTORIDAD VIGENTE
ESTADO RECUPERADO != AUTORIDAD RECUPERADA
RESUMEN != FUENTE
CÓDIGO != LEGISLADOR
```

Lo importante no es memorizar esas líneas. Lo importante es entender qué errores intentan impedir.

## Parada 4 — ¿Cómo se sentiría usar Rudis?

Rudis no debería sentirse como una colección de documentos constitucionales.

Una persona debería poder entrar y ver qué está vivo, qué cambió desde su última visita, qué asuntos requieren atención, qué puede aprender, dónde puede contribuir y qué instituciones están actuando.

Si intenta una acción sensible, no debería recibir simplemente “éxito” o “error 403”. Rudis debería poder explicar progresivamente **quién pidió la acción, qué autoridad se demostró, qué regla se aplicó y qué mandato produjo el efecto**.

Si una autoridad ya no está vigente, el sistema debería poder decirlo de forma comprensible: “esta autorización existió, pero no podemos demostrar que siga vigente”.

Esa es la diferencia entre una arquitectura que sólo vive en diagramas y una arquitectura convertida en experiencia.

Para profundizar en esta capa, continúa por [Vivir Rudis](./VIVIR_RUDIS_ES.md).

## Parada 5 — ¿Qué es real hoy?

Rudis está en una fase **PRE-D3**. Esto significa que existe arquitectura, Corpus, implementación privada, pruebas, investigación y trabajo adversarial, pero todavía no se afirma que exista una plataforma de producción terminada.

Algunas propiedades ya se han movido desde la teoría hacia tests ejecutables y reproducción independiente. Aun así, un componente que pasa una prueba no demuestra que todo el sistema sea seguro, y una build verde tampoco equivale a acreditación independiente.

Estado público actual:

```text
PRE-D3 = ACTIVO
D3 ABIERTO = NO
D4 / PRODUCCIÓN = NO
CLIENTES REALES = NO
DINERO REAL = NO
```

En otras palabras: **hay algo serio que auditar y poner a prueba, pero todavía no algo que debamos presentar como terminado.**

## Parada 6 — ¿Cómo aprende Rudis?

Rudis intenta que descubrir un problema, decidir qué hacer y construir la solución sean actos diferentes.

Un investigador puede demostrar que existe una vulnerabilidad. Eso no le convierte automáticamente en legislador. Una Asamblea puede decidir una regla. Eso no demuestra por sí mismo que la implementación técnica sea correcta. Y un equipo de Forja puede construir una solución sólo cuando exista una base legítima para hacerlo.

La versión resumida es:

```text
DESCUBRIR != DECIDIR != CONSTRUIR
```

Las rondas investigativas actuales atacan cuestiones como continuidad, currentness, recovery, autoridad, privacidad, memoria institucional, captura del coordinador y reconstitución catastrófica. La intención es que Rudis mejore porque sus afirmaciones pueden ser cuestionadas, reproducidas y falsadas.

## Parada 7 — ¿Dónde sigo?

Si quieres entender cómo debería sentirse estar dentro del sistema, ve a **[Vivir Rudis](./VIVIR_RUDIS_ES.md)**.

Si te interesa el producto, continúa por [Superficie de producto](./products/README.md) y [Rudis Habitat](./products/Rudis_Habitat.md).

Si quieres revisar la norma vigente, usa el [Registro de Canon](./Quebranto-00_Registro_de_Canon_Vigente.md).

Si vienes a auditar arquitectura, madurez o seguridad, entra por el [Centro de lectura externa](./external/README.md).

No esperamos que leas todo. El Corpus es la capa fuente; este tour es la puerta.

---

# 💼 Tour para inversores / socios estratégicos

## Parada 1 — La tesis de inversión

A medida que agentes de IA, software autónomo e instituciones digitales adquieren capacidad de actuar, aumenta el coste de confundir **capacidad técnica** con **autoridad legítima**.

Un agente puede saber cómo emitir un pago y no tener autoridad para hacerlo. Un empleado puede conservar un token válido después de perder una competencia. Una interfaz puede mostrar una decisión vieja como si todavía fuera vigente. Un sistema recuperado después de una caída puede restaurar datos correctos y, aun así, no tener derecho a restaurar autoridad antigua.

Rudis investiga una arquitectura donde esas preguntas se vuelven explícitas y auditables.

La tesis de inversión no es “Rudis está terminado”. Es que **autoridad, currentness, continuidad y ejecución auditable son problemas que crecen a medida que los sistemas ganan capacidad de actuar**, y que Rudis ha construido una arquitectura diferenciada que merece ser falsada, probada e integrada.

## Parada 2 — ¿Qué puede financiarse?

Una inversión estratégica puede acelerar trabajo técnico y de producto sin comprar la constitución del proyecto.

Puede financiar integración de StateOS, RAL, Rudis Habitat, recovery, pruebas de stale state, hardening, reproducibilidad, clientes, superficies de agentes, investigación aplicada, preparación legal/IP y demos controladas.

Lo importante es que el capital avance contra evidencia, no sólo contra una lista creciente de features.

Por ejemplo: una fase puede prometer demostrar que un tercero reproduce un candidato PRE-D3 y que una autoridad revocada falla correctamente. Si esa evidencia aparece, se abre la siguiente fase. Si no aparece, el socio debe poder detenerse.

La fórmula compacta es:

```text
GATE ACORDADO
-> PAQUETE DE EVIDENCIA
-> REVISIÓN
-> SIGUIENTE COMPROMISO
```

## Parada 3 — ¿Cuáles son los límites de madurez?

Rudis debe evaluarse hoy como una arquitectura experimental seria en preproducción y bajo desarrollo adversarial.

No hay D3 abierto, D4, producción, clientes reales ni dinero real dentro del sistema. Esa transparencia no debilita la propuesta: permite que un inversor sepa exactamente qué está financiando y qué tendría que demostrarse antes de subir de fase.

```text
PRE-D3 = ACTIVO
D3 ABIERTO = NO
D4 / PRODUCCIÓN = NO
CLIENTES REALES = NO
DINERO REAL = NO
```

## Parada 4 — ¿Qué no compra una inversión?

Un socio puede negociar derechos económicos, licencias, acceso a diligencia, integración preferente, reporting o derechos corporativos en un vehículo comercial futuro.

Lo que no obtiene por defecto es autoridad constitucional sobre Rudis, control del Canon, ciudadanía, votos, Botón Rojo, autoridad monetaria o acceso irrestricto a la Forja.

La razón es sencilla: si Rudis afirma que autoridad y capacidad deben permanecer separadas, no tendría sentido que su propia financiación violara ese principio.

```text
INVERSIÓN != CONTROL DEL CANON
CAPITAL != CAPTURA
```

## Parada 5 — ¿Qué evidencia debería pedir un inversor?

Un inversor serio no debería preguntar únicamente “¿existe el componente?”. Debería preguntar “¿qué afirmación hace ese componente, cómo podría fallar y quién, aparte del constructor, consiguió reproducirla?”.

Una diligencia útil avanza desde tesis pública y arquitectura hacia límites de madurez, evidencia sanitizada y, cuando existe encaje real, revisión restringida y finalista.

La pregunta clave es: **¿puede un tercero independiente demostrar tanto el PASS como el fallo esperado?**

Por eso Rudis trata la falsación como activo de diligencia y no como amenaza reputacional.

## Parada 6 — ¿Cómo se convierte esto en producto?

La arquitectura puede materializarse en varias líneas: autoridad para agentes, StateOS institucional, Rudis Habitat, continuidad/recovery, aprendizaje y evolución mediante Palacio Evolutivo, AssemblyOS, herramientas de auditoría y superficies de integración empresarial.

Las propuestas actuales para socios como Microsoft o Meta son hipótesis estratégicas de integración, no prueba de relación comercial existente. Sirven para mostrar cómo una tecnología abstracta podría conectarse a problemas concretos de agentes, aprendizaje, colaboración, identidad o mundos persistentes.

## Parada 7 — Orden recomendado de lectura

1. [Investor Read First — Español](./external/Investor_Read_First_ES.md)
2. [Dossier para inversores y socios estratégicos — English + Español](./external/Rudis_Investor_Introduction_ES_EN.md)
3. [Vivir Rudis](./VIVIR_RUDIS_ES.md)
4. [Public One-Pager](./external/Rudis_Public_OnePager.md)
5. [Maturity & Limits Statement](./external/Maturity_and_Limits_Statement.md)
6. [Sanitized Security Posture](./external/Sanitized_Security_Posture.md)
7. [Centro de lectura externa](./external/README.md)

---

# La frase que debes recordar

> **Rudis intenta que toda acción digital con consecuencias demuestre de dónde proviene su autoridad — y que el sistema sea honesto cuando esa autoridad no pueda demostrarse.**

Y, si quieres entender qué significa eso para una persona que entra en el sistema:

> **[Vivir Rudis](./VIVIR_RUDIS_ES.md): entrar, orientarse, actuar, comprender una consecuencia y volver a algo que continuó sin ti.**

**Idioma / Language:** **Español** · [English](./TOUR_EN.md)
