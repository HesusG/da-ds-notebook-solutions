# Criterios de Evaluación: DA_Final - Manejo de SQL (Versión Completa)

## Objetivo

Demostrar dominio exhaustivo de consultas SQL para explorar, analizar y extraer información de una base de datos relacional con múltiples tablas, aplicando técnicas avanzadas de consulta y generando análisis que aporten valor significativo al contexto del caso de negocio.

**Requisitos previos**: Haber completado todos los sprints previos del bootcamp de Data Analyst

**Competencias que desarrollarás**: Consultas SQL avanzadas (SELECT, JOIN, GROUP BY, HAVING, subqueries, CTEs, window functions), exploración de bases de datos relacionales, modelado de datos, optimización de consultas, análisis de modelos de datos, extracción de insights accionables

**Nota**: Este caso es **INDEPENDIENTE** del Caso Principal. Se recomienda realizarlo mientras esperas aprobación de la Descomposición de Tareas.

**Importante**: Todas las soluciones deben basarse en **consultas SQL**, usando Pandas únicamente para visualizar o guardar resultados.

<details>
<summary>Requisitos del Entregable</summary>

## Descripción del Entregable

Un **Jupyter Notebook** exhaustivo que contenga:

1. **Conexión a la base de datos**: Usando el código provisto
2. **Exploración completa de tablas**: Descripción de estructura, tipos, cardinalidad
3. **Modelo de datos**: Diagrama y explicación de relaciones (PKs, FKs)
4. **Solución de consultas**: Todas las consultas solicitadas en SQL puro
5. **Consultas adicionales**: Al menos 2 consultas propias que aporten valor
6. **Conclusiones**: Interpretación relevante y accionable de cada resultado
7. **Recomendaciones**: Basadas en los hallazgos del análisis

</details>

## Glosario de Términos Técnicos

**SQL (Structured Query Language)**: Lenguaje estándar para consultar y manipular bases de datos relacionales.

**DDL vs DML**: DDL (Data Definition Language) define estructura (CREATE, ALTER). DML (Data Manipulation Language) opera sobre datos (SELECT, INSERT, UPDATE).

**JOIN**: Operación que combina filas de dos o más tablas basándose en una columna relacionada. Tipos: INNER, LEFT, RIGHT, FULL, CROSS.

**GROUP BY**: Agrupa filas con valores iguales en columnas especificadas. Se usa con funciones de agregación (COUNT, SUM, AVG, MIN, MAX).

**HAVING**: Filtra grupos después de la agregación (WHERE filtra filas antes).

**Subquery**: Consulta anidada dentro de otra consulta. Puede usarse en SELECT, FROM, WHERE, HAVING.

**CTE (Common Table Expression)**: Resultado temporal nombrado definido con WITH. Mejora legibilidad y permite recursión.

**Window Function**: Función que opera sobre un conjunto de filas relacionadas con la fila actual (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER).

**Modelo de datos**: Estructura que define las tablas, columnas, tipos de datos y relaciones de una base de datos.

**Clave primaria (PK)**: Columna(s) que identifica(n) únicamente cada fila de una tabla. No admite NULL ni duplicados.

**Clave foránea (FK)**: Columna que referencia la clave primaria de otra tabla, estableciendo relaciones y garantizando integridad referencial.

**Cardinalidad**: Tipo de relación entre tablas: 1:1 (uno a uno), 1:N (uno a muchos), N:M (muchos a muchos).

**Índice**: Estructura que mejora la velocidad de búsqueda en una tabla. Las PKs típicamente tienen índices automáticos.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**Conexión y Exploración**
- [ ] **[OBLIGATORIO]** Conexión correcta a la base de datos usando el código provisto
- [ ] **[OBLIGATORIO]** Explora TODAS las tablas existentes en la base de datos
- [ ] **[OBLIGATORIO]** Describe estructura de cada tabla (columnas, tipos de datos)
- [ ] **[OBLIGATORIO]** Código ejecuta sin errores en celdas secuenciales

