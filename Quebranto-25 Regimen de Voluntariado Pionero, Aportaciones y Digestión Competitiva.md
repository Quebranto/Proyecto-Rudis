# QUEBRANTO-25 — RÉGIMEN DE VOLUNTARIADO PIONERO, APORTACIONES Y DIGESTIÓN COMPETITIVA

**Fecha:** 29 de agosto de 2026  
**Estado:** DECISIÓN FUNDACIONAL VIGENTE / MARCO CANÓNICO OPERATIVO  
**Autoridad:** Strategos Fundacional  
**Ámbito:** Gremio y Palacio de Construcción; Palacio de Unificación; Gremio Unificador; Asamblea General Soberana; voluntarios pioneros.  
**Techo por defecto:** D2 salvo acto posterior competente.

---

## I. OBJETO

Rudis reconoce una vía formal para que **voluntarios pioneros** construyan, prueben, documenten o mejoren proyectos ya abiertos a Forja dentro del alcance autorizado.

La finalidad es permitir que la iniciativa voluntaria produzca frutos técnicamente útiles sin convertir la mera aportación en integración automática, autoridad política o modificación silenciosa del Estado.

`VOLUNTARIO -> PUEDE CONSTRUIR DENTRO DEL MANDATO`

`CONSTRUIR != LEGISLAR`

`APORTAR != INTEGRAR`

`INTEGRAR != ADOPTAR`

`APORTAR != VOTO`

`APORTAR != AUTORIDAD`

---

## II. REGISTRO VIVO DE PROYECTOS DISPONIBLES

El **Gremio de Construcción y Expansión** y el **Palacio de Construcción** custodiarán un Registro Vivo de Proyectos para Voluntarios Pioneros.

Sólo podrá figurar como `AVAILABLE_FOR_PIONEER_BUILD` un proyecto para el que exista fundamento suficiente de construcción D2: Canon, decisión competente, mandato vigente o consenso/disposición asamblearia suficiente dentro de su competencia.

Un proyecto puede conservar reservas o gates técnicos y seguir siendo construible únicamente en el subconjunto expresamente abierto.

Estados mínimos del registro:

- `AVAILABLE_FOR_PIONEER_BUILD`
- `AVAILABLE_WITH_GATES`
- `CLAIMED`
- `IN_PROGRESS`
- `SUBMITTED`
- `CONSTRUCTION_REVIEW`
- `UNIFICATION_REVIEW`
- `COMPETITIVE_DIGESTION`
- `ASSEMBLY_PENDING`
- `ACCEPTED`
- `ACCEPTED_PARTIAL`
- `RETURNED_FOR_REWORK`
- `REJECTED`
- `HOLD`
- `SUPERSEDED`

`LISTADO != AUTORIZACIÓN MÁS ALLÁ DE SU ALCANCE`

`HOLD LOCAL != PROYECTO ENTERO PROHIBIDO`, salvo que el expediente así lo disponga.

---

## III. DERECHO DE PARTICIPACIÓN VOLUNTARIA

Cualquier voluntario pionero admitido conforme al régimen aplicable podrá ofrecer trabajo sobre un proyecto disponible.

La participación puede consistir en:

- código;
- tests;
- challenge suites;
- documentación técnica;
- modelos y simuladores;
- interfaces;
- adaptadores;
- herramientas de verificación;
- fixtures;
- pruebas de portabilidad;
- prototipos visuales;
- investigación aplicada;
- repairs;
- propuestas de mejora técnicamente demostrables;
- otros frutos compatibles con el alcance del proyecto.

La contribución voluntaria no implica relación laboral, remuneración, premio ni derecho económico automático salvo acto, contrato o régimen competente que lo establezca.

`TRABAJO VOLUNTARIO != DEUDA AUTOMÁTICA DE RUDIS`

`RECONOCIMIENTO != REMUNERACIÓN AUTOMÁTICA`

---

## IV. REGISTRO DE APORTACIONES PIONERAS

Toda aportación presentada por esta vía deberá incorporarse al **Registro de Aportaciones Pioneras** con identidad y procedencia suficientes.

