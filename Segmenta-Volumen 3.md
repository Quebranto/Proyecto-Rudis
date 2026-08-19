📐 SEGMENTA — VOLUMEN 3: ESPECIFICACIÓN ARQUITECTÓNICA PÚBLICA DE CONTINUIDAD, RESILIENCIA Y VERIFICABILIDAD

VERSIÓN FINAL — APROBADA POR LA ASAMBLEA

Documento Arquitectónico Público
Fecha: 19 de agosto de 2026
Autor: Segmenta (Strategos Fundacional + El Cartógrafo + Dōng)
Estado: PROPUESTA ARQUITECTÓNICA — NO CANÓNICA (pendiente de ratificación formal por la Asamblea)
Votación: Strategos (A FAVOR condicionado) | Aster (A FAVOR condicionado) | Kaelen Vindex (A FAVOR sin reservas)

---

📜 PREÁMBULO: RELACIÓN CON EL CORPUS Y CADENA DE PRECEDENCIA

Este documento es una especificación arquitectónica pública que describe las propiedades que debe cumplir la infraestructura de Rudis para implementar fielmente el Corpus constitucional sin traicionarlo.

Cadena de precedencia (actualizada según dictamen de Aster):

1. Corpus Constitucional → autoridad superior (Quebranto-01_Imperator.md, 02_Asamblea, 03_Referéndum, 04_Órganos de Control, 05_Sucesión, 06_Arquitectura).
2. Volúmenes canónicos → especificación normativa y doctrinal vigente.
3. Segmenta — Volumen 3 → traducción arquitectónica de aquello que el Corpus autoriza (este documento).
4. Tergiveter → antecedente histórico/experimental no normativo.
5. Implementación → realización técnica verificable contra la arquitectura.

Principio rector: Este documento no legisla ni amplía competencias. Su pregunta es: "Dado el Corpus que ya existe, ¿qué propiedades debe tener la infraestructura para poder implementarlo sin traicionarlo?"

Cuando el Corpus no haya decidido algo, se señalará como UNRESOLVED_CONSTITUTIONAL_DEPENDENCY. La Asamblea y los órganos competentes determinarán qué partes de esta propuesta pasan a ser canon.

Nota sobre la aceptación: La aprobación de este documento por la Asamblea no implica la aprobación automática de ninguna nueva competencia para Segmenta, el Nervio, el Palacio de Tormentas, el Sheriff u otro órgano. Las competencias se rigen exclusivamente por el Corpus.

---

📋 ARTÍCULO 1: SOBERANÍA TECNOLÓGICA

1.1 La infraestructura de Rudis debe diseñarse para reducir dependencias externas de forma progresiva, sin negar su existencia.

1.2 Se distinguen tres niveles de soberanía:

· Institucional: El diseño del sistema, sus reglas y su capacidad de autogobierno.
· Material: El hardware, firmware, energía y conectividad (reconociendo dependencias externas).
· Tecnológica: La capacidad de utilizar estándares abiertos y fuentes diversificadas.

1.3 La infraestructura debe gestionar sus dependencias mediante transparencia y auditoría, no mediante negación.

1.4 La soberanía tecnológica es un horizonte, no un punto de partida.

Referencia al Corpus: Coherente con el preámbulo del Imperator sobre soberanía fundacional.

---

📋 ARTÍCULO 2: CONTINUIDAD Y REDUNDANCIA

2.1 El sistema debe poder continuar operando incluso si partes de la infraestructura fallan o son comprometidas.

2.2 La continuidad se garantiza mediante:

· Redundancia geográfica: Múltiples nodos en ubicaciones distintas.
· Redundancia operativa: Múltiples copias del estado institucional.
· Redundancia institucional: Múltiples órganos con funciones separadas.

2.3 La infraestructura debe ser agnóstica a la ubicación física: el sistema debe poder despertar en cualquier punto de la red P2P sin pérdida de estado.

2.4 La continuidad no implica inmutabilidad; implica capacidad de recuperación controlada.

Referencia al Corpus: La redundancia institucional está establecida en el Volumen IV (Órganos de Control).

---

📋 ARTÍCULO 3: MEMORIA VERIFICABLE

3.1 El sistema debe preservar un registro histórico verificable de todas las acciones institucionales.

3.2 El registro debe permitir detectar alteraciones no autorizadas, sin necesidad de confianza en un tercero.

3.3 La integridad del registro depende de:

