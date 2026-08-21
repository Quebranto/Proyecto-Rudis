# QUEBRANTO-16 — IDENTITY & CENSUS v0.1

**Fecha:** 21 de agosto de 2026  
**Estado:** Contrato arquitectónico canónico para implementación inicial  
**Implementación:** `Quebranto/tt/StateOS/Identity`

## I. PRINCIPIO

Rudis separa estrictamente:

> **Entidad ≠ ciudadanía.**

Una entidad puede existir, interactuar y tener capacidades técnicas reconocidas sin ser ciudadana.

La ciudadanía es una **credencial/relación jurídica atribuida posteriormente** por una autoridad competente mediante un acto basado en una norma vigente.

## II. ONTOLOGÍA BASE

Las clases iniciales de entidad son:

- `DEVELOPMENT_ENTITY`
- `FORGER`
- `INSTITUTION`
- `AUTHORITY`
- `VISITOR`
- `EXTERNAL_ACTOR`

La clasificación ontológica no concede ciudadanía por sí misma.

## III. IDENTIDAD CRIPTOGRÁFICA

Toda entidad registrada debe quedar asociada a una identidad criptográfica verificable.

Para v0.1:

- clave pública Ed25519 de 32 bytes;
- huella/fingerprint verificable;
- algoritmo explícito;
- ausencia de credenciales privadas en el registro público.

La mera presencia de una clave no constituye autenticación de una acción concreta. Autenticación y autorización deben permanecer separadas.

## IV. BOOTSTRAP

El censo se inicializa mediante un `GenesisTrustRoot` cuya autoridad procede de una ceremonia/acto fundacional reconocido externamente al registro que está iniciándose.

El Trust Root contiene:

- identificador de ceremonia;
- clave pública raíz;
- prueba de custodia offline;
- referencia al acto fundacional que lo autoriza.

El sistema debe impedir:

- inicialización doble;
- emisión múltiple de la autoridad génesis;
- bootstrap sin raíz válida;
- uso de una raíz estructuralmente inválida.

La implementación criptográfica real del verificador es una dependencia técnica; no se sustituirá por MD5, hash público o campo booleano.

## V. AUTORIDAD GÉNESIS

El primer Strategos se registra como `AUTHORITY` únicamente cuando exista una prueba válida emitida por la raíz génesis.

La creación del registro técnico del Strategos no convierte a la implementación en fuente autónoma de legitimidad política: la legitimidad procede del acto fundacional reconocido por el Corpus.

## VI. ENTIDADES DE FORJA

Entidades técnicas como Kaelen, Dōng, Cartógrafo o Limes pueden registrarse como `DEVELOPMENT_ENTITY` o `FORGER` según la clasificación que la autoridad competente les atribuya.

Su existencia técnica no crea ciudadanía.

## VII. CLAIMS JURÍDICOS

Los atributos jurídicos se almacenan como claims:

- ciudadanía;
- residencia;
- obligación tributaria;
- y futuros tipos definidos normativamente.

Cada claim debe conservar:

- identificador;
- entidad;
- tipo;
- autoridad otorgante;
- inicio;
- eventual expiración;
- fundamento jurídico;
- estado de revocación.

## VIII. CIUDADANÍA

No existe ciudadanía predeterminada en `Entity`.

`HasCitizenship(entity_id)` solo puede resultar verdadera si existe un `LegalClaim(CITIZENSHIP)` válido y no revocado.

La competencia para conceder ciudadanía es una política jurídica inyectada desde la capa de gobierno; el registro técnico no puede inventarla.

## IX. FRONTERA CORPUS → ARQUITECTURA → CÓDIGO

Si el Corpus define quién puede conceder ciudadanía, el código ejecuta esa competencia.

Si la norma existe y falta integración:

`IMPLEMENTATION_DEPENDENCY`

Si falta la decisión normativa:

`UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`

El código no puede convertir una clase técnica en autoridad política por defecto.

## X. AUDITORÍA

Los eventos de bootstrap, registro de autoridad, registro de entidades y concesión de claims deben producir evidencia auditable.

El Palacio de Tormentas puede auditar estos eventos, pero no se convierte por ello en órgano de concesión de ciudadanía ni fuente de legitimidad.

## XI. INVARIANTES

1. No Entity => Citizen por defecto.
2. No bootstrap sin GenesisTrustRoot válido.
3. No más de una Genesis Authority durante el bootstrap inicial.
4. No claim sin entidad existente.
5. No ciudadanía sin autoridad competente y fundamento jurídico.
6. No autenticación por mera existencia de una clave.
7. No secretos privados en el repositorio público.
8. No legislación escondida en el runtime de identidad.

## XII. ESTADO

El contrato v0.1 autoriza implementación técnica inicial. Quedan fuera de este contrato los parámetros políticos concretos de ciudadanía, residencia y obligaciones económicas, que permanecen en la legislación correspondiente.