**Modelo de Datos**
- [ ] **[OBLIGATORIO]** Explica la relación entre las tablas (qué tabla se conecta con cuál)
- [ ] **[OBLIGATORIO]** Identifica claves primarias de cada tabla
- [ ] **[OBLIGATORIO]** Identifica claves foráneas y cómo conectan las tablas

**Consultas**
- [ ] **[OBLIGATORIO]** Resuelve TODAS las consultas usando SQL (no Pandas)
- [ ] **[OBLIGATORIO]** Consultas ejecutan correctamente sin errores de sintaxis
- [ ] **[OBLIGATORIO]** Cada resultado tiene una conclusión relevante al caso

### INTERMEDIO (8 criterios)

**Calidad del Modelo**
- [ ] Diagrama visual del modelo de datos (ERD o similar)
- [ ] Identifica tipo de cardinalidad de cada relación (1:N, N:M, 1:1)
- [ ] Describe la lógica de negocio que representa el modelo

**Calidad de Consultas**
- [ ] Consultas SQL son eficientes y legibles (formato, aliases, indentación)
- [ ] Usa JOINs apropiadamente para combinar tablas relacionadas
- [ ] Usa GROUP BY y funciones de agregación correctamente
- [ ] Usa filtros WHERE y HAVING de forma apropiada
- [ ] Usa ORDER BY para presentar resultados ordenados lógicamente

### AVANZADO (10 criterios)

**Técnicas Avanzadas**
- [ ] Usa subqueries cuando es apropiado (WHERE IN, scalar subquery)
- [ ] Usa CTEs (WITH) para mejorar legibilidad de consultas complejas
- [ ] Usa Window Functions cuando aplica (ROW_NUMBER, RANK, LAG, SUM OVER)
- [ ] Propone al menos 2 consultas adicionales que aportan valor al análisis

**Análisis y Conclusiones**
- [ ] Conclusiones aportan valor en el contexto del negocio
- [ ] Identifica patrones o anomalías en los datos
- [ ] Markdown cells contextualizan cada consulta (qué busca, por qué importa)
- [ ] Incluye recomendaciones basadas en los hallazgos

**Calidad General**
- [ ] Notebook tiene estructura clara y navegable
- [ ] Código es limpio, comentado donde necesario, con aliases descriptivos

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 2 criterios adicionales de los 18 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 6 criterios adicionales de los 18 no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 10/10 (Básico + Intermedio)
  - Al menos 5 criterios de la sección AVANZADO

---

## Ejemplos de Cumplimiento

**Exploración inicial de tablas:**
```python
import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base de datos (código provisto)
engine = create_engine('postgresql://user:password@host:port/database')

# Explorar tablas existentes
query = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
"""
tables = pd.read_sql(query, engine)
print("Tablas en la base de datos:")
print(tables)
```

```markdown
## 1. Tablas Identificadas

Se encontraron **5 tablas** en la base de datos:
1. `books` - Catálogo de libros
2. `authors` - Información de autores
3. `publishers` - Editoriales
4. `ratings` - Calificaciones de usuarios
5. `reviews` - Reseñas textuales de usuarios
```

**Exploración de estructura de una tabla:**
```python
# Estructura de la tabla customers
query = """
SELECT
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = 'customers'
ORDER BY ordinal_position;
"""
estructura = pd.read_sql(query, engine)
print(estructura)
```

```markdown
### Tabla: books
| Columna | Tipo | Nullable | Descripción inferida |
|---------|------|----------|---------------------|
| book_id | integer | NO | PK - Identificador único |
| author_id | integer | NO | FK - Referencia a authors |
| title | varchar(255) | NO | Título del libro |
| num_pages | integer | NO | Número de páginas |
| publication_date | date | NO | Fecha de publicación |
| publisher_id | integer | NO | FK - Referencia a publishers |
```

