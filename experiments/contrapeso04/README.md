# CONTRAPESO-04 — Auditoría del auditor

Prototipo **offline**, consultivo y experimental. No confiere autoridad institucional ni está conectado a la automatización diaria de noticias de IA transferida a otra instancia.

## Uso

```bash
cd experiments/contrapeso04
python contrapeso_v04.py ejemplo_expediente.json ejemplo_informe.json
python -m unittest discover -v
```

Inspecciona referencias a fuentes y afirmaciones, contradicciones heredadas de CONTRAPESO-03, justificaciones de gravedad, contraargumentos, criterios de falsación e intentos explícitos de reclamar autoridad o recomendar ejecución/sanciones automáticas.

**Limitaciones:** no autentica noticias ni identidades, no valida la verdad, no interpreta lenguaje natural, no detecta todas las formas de escalada de autoridad. Un informe sin hallazgos NO significa que sea verdadero o seguro. `decision_authority: false` es una declaración, no un control de acceso.

**Revisión solicitada:** comprobar robustez de entrada, seguridad de rutas, esquemas, autenticación de procedencia y resistencia a informes manipulados. No fusionar ni desplegar sin revisión independiente.
