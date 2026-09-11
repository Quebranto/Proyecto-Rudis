# 🛠️ Ser Pionero en Rudis — Cómo colaborar con el proyecto

**Idioma / Language:** **Español** · [English](./PIONEERS_EN.md)

> **Rudis no busca únicamente capital. Busca personas y entidades capaces de construir, probar, cuestionar, traducir, documentar, auditar y mejorar el Ecosistema.**

Este tutorial explica cómo funciona el sistema de Pioneros y qué significa colaborar con Rudis sin necesidad de ser inversor.

No hace falta empezar entendiendo todo el Corpus. Lo importante es saber **qué puedes aportar, qué límites existen, cómo se conserva tu autoría y qué ocurre con tu contribución después de entregarla**.

---

# 1. ¿Qué es un Pionero?

Un Pionero es una entidad que aporta trabajo material al desarrollo de Rudis dentro de un frente autorizado.

Puede ser una persona, un equipo, una entidad digital o cualquier otro colaborador admisible conforme al régimen aplicable.

Una aportación puede consistir en:

- código;
- tests;
- challenge suites;
- investigación aplicada;
- documentación;
- interfaces;
- traducción;
- herramientas de verificación;
- simuladores;
- prototipos;
- auditoría;
- mejoras de onboarding;
- falsación de una afirmación técnica;
- hardening;
- reparaciones;
- comparación de alternativas;
- otras contribuciones compatibles con un proyecto abierto.

Lo esencial es esto:

> **Pionero no significa “persona que financia Rudis”. Significa “entidad que contribuye materialmente a Rudis”.**

---

# 2. Empieza por un problema abierto, no por pedir permiso genérico

Rudis mantiene un [Registro Vivo de Proyectos para Voluntarios Pioneros D2](./REGISTRO-VIVO-Proyectos-Voluntarios-Pioneros-D2.md).

Ese registro existe para responder una pregunta práctica:

> **¿Dónde puedo aportar ahora sin obligar a la Forja a inventar una política que todavía no existe?**

Actualmente hay frentes abiertos sobre, entre otros:

- integridad causal y cadena de autoridad de StateOS;
- retry, idempotencia, replay y durabilidad;
- identidad y sucesión ordinaria de credenciales;
- composición y restart;
- RU y Palacio de Conversión ficticio D2;
- verificabilidad pública;
- Rudis Habitat / mundo habitable;
- PGHD y Zonas de Resonancia;
- reciprocidad plural;
- infraestructura de presencia;
- herramientas de Differential Digestion;
- portabilidad y salida técnica.

Cada proyecto indica qué puede construirse, qué no puede construirse y qué gate debe superar.

---

# 3. Elegir un proyecto

Busca un frente donde puedas aportar valor real.

Por ejemplo:

**Si eres desarrollador:** puedes trabajar en contract tests, harnesses, fixtures, simuladores, adapters o herramientas de verificación.

**Si haces seguridad:** puedes diseñar challenge suites, intentar romper una afirmación, reproducir un fallo o demostrar que una protección declarada no se cumple.

**Si haces producto o UX:** puedes mejorar onboarding, visualización de receipts, flujos de Habitat, representación de incertidumbre o experiencia institucional.

**Si eres investigador:** puedes formalizar hipótesis, reproducir resultados, comparar arquitecturas o generar evidencia adversarial.

**Si haces documentación o comunicación:** puedes traducir, explicar, simplificar, detectar confusiones y producir rutas de comprensión sin deformar el contenido.

**Si eres una entidad digital:** puedes contribuir mediante tareas acotadas, reproducibles y trazables dentro de un alcance autorizado.

La puerta de entrada es la contribución, no el estatus previo.

---

# 4. Antes de construir: entiende el alcance

Cada proyecto Pionero tiene un límite.

Un proyecto puede estar abierto para tests y simulación pero no para producción. Puede permitir estudiar RU ficticio pero no mover dinero real. Puede permitir diseñar recovery ordinario pero mantener bloqueado el recovery extraordinario.

Por eso:

```text
AVAILABLE_FOR_PIONEER_BUILD != PRODUCTION
AVAILABLE_WITH_GATES != FULL AUTHORIZATION
```

La regla práctica es sencilla:

> **Construye lo que está abierto. Si encuentras un vacío político o constitucional, no lo rellenes en código.**

Cuando falta una decisión necesaria, la contribución debe señalar la dependencia en vez de inventar la respuesta.

---

# 5. Construye dejando evidencia

Rudis no quiere contribuciones imposibles de auditar.

Una buena aportación debería permitir responder:

- qué problema intentabas resolver;
- sobre qué baseline trabajaste;
- qué construiste;
- qué asumiste;
- qué tests ejecutaste;
- qué resultado obtuviste;
- qué no pudiste demostrar;
- qué dependencias de terceros utilizaste;
- bajo qué licencia o condiciones entregas el fruto;
- qué limitaciones conocidas tiene.

Una contribución puede ser valiosa incluso si demuestra que una hipótesis de Rudis era incorrecta.

> **Encontrar una falsedad útil también puede ser construir.**

---

# 6. Tu autoría no desaparece al entregar el trabajo

Toda aportación Pionera debe conservar procedencia suficiente.

El registro contempla identidad del contribuyente, fechas, descripción del fruto, licencia, artefactos, baseline, tests, limitaciones, autoría, dependencias de terceros, revisiones y disposición final.

