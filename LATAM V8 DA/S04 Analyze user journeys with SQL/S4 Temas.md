# Sprint 4: Analiza Journeys de usuarios con SQL
🗓️ Fecha de creación: 10 Noviembre 2025  
🗓️ Fecha de actualización: 10 Noviembre 2025<br><br>

---
## Capitulo 1: Entendendiendo el user journey y estructurando el análisis
### C1 - Lección 1: Entendiendo un journey en los datos
<br>

**🎯 Propósito de la lección**

Introducir el user journey como la ruta secuencial de eventos que un usuario recorre hasta (o sin) lograr un objetivo de negocio, y mostrar cómo esa ruta se convierte en embudos medibles con SQL para identificar fricción, eficiencia y oportunidades de mejora.

**🧠 Idea central**

El journey se modela en una tabla de eventos ordenados por tiempo. Medir un journey equivale a construir un embudo (funnel): contar cuántos avanzan entre etapas, cuánto tardan y dónde se detienen, definiendo desde el inicio unidad de análisis (usuario o sesión) y ventana temporal.

**🧩 Conceptos y estructura del análisis**

**Macro vs. Micro-journey**

    - Macro-journey: vista de punta a punta (p. ej., page_view → view_item → add_to_cart → begin_checkout → purchase). Útil para visión global, tasa de conversión final y tiempo total.
    - Micro-journey: tramo específico (p. ej., add_to_cart → purchase). Útil para aislar fricciones concretas y ejecutar mejoras tácticas.

**Dimensiones de análisis**

    - Usuario (user_id): mide conversión “real” (personas únicas). Impacta lealtad, re-compra y cohortes.
    - Sesión (session_id): mide eficiencia de la interfaz en un episodio; detecta pasos redundantes.
    - Evento (event_name): acción puntual que permite diagnósticos finos (scrolls, clicks críticos, errores).

**Requisitos de datos**

    - Timestamps con zona horaria consistente.
    - Identificadores estables (mismo user_id entre etapas).
    - Enum de eventos con definición clara (qué dispara cada uno).

**📊 Métricas clave del embudo (con supuestos y SQL base)**

**Supuesto común:** medición por usuario (ajustar a sesión si el objetivo es UX puntual). Orden por tiempo es obligatorio.

1. **Tasa de conversión (A→B)**

    **SQL (esqueleto):**

    `WITH a AS (`
    `SELECT DISTINCT user_id FROM events WHERE event_name = 'view_item'  AND event_date BETWEEN :d1 AND :d2`
    `),`
    `b AS (`
    `SELECT DISTINCT user_id FROM events WHERE event_name = 'add_to_cart' AND event_date BETWEEN :d1 AND :d2`
    `)`
    `SELECT 100.0 * COUNT(DISTINCT b.user_id) / NULLIF(COUNT(DISTINCT a.user_id),0) AS conv_pct`
    `FROM a LEFT JOIN b ON a.user_id = b.user_id;`

2. **Volumen por etapa**

    `COUNT(DISTINCT user_id)` por evento/etapa dentro del periodo.

3. **Velocidad de conversión (inicio→objetivo)**

    Promedio del tiempo total desde el primer evento hasta purchase. Señala fluidez global.

**Interpretación rápida**

- Conversión alta + tiempo corto ⇒ eficiencia.
- Conversión baja + tiempo alto ⇒ fricción (UI, precio, confianza).
- Volumen alto con conversión baja ⇒ cuello de botella en esa etapa.

**🛠️ “Cómo hacerlo” (procedimiento operativo)**

1. Alinear objetivo de negocio (venta, registro, activación) y definir etapas.
2. Elegir unidad (usuario / sesión) y ventana temporal (día, semana, mes; TZ).
3. Normalizar eventos (diccionario) y ordenar por timestamp.
4. Construir conteos por etapa y tablas A/B; derivar conversión y drop-off.
5. Calcular tiempos entre etapas y velocidad global.
6. Visualizar embudo con volumen y %; destacar el mayor drop-off.
7. Hipótesis sobre causas (precio, latencia, UX) y pruebas (A/B, copy, CU).
8. Iterar: medir después del cambio y comparar.

**Errores comunes**

- ❌ No definir unidad y mezclar usuarios con sesiones ✅ fijar COUNT(DISTINCT user_id) o session_id según el objetivo.
- ❌ Ignorar orden temporal ✅ forzar MIN(event_ts) por etapa y filtrar t_b > t_a.
- ❌ Doble conteo por múltiples acciones del mismo usuario ✅ usar DISTINCT por etapa.
- ❌ Comparar etapas no contiguas (A→C saltando B) ✅ construir pasos adyacentes y luego encadenar.
- ❌ IDs y zonas horarias inconsistentes ✅ normalizar TZ; limpiar IDs antes de los ejemplos.
- ❌ Ejemplos SQL con formato tipográfico (comillas curvas, guion largo) ✅ usar ' y --.

<br>

### C1 - Lección 2: Identificando eventos y campos en una base de datos
<br>

**🎯 Propósito de la lección**

- Reconstruir la secuencia de acciones de un usuario.
- Contar usuarios únicos por etapa usando COUNT(DISTINCT ...).
- Introducir segmentación por campos de contexto (p. ej., país o dispositivo) para enriquecer el análisis.

**🧠 Idea central**

Un journey no “viene armado” en la base; se reconstruye enlazando eventos por `user_id`, ordenando por `event_timestamp` y seleccionando los `event_name` que definen el embudo. Con esa base, `COUNT(DISTINCT user_id)` entrega el volumen real de personas que alcanzan cada etapa y permite calcular conversiones y abandono más adelante.

**📦 Dataset y campos clave**

- Tabla: `ecommerce_jan_2021` (una fila = un evento).
- Claves mínimas:
    - `user_id` → quién.
    - `event_timestamp` → cuándo (orden secuencial).
    - `event_name` → qué acción (etapa).
- Contexto (opcionales, pero valiosos):
    - `country`, `traffic_source`, `operating_system` (para segmentar y explicar diferencias).

**🧭 Paso a paso técnico**

1. **Explorar eventos clave**

`SELECT DISTINCT event_name`
`FROM ecommerce_jan_2021;`

2. **Reconstruir la secuencia por usuario**

`SELECT user_id, event_timestamp, event_name`
`FROM ecommerce_jan_2021`
`WHERE event_name IN ('page_view','view_item','add_to_cart','begin_checkout','purchase')`
`ORDER BY user_id, event_timestamp;`

3. **Contar usuarios únicos por etapa**

`SELECT event_name,`
       `COUNT(DISTINCT user_id) AS users`
`FROM ecommerce_jan_2021`
`WHERE event_name IN ('page_view','view_item','add_to_cart','begin_checkout','purchase')`
`-- Recomendación: aplicar el mismo rango temporal en todo el análisis`
`-- AND event_timestamp BETWEEN '2021-01-01' AND '2021-01-31'`
`GROUP BY event_name`
`ORDER BY users DESC;`

4. **Segmentar por contexto (ej., país)**

`SELECT country,`
       `event_name,`
       `COUNT(DISTINCT user_id) AS users`
`FROM ecommerce_jan_2021`
`WHERE event_name IN ('page_view','view_item','add_to_cart','begin_checkout','purchase')`
`GROUP BY country, event_name`
`ORDER BY country, event_name;`

**Errores comunes (y cómo evitarlos)**

- ❌ Contar eventos en lugar de usuarios (COUNT(*) vs COUNT(DISTINCT user_id)).
- ❌ Mezclar rango temporal entre etapas (comparar enero vs todo el histórico).
- ❌ No estandarizar event_name (mayúsculas, espacios, camelCase vs snake_case).
- ❌ Ignorar empates de tiempo y no tener un segundo criterio de orden.
- ❌ Olvidar nulos en user_id o diferencias de zona horaria en event_timestamp.

