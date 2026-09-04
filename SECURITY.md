# Política de seguridad y frontera de publicación — Proyecto Rudis

## 1. Principio

Proyecto-Rudis es la superficie pública del Corpus, contratos, arquitectura, decisiones, documentación y resultados sanitizados de auditoría.

La implementación operativa, pruebas internas, seguridad, CI privado, ramas de trabajo y futuras integraciones de producción permanecen en la superficie privada autorizada.

Máximas:

`público != implementación privada`

`acceso privado autorizado != derecho de publicación`

`transparencia constitucional != transparencia operativa irrestricta`

`evidencia pública != mapa operativo privado`

## 2. Actores autorizados

La superficie privada puede compartirse mediante controles de acceso técnicos apropiados con actores autorizados de Quebranto Fundacional y Segmenta.

La autorización institucional no sustituye autenticación, ACL, identidad técnica ni trazabilidad del acceso.

## 3. Permitido en el repositorio público

- Corpus y normas públicas;
- contratos e interfaces públicas;
- invariantes y propiedades arquitectónicas;
- decisiones y actas asamblearias;
- resultados de auditoría sanitizados;
- clasificación de riesgos;
- estados `APTO / APTO CON RESERVAS / NO APTO`, G1/G2/G3, D0/D1/D2, UCD y dependencias;
- hashes o referencias sólo cuando una decisión expresa determine que su publicación es necesaria y segura;
- enlaces a recursos ya públicos.

## 4. No publicar por defecto

Salvo decisión expresa de publicación y revisión de seguridad previa:

- secretos, tokens, credenciales, claves privadas o material de recuperación;
- URLs directas a repositorios/PR/issues privados;
- heads, branches internas o hashes de trabajo privado;
- IDs o URLs de CI privado;
- diffs o código interno;
- paths internos que revelen estructura sensible;
- nombres de artefactos de seguridad, fixtures o harnesses internos cuando no sean necesarios públicamente;
- configuraciones de proveedores, endpoints, cuentas, identificadores o infraestructura;
- detalles de explotación que reduzcan materialmente el coste de atacar una vulnerabilidad abierta;
- volcados de logs privados;
- datos personales o identificadores no necesarios para el objeto público;
- rutas locales de worktree, directorios de usuario o topología del host;
- identificadores o enlaces de sesión de herramientas externas;
- valores exactos de ataque cuando una propiedad puede describirse sin ellos.

## 5. Regla para Asambleas públicas

Una Asamblea pública puede exigir evidencia privada sin reproducirla.

Formato recomendado:

`propiedad exigida -> auditor autorizado -> evidencia privada reproducible -> disposición pública sanitizada`

Nunca:

`auditoría privada -> copiar código/diff/CI al issue público`

Un voto puede declarar que revisó evidencia privada y registrar su conclusión sin exponer localizadores o internals.

## 6. Vulnerabilidades

Mientras una vulnerabilidad permanezca abierta, la superficie pública debe publicar sólo lo necesario para:

- describir el riesgo;
- establecer la propiedad de seguridad requerida;
- registrar el estado de reparación;
- permitir escrutinio institucional.

La prueba de concepto, secuencia de explotación, offsets, líneas exactas, rutas internas, valores de ataque o mecanismos de bypass deben permanecer privados salvo decisión específica de disclosure responsable.

## 7. Credenciales

Toda credencial expuesta o sospechosa debe considerarse comprometida y rotarse/revocarse. Nunca debe copiarse a issues, commits, chats públicos o documentación.

La rotación de una credencial no elimina la necesidad de revisar logs, alcance y uso histórico cuando exista sospecha de exposición.

## 8. Corrección de filtraciones

Si aparece información privada en Proyecto-Rudis:

1. clasificar si es secreto, metadato operativo, código, localizador privado o información pública legítima;
2. retirar/sanitizar lo innecesario;
3. preservar el significado histórico y la decisión institucional;
4. rotar credenciales si procede;
5. revisar comentarios, issues, PRs y archivos relacionados;
6. registrar una nota de sanitización sin volver a reproducir el material filtrado.

La sanitización no puede utilizarse para borrar evidencia desfavorable:

`SANITIZE SECRET != SANITIZE FAILURE`

Deben preservarse expresamente `FAIL`, `HOLD`, `NOT RUN`, reservas, disenso, limitaciones y condiciones de salida.

## 9. Revisión previa a publicar

Antes de publicar desde la superficie privada, comprobar:

- ¿es necesario para el Corpus o la decisión pública?;
- ¿revela estructura interna que no aporta valor público?;
- ¿incluye identificadores privados o infraestructura?;
- ¿facilita explotación de un hallazgo abierto?;
- ¿puede expresarse como propiedad, resultado o evidencia sanitizada?;
- ¿ha sido autorizado su disclosure?;
- ¿incluye una rama, hash, path, worktree, CI ID, sesión externa o valor de ataque que pueda sustituirse por un handle opaco?;

Si la respuesta segura no es clara: **no publicar y someter a revisión**.

## 10. Handles públicos de evidencia privada

Cuando una Asamblea necesite referirse a evidencia privada sin exponer su localización, se usará un handle público opaco y estable.

Formato recomendado:

`EVIDENCE-<GATE>-<YYYYMMDD>-<NN>`

Ejemplo conceptual:

`EVIDENCE-G8-20260904-01`

El handle público no debe codificar:

- rama;
- hash;
- path;
- repositorio privado;
- CI run;
- host;
- identidad técnica sensible;
- mecanismo de explotación.

La correspondencia entre handle y evidencia real se mantiene únicamente en la superficie privada autorizada.

Formato público preferido:

`PROPERTY -> AUDITOR -> PRIVATE EVIDENCE HANDLE -> RESULT -> LIMITATION -> EXIT CONDITION`

## 11. Gate de publicación PRE-D3

Todo informe PRE-D3 derivado de la Forja privada debe pasar antes de publicación por esta reducción mínima:

```text
PRIVATE REPORT
-> REMOVE LOCATORS
-> REMOVE CODE/DIFF
-> REMOVE EXPLOIT RECIPE
-> REMOVE HOST/SESSION DETAILS
-> PRESERVE FINDING
-> PRESERVE RESULT
-> PRESERVE LIMITATION
-> PRESERVE DISSENT
-> PRESERVE EXIT CONDITION
-> PUBLIC SANITIZED REPORT
```

Publicación recomendada:

```text
PROPERTY
RESULT
SEVERITY
STATUS
LIMITATION
EXIT CONDITION
D3 IMPACT
SANITIZED EVIDENCE HANDLE
```

No publicación por defecto:

```text
BRANCH
HASH
PRIVATE PR/ISSUE
PRIVATE CI ID/URL
WORKTREE
INTERNAL PATH
SOURCE CODE
EXPLOIT VALUES
SESSION LINK
```

## 12. Principio final

> Rudis debe ser auditable sin convertir su repositorio público en un inventario de ataque de su implementación privada.