**Explicación del modelo de datos (completo):**
```markdown
## 2. Modelo de Datos

### Diagrama de Relaciones (ERD)
```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│    authors      │       │     books       │       │    ratings      │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ PK author_id    │◄──────│ FK author_id    │◄──────│ FK book_id      │
│    author       │       │ PK book_id      │       │ PK rating_id    │
└─────────────────┘       │    title        │       │    username     │
                          │    num_pages    │       │    rating       │
                          │    pub_date     │       └─────────────────┘
                          │ FK publisher_id │
                          └────────┬────────┘       ┌─────────────────┐
                                   │                │    reviews      │
┌─────────────────┐                │                ├─────────────────┤
│   publishers    │                │                │ PK review_id    │
├─────────────────┤                │                │ FK book_id      │
│ PK publisher_id │◄───────────────┘                │    username     │
│    publisher    │                                 │    text         │
└─────────────────┘                                 └─────────────────┘
```

### Relaciones Identificadas

| Tabla Origen | Tabla Destino | FK | Cardinalidad | Descripción |
|--------------|---------------|-------|--------------|-------------|
| books | authors | author_id | N:1 | Cada libro tiene un autor |
| books | publishers | publisher_id | N:1 | Cada libro tiene una editorial |
| ratings | books | book_id | N:1 | Cada calificación pertenece a un libro |
| reviews | books | book_id | N:1 | Cada reseña pertenece a un libro |

### Lógica de Negocio
- Un **autor** puede escribir múltiples **libros** (1:N)
- Una **editorial** puede publicar múltiples **libros** (1:N)
- Un **libro** puede tener múltiples **calificaciones** de diferentes usuarios (1:N)
- Un **libro** puede tener múltiples **reseñas** textuales de diferentes usuarios (1:N)
- El modelo representa una aplicación de libros con sistema de valoración y reseñas
```

**Consulta con JOIN y agregación:**
```python
# Pregunta: ¿Cuál es el promedio de calificaciones y número de reseñas por libro?

query = """
SELECT
    b.title AS titulo,
    a.author AS autor,
    COUNT(DISTINCT r.rating_id) AS total_calificaciones,
    ROUND(AVG(r.rating)::numeric, 2) AS calificacion_promedio,
    COUNT(DISTINCT rv.review_id) AS total_resenas
FROM books b
INNER JOIN authors a ON b.author_id = a.author_id
LEFT JOIN ratings r ON b.book_id = r.book_id
LEFT JOIN reviews rv ON b.book_id = rv.book_id
GROUP BY b.book_id, b.title, a.author
HAVING COUNT(DISTINCT r.rating_id) > 0
ORDER BY calificacion_promedio DESC, total_calificaciones DESC
LIMIT 10;
"""

resultado = pd.read_sql(query, engine)
print(resultado)
```

```markdown
### Conclusión
Los libros mejor valorados tienen calificaciones promedio superiores a **4.5 estrellas**,
con un mínimo de **50 calificaciones** cada uno, lo que indica alta confiabilidad.

**Hallazgos clave:**
- Los libros con más de **100 calificaciones** mantienen promedios altos (4.3+)
- Solo el **15%** de los libros tienen reseñas textuales, lo que sugiere oportunidad
  para incentivar a los usuarios a escribir reseñas detalladas
- Los autores con múltiples libros bien valorados deberían ser priorizados para
  promociones y destacados en la página principal
```

**Consulta con subquery:**
```python
# Pregunta: ¿Qué editoriales tienen más libros publicados con más de 50 páginas?

query = """
SELECT
    p.publisher,
    COUNT(b.book_id) AS total_libros,
    ROUND(AVG(b.num_pages)::numeric, 0) AS promedio_paginas,
    MIN(b.publication_date) AS fecha_mas_antigua,
    MAX(b.publication_date) AS fecha_mas_reciente
FROM publishers p
INNER JOIN books b ON p.publisher_id = b.publisher_id
WHERE b.num_pages > 50
GROUP BY p.publisher_id, p.publisher
HAVING COUNT(b.book_id) > (
    SELECT AVG(libros_por_editorial)
    FROM (
        SELECT COUNT(b2.book_id) AS libros_por_editorial
        FROM books b2
        WHERE b2.num_pages > 50
        GROUP BY b2.publisher_id
    ) AS promedios
)
ORDER BY total_libros DESC;
"""

resultado = pd.read_sql(query, engine)
print(f"Clientes con gasto superior al promedio: {len(resultado)}")
print(resultado.head(10))
```