**Práctica guiada**

1. **Objetivo:** Debes crear una consulta SQL para segmentar y medir la eficiencia de nuestro embudo de ventas digital. Queremos ir más allá de los totales generales agrupando los resultados por país, tipo de evento y por categoría de producto.

**Instrucciones:**

- Seleccionar las columnas country, category y event_name de la tabla ecommerce_jan_2021.
- No uses alias.
- Filtra por los eventos 'page_view', 'view_item', 'add_to_cart', 'begin_checkout','purchase'
- Ordena por country y category de forma ascendente

**Respuesta**

`SELECT country,` 
			`category,` 
			`event_name,`
			`COUNT(DISTINCT user_id)`
`FROM ecommerce_jan_2021`
`WHERE event_name IN ('page_view', 'view_item', 'add_to_cart',`
										`'begin_checkout','purchase')`
`group by country, category, event_name`
`ORDER BY country, category ASC`

2. **Objetivo:** El equipo de mercadeo te pide un listado que muestre  todas las combinaciones de categoría y país, para entender cuales son los dispositivos utilizados en cada país.  

**Instrucciones:**

- Usar DISTINCT para listar todas las combinaciones únicas de category y country (tipo de dispositivo y país).
- Identificar si hay alguna combinación que se de solamente en un país y no en otro.

**Respuesta**

`SELECT distinct category, country`
`FROM ecommerce_jan_2021`

<br>

### C1 - Lección 3: Validando la calidad de los datos
<br>

**🎯 Propósito de la lección**

Establecer un protocolo mínimo de aseguramiento de calidad en datos de eventos antes de medir conversión.

Enseñar patrones SQL para detectar y tratar duplicados, eventos faltantes y problemas de tiempo/secuencia.

Documentar hallazgos de calidad con trazabilidad para que análisis posteriores sean confiables y reproducibles.

**🧠 Idea central**

En embudos de conversión, pequeños defectos de calidad (registros duplicados, pasos ausentes o timestamps desordenados) distorsionan conversiones, abandonos y tiempos en etapa. Por eso, antes de construir métricas, la lección guía a validar y corregir la base con consultas SQL simples pero efectivas, y a dejar evidencia escrita del impacto (porcentajes afectados, reglas aplicadas y decisiones de inclusión/exclusión).

**Temáticas trabajadas**

- **Tipos de problemas y su impacto de negocio**

    - Duplicados: inflan ingresos/finalizaciones y la base de cada etapa.
    - Eventos faltantes: rompen la narrativa del funnel (p. ej., purchase sin add_to_cart).
    - Inconsistencias temporales: hacen imposible medir “tiempo en etapa” y análisis por cohortes.

- **Detección de duplicados (clave quién–qué–cuándo)**

    - Conteo por clave:

    SELECT user_id, event_name, event_timestamp, COUNT(*) AS numero_registros
    FROM ecommerce_jan_2021
    GROUP BY user_id, event_name, event_timestamp
    HAVING COUNT(*) > 1
    ORDER BY numero_registros DESC;

- **Dedupe robusto conservando una fila:**

    WITH x AS (
    SELECT *, ROW_NUMBER() OVER(
        PARTITION BY user_id, event_name, event_timestamp
        ORDER BY event_timestamp
    ) AS rn
    FROM ecommerce_jan_2021
    )
    SELECT * FROM x WHERE rn = 1;     -- base deduplicada

- **Eventos faltantes (anti-join entre etapas)**

    - Usuarios con purchase sin add_to_cart:

    WITH compra AS (
    SELECT DISTINCT user_id FROM ecommerce_jan_2021 WHERE event_name='purchase'
    ),
    carrito AS (
    SELECT DISTINCT user_id FROM ecommerce_jan_2021 WHERE event_name='add_to_cart'
    )
    SELECT c.user_id
    FROM compra c
    LEFT JOIN carrito a ON c.user_id = a.user_id
    WHERE a.user_id IS NULL;

- **Coherencia temporal y secuencia**

    - Rango de fechas del dataset:

    SELECT MIN(event_timestamp) AS min_ts, MAX(event_timestamp) AS max_ts
    FROM ecommerce_jan_2021;

    - Orden lógico por usuario (detección de desorden):

    WITH t AS (
    SELECT user_id, event_name, event_timestamp,
            LAG(event_timestamp) OVER (PARTITION BY user_id ORDER BY event_timestamp) AS prev_ts
    FROM ecommerce_jan_2021
    )
    SELECT * FROM t WHERE prev_ts IS NOT NULL AND event_timestamp < prev_ts;

    - Validación de precedencias (p. ej., add_to_cart antes de begin_checkout) con MIN(CASE WHEN …) por usuario.

- Decisiones de tratamiento y documentación

    - Clasificación de duplicados: error de sistema/reintento (eliminar), redondeo de timestamp (ventana), repetición intencional (conservar).
    - Recomendación de nota de zona horaria (normalizar a UTC o guardar offset).
    - Resumen mínimo a registrar: % duplicados, % rutas “paso posterior sin previos”, outliers de tiempo/rango, reglas aplicadas y su impacto en métricas.

**Errores comunes y cómo evitarlos**

- ❌ Contar eventos en vez de usuarios por etapa. ✅ COUNT(DISTINCT user_id) para tasas de avance.
- ❌ Asumir que DISTINCT siempre es seguro. ✅ definir la clave de negocio para dedupe y preferir ROW_NUMBER() si hay columnas adicionales que no deben colapsar.
- ❌ Eliminar automáticamente rutas alternativas (p. ej., promo que salta pasos). ✅ decidir según objetivo; si se incluyen, etiquetar para análisis separado.
- ❌ Ignorar zonas horarias o rangos del dataset. ✅ normalizar a UTC, verificar MIN/MAX(event_timestamp) y chequear mes/año esperados.
- ❌ No medir el impacto del saneamiento. ✅ reportar “3.6% duplicados → +X% sobrestimación en conversión A→B”.
- ❌ No documentar decisiones. ✅ añadir un bloque de “Hallazgos de calidad” accesible al equipo con consultas y criterios aplicados.

**Práctica guiada**

1. **Objetivo:** Tu mismo, vas a completar una validacion de calidad del dataset de e-commerce antes de construir el funnel. 

Detectar si existen duplicados en purchase. Un duplicado es una operación realizada por un mismo usuario a la misma hora y fecha.

**Instrucciones:**

- Muestra las columnas user_id y event_timestamp.
- Cuenta el número de eventos utilizando el alias numero_registros.
- Filtra por tipo de evento purchase.
- Agrupa por user_id , event_timestamp, y event_name
- De esta manera podríamos detectar usuarios que compraron productos en la misma fecha y hora exacta, algo que no debiera suceder o que podría ser un fraude. 

**Respuesta:**

`SELECT user_id,`
        `event_timestamp,`
        `count(*) as numero_registros`
`FROM ecommerce_jan_2021`
`WHERE event_name = 'purchase'`
`GROUP BY user_id, event_timestamp, event_name`

2. **Objetivo:** Quieres analizar que cantidad de productos son agregados por cada usuario al carrito. El objetivo es detectar comportamientos atípicos (por ejemplo, un usuario con miles de productos en su carrito).

**Instrucciones:**

- Muestra los usuarios que tengan el evento add_to_cart.
- Cuenta las veces que agregaron productos al carrito.
- Ordena de forma descendente por el conteo; así podemos ver los casos con números mas altos, primero.

**Respuesta:**

`SELECT `
`user_id,`
`count(*)`
`FROM ecommerce_jan_2021`
`WHERE event_name = 'add_to_cart'`
`GROUP BY user_id`
`ORDER BY count(*) DESC`

<br>