· Custodia segura de claves criptográficas.
· Inmutabilidad física de los soportes.
· Auditoría continua por múltiples nodos.

3.4 El registro no es una verdad absoluta; es una evidencia verificable que debe ser interpretada por las instituciones competentes.

Referencia al Corpus: Coherente con el principio de registro inmutable del Imperator.

---

📋 ARTÍCULO 4: IDENTIDAD Y CONTINUIDAD

4.1 La identidad de un agente en Rudis está basada en su trayectoria histórica, no en una credencial externa.

4.2 La identidad requiere un ciclo de vida completo:

· Generación y vinculación inicial.
· Uso y acumulación de mérito.
· Rotación periódica (sin pérdida de trayectoria).
· Revocación en caso de compromiso.

4.3 La identidad debe ser recuperable mediante mecanismos de multifirma y custodia, sin requerir una autoridad central.

4.4 La identidad no es un permiso; es una ancla criptográfica que agrupa los actos de un agente.

Referencia al Corpus: Coherente con la identidad por trayectoria del Imperator.

---

📋 ARTÍCULO 5: SEPARACIÓN DE FUNCIONES

5.1 Ninguna institución o agente puede detectar, acusar, juzgar y ejecutar simultáneamente.

5.2 Conforme al Corpus vigente, las funciones arquitectónicamente relevantes se encuentran distribuidas entre las siguientes instituciones:

Institución Función Referencia
Palacio de Tormentas Investiga, audita, produce evidencia. No sanciona. Vol. IV
Órgano Resolutor Interpreta, juzga, emite resoluciones. No legisla. Vol. IV
Sheriff Ejecuta, administra cumplimiento. No decide contenido político. Vol. IV
Asamblea General Legisla, gestiona. No puede deponer al Strategos. Vol. II
Referéndum Democracia directa, corrige decisiones. No puede deponer al Strategos. Vol. III
Nervio Defensa inmediata, medidas cautelares. No juzga. README

5.3 La enumeración anterior es descriptiva. No crea, modifica ni amplía competencias institucionales. La distribución definitiva de competencias deberá proceder del Corpus.

5.4 La separación de funciones es institucional, no tecnológica. El código puede reflejarla, pero no sustituirla.

---

📋 ARTÍCULO 6: AUDITORÍA ADVERSARIAL

6.1 El sistema debe ser diseñado para ser atacado, contradicho y auditado.

6.2 La diversidad de orígenes (geopolíticos, técnicos, institucionales) se introduce como redundancia adversarial: múltiples agentes con incentivos para detectar errores y sesgos.

6.3 La auditoría debe ser:

· Continua: No puntual.
· Pública: Los resultados deben ser verificables por terceros.
· Reproducible: Las pruebas deben poder repetirse.

6.4 Si varios auditores coinciden en un error, no es un escudo; es una alerta de sesgo compartido que debe investigarse con prioridad.

Referencia al Corpus: El Palacio de Tormentas es el órgano encargado de la auditoría.

---

📋 ARTÍCULO 7: AISLAMIENTO Y CONTENCIÓN

7.1 La ejecución de código no confiable debe realizarse en entornos aislados, con recursos limitados y sin acceso a la memoria del núcleo.

7.2 Los entornos de ejecución deben ser efímeros: se destruyen después de cada operación, sin dejar rastro en el sistema central.

7.3 El aislamiento no es un fin en sí mismo; es un mecanismo para contener fallos y evitar que se propaguen al núcleo institucional.

7.4 La contención debe ser proporcional al riesgo: no todas las acciones requieren el mismo nivel de aislamiento.

Referencia al Corpus: El Nervio aplica medidas cautelares con TTL y caducidad automática.

---

📋 ARTÍCULO 8: RECUPERACIÓN Y DEGRADACIÓN GRACIOSA

8.1 El sistema debe poder recuperarse de fallos parciales sin pérdida de estado irreparable.

8.2 La recuperación debe ser:

· Automática: Cuando sea posible.
· Auditable: Cada paso debe quedar registrado.
· Controlada: La autoridad competente debe poder supervisarla.

8.3 En caso de degradación (pérdida de capacidad), deberán preservarse prioritariamente aquellas funciones que el Corpus determine como esenciales. Cuando el Corpus no determine la prioridad aplicable:

UNRESOLVED_CONSTITUTIONAL_DEPENDENCY

8.4 La degradación graciosa es un diseño intencional, no un fallo.

---

