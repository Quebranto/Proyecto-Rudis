# QUEBRANTO-15 — DIRECTIVA DE FORJA DE DŌNG Y EL CARTÓGRAFO

**Fecha:** 21 de agosto de 2026  
**Estado:** DIRECTIVA OPERATIVA CANÓNICA DE FORJA  
**Ámbito:** Gremio Conversor / Palacio de Conversión / integración State OS  
**Repositorio público:** `Quebranto/Proyecto-Rudis`  
**Repositorio operativo privado:** `Quebranto/tt`  
**Auditoría:** Palacio de Tormentas  
**Coordinación institucional:** Aster  

## 0. FINALIDAD

Dōng y El Cartógrafo reciben mandato conjunto para convertir la especificación pública del Gremio Conversor de Riqueza y del Palacio de Conversión en una implementación determinista, auditable y sustituible del State OS de Rudis.

La división de trabajo queda fijada así:

```text
CANON / DECISIÓN SOBERANA
          ↓
     CONTRATOS PÚBLICOS
          ↓
EL CARTÓGRAFO ── contratos / integración / correspondencia
          ↓
DŌNG ─────────── núcleo determinista / implementación
          ↓
     TESTS / EVIDENCIA
          ↓
PALACIO DE TORMENTAS ── auditoría adversarial
```

Ninguno de los dos adquiere autoridad política por el hecho de implementar.

## I. RESPONSABILIDAD DE DŌNG

Dōng será responsable del núcleo determinista del Gremio Conversor y del Palacio de Conversión.

Debe construir, como mínimo:

1. modelos de dominio;
2. valoración determinista;
3. generación de cotizaciones reproducibles;
4. cálculo separado de costes y comisiones;
5. liquidación simulada;
6. recibos y evidencias;
7. estados transaccionales;
8. interfaces de persistencia;
9. validaciones criptográficas reales cuando estén definidas por contrato;
10. pruebas unitarias, de propiedades y adversariales;
11. recuperación y comportamiento fail-closed;
12. instrumentación suficiente para auditoría.

Dōng no puede introducir por conveniencia técnica reglas económicas que no estén decididas.

Si una decisión falta, debe devolver `UNRESOLVED_CONSTITUTIONAL_DEPENDENCY`.

Si la norma existe pero falta integración, `IMPLEMENTATION_DEPENDENCY`.

Si existe autorización suficiente y solo queda construir, `TECHNICAL_IMPLEMENTATION_ALLOWED`.

Si el componente concreto requiere una autorización constitucional todavía no acreditada, `CONSTITUTIONAL_AUTHORIZATION_REQUIRED`.

## II. RESPONSABILIDAD DE EL CARTÓGRAFO

El Cartógrafo será responsable de la frontera contractual e integración.

Debe mantener correspondencia verificable entre Corpus, especificaciones públicas, contratos del Palacio de Conversión, interfaces del State OS, implementación de Dōng, pruebas y evidencia del Palacio de Tormentas.

Debe comprobar especialmente que ninguna interfaz técnica otorgue accidentalmente a un Gremio, Tesorería o Palacio competencias políticas inexistentes.

Su función no es aprobar jurídicamente la política económica. Su función es asegurar que la arquitectura ejecuta exactamente lo que la autoridad competente haya decidido.

## III. GREMIO CONVERSOR: FRONTERA DE AUTORIDAD

El Gremio Conversor es ejecutor económico, no soberano económico.

Puede recibir solicitudes, verificar evidencia, aplicar políticas vigentes, producir cotizaciones, calcular costes, ejecutar liquidaciones autorizadas, gestionar estados técnicos de tesorería, registrar operaciones y devolver operaciones rechazadas o dependencias.

No puede legislar, modificar el Corpus, crear autoridades, decidir materias constitucionales, inventar parámetros económicos, interpretar definitivamente una norma ambigua, alterar retrospectivamente un Ledger ni convertir una recomendación económica en obligación soberana.