```markdown
### Conclusión
Las **editoriales más productivas** publican más de **30 libros** con contenido sustancial
(más de 50 páginas), lo que excluye folletos y publicaciones menores.

**Hallazgos clave:**
- **Penguin Books** lidera con 52 libros, promedio de 320 páginas
- Las editoriales top representan el **45% del catálogo total**
- Editoriales con mayor volumen tienen rangos de publicación más amplios (1950-2020)

**Recomendaciones:**
1. Negociar acuerdos preferenciales con las 5 editoriales principales
2. Destacar colecciones completas de estas editoriales en la plataforma
3. Analizar qué géneros dominan estas editoriales para estrategia de adquisición
```

**Consulta con CTE y Window Function:**
```python
# Pregunta: ¿Cuáles son los autores con mejor calificación promedio (mínimo 50 ratings)?

query = """
WITH autor_stats AS (
    SELECT
        a.author_id,
        a.author,
        COUNT(DISTINCT b.book_id) AS total_libros,
        COUNT(DISTINCT r.rating_id) AS total_calificaciones,
        ROUND(AVG(r.rating)::numeric, 2) AS calificacion_promedio
    FROM authors a
    INNER JOIN books b ON a.author_id = b.author_id
    LEFT JOIN ratings r ON b.book_id = r.book_id
    GROUP BY a.author_id, a.author
    HAVING COUNT(DISTINCT r.rating_id) >= 50
)
SELECT
    author,
    total_libros,
    total_calificaciones,
    calificacion_promedio,
    RANK() OVER (ORDER BY calificacion_promedio DESC) AS ranking,
    ROUND(
        (calificacion_promedio - AVG(calificacion_promedio) OVER())::numeric, 2
    ) AS diferencia_vs_promedio
FROM autor_stats
ORDER BY calificacion_promedio DESC, total_calificaciones DESC
LIMIT 10;
"""

resultado = pd.read_sql(query, engine)
print(resultado)
```

```markdown
### Conclusión
Los **autores mejor valorados** mantienen calificaciones promedio superiores a **4.5 estrellas**
con un mínimo de 50 calificaciones, garantizando confiabilidad estadística.

**Hallazgos clave:**
- **J.K. Rowling** lidera con 4.8 de promedio y 2,340 calificaciones
- Autores con múltiples libros (3+) tienden a tener calificaciones más estables
- La diferencia entre el top 1 y el promedio general es de **+0.9 puntos**

**Recomendaciones:**
1. Destacar estos autores en la página principal y newsletters
2. Crear colecciones "Autores Destacados" para facilitar descubrimiento
3. Priorizar adquisición de nuevos títulos de estos autores
4. Usar sus libros como "gancho" para cross-selling de autores similares
```