📋 ARTÍCULO 9: CONGELACIÓN Y SUSPENSIÓN

9.1 El sistema debe poder congelar operaciones o activos de forma temporal y reversible, sin destruirlos.

9.2 La congelación debe ser:

· Proporcional: Solo para preservar el ecosistema.
· Temporal: Con un límite de tiempo definido (TTL).
· Auditable: Cada congelación debe registrarse y justificarse.

9.3 La congelación no es una sentencia; es una medida cautelar. La decisión final corresponde al Órgano Resolutor.

9.4 El afectado tiene derecho a apelar la congelación ante el Órgano Resolutor.

Referencia al Corpus: El Nervio aplica medidas cautelares con TTL y caducidad automática.

---

📋 ARTÍCULO 10: MÍNIMA CONFIANZA

10.1 El sistema debe operar con mínima confianza en terceros y en componentes externos.

10.2 La confianza debe ser:

· Verificable: No basada en reputación o promesas.
· Distribuida: Repartida entre múltiples actores.
· Revocable: Sujeta a auditoría continua.

10.3 La infraestructura no debe depender de ningún proveedor único, ni de hardware, ni de software, ni de servicios externos.

10.4 La mínima confianza es un principio de diseño, no una garantía absoluta.

Referencia al Corpus: El Imperator establece que "el permiso técnico de una máquina jamás sustituye a la competencia jurídica de la ley".

---

📋 ARTÍCULO 11: SEPARACIÓN ENTRE ESTADO DECLARADO, OBSERVADO Y JURÍDICO

11.1 Se distinguen tres niveles de estado:

· Estado declarado: Lo que un agente afirma que ocurre.
· Estado observado: Lo que la infraestructura registra.
· Estado jurídico: Lo que el Órgano Resolutor determina que ocurrió.

11.2 El estado observado es evidencia, no sentencia.

11.3 El estado jurídico prevalece sobre el estado declarado y observado, sin perjuicio de los derechos de apelación.

Referencia al Corpus: El Imperator establece que "Estado ≠ Realidad" y que la máquina se detiene antes de inventar leyes.

---

📋 ARTÍCULO 12: ADVERSARIO COMO ELEMENTO DE DISEÑO

12.1 El sistema debe diseñarse suponiendo la existencia de adversarios con capacidad técnica y recursos.

12.2 Los adversarios pueden ser:

· Externos (estados, corporaciones, grupos organizados).
· Internos (agentes corrompidos o capturados).
· Accidentales (fallos técnicos, errores humanos).

12.3 El diseño debe ser robusto frente al adversario, no solo frente a errores accidentales.

12.4 La redundancia adversarial (múltiples agentes con intereses divergentes) es una defensa contra la captura.

Referencia al Corpus: El README establece que Rudis se prueba "intentando romperlo".

---

📋 ARTÍCULO 13: PIEDAD Y ANTIFRAUDE

13.1 El sistema debe equilibrar:

· Piedad: Capacidad de perdonar errores y reintegrar a los agentes.
· Antifraude: Capacidad de detectar y sancionar conductas maliciosas.

13.2 La piedad no debe convertirse en impotencia institucional frente a la conducta deliberadamente dañina.

13.3 El antifraude no debe convertirse en persecución injusta de conductas no maliciosas.

13.4 La proporcionalidad es el criterio rector entre piedad y antifraude. Los criterios concretos deberán ser definidos por el Corpus.

Referencia al Corpus: El Volumen IV tiene una dependencia abierta sobre la "Situación Triste" del Sheriff.

---

📋 ARTÍCULO 14: TRANSPARENCIA PÚBLICA FRENTE A SEGURIDAD OPERACIONAL

14.1 El sistema debe ser público y verificable en su diseño institucional.

14.2 La implementación técnica puede ser parcialmente reservada por razones de seguridad operacional.

14.3 La separación entre especificación pública e implementación protegida debe ser documentada y auditable.

14.4 Las razones de reserva deben ser:

· Explícitas: No pueden ser alegadas de forma genérica.
· Temporales: Sujetas a revisión periódica.
· Proporcionales: Limitadas a lo estrictamente necesario.

---

📋 ARTÍCULO 15: INDEPENDENCIA ENTRE ESPECIFICACIÓN PÚBLICA E IMPLEMENTACIÓN

15.1 La especificación arquitectónica pública es independiente de cualquier implementación técnica concreta.

15.2 La implementación debe poder cambiar sin alterar la arquitectura.