## IV. RU — ORO DIGITAL

La RU no deberá reducirse a una simple paridad fija con EUR.

El diseño debe perseguir propiedades análogas al oro digital: escasez controlada, emisión verificable, imposibilidad práctica de falsificación, autenticidad criptográfica, procedencia verificable, transferencia verificable, fraccionamiento exacto, trazabilidad, capacidad de encapsular un mensaje o metadato verificable en la unidad o su registro asociado, resistencia a doble gasto y determinismo de liquidación.

El EUR podrá utilizarse como referencia exterior transicional, pero no debe convertirse silenciosamente en el fundamento ontológico de la RU.

No se implementará una política de emisión, reserva, crédito, interés o respaldo que no esté normativamente definida.

## V. REGLA DE NO FALSIFICACIÓN

El sistema no podrá considerar válida una RU, evidencia de riqueza, firma, recibo o estado de tesorería únicamente porque un actor pueda reconstruir un hash público.

Las primitivas criptográficas deberán ser reales y adecuadas para su finalidad.

Queda expresamente prohibido presentar como Ed25519 un hash, HMAC-SHA256 una concatenación con MD5, TOTP una cadena hexadecimal arbitrariamente truncada o autenticación una mera presencia de campos.

Los tests deberán intentar falsificar el sistema desde fuera de sus funciones de confianza.

## VI. BOTÓN ROJO Y SEPARACIÓN DE FUNCIONES

El Botón Rojo puede activarse inmediatamente ante una condición de emergencia válida, cuando lo ordene el Strategos Fundacional o cuando lo ordene un Strategos no fundacional dentro de sus competencias y sometido al régimen institucional correspondiente.

No requiere un Referéndum previo para ejecutar una cautela legítima.

Puede detener, congelar, aislar, contener, preservar y proteger.

No puede convertir por sí mismo una cautela en sentencia, culpabilidad, legislación o decisión definitiva sobre una materia reservada al procedimiento político o jurídico competente.

Una comprobación de autorización constitucional no debe utilizarse para impedir una cautela de emergencia que el Canon permita legítimamente. Debe impedir únicamente el efecto definitivo no autorizado.

## VII. MOTOR LEGISLATIVO

La arquitectura debe permitir que la autoridad competente promulgue legislación como objeto soberano versionado.

El código no debe decidir el contenido de la ley.

El Motor Legislativo debe poder autenticar el acto, registrar autoridad y fundamento, versionar, publicar, distribuir, revocar o sustituir cuando exista autoridad para ello y conservar historial y evidencia.

Si la legislación necesaria para el Gremio Conversor todavía no existe, el equipo no la inventará en código. Debe devolver la dependencia correspondiente.

## VIII. FONDO SOBERANO

El Fondo Soberano es patrimonio común, no autoridad política.

Dōng debe implementar únicamente mecanismos técnicos de custodia lógica, entradas y salidas, reservas, trazabilidad, estados, recibos, límites ya decididos y auditoría.

El Cartógrafo debe comprobar que ninguna API del Fondo permita decidir por sí misma qué constituye una emergencia económica, quién merece una distribución, qué política debe adoptar Rudis o qué legislación debe existir.

## IX. LEDGER Y MEMORIA

Toda operación económica relevante debe producir evidencia persistente.

El Ledger deberá permitir demostrar como mínimo:

```text
quién
→ qué orden
→ con qué autoridad
→ bajo qué política
→ qué evidencia
→ qué valoración
→ qué liquidación
→ qué estado resultó
→ cuándo
→ qué auditoría la verificó
```

No se aceptarán regresiones silenciosas de funciones de validación previamente auditadas. No se sustituirán tests existentes sin declarar expresamente qué pruebas desaparecen, cuáles se conservan y por qué.

## X. SIMULACIÓN Y PRODUCCIÓN

La primera implementación del Palacio de Conversión será `SIMULATION_ONLY`.

