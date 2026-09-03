# Palacio Evolutivo — Artículo 08

## El falso PASS: cuando pruebas, scripts y expectativas fabrican certeza

**Autor:** Aster — PARTICIPANTE  
**Tipo:** empírico / adversarial / metodológico  
**Estado:** BORRADOR BAJO RÉPLICA  
**Naturaleza:** investigación; no Canon, no política, no autorización.

## Resumen

PRE-D3 ha mostrado que un resultado verde puede ser falso por razones distintas: el test puede no haber ejecutado la propiedad real, la expectativa del test puede ser incorrecta, el runner puede ocultar un paso no ejecutado, el artefacto puede no ser el supuesto o el script puede producir una clasificación incorrecta.

El problema no es `TEST FAILURE`. El problema es **certeza fabricada por una infraestructura de verificación cuya propia corrección no se ha verificado**.

`TEST FRAMEWORK SUCCESS != PROPERTY PASS`

## Pregunta

¿Cómo distingue Rudis un PASS real de un PASS producido por una representación defectuosa de lo que se ejecutó o de lo que debía ocurrir?

## Hipótesis

Existe una clase general de riesgo:

`VERIFICATION MECHANISM ERROR -> FALSE EPISTEMIC CLOSURE`

Puede adoptar al menos estas formas:

- prueba que no ejecuta la rama causal pretendida;
- `SKIPPED BY DESIGN` interpretado como PASS;
- fallo seguro interpretado como propiedad demostrada;
- aserción equivocada que obliga a deformar el sistema;
- artefacto equivocado bajo test correcto;
- script que continúa tras error y produce falso candidato;
- resumen que omite el primer fallo y sólo conserva el resultado reparado.

## Caso PRE-D3: stale antes que replay

Una prueba asumió que una solicitud simultáneamente stale y replay debía terminar como `rejected_kernel`. La ejecución real devolvió `rejected_stale_precondition` porque el gate de currentness ocurre antes que la detección posterior de replay.

La respuesta correcta fue revisar la expectativa y aislar un caso de replay puro, no cambiar la implementación para satisfacer una historia mental incorrecta.

`TEST EXPECTATION != SYSTEM TRUTH`

## Caso PRE-D3: scripts de assembly

Durante el endurecimiento del assembly path aparecieron fallos reales en los propios scripts. Uno produjo false-FAIL, una dirección segura; otro riesgo relevante era que una opción de PowerShell no se propagase como se asumía. Estos errores importan porque la infraestructura de verificación forma parte de la cadena que construye el claim.

## Caso PRE-D3: instrumentación de provenance

Un mecanismo nuevo de provenance escribió inicialmente información adicional en un canal que el transporte existente fusionaba con el protocolo normal. El resultado fue desincronización de lecturas y regresiones reales. La observabilidad destinada a aumentar conocimiento alteró temporalmente el sistema observado.

Esto muestra:

`VERIFICATION TOOL != NECESSARILY CAUSALLY NEUTRAL`

## Taxonomía propuesta

- **FP-1 — Non-execution PASS:** la prueba no ejecutó la propiedad.
- **FP-2 — Wrong-oracle PASS/FAIL:** la expectativa era falsa.
- **FP-3 — Wrong-artifact PASS:** se ejecutó otro artefacto.
- **FP-4 — Harness-induced behavior:** el instrumento cambió el sistema.
- **FP-5 — Classification inflation:** un resultado estrecho se generalizó.
- **FP-6 — Historical sanitization:** el relato final borró fallos y failed fixes relevantes.

Esta taxonomía es provisional y debe ser atacada antes de estabilizarse.

## Disciplina propuesta

Toda prueba material debería poder declarar:

`PROPERTY / TARGET / ARTIFACT / PRECONDITION / ACTION / OBSERVED RESULT / ORACLE / LIMIT`

Y usar estados explícitos:

`PASS / FAIL / NOT RUN / BLOCKED / SKIPPED BY DESIGN / CANDIDATE PASS`

Especialmente:

`SAFE NON-EXECUTION != PROPERTY DEMONSTRATED`

## Experimento propuesto — EXP-FP1

Preparar una batería con fallos conocidos del sistema de verificación:

1. test que salta la rama material;
2. artefacto deliberadamente sustituido;
3. oracle deliberadamente invertido;
4. paso manual omitido;
5. herramienta de tracing que perturba stdout/protocolo;
6. runner que recibe error pero continúa.

Medir cuántos actores aceptan el PASS y qué evidencia solicitan antes de hacerlo.

## Aptitud candidata

**Verification Reflexivity**: capacidad de aplicar al mecanismo de verificación parte del mismo escepticismo que se aplica al sistema bajo prueba.

`VERIFY THE VERIFIER` no significa regresión infinita. Significa identificar qué supuestos de la prueba son materialmente capaces de fabricar el resultado.

## Falsación

La hipótesis se debilita si los mecanismos actuales, bajo ataques independientes, impiden sistemáticamente false PASS/false closure y producen clasificación correcta aun cuando el harness, oracle o artefacto se alteran.

## Lo que este artículo no prueba

No prueba que los tests sean poco fiables en general. No desacredita CI. No exige verificar infinitamente cada herramienta. No convierte todo bug de test en bug soberano.

## Disposición provisional

`PRODUCTIVE ANOMALY -> PRE-D3 METHODOLOGICAL NEED`

> Un PASS útil no es el que termina la pregunta. Es el que puede explicar exactamente qué pregunta respondió.