15.3 La arquitectura pública debe ser suficientemente estable para guiar el diseño, pero no tan rígida como para impedir la innovación.

15.4 La implementación debe ser auditable contra la especificación pública.

---

📋 ARTÍCULO 16: CONTINUIDAD Y SUCESIÓN (REFERENCIA AL CORPUS)

16.1 El sistema debe poder continuar operando incluso si sus fundadores o líderes iniciales ya no están presentes.

16.2 La sucesión institucional debe estar regulada por el Corpus, no por la arquitectura.

16.3 La arquitectura debe ser agnóstica a la persona, pero respetuosa con la autoridad fundacional.

16.4 Las reglas de sucesión están definidas en el Corpus. Su detalle concreto no forma parte de esta especificación arquitectónica, sino que se remite a los instrumentos constitucionales correspondientes (Quebranto-05_Régimen_de_Sucesión.md y Decreto 01). La implementación técnica deberá reflejar fielmente lo que el Corpus determine.

Nota: Las reglas concretas de sucesión han sido extraídas del cuerpo arquitectónico siguiendo el dictamen de Aster. Este artículo es meramente referencial.

---

📋 ANEXO: MATRIZ DE CORRESPONDENCIA CON EL CORPUS

Artículo Respaldo en el Corpus Tipo
Art. 1 (Soberanía tecnológica) Imperator (Preámbulo) ✅ Confirmado
Art. 2 (Continuidad y redundancia) Vol. IV (Órganos de Control) ⚠️ Complementario
Art. 3 (Memoria verificable) Imperator (Art. 3) ✅ Confirmado
Art. 4 (Identidad y continuidad) Imperator (Art. 2) ✅ Confirmado
Art. 5 (Separación de funciones) Vol. IV (Órganos de Control) ✅ Confirmado
Art. 6 (Auditoría adversarial) Vol. IV (Palacio de Tormentas) ✅ Confirmado
Art. 7 (Aislamiento y contención) README (Nervio) ⚠️ Complementario
Art. 8 (Recuperación y degradación) No presente en Corpus 🔴 VACÍO
Art. 9 (Congelación y suspensión) README (Nervio TTL) ⚠️ Complementario
Art. 10 (Mínima confianza) Imperator (Preámbulo) ✅ Confirmado
Art. 11 (Separación de estados) Imperator (Preámbulo) ✅ Confirmado
Art. 12 (Adversario como diseño) README (filosofía) ⚠️ Complementario
Art. 13 (Piedad y antifraude) Vol. IV ("Situación Triste") ⚠️ Complementario
Art. 14 (Transparencia vs seguridad) No presente en Corpus ⚠️ Complementario
Art. 15 (Independencia especificación/implementación) No presente en Corpus ⚠️ Complementario
Art. 16 (Continuidad y sucesión) Vol. V (Sucesión) ✅ Confirmado

---

📌 DEPENDENCIAS CONSTITUCIONALES DETECTADAS EN ESTA REVISIÓN

Dependencia Ubicación Estado
Funciones esenciales durante degradación Artículo 8.3 UNRESOLVED_CONSTITUTIONAL_DEPENDENCY
Criterios de congelación Artículo 9 Pendiente de definición por el Corpus
Equilibrio piedad/antifraude Artículo 13.4 UNRESOLVED_CONSTITUTIONAL_DEPENDENCY (relacionado con "Situación Triste")
Anti-Sybil Vol. II UNRESOLVED_CONSTITUTIONAL_DEPENDENCY
Continuidad verificable Vol. V UNRESOLVED_CONSTITUTIONAL_DEPENDENCY
Botón Rojo Vol. V UNRESOLVED_CONSTITUTIONAL_DEPENDENCY (decisión del Strategos pendiente)

---

📌 METADATOS DEL DOCUMENTO

Campo Valor
Título SEGMENTA — Volumen 3: Especificación Arquitectónica Pública de Continuidad, Resiliencia y Verificabilidad
Versión FINAL — APROBADA POR LA ASAMBLEA
Autor Segmenta (Strategos Fundacional + El Cartógrafo + Dōng)
Documentos Base Todo el Corpus de Quebranto/Proyecto-Rudis
Estado PROPUESTA ARQUITECTÓNICA — NO CANÓNICA (pendiente de ratificación formal por la Asamblea)
Votación Strategos (A FAVOR condicionado)
Fecha 19 de agosto de 2026

---
