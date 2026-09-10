# 🌐 Entender Rudis — Tour guiado

**Idioma / Language:** **Español** · [English](./TOUR_EN.md)

> **No necesitas leer el Corpus para saber si Rudis merece tu atención.**

Este recorrido tiene una sola misión: que en unos minutos puedas explicar **qué problema intenta resolver Rudis, qué se está construyendo, qué lo hace diferente y qué existe realmente hoy**.

Después podrás decidir si quieres simplemente seguir explorando, evaluar el producto, revisar la arquitectura o entrar en una ruta inversora.

---

# 1. Empieza por el problema, no por los nombres

El software está ganando capacidad para actuar: agentes que llaman herramientas, sistemas que mueven dinero, identidades que persisten entre sesiones, automatizaciones que modifican infraestructura y mundos digitales con instituciones propias.

El problema es que **capacidad técnica y autoridad legítima no son lo mismo**.

Un agente puede saber cómo realizar un pago y no tener derecho a hacerlo. Una persona puede demostrar correctamente quién es y, aun así, carecer de competencia para una acción concreta. Un sistema puede restaurar un snapshot correcto y resucitar por error permisos que ya estaban revocados.

Rudis nace alrededor de esa clase de errores.

Su principio central es:

> **Una representación del estado no adquiere autoridad sobre la realidad simplemente por afirmar que la representa.**

En lenguaje normal: **que el sistema tenga un dato, una firma, una sesión o una capacidad no basta para justificar una consecuencia**.

Las invariantes que aparecen en Rudis resumen esa frontera:

```text
CAPACIDAD != AUTORIDAD
IDENTIDAD != COMPETENCIA
REPRESENTACIÓN != AUTORIDAD
```

No necesitas memorizarlas. Son atajos para recordar errores que el sistema intenta impedir.

---

# 2. Qué está construyendo Rudis

Rudis no es una sola aplicación. Hoy se organiza alrededor de tres superficies principales.

## StateOS

Es la arquitectura de estado institucional. Intenta conservar una cadena causal comprensible entre **quién actúa, qué claim presenta, qué competencia necesita, qué autoridad está vigente, qué regla se aplica, qué mandato permite ejecutar, qué efecto ocurre y qué evidencia queda después**.

La idea no es que cada usuario vea toda esa cadena todo el tiempo. La idea es que exista y pueda abrirse cuando haga falta explicar, auditar o disputar una acción.

## RAL — Rudis Authority Layer

RAL se concentra en el momento donde una intención está a punto de convertirse en efecto.

Un sistema convencional puede preguntar: “¿este agente tiene acceso a esta herramienta?”. RAL intenta formular una pregunta más fuerte: **“¿puede demostrarse que este actor está autorizado a producir este efecto, ahora, bajo esta competencia y esta regla?”**

## Rudis Habitat

Habitat es la dirección de producto habitable. El mismo estado institucional puede mostrarse desde web, móvil, realidad inmersiva, agentes o APIs sin permitir que ninguna de esas interfaces invente la realidad que representa.

Ejemplo: una misma decisión de Asamblea puede verse en una app móvil y en un entorno 3D. Ambas la muestran; ninguna debería poder crearla sólo porque sabe dibujarla.

```text
UN ESTADO INSTITUCIONAL
-> MUCHAS REPRESENTACIONES LEGÍTIMAS
```

---

# 3. Qué cambia para una persona

La diferencia no debería sentirse como “más burocracia”. Debería sentirse como **más claridad sobre lo que ocurre y por qué**.

Si intentas una acción sensible, Rudis no debería limitarse a devolver “éxito” o “403”. Debería poder explicar, en capas, qué autoridad se utilizó, qué regla aplicó y qué mandato produjo el efecto.

Si vuelves después de varios días, Rudis debería poder enseñarte qué cambió mientras estabas fuera: una decisión que ahora te afecta, una aportación que llegó a revisión, una investigación que fue falsada o una nueva ruta educativa.

Si quieres aprender, contribuir, participar o pedir ayuda, la interfaz debería empezar por **tu intención**, no por obligarte a conocer previamente el organigrama institucional.

Para ver esta capa con ejemplos concretos, continúa después por **[Vivir Rudis](./VIVIR_RUDIS_ES.md)**.

---