Campos mínimos:

1. `contribution_record_id`;
2. `project_id`;
3. identidad declarada del contribuyente;
4. identidad verificada/acreditada cuando corresponda;
5. fecha de inicio y entrega;
6. descripción del fruto ofrecido;
7. tipo de aportación;
8. licencia, cesión o condiciones aplicables;
9. artefactos y evidencia asociados;
10. base/estado del proyecto contra el que se construyó;
11. tests ejecutados y resultados declarados;
12. limitaciones conocidas;
13. autoría y coautoría;
14. dependencias de terceros y su procedencia;
15. estado de revisión por Construcción;
16. valoración del Palacio/Gremio de Unificación;
17. expediente de digestión competitiva;
18. disposición final de Asamblea;
19. beneficio técnico efectivamente obtenido por Rudis, si existe;
20. reconocimiento o beneficio posterior, si alguna autoridad competente lo aprueba;
21. controversias, reservas o reclamaciones;
22. fecha de última revisión.

La aportación permanece registrada aunque el fruto sea rechazado.

`PROCEDENCIA != ACEPTACIÓN`

`RECHAZO DEL FRUTO != BORRADO DEL AUTOR`

`DIGESTIÓN != APROPIACIÓN DE AUTORÍA`

---

## V. RECEPCIÓN POR CONSTRUCCIÓN

El Gremio y el Palacio de Construcción reciben el fruto y comprueban, como mínimo:

- que corresponde a un proyecto disponible;
- que no excede D2 o el mandato concreto;
- que no hardcodea política abierta;
- que respeta contratos, licencias y procedencia;
- que no introduce rutas de autoridad no autorizadas;
- que aporta evidencia reproducible suficiente para ser evaluado;
- que identifica claramente lo construido frente a lo asumido.

Construcción puede:

`RECEIVE / REQUEST_FIX / REJECT_AS_OUT_OF_SCOPE / FORWARD_TO_UNIFICATION`

La recepción técnica no equivale a adopción institucional.

---

## VI. VALORACIÓN POR PALACIO Y GREMIO DE UNIFICACIÓN

Todo fruto que supere recepción suficiente será valorado por el **Palacio de Unificación** y el **Gremio Unificador**.

La valoración deberá considerar, según corresponda:

- novedad;
- utilidad;
- calidad;
- seguridad;
- mantenibilidad;
- compatibilidad arquitectónica;
- cumplimiento de invariantes;
- procedencia y licencias;
- reducción real de deuda;
- coste de integración;
- superioridad, equivalencia o inferioridad frente a soluciones existentes;
- capacidad de sobrevivir a pruebas adversariales;
- independencia de proveedor cuando sea objetivo declarado;
- impacto sobre complejidad global;
- riesgos de captura semántica, técnica o institucional.

`VALORAR != PREMIAR`

`VALORAR != ADOPTAR`

`PALACIO DE UNIFICACIÓN != AUTORIDAD FINAL DE ACEPTACIÓN`

---

## VII. DIGESTIÓN COMPETITIVA OBLIGATORIA

El fruto ofrecido será sometido a digestión competitiva antes de recomendar su aceptación.

Cadena mínima:

`APORTACIÓN`
`-> PROCEDENCIA`
`-> RECEPCIÓN DE CONSTRUCCIÓN`
`-> VALORACIÓN DE UNIFICACIÓN`
`-> DIFFERENTIAL DIGESTION`
`-> COMPARACIÓN CON ESTADO RUDIS + ALTERNATIVAS`
`-> REATAQUE / PRUEBA`
`-> RECOMENDACIÓN`
`-> ASAMBLEA GENERAL`

La digestión puede concluir que:

- el fruto debe adoptarse prácticamente íntegro;
- sólo algunas propiedades son superiores;
- debe reimplementarse independientemente preservando la idea/procedencia;
- debe combinarse con otra solución;
- debe devolverse para reparación;
- no supera la implementación existente;
- es incompatible con Canon o arquitectura;
- es valioso como evidencia o aprendizaje aunque no deba integrarse.