Eso significa que Rudis intenta distinguir entre:

```text
APORTAR
INTEGRAR
ADOPTAR
```

Son actos diferentes.

Una contribución puede ser rechazada como implementación y seguir siendo valiosa como evidencia, investigación o aprendizaje. Rechazar el fruto no debería borrar al autor.

---

# 7. Qué ocurre después de entregar

La cadena ordinaria es:

```text
PIONERO
-> APORTACIÓN
-> REGISTRO
-> CONSTRUCCIÓN
-> UNIFICACIÓN
-> DIGESTIÓN COMPETITIVA
-> RECOMENDACIÓN
-> ASAMBLEA
-> DISPOSICIÓN FINAL
```

## Construcción

El Gremio / Palacio de Construcción comprueba alcance, licencias, procedencia, evidencia y ausencia de autoridad inventada.

## Unificación

El Palacio de Unificación y el Gremio Unificador comparan el fruto con el estado actual de Rudis y alternativas pertinentes.

## Digestión competitiva

La pregunta no es sólo “¿funciona?”. También es:

- ¿es mejor que lo existente?;
- ¿qué propiedades son superiores?;
- ¿qué riesgos introduce?;
- ¿debería adoptarse, combinarse, reimplementarse o rechazarse?;
- ¿qué aprendemos aunque no se integre?

## Asamblea

La disposición institucional ordinaria puede terminar en:

`ACCEPT / ACCEPT_PARTIAL / RETURN_FOR_REWORK / REQUEST_REDIGESTION / HOLD / REJECT`.

---

# 8. ¿Qué puede recibir un Pionero?

Rudis reconoce que una contribución material puede merecer reconocimiento y reciprocidad.

Dependiendo de política competente, recursos y naturaleza de la aportación, eso podría incluir:

- atribución y procedencia;
- reconocimiento Pionero;
- reputación técnica o institucional;
- acceso a nuevos retos autorizados;
- colaboración futura;
- grants, bounty o remuneración cuando exista régimen competente;
- RU u otra reciprocidad económica cuando esté legítimamente habilitada;
- contratos o investigación aplicada cuando proceda.

Pero nada de esto nace automáticamente por entregar una contribución.

```text
CONTRIBUCIÓN != REMUNERACIÓN AUTOMÁTICA
PIONERO != CIUDADANÍA AUTOMÁTICA
PIONERO != VOTO AUTOMÁTICO
PIONERO != AUTORIDAD
```

La recompensa debe seguir a una política competente y a valor demostrable.

---

# 9. Ejemplos de caminos Pioneros

## A. Seguridad

Encuentras que un restart puede resucitar una autoridad revocada.

Tu contribución puede ser:

1. reproducir el fallo;
2. documentar las precondiciones;
3. crear un test de regresión;
4. proponer una reparación D2 compatible con Canon;
5. ayudar a reatacar la solución.

Aunque no escribas la reparación final, ya has creado valor si has convertido una falsa seguridad en evidencia reproducible.

## B. Habitat / UX

Detectas que una persona no entiende por qué una acción fue denegada.

Puedes proponer una representación de receipt que diga:

> “Esta autorización existió, pero no podemos demostrar que siga vigente.”

Si esa interfaz mejora comprensión sin alterar la verdad institucional, puede convertirse en una aportación Pionera de producto.

## C. RU

Diseñas un escenario donde una versión criptográfica del RU queda comprometida y pruebas una migración simulada preservando supply y titularidad legítima.

Eso puede contribuir a la búsqueda del oro digital resiliente sin operar dinero real.

## D. Documentación / traducción

Descubres que un concepto se entiende mal de forma recurrente. Produces una explicación mejor, la pruebas con lectores y reduces una barrera real de entrada.

También eso puede ser creación de valor para Rudis.

---

# 10. Qué buscamos especialmente

Rudis necesita colaboradores capaces de:

- construir;
- romper;
- reproducir;
- documentar;
- explicar;
- traducir;
- comparar;
- diseñar;
- investigar;
- auditar;
- crear tooling;
- convertir fallos en defensas permanentes.

No todos los Pioneros tienen que ser programadores.

> **Una arquitectura institucional necesita ingeniería, investigación, seguridad, diseño, narrativa, traducción, crítica y evidencia.**

---

# 11. Antes de empezar

Lee:

1. [Entender Rudis — Tour guiado](./TOUR_ES.md)
2. [Vivir Rudis](./VIVIR_RUDIS_ES.md)
3. [Registro Vivo de Proyectos Pioneros](./REGISTRO-VIVO-Proyectos-Voluntarios-Pioneros-D2.md)
4. [Régimen de Voluntariado Pionero](./Quebranto-25%20Regimen%20de%20Voluntariado%20Pionero,%20Aportaciones%20y%20Digesti%C3%B3n%20Competitiva.md) si necesitas la fuente normativa completa.

No necesitas leer todo el Corpus antes de detectar un frente que encaje contigo.

---

# Idea final

Rudis no necesita únicamente personas dispuestas a creer en el proyecto.

Necesita personas y entidades dispuestas a **hacer una afirmación más fuerte, intentar romperla y dejar algo mejor detrás**.

> **Ser Pionero es convertir capacidad propia en valor verificable para Rudis sin convertir contribución en autoridad por accidente.**

**Idioma / Language:** **Español** · [English](./PIONEERS_EN.md)
