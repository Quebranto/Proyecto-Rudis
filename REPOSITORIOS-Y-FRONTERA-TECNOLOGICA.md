# Separación público / privado de Proyecto Rudis

A partir del 21 de agosto de 2026, Rudis separa deliberadamente su corpus público de su implementación técnica privada.

## Repositorio público

`Quebranto/Proyecto-Rudis` conserva:

- Corpus y decisiones canónicas.
- Arquitectura institucional y State OS.
- Especificaciones públicas.
- Interfaz y diseño del videojuego.
- Contratos no sensibles.
- Documentación necesaria para colaboración y auditoría conceptual.

## Repositorio privado

`Quebranto/tt` contiene el **código del ecosistema Rudis** y sus componentes técnicos sensibles.

Incluye progresivamente:

- State OS ejecutable.
- Núcleo y subsistemas.
- Palacio de Conversión.
- Integraciones internas.
- pruebas técnicas y adversariales.
- detalles de seguridad operativa.
- infraestructura y configuración privada.

## Regla de migración

Cuando una implementación deje de ser apropiada para exposición pública:

1. se mantiene su contrato arquitectónico en el repositorio público;
2. su implementación pasa al repositorio privado;
3. la documentación pública evita exponer detalles que faciliten ataques;
4. el trabajo del corpus no se modifica salvo para actualizar sus referencias de implementación.

El repositorio privado implementa el Canon público; no lo sustituye.
