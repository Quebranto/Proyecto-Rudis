# Controles de seguridad para la demo D2

Este documento describe controles verificables; no acredita producción.

## Controles administrativos requeridos

- rama principal protegida, sin force-push ni borrado;
- revisión obligatoria y resolución de conversaciones;
- checks de seguridad requeridos sobre el head exacto;
- permisos de workflows de sólo lectura por defecto;
- acciones externas fijadas a commits inmutables;
- secret scanning y push protection cuando el plan lo permita;
- revisión explícita de contribuciones no confiables;
- CODEOWNERS para workflows y política de seguridad.

Los estados de configuración no demostrables por evidencia administrativa deben
marcarse `NO VERIFICABLE`. Ningún documento sustituye el control real.

## Frontera de publicación

La superficie pública puede registrar propiedades, resultados sanitizados,
decisiones y riesgos residuales. No publicará secretos, localizadores privados,
hashes internos, topología sensible, recetas de explotación ni evidencia
reutilizable.

`transparencia constitucional != exposición operacional`
