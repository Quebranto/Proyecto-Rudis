# Separación público / privado de Proyecto Rudis

A partir del 21 de agosto de 2026, Rudis separa deliberadamente su corpus público de su implementación técnica privada.

## Superficie pública

`Quebranto/Proyecto-Rudis` conserva:

- Corpus y decisiones canónicas.
- Arquitectura institucional y State OS.
- Especificaciones públicas.
- Interfaz y diseño del videojuego.
- Contratos no sensibles.
- Documentación necesaria para colaboración y auditoría conceptual.

## Superficie privada autorizada

La implementación operativa del ecosistema Rudis y sus componentes técnicos sensibles se mantienen en una superficie privada con acceso controlado.

Por defecto, la superficie pública no identifica:

- localización del repositorio privado;
- ramas o heads internos;
- hashes de trabajo;
- PR/issues privados;
- CI privado;
- paths internos;
- artefactos, fixtures o harnesses sensibles;
- configuración de infraestructura;
- detalles de explotación.

La superficie privada contiene progresivamente:

- State OS ejecutable;
- núcleo y subsistemas;
- Palacio de Conversión;
- integraciones internas;
- pruebas técnicas y adversariales;
- detalles de seguridad operativa;
- infraestructura y configuración privada.

## Regla de migración

Cuando una implementación deje de ser apropiada para exposición pública:

1. se mantiene su contrato arquitectónico en la superficie pública;
2. su implementación permanece o pasa a la superficie privada autorizada;
3. la documentación pública evita exponer detalles que faciliten ataques;
4. el trabajo del Corpus no se modifica salvo para actualizar referencias de implementación que sean seguras y necesarias.

La superficie privada implementa el Canon público; no lo sustituye.

## Regla de referencia

Cuando una Asamblea pública necesite referirse a evidencia privada, deberá utilizar una referencia sanitizada o un handle opaco conforme a `SECURITY.md`.

```text
PUBLIC PROPERTY
-> AUTHORIZED PRIVATE EVIDENCE
-> SANITIZED PUBLIC DISPOSITION
```

Nunca se requiere publicar el localizador privado para que una evidencia sea institucionalmente exigible.