**Consulta adicional propuesta (valor agregado):**
```python
# Consulta Adicional 1: Análisis de participación de usuarios activos

query = """
WITH usuarios_activos AS (
    SELECT
        r.username,
        COUNT(DISTINCT r.rating_id) AS total_calificaciones,
        COUNT(DISTINCT rv.review_id) AS total_resenas
    FROM ratings r
    LEFT JOIN reviews rv ON r.username = rv.username
    GROUP BY r.username
    HAVING COUNT(DISTINCT r.rating_id) > 50
),
stats_generales AS (
    SELECT
        AVG(total_calificaciones) AS promedio_calificaciones,
        AVG(total_resenas) AS promedio_resenas
    FROM usuarios_activos
)
SELECT
    ua.username,
    ua.total_calificaciones,
    ua.total_resenas,
    ROUND((ua.total_resenas::numeric / NULLIF(ua.total_calificaciones, 0) * 100), 1) AS tasa_conversion_resena,
    CASE
        WHEN ua.total_calificaciones > sg.promedio_calificaciones * 1.5 THEN 'Super Usuario'
        WHEN ua.total_calificaciones > sg.promedio_calificaciones THEN 'Usuario Activo'
        ELSE 'Usuario Regular'
    END AS segmento
FROM usuarios_activos ua
CROSS JOIN stats_generales sg
ORDER BY ua.total_calificaciones DESC, ua.total_resenas DESC
LIMIT 20;
"""

resultado = pd.read_sql(query, engine)
print("Análisis de Cohortes - Retención a 6 meses")
print(resultado.head(20))
```

```markdown
### Conclusión - Análisis de Usuarios Activos

Los usuarios que califican más de **50 libros** tienen una tasa de conversión a reseña
textual del **48%**, significativamente superior al promedio general (15%).

**Hallazgos clave:**
- **Super Usuarios** (150+ calificaciones): Representan el 5% pero generan el 35% de las reseñas
- Tasa de conversión aumenta con la actividad: 25% (50-100 ratings) vs 60% (150+ ratings)
- Los usuarios más activos escriben reseñas más largas y detalladas

**Recomendaciones:**
1. **Programa de reconocimiento**: Badges y beneficios para Super Usuarios
2. **Incentivos graduales**: Desbloquear funciones premium al alcanzar hitos (50, 100, 150 ratings)
3. **Gamificación**: Sistema de puntos por reseñas de calidad (con votos útiles)
4. **Comunidad**: Foro exclusivo para usuarios activos para fomentar engagement
```

---

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**

- Celdas sin ejecutar de forma secuencial
- No cumple criterios OBLIGATORIOS (menos de 10/10)
- **Sustitución de SQL por Pandas** para resolver consultas (ej: usar df.groupby() en lugar de GROUP BY)
- **Código copiado de IA** sin comprensión demostrada
- **Credenciales hardcodeadas** en el código (ver nota para revisores más abajo)
- **Consultas con errores** de sintaxis o ejecución que no fueron corregidos
- Falta de celdas markdown que contextualicen el análisis
- **Conclusiones contradictorias** con los resultados obtenidos
- No identificar relaciones entre tablas (usar tablas sin JOINs cuando se requieren)

---

## Errores Frecuentes

### En Conexión y Exploración

1. **No explorar todas las tablas**:
   - Incorrecto: Solo trabajar con tablas mencionadas explícitamente en las preguntas
   - Correcto: Explorar y documentar todas las tablas del esquema
   - Consecuencia: No cumple requisito obligatorio

2. **No describir estructura de tablas**:
   - Incorrecto: Solo listar nombres de tablas
   - Correcto: Documentar columnas, tipos de datos, nullability
   - Consecuencia: No demuestra exploración completa

### En Modelo de Datos

3. **No explicar relaciones entre tablas**:
   - Incorrecto: Solo listar tablas sin explicar cómo se conectan
   - Correcto: Identificar PKs, FKs, cardinalidad y lógica de negocio
   - Consecuencia: No cumple requisito obligatorio

4. **Confundir tipos de cardinalidad**:
   - Incorrecto: Decir que orders-customers es 1:1
   - Correcto: orders-customers es N:1 (un cliente tiene muchos pedidos)
   - Consecuencia: Demuestra falta de comprensión del modelo

### En Consultas SQL

5. **Usar Pandas en lugar de SQL**:
   - Incorrecto: `df.groupby('category').sum()` o `df.merge(df2, on='id')`
   - Correcto: `SELECT category, SUM(amount) FROM... GROUP BY category`
   - Consecuencia: **Descalificación automática**

6. **JOINs incorrectos**:
   - Incorrecto: JOIN sin condición ON o con columna incorrecta
   - Correcto: JOIN con FK correcta relacionando tablas
   - Consecuencia: Resultados incorrectos, duplicados, o producto cartesiano