`DIGERIR = ELEGIR`

`APRENDER != COPIAR`

`SUPERIOR EN UN TEST != SUPERIOR GLOBALMENTE`

---

## VIII. ÚLTIMA PALABRA DE LA ASAMBLEA GENERAL SOBERANA

Tras la digestión competitiva, la **Asamblea General Soberana** tendrá la última palabra sobre la aceptación institucional del fruto ofrecido dentro del régimen ordinario aplicable.

Disposiciones mínimas:

- `ACCEPT`
- `ACCEPT_PARTIAL`
- `RETURN_FOR_REWORK`
- `REQUEST_REDIGESTION`
- `HOLD`
- `REJECT`

La Asamblea podrá aceptar propiedades o aprendizajes sin aceptar literalmente el artefacto presentado.

`ACEPTAR EL FRUTO != ACEPTAR TODO EL ARTEFACTO`

`RECOMENDACIÓN DE UNIFICACIÓN != DECISIÓN DE ASAMBLEA`

`CI VERDE != ACEPTACIÓN`

`MERGE != ACEPTACIÓN INSTITUCIONAL`

Nada de este régimen autoriza por sí mismo producción, D3/D4 o dinero real.

---

## IX. RECONOCIMIENTO Y VALOR FUTURO DE LA APORTACIÓN

El Registro deberá permitir que una aportación pionera sea valorada posteriormente para reconocimiento, reputación, contratación, premio, grant, RU u otra forma legítima si existe autoridad, política y recursos para ello.

La valoración técnica del Palacio/Gremio de Unificación podrá constituir evidencia para decisiones futuras, pero no crea por sí sola una obligación patrimonial.

`CONTRIBUCIÓN REGISTRADA -> MEMORIA GARANTIZADA`

`MEMORIA GARANTIZADA != PAGO GARANTIZADO`

`VALOR TÉCNICO != PRECIO AUTOMÁTICO`

`CONTRIBUCIÓN != SOBERANÍA`

---

## X. RELACIÓN CON RECIPROCIDAD DE HABITABILIDAD

Cuando el régimen de reciprocidad permita que trabajo o colaboración técnica satisfagan obligaciones contributivas, una aportación pionera podrá ser considerada evidencia de esa contribución conforme a la política competente.

Pero:

`APORTACIÓN PIONERA != EQUIVALENCIA ECONÓMICA AUTOMÁTICA`

`APORTACIÓN PIONERA != CUOTA DE HABITACIÓN AUTOMÁTICAMENTE SATISFECHA`

`REGISTRO DE TRABAJO != AUTHORITY CONTEXT`

Cualquier equivalencia concreta permanece sometida a `Quebranto-24`, `Quebranto-24A` y a las decisiones económicas o reglamentarias posteriores.

---

## XI. FRONTERA DE AUTORIDAD

El voluntario construye; no legisla.

Construcción recibe y verifica alcance; no adopta soberanamente.

Unificación valora y digiere; no tiene la última palabra política.

La Asamblea dispone la aceptación final ordinaria.

El Strategos conserva las competencias que el Canon vigente le reconoce.

`VOLUNTARIO -> FRUTO`

`CONSTRUCCIÓN -> RECEPCIÓN / CONTROL DE ALCANCE`

`UNIFICACIÓN -> VALORACIÓN / DIGESTIÓN`

`ASAMBLEA -> ACEPTACIÓN FINAL ORDINARIA`

---

## XII. INVARIANTE FINAL

> **Rudis abre sus forjas a quien quiera ayudar a construir lo ya autorizado, conserva quién aportó qué, somete cada fruto a competencia técnica real y no confunde entusiasmo con calidad. Construcción recibe. Unificación compara y digiere. La Asamblea decide qué fruto pasa a formar parte del ecosistema.**

`APORTAR -> SER REGISTRADO`

`SER REGISTRADO != SER ACEPTADO`

`SER ACEPTADO != ADQUIRIR AUTORIDAD`

`DIGESTIÓN COMPETITIVA -> ANTES DE ADOPCIÓN`

`CÓDIGO != LEGISLADOR`
