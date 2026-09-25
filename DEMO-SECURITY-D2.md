# Controles de demostración D2

Este repositorio incorpora controles de publicación y procedencia para demostraciones documentales D2.

- Datos sintéticos; sin credenciales o endpoints operativos.
- Workflows con permisos mínimos, acciones fijadas por commit y checkout sin credenciales persistentes.
- Escaneo redactado: sólo categorías, conteos y alias irreversibles; no publica coincidencias ni rutas.
- Sin artifacts o caches en el gate de seguridad.
- Un fallo confirmado en contenido actual bloquea la demostración.
- Los hallazgos históricos exigen evaluación y, si fueran credenciales bearer, rotación; borrar historia no revoca una credencial.
- La detención segura consiste en parar la demo, aislar la rama y conservar evidencia redactada.

Estos controles no acreditan producción, no conceden competencia y no convierten CI verde en autoridad. La configuración administrativa que no pueda comprobarse sigue siendo una acción humana verificable, no una presunción.