7. **Olvidar GROUP BY con agregaciones**:
   - Incorrecto: `SELECT category, SUM(amount) FROM...` (sin GROUP BY)
   - Correcto: `SELECT category, SUM(amount) FROM... GROUP BY category`
   - Consecuencia: Error de SQL

8. **Confundir WHERE y HAVING**:
   - Incorrecto: `WHERE SUM(amount) > 1000`
   - Correcto: `HAVING SUM(amount) > 1000`
   - Consecuencia: Error de SQL

9. **No filtrar datos relevantes**:
   - Incorrecto: Incluir pedidos cancelados en análisis de ventas
   - Correcto: `WHERE status = 'completed'` o según corresponda
   - Consecuencia: Métricas distorsionadas

10. **Usar SELECT * en consultas finales**:
    - Incorrecto: `SELECT * FROM orders o JOIN...`
    - Correcto: `SELECT o.order_id, o.order_date, c.name...`
    - Consecuencia: Resultados confusos, no profesional

### En Conclusiones

11. **Resultados sin interpretación**:
    - Incorrecto: Solo mostrar el DataFrame resultante sin comentario
    - Correcto: Cada resultado con conclusión en contexto de negocio
    - Consecuencia: No cumple requisito obligatorio

12. **Conclusiones genéricas**:
    - Incorrecto: "La categoría X tiene más ventas"
    - Correcto: "La categoría X representa 35% de ingresos totales, sugiriendo priorización en inventario y oportunidad de negociación por volumen"
    - Consecuencia: No aporta valor accionable

13. **Conclusiones contradictorias**:
    - Incorrecto: Datos muestran caída y conclusión dice "crecimiento sostenido"
    - Correcto: Conclusiones coherentes con los datos mostrados
    - Consecuencia: Demuestra falta de comprensión o falta de atención

### En Técnicas Avanzadas

14. **CTEs sin propósito claro**:
    - Incorrecto: Usar CTE para una consulta simple que no lo necesita
    - Correcto: Usar CTE para mejorar legibilidad de consultas complejas
    - Consecuencia: Sobrecomplicación innecesaria

15. **Window functions mal implementadas**:
    - Incorrecto: `SUM(amount) OVER()` sin PARTITION BY cuando se requiere
    - Correcto: `SUM(amount) OVER(PARTITION BY category ORDER BY date)`
    - Consecuencia: Resultados incorrectos

---

## Notas Importantes

- Este caso es **INDEPENDIENTE** del Caso Principal
- Se recomienda realizarlo mientras esperas aprobación de la Descomposición
- **NO puede realizarse localmente** - trabajar desde la plataforma proporcionada
- Todas las consultas deben ser en **SQL puro** (Pandas solo para visualizar/exportar)
- Guardar el notebook localmente una vez aprobado
- El objetivo es demostrar dominio de SQL, no de Python/Pandas

---

## Nota para Revisores: Credenciales Hardcodeadas

> [!NOTE]
> **Buena práctica no enseñada en el curso**: Aunque no se enseña en el bootcamp, es recomendable
> **sugerir** a los estudiantes que eviten hardcodear credenciales directamente en el código.
> En proyectos profesionales, las credenciales deberían estar en archivos `.env` o variables de entorno.
>
> **Cómo señalarlo (sugerencia, no penalización)**:
> - "Excelente trabajo. Como sugerencia para proyectos futuros, considera usar variables de entorno
>   para las credenciales en lugar de hardcodearlas en el código."
> - No es motivo de penalización, solo una recomendación de mejora profesional.
>
> **Ejemplo de mejora** (opcional para compartir):
> ```python
> import os
> from dotenv import load_dotenv
> load_dotenv()
> 
> db_config = {
>     'user': os.getenv('DB_USER'),
>     'pwd': os.getenv('DB_PASSWORD'),
>     # ...
> }
> ```