## Capitulo 2: Construccion de funnels con SQL
### C2 - Lección 1: Extrayendo y filtrando eventos relevantes con CTEs
<br>

**🎯 Propósito de la lección**

Transformar una consulta suelta de conteos de eventos en un embudo (funnel) claro y ordenado usando CTEs (Common Table Expressions), de forma que cada etapa del journey sea un bloque con nombre y podamos imponer el orden lógico del flujo (registro/entrada → exploración → carrito → checkout → compra).

**🧠 Idea central**

Las CTEs permiten modularizar la query: cada etapa del embudo es un subconjunto con nombre (p. ej., cte_view_item) que devuelve usuarios únicos que alcanzaron esa etapa. Luego, un SELECT final combina esas CTEs para contar usuarios por etapa (con COUNT(DISTINCT user_id)), ordenar el funnel y dejar la consulta legible, mantenible y depurable.

**📚 Temáticas trabajadas**

1. **Por qué CTEs para funnels**

    - Problema inicial: el conteo por event_name sale “desordenado” y mezcla granularidades.
    - Solución: CTEs con WITH nombre_cte AS ( subconsulta ) para separar etapas y documentarlas.

2. **Diseño del embudo y orden explícito**

    - Definir etapas clave y su orden (ej.: page_view → view_item → add_to_cart → begin_checkout → purchase).
    - Imponer el orden en el resultado con ORDER BY CASE … END.

3. **CTE de etapa (patrón base)**

    `WITH cte_view_item AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'view_item'`
    `)`
    `SELECT COUNT(*) AS usuarios FROM cte_view_item;`

4. **Construcción incremental**

    - Agregar CTEs por cada etapa: cte_add_to_cart, cte_begin_checkout, cte_purchase.
    - SELECT final que combine y ordene:

    `WITH`
    `cte_view_item AS ( ... ),`
    `cte_add_to_cart AS ( ... ),`
    `cte_begin_checkout AS ( ... ),`
    `cte_purchase AS ( ... )`
    `SELECT etapa, usuarios`
    `FROM (`
    `SELECT 'view_item' AS etapa, COUNT(*) AS usuarios FROM cte_view_item`
    `UNION ALL`
    `SELECT 'add_to_cart', COUNT(*) FROM cte_add_to_cart`
    `UNION ALL`
    `SELECT 'begin_checkout', COUNT(*) FROM cte_begin_checkout`
    `UNION ALL`
    `SELECT 'purchase', COUNT(*) FROM cte_purchase`
    `) t`
    `ORDER BY CASE etapa`
    `WHEN 'view_item' THEN 1`
    `WHEN 'add_to_cart' THEN 2`
    `WHEN 'begin_checkout' THEN 3`
    `WHEN 'purchase' THEN 4`
    `END;`

    **Ventaja:** salida legible y en orden del journey.

5. **Granularidad del análisis**

    - Por usuario: usa user_id (lealtad/avance individual).
    - Por sesión: usa session_id (eficiencia de interfaz).
    - Dejar notado en la lección cuál se usa y por qué.

**⚠️ Errores comunes y cómo evitarlos**

- ❌ Contar eventos en vez de usuarios por etapa. ✅ Usa COUNT(DISTINCT user_id) dentro de cada CTE o en el SELECT final para tasas de avance.
- ❌ Confundir “signup” con “session_start”. ✅ Alinea nombres del copy con el filtro real (event_name = 'sign_up' o session_start) y mantenlo consistente en todo el capítulo.
- ❌ Embudo sin orden explícito. ✅ Ordena la salida con ORDER BY CASE etapa … END o con una columna step_order.
- ❌ Granularidad incorrecta (usuario vs sesión). ✅ Define al inicio si el funnel es por usuario o por sesión y ajusta los DISTINCT y joins.
- ❌ CTEs ruidosas (demasiadas columnas / sin DISTINCT). ✅ Mantén cada CTE mínima: SELECT DISTINCT user_id FROM … WHERE event_name = '…'.
- ❌ No documentar cada etapa. ✅ Añade un comentario corto por CTE (qué representa y por qué es necesaria).

**Práctica guiada**

1. **Objetivo:** Aislar a los usuarios que iniciaron sesión para usarlos luego en un funnel. 

La consulta intenta crear una CTE, pero tiene errores de sintaxis.

**Instrucciones:**

- Arregla la CTE y el SELECT final para contar a los usuarios.
- Muestra el conteo con el alias total_usuarios.

**Respuesta:**

    `WITH cte_session_start AS(`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'session_start'`
    `)`
    `SELECT COUNT(*) AS total_usuarios`
    `FROM cte_session_start;`

2. **Objetivo:** Producto quiere saber cuántos usuarios agregaron al carrito en enero 2021, continuamos con la tabla ecommerce_jan_2021.

**Instrucciones:**

- Crear una CTE llamada cte_add_to_cart que devuelva los usuarios únicos que agregaron un producto al carrito (add_to_cart).
- Escribir el SELECT final que muestre el conteo como total_add_to_cart.

**Respuesta:**

    `WITH cte_add_to_cart AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'add_to_cart'`
    `)`
    `SELECT COUNT(*) AS total_add_to_cart`
    `FROM cte_add_to_cart;`

<br>

### C2 - Lección 2: Escribir funnels con CTEs
<br>

**🎯 Propósito de la lección**

Construir un funnel de usuario con SQL ordenado y modular utilizando CTEs (Common Table Expressions), y comparar dos estrategias para obtener métricas por etapa: subconsultas en el SELECT versus LEFT JOINs entre CTEs, cuidando el conteo correcto de usuarios y la relación entre pasos del embudo.

**🧠 Idea central**

Dividir el embudo en bloques nombrados (CTEs) —p. ej., signup → add_to_cart → purchase—, deduplicar por usuario en cada bloque y luego ensamblarlos en un SELECT final. Las CTEs mejoran legibilidad, prueba, y mantenimiento; los LEFT JOINs suelen ofrecer mejor eficiencia y permiten calcular conversiones encadenadas con menos relecturas.

**Temáticas trabajadas**

1. **CTEs en SQL – sintaxis y patrón mental**

    - **Estructura:** WITH nombre_cte AS ( … ) SELECT …
    - Cada CTE representa una etapa del funnel. Ejemplo base:

    `WITH cte_signup AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'signup'   -- o 'session_start' (unificar criterio)`
    `),`
    `cte_cart AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'add_to_cart'`
    `),`
    `cte_purchase AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'purchase'`
    `)`

    - **Buenas prácticas:** nombres explícitos, comentarios arriba de cada CTE (qué filtra, por qué), y DISTINCT user_id para medir personas, no eventos.

2. **Dos estrategias de salida**

    **A) Subconsultas en el SELECT (más simple de leer):**

    `SELECT`
    `(SELECT COUNT(*) FROM cte_signup)   AS signup_users,`
    `(SELECT COUNT(*) FROM cte_cart)     AS cart_users,`
    `(SELECT COUNT(*) FROM cte_purchase) AS purchase_users;`


    **Ventajas:** claridad y rapidez para explicar. Desventaja: no encadena pasos por sí sola; si hay que estimar conversión A→B, se debe controlar población.

    **B) LEFT JOINs (más eficiente y escalable):**

    `SELECT`
    `COUNT(DISTINCT s.user_id) AS signup_users,`
    `COUNT(DISTINCT c.user_id) AS cart_users,`
    `COUNT(DISTINCT p.user_id) AS purchase_users`
    `FROM cte_signup  s`
    `LEFT JOIN cte_cart     c ON s.user_id = c.user_id`
    `LEFT JOIN cte_purchase p ON s.user_id = p.user_id;`

3. **Conversiones encadenadas (evitar sobreestimación)**

    - Si se quiere conversiones reales A→B, asegura la dependencia entre etapas. Opciones:

    - Restringir CTEs encadenando:

        `cte_cart AS (`
        `SELECT DISTINCT user_id`
        `FROM ecommerce_jan_2021`
        `WHERE event_name = 'add_to_cart'`
            `AND user_id IN (SELECT user_id FROM cte_signup)`
        `)`

    - O calcular intersecciones con joins/INTERSECT para A∩B, B∩C.

4. **Control de duplicados y orden temporal**

    Cada CTE deduplica por usuario. Si necesitas el primer momento de la etapa:

    `SELECT user_id, MIN(event_timestamp) AS first_ts`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'add_to_cart'`
    `GROUP BY user_id`

    Esto evita inconsistencias al ordenar journeys y mejora la trazabilidad por usuario.

