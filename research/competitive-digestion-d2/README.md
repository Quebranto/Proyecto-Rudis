# Campaña D2 de digestión competitiva — Wave 15 v0.1

Estado: investigación D2 abierta; sin acreditación productiva ni integración material.  
Autoridad de trabajo: [Issue #32](https://github.com/Quebranto/Proyecto-Rudis/issues/32).  
Fecha de corte: 24 de agosto de 2026.

## Propósito

Estudiar OAGS, OpenEAGO, ACP, OpenAGP y Anumati como fuentes externas, comparar sus mecanismos y delimitar qué puede absorber Rudis sin importar autoridad, semántica jurídica o una segunda historia soberana.

`evidencia externa != autoridad`

`conformance != acreditación Rudis`

`consentimiento técnico != mandato jurídico`

## Entregables iniciales

- [Snapshot de fuentes v0.1](SOURCE-SNAPSHOT-v0.1.md): identidades, commits, versiones, licencias, colisiones nominales y estado Radar propuesto.
- [Mapa competitivo transversal v0.1](TRANSVERSAL-MAP-v0.1.md): fortalezas, brechas, conceptos absorbibles y rutas de aislamiento.
- [Threat model transversal v0.1](THREAT-MODEL-v0.1.md): amenazas de captura, downgrade, replay, sustitución de verifier y confusión de autoridad.
- [Manifest sellado v0.1](campaign-manifest-v0.1.json), validador y pruebas: guardas offline contra sustitución de snapshot, escalada de fase y rutas soberanas prohibidas.

Verificación offline:

```text
python validate_campaign.py
python -m unittest -v test_validate_campaign.py
```

## Frontera de la campaña

Permitido: análisis, modelos, pruebas de reproducibilidad, prototipos offline y simulaciones etiquetadas.  
Prohibido: D3/D4, producción, reconocimiento político, credenciales reales, red en runtime, integración con Kernel o Continuity, y cualquier bypass de `AuthorityResolver -> LawEngine -> Mandate`.

## Estado inicial de expedientes

| Expediente | Frente | Estado de trabajo | Próximo gate |
|---|---|---|---|
| OAGS | Digestión profunda | D2 documental condicionado | Reproducir conformance y revisar canonicalización |
| OpenEAGO | Digestión profunda | D2-candidate / D1 acreditación Rudis | Auditoría de captura y fixture offline |
| ACP | Dossier paralelo | D1 propuesto | Threat-model y límites de enforcement |
| OpenAGP | Dossier paralelo | D1-pending | Snapshot multirrepo y reproducción CTS |
| Anumati / ACAP | Dossier paralelo | D1-pending; identidad candidata | Resolver identidad y reproducir invariantes |

Ningún estado de esta tabla constituye promoción competente. Es una recomendación técnica sometida a revisión.

