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

<br>

### C2 - Lección 2: Escribir funnels con CTEs
<br>

<br>

### C2 - Lección 3: Contando usuarios en cada etapa
<br>

<br>

### C2 - Lección 4: Analizando tasas de conversión y abandono
<br>

<br>

## Capitulo 3: Análisis de retención con cohortes
### C3 - Lección 1: Agrupando usuarios en cohorts
<br>

<br>

### C3 - Lección 2: Midiendo la retención en el tiempo
<br>

<br>

### C3 - Lección 3: Creando heatmaps de retención
<br>

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