5. **Rendimiento y mantenibilidad**

    - Índices/particiones o clustering en event_name, user_id, event_timestamp.
    - Para >100M eventos, evaluar APPROX_COUNT_DISTINCT(user_id) si la precisión lo permite.
    - Comentar el SQL y usar una convención: `cte_<etapa>_users`, fechas en WHERE, y nota de supuestos (p. ej., session_start se usa como equivalente a signup).

**Errores comunes y cómo evitarlos**

- ❌ Contar eventos en vez de usuarios por etapa. ✅ Usa COUNT(DISTINCT user_id) o deduplica en cada CTE y luego COUNT(*).
- ❌ Calcular conversión A→B con poblaciones no encadenadas (totales independientes). ✅ Encadena CTEs (IN/joins) o calcula A∩B explícitamente.
- ❌ Inconsistencia de nombres de evento (signup vs session_start). ✅ Unifica el evento o documenta el mapeo (proxy) en el código y el texto.
- ❌ Duplicados por usuario dentro de una etapa. ✅ SELECT DISTINCT user_id y, si importa el orden, MIN(event_timestamp) por usuario.
- ❌ Cambiar a INNER JOIN sin analizar el impacto. ✅ Mantén LEFT JOIN si quieres conservar la población de la etapa A como base del funnel.
- ❌ Diferencias entre conteos con subconsultas y joins sin explicación. ✅ Explica que subconsultas leen varias veces y joins consolidan; valida cardinalidad.
- ❌ Omitir límites temporales. ✅ Filtra el período analizado (ej.: Enero 2021) para comparabilidad.
- ❌ SQL poco legible. ✅ Nombra CTEs por etapa y agrega comentarios breves (“filtra usuarios únicos que …”).

**Práctica guiada**

1. **Objetivo:** Producto quiere medir cuántos usuarios únicos avanzan en el funnel básico.

Continuamos con la tabla `ecommerce_jan_2021`.

**Instrucciones:**

- Crea una CTE para signup con el evento session_start.
- Crea una CTE para add_to_cart.
- Crea una CTE para purchase.
- Muestra en un solo SELECT el conteo de cada etapa.
- Utiliza sub consultas en el SELECT final para realizar los conteos por etapa.

**Respuesta:**

    `WITH cte_signup AS (``
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'session_start'`
    `),`
    `cte_cart AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'add_to_cart'`
    `),`
    `cte_purchase AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'purchase'`
    `)`
    `SELECT`
    `(SELECT COUNT(*) FROM cte_signup)   AS signup_users,`
    `(SELECT COUNT(*) FROM cte_cart)     AS cart_users,`
    `(SELECT COUNT(*) FROM cte_purchase) AS purchase_users;`

2. **Objetivo:** Marketing quiere analizar otro funnel:
view_item → begin_checkout → purchase.

**Instrucciones:**

1. Crea 3 CTEs (una por cada evento).
    - cte_view
    - cte_checkout
    - cte_purchase
2. Muestra los conteos de cada etapa en un SELECT final.
3. Utiliza sub consultas en el SELECT final para realizar los conteos por etapa. Usa los siguientes nombres para las columnas de la tabla final:
    - view_users
    - checkout_users
    - purchase_users
4. Identifica en qué etapa se pierden más usuarios.

**Respuesta:**

    `WITH cte_view AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'view_item'`
    `),`
    `cte_checkout AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'begin_checkout'`
    `),`
    `cte_purchase AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'purchase'`
    `)`
    `SELECT`
    `(SELECT COUNT(*) FROM cte_view)     AS view_users,`
    `(SELECT COUNT(*) FROM cte_checkout) AS checkout_users,`
    `(SELECT COUNT(*) FROM cte_purchase) AS purchase_users;`

<br>

### C2 - Lección 3: Contando usuarios en cada etapa
<br>

**🎯 Propósito de la lección**

Calcular, con una sola consulta clara y robusta, cuántos usuarios únicos llegan a cada etapa del funnel y qué porcentaje se pierde entre pasos consecutivos (drop-off) para detectar dónde se estrecha el embudo y priorizar mejoras.

**🧠 Idea central**

Modelamos cada paso del funnel como una CTE (WITH … AS …) que guarda usuarios únicos por evento (p. ej., `session_start` → `add_to_cart` → `purchase`). Luego, en el SELECT final:

- contamos usuarios por etapa con COUNT(*) sobre cada CTE;
- calculamos conversión y drop-off entre etapas usando aritmética simple y NULLIF para evitar divisiones por cero;
- opcionalmente, normalizamos el resultado en formato “largo” para reportar etapa por etapa con LAG().

**📚 Temáticas trabajadas**

1. **CTEs por etapa (usuarios únicos)**

    `WITH cte_signup AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name IN ('session_start','sign_up')`
    `),`
    `cte_cart AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'add_to_cart'`
    `),`
    `cte_purchase AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'purchase'`
    `)`

2. **Conteos + drop-off + conversión en una sola salida**

    `SELECT`
    `(SELECT COUNT(*) FROM cte_signup)   AS signup_users,`
    `(SELECT COUNT(*) FROM cte_cart)     AS cart_users,`
    `(SELECT COUNT(*) FROM cte_purchase) AS purchase_users,`

    `-- % que se pierde de signup -> cart`
    `ROUND(`
       `((SELECT COUNT(*) FROM cte_signup) - (SELECT COUNT(*) FROM cte_cart))`
        `/ NULLIF((SELECT COUNT(*) FROM cte_signup), 0.0) * 100, 2`
    `) AS dropoff_after_signup_pct,`

    `-- % que se pierde de cart -> purchase`
    `ROUND(`
        `((SELECT COUNT(*) FROM cte_cart) - (SELECT COUNT(*) FROM cte_purchase))`
        `/ NULLIF((SELECT COUNT(*) FROM cte_cart), 0.0) * 100, 2`
    `) AS dropoff_after_cart_pct,`

    `-- conversiones útiles`
    `ROUND((SELECT COUNT(*) FROM cte_cart) / NULLIF((SELECT COUNT(*) FROM cte_signup), 0.0) * 100, 2)`
        `AS conv_signup_to_cart_pct,`
    `ROUND((SELECT COUNT(*) FROM cte_purchase) / NULLIF((SELECT COUNT(*) FROM cte_cart), 0.0) * 100, 2)`
        `AS conv_cart_to_purchase_pct,`
    `ROUND((SELECT COUNT(*) FROM cte_purchase) / NULLIF((SELECT COUNT(*) FROM cte_signup), 0.0) * 100, 2)`
        `AS conv_signup_to_purchase_pct;`

3. **Buenas prácticas de estabilidad**

- Usa `DISTINCT user_id` dentro de cada CTE para evitar doble conteo.

- Aplica `NULLIF(…,0)` en divisiones y `ROUND` para porcentajes legibles.

- Si tu producto tiene sinónimos de eventos, normalízalos con IN (…).

- Si necesitas asegurar una sola ocurrencia por usuario/etapa, deduplica con `ROW_NUMBER()` por `user_id`, `event_name ORDER BY event_timestamp`.