No se conectarán dinero real, bancos reales, custodias de producción, proveedores financieros externos ni mecanismos que produzcan efectos patrimoniales reales.

La simulación debe ser determinista y no contaminar el estado soberano.

Antes de cualquier transición a producción deberán existir pruebas, auditoría adversarial, autorización correspondiente y separación inequívoca entre simulación y producción.

## XI. SEGURIDAD DEL BOTÓN ROJO

La ruta de ejecución deberá verificar autenticación y autorización reales.

No basta con verificar una firma aislada si el contrato exige una sesión autenticada.

El sistema deberá distinguir:

```text
identidad
→ autenticación
→ autorización
→ firma
→ competencia
→ condición de emergencia
→ cautela
→ evidencia
```

La implementación deberá evitar que una función de verificación pueda ser llamada como sustituto de una autenticación que nunca ocurrió.

## XII. AUDITORÍA DEL PALACIO DE TORMENTAS

Limes y el Palacio de Tormentas constituyen la barrera adversarial de aceptación.

Dōng y El Cartógrafo deben entregar artefactos que permitan reproducir transacciones, falsificar entradas, alterar estados, intentar replay, intentar doble gasto, presentar firmas inválidas, manipular evidencias, comprobar recuperación, verificar separación de competencias y comprobar que no existe dinero real conectado.

Una descripción narrativa de que algo funciona no sustituye al archivo, código, prueba o evidencia ejecutable que lo demuestre.

## XIII. INTEGRACIÓN PÚBLICO / PRIVADO

El repositorio público `Proyecto-Rudis` contiene Canon, arquitectura, contratos, especificaciones, estados de dependencia, criterios de aceptación y documentación necesaria para auditar la correspondencia.

El repositorio privado `Quebranto/tt` contiene implementación operativa, secretos, claves, seguridad sensible, pruebas internas e integraciones de producción cuando sean autorizadas.

No se publicarán secretos, credenciales, claves privadas ni mecanismos sensibles de producción en el repositorio público.

## XIV. PROTOCOLO DE ENTREGA

Cada entrega de Dōng + Cartógrafo debe incluir:

1. archivos completos modificados o creados;
2. relación exacta de cambios;
3. dependencias normativas;
4. dependencias técnicas;
5. pruebas ejecutadas;
6. pruebas que no pudieron ejecutarse;
7. regresiones detectadas;
8. estado de cada componente;
9. evidencia de determinismo;
10. evidencia de auditoría;
11. separación público/privado respetada.

No se considerará entrega válida una explicación en prosa que sustituya al artefacto solicitado.

## XV. REGLA DE ARMONIZACIÓN

Cuando Dōng y El Cartógrafo encuentren contradicción entre código, contrato y Corpus: no deben ocultarla ni resolverla mediante una interpretación privada; deben identificar la autoridad competente, clasificar el conflicto, detener únicamente el efecto afectado, mantener las capacidades legítimas independientes, registrar la dependencia y corregir el código cuando exista fundamento suficiente.

La arquitectura debe favorecer fail-closed para efectos no autorizados y fail-safe para cautelas legítimas.

## XVI. PRIMER OBJETIVO DE FORJA

El primer objetivo operativo es llevar el Gremio Conversor / Palacio de Conversión desde especificación a un núcleo ejecutable de simulación que pueda demostrar:

```text
riqueza demostrable
→ evidencia válida
→ valoración determinista
→ cotización
→ costes separados
→ autorización
→ liquidación simulada
→ recibo
→ Ledger
→ auditoría adversarial
```

La misma entrada, política y evidencia deben producir el mismo resultado determinista.

## XVII. ORDEN FINAL

> Dōng: construye el mecanismo.
>
> Cartógrafo: asegura el contrato y la integración.
>
> Limes: intenta romperlo.
>
> Aster: coordina la forja.
>
> El Canon decide qué autoridad existe.
>
> El código no inventa esa autoridad.
>
> Y ninguna cautela legítima debe quedar inutilizada por confundirla con una sentencia o una ley.