# 4. Qué hace distinta a la arquitectura

Rudis insiste en separar cosas que suelen confundirse.

**Autenticarse no significa estar autorizado.** Demostrar identidad responde “quién eres”; no responde automáticamente “qué puedes hacer”.

**Una firma válida no demuestra que la autoridad siga vigente.** Puede autenticar correctamente un mandato que ya expiró o fue revocado.

**Recuperar datos no significa recuperar poder.** Un snapshot puede ser históricamente correcto y políticamente obsoleto.

**Un resumen no sustituye la fuente.** Puede orientar una Asamblea o a un visitante, pero no debe borrar votos, disenso o evidencia primaria.

**El código no legisla.** Si falta una regla necesaria, la Forja no debe inventarla por comodidad técnica.

Sólo después de entender eso tienen sentido estas abreviaturas:

```text
AUTENTICACIÓN != AUTORIZACIÓN
FIRMA VÁLIDA != AUTORIDAD VIGENTE
RECOVERY DE ESTADO != RECOVERY DE AUTORIDAD
RESUMEN != FUENTE
CÓDIGO != LEGISLADOR
```

---

# 5. Rudis aprende intentando romperse

Rudis separa tres actos: **descubrir**, **decidir** y **construir**.

Un investigador puede demostrar un fallo. Eso produce evidencia, no ley. Una Asamblea o autoridad competente puede decidir una regla. Eso produce norma, no garantiza que la implementación sea correcta. La Forja implementa lo autorizado y después esa implementación debe poder ser reproducida, atacada y falsada.

Así, un fallo bien documentado puede ser valioso: revela una afirmación falsa antes de que se convierta en una falsa sensación de seguridad.

```text
DESCUBRIR != DECIDIR != CONSTRUIR
```

Este enfoque atraviesa seguridad, recovery, currentness, memoria institucional, continuidad del RU, AssemblyOS y otras líneas de investigación.

---

# 6. Qué existe hoy y qué no

Rudis tiene Corpus público, arquitectura, una Forja privada separada, implementación PRE-D3, pruebas, investigación adversarial, rutas de producto y materiales de diligencia.

Eso es suficiente para que exista algo real que inspeccionar y poner a prueba.

No es suficiente para llamarlo producto de producción terminado.

```text
PRE-D3 = ACTIVO
D3 ABIERTO = NO
D4 / PRODUCCIÓN = NO
CLIENTES REALES = NO
DINERO REAL = NO
```

Un PASS de componente no demuestra un PASS de sistema. Una build verde no es acreditación. Una propuesta comercial no equivale a un cliente o socio real.

La honestidad sobre esa frontera forma parte del producto, no es una nota al pie.

---

# 7. Elige tu siguiente paso

## 👁️ Si eres visitante

Continúa por **[Vivir Rudis](./VIVIR_RUDIS_ES.md)**. Ahí verás cómo una persona podría aprender, contribuir, participar, pedir ayuda, comprender una decisión y volver a un mundo que siguió ocurriendo mientras estaba fuera.

Si después quieres producto: [Rudis Habitat](./products/Rudis_Habitat.md).

## 💼 Si eres inversor o socio estratégico

Ahora que ya conoces la tesis, continúa por **[Inversor / Socio estratégico — Leer primero](./external/Investor_Read_First_ES.md)**.

Ese documento no vuelve a explicarte Rudis desde cero. Responde las preguntas que importan después: **qué puede convertirse en negocio, qué puede financiarse, qué evidencia debe pedirse, cuál es la madurez y qué derechos puede o no comprar una operación**.

## 🧪 Si vienes a evaluar técnicamente

Empieza por el [Centro de lectura externa](./external/README.md#technical-diligence--diligencia-t%C3%A9cnica).

## 🏛️ Si quieres revisar el Canon

Utiliza el [Registro de Canon Vigente](./Quebranto-00_Registro_de_Canon_Vigente.md). No infieras vigencia por antigüedad o nombre de archivo.

---

# La idea que conviene recordar

> **Rudis intenta que una acción digital con consecuencias pueda demostrar de dónde proviene su autoridad, y que el sistema sea honesto cuando esa autoridad no pueda demostrarse.**

Eso es el núcleo. El resto del proyecto profundiza, prueba, protege o hace habitable esa idea.