**Errores comunes y cómo evitarlos**

- ❌ Contar eventos en vez de usuarios por etapa. ✅ Usa COUNT(DISTINCT user_id) dentro de cada CTE.
- ❌ Comparar etapas con ventanas temporales distintas (p. ej., signup en enero y purchase en todo el año). ✅ Filtra el mismo rango temporal para todas las CTE (ej. WHERE event_date BETWEEN '2021-01-01' AND '2021-01-31').
- ❌ No controlar divisiones por cero (embudos con 0 usuarios en la etapa anterior). ✅ Protege con NULLIF(denominador,0) y muestra 0/NULL según tu regla de negocio.
- ❌ Olvidar sinónimos de eventos (session_start vs sign_up). ✅ Unifica con IN ('session_start','sign_up') o crea una CTE de mapeo.
- ❌ Duplicados por múltiples hits válidos del mismo usuario en una etapa. ✅ Forza unicidad por user_id dentro de cada CTE (o toma el primer hit con ROW_NUMBER() y filtra WHERE rn=1).
- ❌ Orden lógico implícito. ✅ Define el orden del funnel explícitamente (stage_order) para que LAG() y los cálculos sean consistentes.

**Práctica guiada**

1. **Objetivo:** Marketing quiere ver el funnel básico de los siguientes pasos: 

add_to_cart → begin_checkout → purchase

![alt text](image-1.png)

**Instrucciones:**

- Calcular el drop-off entre add_to_cart y begin_checkout.
- Calcular el drop-ff entre begin_checkout y purchase

**Respuesta:**

    `WITH cte_cart AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'add_to_cart'`
    `),`
    `cte_checkout AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'begin_checkout'`
    `),`
    `cte_purchase AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'purchase'`
    `)`
    `SELECT`
    `(SELECT COUNT(*) FROM cte_cart)     AS cart_users,`
    `(SELECT COUNT(*) FROM cte_checkout) AS checkout_users,`
    `(SELECT COUNT(*) FROM cte_purchase) AS purchase_users,`
    `((SELECT COUNT(*) FROM cte_cart) - (SELECT COUNT(*) FROM cte_checkout)) * 100`
        `/ NULLIF((SELECT COUNT(*) FROM cte_cart), 0) AS dropoff_after_cart_pct,`
    `((SELECT COUNT(*) FROM cte_checkout) - (SELECT COUNT(*) FROM cte_purchase)) * 100`
        `/ NULLIF((SELECT COUNT(*) FROM cte_checkout), 0) AS dropoff_after_checkout_pct;`

2. **Objetivo:** El equipo de producto quiere identificar en qué punto del recorrido los usuarios interesados dejan de avanzar hacia la compra.

Para ello, construirás un funnel con las etapas iniciales del proceso:

view_item, add_to_cart y begin_checkout.

![alt text](image-2.png)

**Instrucciones:**

Continuamos con la tabla ecommerce_jan_2021.

- Crea tres CTEs que representen las etapas del funnel (cte_view, cte_cart, cte_checkout).
- Muestra el número de usuarios únicos en cada etapa.
- Calcula el porcentaje de abandono (drop-off) entre cada paso del funnel. Usa los alias 
- dropoff_after_view_pct y dropoff_after_cart_pct respectivamente.
- Presenta los resultados en una tabla final que muestre tanto los conteos como los porcentajes.

**Respuesta:**

    `WITH cte_view AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'view_item'`
    `),`
    `cte_cart AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'add_to_cart'`
    `),`
    `cte_checkout AS (`
    `SELECT DISTINCT user_id`
    `FROM ecommerce_jan_2021`
    `WHERE event_name = 'begin_checkout'`
    `)`
    `SELECT`
    `(SELECT COUNT(*) FROM cte_view)     AS viewed_products,`
    `(SELECT COUNT(*) FROM cte_cart)     AS added_to_cart,`
    `(SELECT COUNT(*) FROM cte_checkout) AS started_checkout,`
    `((SELECT COUNT(*) FROM cte_view) - (SELECT COUNT(*) FROM cte_cart)) * 100`
        `/ NULLIF((SELECT COUNT(*) FROM cte_view), 0) AS dropoff_after_view_pct,`
    `((SELECT COUNT(*) FROM cte_cart) - (SELECT COUNT(*) FROM cte_checkout)) * 100`
        `/ NULLIF((SELECT COUNT(*) FROM cte_cart), 0) AS dropoff_after_cart_pct;`

<br>

### C2 - Lección 4: Analizando tasas de conversión y abandono
<br>

**🎯 Propósito de la lección**

Transformar la salida del funnel en métricas interpretables: usuarios únicos por etapa, conversión entre etapas, drop-off entre etapas y conversión global; y convertir esos números en insights accionables que prioricen mejoras del producto/UX.

**🧠 Idea central**

Con CTEs que representan cada paso del funnel, puedes calcular de forma consistente:

    - Usuarios únicos por etapa (COUNT(*) sobre CTEs con SELECT DISTINCT user_id).
    - Conversión etapa→etapa next/prev * 100.
    - Drop-off etapa→etapa (prev - next)/prev * 100.
    - Conversión acumulada desde el inicio hasta purchase.
    - Luego interpretas: detectas el mayor drop-off, formulas hipótesis (precio, relevancia, fricción), y cierras con un mini-reporte C → F → I (Context, Finding, Insight).

**Temáticas trabajadas**

1. Estandarización del funnel: page_view → view_item → add_to_cart → begin_checkout → purchase. Aclara si el capítulo usará este orden (evita mezclar con session_start/signup).
2. CTEs por etapa con usuarios únicos: SELECT DISTINCT user_id en cada CTE para no contar duplicados.
3. Tabla de conteos: CTE/consulta counts que expone *_users por etapa y sirve de base para todos los cálculos.
4. Conversión entre etapas: ROUND(100.0 * next / NULLIF(prev,0), 1) para cada transición.
5. Drop-off entre etapas: ROUND(100.0 * (1 - next/NULLIF(prev,0)), 1) equivalente a (prev - next)/prev * 100.
6. Conversión acumulada: ROUND(100.0 * purchase_users / NULLIF(page_view_users,0), 2).
7. Formateo y robustez: NULLIF(...,0) para evitar división por cero y ROUND para lecturas limpias.
8. Lectura accionable: detectar el máximo drop-off, proponer hipótesis, priorizar pruebas (pricing, copia, visibilidad CTA, tiempo de carga, etc.).
9. Reporte C→F→I: guía para cerrar cada análisis con un insight ejecutable (no solo números).

**SQL recomendado (limpio, con conversión y abandono)**

    `WITH`
    `cte_page_view AS (`
        `SELECT DISTINCT user_id`
        `FROM ecommerce_jan_2021`
        `WHERE event_name = 'page_view'`
    `),`
    `cte_view_item AS (`
        `SELECT DISTINCT user_id`
        `FROM ecommerce_jan_2021`
        `WHERE event_name = 'view_item'`
    `),`
    `cte_add_to_cart AS (`
        `SELECT DISTINCT user_id`
        `FROM ecommerce_jan_2021`
        `WHERE event_name = 'add_to_cart'`
    `),`
    `cte_begin_checkout AS (`
        `SELECT DISTINCT user_id`
        `FROM ecommerce_jan_2021`
        `WHERE event_name = 'begin_checkout'`
    `),`
    `cte_purchase AS (`
        `SELECT DISTINCT user_id`
        `FROM ecommerce_jan_2021`
        `WHERE event_name = 'purchase'`
    `),`
    `counts AS (`
       `SELECT`
        `(SELECT COUNT(*) FROM cte_page_view)     AS page_view_users,`
        `(SELECT COUNT(*) FROM cte_view_item)     AS view_item_users,`
        `(SELECT COUNT(*) FROM cte_add_to_cart)   AS add_to_cart_users,`
        `(SELECT COUNT(*) FROM cte_begin_checkout) AS begin_checkout_users,`
        `(SELECT COUNT(*) FROM cte_purchase)      AS purchase_users`
    `)`
    `SELECT`
    `page_view_users,`
    `view_item_users,`
    `add_to_cart_users,`
    `begin_checkout_users,`
    `purchase_users,`

    `-- Conversión entre etapas`
    `ROUND(100.0 * view_item_users      / NULLIF(page_view_users,0), 1) AS conv_page_to_item_pct,`
    `ROUND(100.0 * add_to_cart_users    / NULLIF(view_item_users,0), 1)  AS conv_item_to_cart_pct,`
    `ROUND(100.0 * begin_checkout_users / NULLIF(add_to_cart_users,0), 1) AS conv_cart_to_checkout_pct,`
    `ROUND(100.0 * purchase_users       / NULLIF(begin_checkout_users,0), 1) AS conv_checkout_to_purchase_pct,`

    `-- Drop-off entre etapas`
    `ROUND(100.0 * (1 - view_item_users      / NULLIF(page_view_users,0)), 1) AS `dropoff_after_page_view_pct,`
    `ROUND(100.0 * (1 - add_to_cart_users    / NULLIF(view_item_users,0)), 1)  AS `dropoff_after_view_item_pct,`
    `ROUND(100.0 * (1 - begin_checkout_users / NULLIF(add_to_cart_users,0)), 1) AS dropoff_after_cart_pct,`
    `ROUND(100.0 * (1 - purchase_users       / NULLIF(begin_checkout_users,0)), 1) AS `dropoff_after_checkout_pct,

    `-- Conversión global`
    `ROUND(100.0 * purchase_users / NULLIF(page_view_users,0), 2) AS conv_overall_pct`
    `FROM counts;`

**Errores comunes y cómo evitarlos**

- ❌ Contar eventos en vez de usuarios por etapa. ✅ Usa SELECT DISTINCT user_id en cada CTE y cuenta con COUNT(*).
- ❌ Dividir por la etapa incorrecta. ✅ Para transición A→B, el denominador siempre es A.
- ❌ No multiplicar por 100 o no redondear. ✅ ROUND(100.0 * expr, 1) y nombres con sufijo _pct.
- ❌ Identificadores inválidos (guiones) en CTEs. ✅ Usa snake_case: cte_add_to_cart.
- ❌ Mezclar etapas entre lecciones (signup vs page_view). ✅ Declara al inicio el funnel estándar que se usará en L4.
- ❌ Interpretar mal el gráfico. ✅ Rotula explícitamente si el % es drop-off o conversión; idealmente muestra ambos.
- ❌ Ignorar calidad de datos. ✅ Revisa duplicados y secuencia (lección de calidad) antes de calcular métricas.

<br>

## Capitulo 3: Análisis de retención con cohortes
### C3 - Lección 1: Agrupando usuarios en cohorts
<br>
**🎯 Propósito de la lección**

Asignar a cada cliente una etiqueta de cohorte (semanal, mensual o trimestral) basada en su primera fecha de relación con el banco, para luego comparar adopción/retención entre grupos homogéneos en el tiempo.

**🧠 Idea central**

Una cohorte agrupa usuarios que empezaron en el mismo período. Calcularla correctamente exige (1) validar la fecha de alta, (2) fijar la primera fecha por cliente y (3) truncarla al período de análisis (semana/mes/trimestre).

**Temáticas trabajadas**

1. **Dataset de referencia (clientes_banco):** Campos relevantes para cohorts: `customer_id`, `signup_date (alta)`, `exited (abandono)`, opcionales demográficos y de relación (tenure_months, productos, etc.).

2. **Validar la fecha de registro:** Detectar clientes con más de una fecha de alta (o nulos) antes de calcular cohorts.

        `-- ¿Algún cliente tiene >1 fecha de alta no nula?`
        `SELECT customer_id, COUNT(signup_date) AS conteo_signups`
        `FROM clientes_banco`
        `GROUP BY customer_id`
        `HAVING COUNT(signup_date) > 1;`

_Si hay duplicados reales, depurar o elegir la primera fecha._

3. **Obtener la PRIMERA fecha de relación por cliente**

        `SELECT`
        `customer_id,`
        `MIN(signup_date) AS first_signup_date`
        `FROM clientes_banco`
        `GROUP BY customer_id;`

4. **Etiquetar cohortes por período con DATE_TRUNC**

Trunca la primera fecha al inicio del período elegido.

        `-- Cohorte semanal (inicio de semana según motor; en Postgres es lunes)`
        `SELECT`
        `customer_id,`
        `DATE_TRUNC('week', MIN(signup_date))  AS cohort_week`
        `FROM clientes_banco`
        `GROUP BY customer_id;`

        `-- Cohorte mensual`
        `SELECT`
        `customer_id,`
        `DATE_TRUNC('month', MIN(signup_date)) AS cohort_month`
        `FROM clientes_banco`
        `GROUP BY customer_id;`

        `-- Cohorte trimestral`
        `SELECT`
        `customer_id,`
        `DATE_TRUNC('quarter', MIN(signup_date)) AS cohort_quarter`
        `FROM clientes_banco`
        `GROUP BY customer_id;`

**Notas prácticas**

- Si signup_date es timestamp en UTC y tu negocio usa hora local, normalizar: `DATE_TRUNC('month', (signup_ts AT TIME ZONE 'UTC')::date)`.
- Si necesitas semana que empiece en domingo, define calendario auxiliar o ajustar con `DATE_TRUNC('week', (signup_date + INTERVAL '1 day')) - INTERVAL '1 day'`.

**Variantes útiles**

- Persistir una tabla de dimensionalidad: dim_customer_cohort(customer_id, cohort_month, cohort_week, cohort_quarter).
- Filtrar por producto/segmento/país antes de truncar si el análisis de retención será por esa dimensión.

**Errores comunes y cómo evitarlos**

- ❌ Mezclar signup_date con MIN(signup_date) y agrupar por ambos. ✅ Usa solo MIN(signup_date) y GROUP BY customer_id para garantizar la primera fecha real.
- ❌ No aclarar el inicio de semana o la zona horaria al usar DATE_TRUNC('week', …). ✅ Documenta: día de inicio y TZ del cálculo. Normaliza timestamp → date en la TZ de negocio antes de truncar.
- ❌ Columnas inconsistentes entre tablas o capturas (has_or_card vs has_cr_card, is_active_mem). ✅ Estandariza nombres o crea un diccionario de mapeo y úsalo en todas las consultas.
- ❌ Usar el registro del dataset sin validar duplicados/nulos. ✅ Corre la verificación de duplicados y nulos; decide reglas (p. ej., “si hay varias altas, tomar la más antigua”).
- ❌ Cohortes con períodos ambiguos (semana ISO vs fiscal). ✅ Alinea a la semana de negocio (ISO/fiscal) y deja constancia en el encabezado del notebook/tablero.

**Práctica guiada**

1. **Objetivo:**  El equipo de producto del banco quiere entender cómo se comportan los clientes según el mes en que se registraron. Para ello, necesitan agruparlos en cohortes mensuales usando la fecha de registro.

**Instrucciones:**

1. Obtener la primera fecha de registro de cada cliente.
2. Crear una columna cohort_mensual para cada cliente.
3. Muestra el customer_id y su cohorte mensual.

**Respuesta:**

    `SELECT customer_id,`
        `DATE_TRUNC('month', MIN(signup_date)) AS cohort_mensual`
    `FROM clientes_banco`
    `GROUP BY customer_id;`

2. **Objetivo:** El equipo de marketing del banco realiza reportes trimestrales sobre adquisición y retención de clientes.
Necesitan agrupar a los clientes en cohortes trimestrales según la fecha en que abrieron su primera cuenta (signup_date).

**Instrucciones:**

1. Obtener la primera fecha de registro de cada cliente.
2. Crear una columna cohort_trimestral que agrupe por trimestre.
3. Muestra el customer_id y su cohorte trimestral.

**Respuesta:**

    `SELECT customer_id,`
        `DATE_TRUNC('quarter', MIN(signup_date)) AS cohort_trimestral`
    `FROM clientes_banco`
    `GROUP BY customer_id;`

<br>

### C3 - Lección 2: Midiendo la retención en el tiempo
<br>

**🎯 Propósito de la lección**

Medir retención por cohorte mensual (qué proporción de clientes sigue activa tras 1, 2 y 3 meses desde su registro) y presentar el resultado en una tabla interpretable para producto/marketing.

**🧠 Idea central**

Construyes una CTE de cohortes con la primera fecha de registro, cuentas clientes retenidos por mes de vida usando condiciones (CASE) y conviertes esos conteos a porcentajes sobre el total inicial de la cohorte para compararlas entre sí.

**Temáticas trabajadas**

1. Definir la cohorte (mes de registro)

    - CTE `cohortes` con `MIN(signup_date)` y `DATE_TRUNC('month', …)` → `cohorte_mes`.
    - **Buenas prácticas:** si puede haber múltiples filas por cliente, agrupa solo por customer_id (y luego trae atributos si los necesitas).

2. Contar retenidos por horizonte (M+1, M+2, M+3)

    - Usar `COUNT(CASE WHEN tenure_months >= k AND exited = FALSE THEN 1 END)` para cada horizonte.
    - **Opción robusta:** `COUNT(DISTINCT CASE WHEN … THEN customer_id END)` si la granularidad no es 1-fila-por-cliente.

3. Transformar a proporciones/porcentajes

    - Dividir por `clientes_iniciales` y uniformar: o dejas proporción (0–1) o multiplicar por 100 y renombrar con sufijo `_pct`.

4. Interpretación de la tabla de cohortes

    - **Fila** = cohorte (mes de alta).
    - **Columnas** = % retenido a 1, 2, 3 meses.
    - **Lectura:** comparar diagonales/filas para detectar mejoras o deterioros en retención por mes de adquisición.

5. Notas de método (limitaciones y extensiones)

    - **Simplificación:** `exited` refleja estado actual; para retención “real” por cohorte se recomienda tabla de actividad mensual o snapshots (estado por mes de vida).
    - Extender a M0–M12 y exportar a heatmap.

6. SQL de referencia (esqueleto limpio y consistente)

        `/* Paso 1: Cohortes mensuales (robusto) */`
        `WITH cohortes AS (`
        `SELECT`
            `customer_id,`
            `DATE_TRUNC('month', MIN(signup_date)) AS cohorte_mes`
        `FROM clientes_banco`
        `GROUP BY customer_id`
        `),`
        `/* Paso 2: Retenidos por horizonte */`
        `retencion AS (`
        `SELECT`
            `c.cohorte_mes,`
            `COUNT(DISTINCT b.customer_id)                                    AS clientes_iniciales,`
            `COUNT(DISTINCT CASE WHEN b.tenure_months >= 1 AND b.exited=false THEN b.customer_id END) AS retained_m1,`
            `COUNT(DISTINCT CASE WHEN b.tenure_months >= 2 AND b.exited=false THEN b.customer_id END) AS retained_m2,`
            `COUNT(DISTINCT CASE WHEN b.tenure_months >= 3 AND b.exited=false THEN b.customer_id END) AS retained_m3`
        `FROM cohortes c`
        `JOIN clientes_banco b USING (customer_id)`
        `GROUP BY c.cohorte_mes`
        `)`
        `/* Paso 3: Proporciones o porcentajes */`
        `SELECT`
        `/* Proporción */`
        `TO_CHAR(cohorte_mes, 'YYYY-MM') AS cohorte,`
        `ROUND(retained_m1::numeric / clientes_iniciales, 2) AS mes_1,`
        `ROUND(retained_m2::numeric / clientes_iniciales, 2) AS mes_2,`
        `ROUND(retained_m3::numeric / clientes_iniciales, 2) AS mes_3`
        `FROM retencion`
        `ORDER BY cohorte_mes;`
        `-- Si quieres %: reemplaza cada columna por ROUND(100.0 * retained_mk / clientes_iniciales, 2) AS mes_k_pct`

**Errores comunes y cómo evitarlos**

❌ Llamar “%” a proporciones 0–1 ✅ añade * 100 o aclara que son proporciones.

❌ Fragmentar cohortes sin querer (GROUP BY incluyendo tenure_months/exited). ✅ en la CTE de cohortes agrupa solo por customer_id.

❌ Doble conteo cuando hay más de una fila por cliente. ✅ COUNT(DISTINCT customer_id) en iniciales y retenidos.

❌ Aliases inconsistentes (m1 vs retained_m1). ✅ usa un solo esquema de nombres en todo el flujo y en el código final.

❌ Suponer retención histórica con exited actual. ✅ explica la simplificación y, si es posible, construye una tabla mensual de actividad o snapshots.

❌ Dependencia del motor SQL. ✅ agrega una sección de portabilidad (Postgres/BigQuery/Spark/SQL Server) para TO_CHAR/FORMAT_DATE/date_format y casts.


**Práctica guiada**

1. **Objetivo:** El equipo de producto del banco quiere entender la retención trimestral de los clientes para observar tendencias más amplias.
Tu tarea será calcular qué proporción de clientes permanecen activos después de 1, 2 y 3 trimestres desde su registro.

**Instrucciones:**

Continuamos con la tabla `clientes_banco`.

1. Agrupa a los clientes por cohorte trimestral según su fecha de registro (`signup_date`).
2. Calcula cuántos siguen activos después de 1, 2 y 3 trimestres. 
    - Usa los alias `retained_q1`, `retained_q2` y `retained_q3`.
3. Convierte los resultados en proporción de retención. 
    - Muestra el trimestre usando `TO_CHAR()` con el formato `'YYYY-"Q"Q'` para mostrar el trimestre con el alias `cohorte`.
    - Muestra `clientes_iniciales`.
    - Calcula la proporción, redondea a 2 decimales y para mostrarlos, usa los alias `trimestre_1`, `trimestre_2` y `trimestre_3`.
    - Ordena las cohortes cronológicamente.

**Respuesta:**

        `/* PASO 1: Identificar la cohorte trimestral de cada cliente */`
        `WITH cohortes AS (`
        `SELECT`
            `customer_id,`
            `DATE_TRUNC('quarter', MIN(signup_date)) AS cohorte_trimestre,`
            `tenure_months,`
            `exited`
        `FROM clientes_banco`
        `GROUP BY customer_id, tenure_months, exited`
        `),`
        `/* PASO 2: Calcular clientes retenidos por trimestre */`
        `retencion AS (`
        `SELECT`
            `cohorte_trimestre,`
            `COUNT(*) AS clientes_iniciales,`
            `COUNT(CASE WHEN tenure_months >= 3 AND exited = FALSE THEN 1 END) AS retained_q1,`
            `COUNT(CASE WHEN tenure_months >= 6 AND exited = FALSE THEN 1 END) AS retained_q2,`
            `COUNT(CASE WHEN tenure_months >= 9 AND exited = FALSE THEN 1 END) AS retained_q3`
        `FROM cohortes`
        `GROUP BY cohorte_trimestre`
        `)`
        `/* PASO 3: Crear la tabla de retención con porcentajes */`
        `SELECT`
        `TO_CHAR(cohorte_trimestre, 'YYYY-"Q"Q') AS cohorte,`
        `clientes_iniciales,`
        `ROUND(retained_q1::numeric / clientes_iniciales, 2) AS trimestre_1,`
        `ROUND(retained_q2::numeric / clientes_iniciales, 2) AS trimestre_2,`
        `ROUND(retained_q3::numeric / clientes_iniciales, 2) AS trimestre_3`
        `FROM retencion`
        `ORDER BY cohorte_trimestre;`

2. **Objetivo:** El equipo de marketing necesita analizar la retención durante los primeros seis meses para identificar en qué etapa los clientes tienden a abandonar el servicio.

Esto permite detectar si los usuarios desertan en los primeros meses o si mantienen su compromiso durante el primer semestre, información clave para mejorar la experiencia inicial.

**Instrucciones:**

1. Crea una CTE `cohortes` para agrupar a los clientes por cohorte mensual según su fecha de registro (`signup_date`).
    - Usa el alias `cohorte_mes` para los cohortes.
    - Mantén las columnas que necesitaras para la siguiente CTE.
2. Crea una CTE `retencion`, a partir de la anterior, para calcular cuántos clientes siguen activos después de 1, 3 y 6 meses.
    - Cuenta los usuarios que iniciaron en cada cohorte con el alias `clientes_iniciales`.
    - Usa los alias `mes_1`, `mes_3` y `mes_6` para la cantidad de clientes activos por mes.
    - Mantén las columnas que necesitaras para la tabla final.
3. Convierte los resultados en porcentajes de retención para comparar entre cohortes.
    - Muestra la cohorte con el formato '`YYYY-MM`’ usando el alias `cohorte`.
    - Muestra los `clientes_iniciales` de cada cohorte.
    - Muestra el porcentaje de retención de cada mes de interés redondeando a 2 decimales. Usa los alias `retencion_mes_1`, `retencion_mes_3` y `retencion_mes_6` respectivamente.
    - Ordena la tabla cronológicamente.

**Nota:** No agruparemos mes a mes, sino que usaremos los meses 1, 3 y 6, ya que representan hitos clave del primer semestre. Estos puntos permiten analizar la retención de manera significativa sin perderse en demasiados detalles.

**Respuesta:**

        `/* PASO 1: Identificar la cohorte mensual de cada cliente */`
        `WITH cohortes AS (`
        `SELECT`
            `customer_id,`
            `DATE_TRUNC('month', MIN(signup_date)) AS cohorte_mes,`
            `tenure_months,`
            `exited`
        `FROM clientes_banco`
        `GROUP BY customer_id, tenure_months, exited`
        `),`

        `/* PASO 2: Calcular clientes retenidos por periodo */`
        `retencion AS (`
        `SELECT`
            `cohorte_mes,`
            `COUNT(*) AS clientes_iniciales,`
            `COUNT(CASE WHEN tenure_months >= 1 AND exited = FALSE THEN 1 END) AS mes_1,`
            `COUNT(CASE WHEN tenure_months >= 3 AND exited = FALSE THEN 1 END) AS mes_3,`
            `COUNT(CASE WHEN tenure_months >= 6 AND exited = FALSE THEN 1 END) AS mes_6`
        `FROM cohortes`
        `GROUP BY cohorte_mes`
        `)`

        `/* PASO 3: Crear la tabla de retención con porcentajes */`
        `SELECT`
        `TO_CHAR(cohorte_mes, 'YYYY-MM') AS cohorte,`
        `clientes_iniciales,`
        `ROUND(mes_1::numeric / clientes_iniciales * 100, 2) AS retencion_mes_1,`
        `ROUND(mes_3::numeric / clientes_iniciales * 100, 2) AS retencion_mes_3,`
        `ROUND(mes_6::numeric / clientes_iniciales * 100, 2) AS retencion_mes_6`
        `FROM retencion`
        `ORDER BY cohorte_mes;`

<br>

### C3 - Lección 3: Creando heatmaps de retención
<br>

**🎯 Propósito de la lección**

Visualizar la retención por cohortes con un heatmap para detectar, de un vistazo, patrones, mejoras y puntos de abandono; y complementar con curvas de retención para comparar la velocidad de caída entre cohortes.

**🧠 Idea central**

Partiendo de una tabla con conteos por cohorte y mes de vida, normalizamos contra mes_0 para obtener porcentajes, aplicamos formato condicional (mínimo–medio–máximo) y luego creamos gráficos de línea que muestran la curva de retención por cohorte.

**Temáticas trabajadas**

- De conteos a porcentajes (normalización):

    - Tabla base: cohorte, mes_0, mes_1, mes_2, mes_3 (u horizontes que tengas).
    - Cálculo en Sheets/Excel (ejemplo):
        - pct_mes_1 = C2/$B2, pct_mes_2 = D2/$B2, pct_mes_3 = E2/$B2.
    - Asegura formato porcentaje antes de graficar.

- Heatmap (formato condicional):

    - Selecciona el rango de porcentajes y usa Escala de color.
    - Sugerido: Mínimo = rojo (baja retención), Punto medio = amarillo, Máximo = verde.
    - Define los umbrales según el tipo de dato:
        - Porcentajes: 0% / 50% / 100%.
        - Decimales: 0 / 0.5 / 1.

- Lectura del heatmap (dos ejes de análisis):

    - Horizontal: curva de retención de una cohorte a lo largo del tiempo (oscurece hacia rojo = mayor abandono).
    - Vertical: comparación entre cohortes en el mismo mes de vida (cuáles retienen mejor/peor en “Mes 1”, “Mes 2”, etc.).
    - Identifica saltos bruscos (puntos de fricción) y bloques verdes (cohortes o meses con buena fidelidad).

- Curvas de retención (líneas):

    - Eje X: meses de vida (Mes 1–3). Eje Y: % de retención.
    - Series: 2–3 cohortes recientes para comparar.
    - Útil para explicar velocidad de caída y separación entre cohortes.

- Entrega accionable (mini-reporte C → F → I):

    - Context: período, dataset y definición de “activo”.
    - Finding: dónde están los picos de abandono / cohortes destacadas.
    - Insight: hipótesis y acciones (onboarding, pricing, UX de carrito, campañas de reactivación, etc.).

**Errores comunes y cómo evitarlos**

- ❌ Mezclar unidades de tiempo (D+ vs Mes). ✅ Estandariza nomenclatura en todo el capítulo (recom.: Mes 0–N).
- ❌ Fórmulas mal referenciadas (autorreferencia G2/$B2). ✅ Usa C2/$B2, D2/$B2, E2/$B2 (copiar a derecha) y fija mes_0 con $.
- ❌ Aplicar heatmap a conteos absolutos. ✅ Siempre normaliza (mes_X / mes_0) antes del formato condicional.
- ❌ Colores que no reflejan porcentajes por formato incorrecto. ✅ Define si tus celdas están en % o decimales y ajusta los umbrales (0–1 vs 0%–100%).
- ❌ Tildes y estilo inconsistentes. ✅ Revisión rápida de ortografía (retención, fácil, comparación, más) y uso consistente de heatmap.
- ❌ Curvas con series “automáticas” ruidosas. ✅ Elige cohortes representativas (p.ej., 3 más recientes) y el mismo horizonte (Mes 1–3) para comparabilidad.

<br>

### C3 - Lección 4: Segmentando la retención por atributos de usuario
<br>





<br>

## Capitulo 4: Modelado de escenarios e impacto en negocio
### C4 - Lección 1: Pruebas A/B en funnels y simulando mejoras
<br>

<br>

### C4 - Lección 2: Estimando el impacto en métricas de negocio
<br>

<br>

### C4 - Lección 3: Comparando escenarios entre segmentos
<br>

<br>

### C4 - Lección 4: Visualización de Embudos para los Stakeholders
<br>

<br>