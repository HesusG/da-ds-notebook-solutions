# Sprint 3: Explorar KPIs con SQL
🗓️ Fecha de creación: 9 octubre 2025  
🗓️ Fecha de actualización: 10 octubre 2025<br><br>

---
## Capitulo 1: Entender la estructura de una base de datos relacional
### C1 - Lección 1: Explorar bases de datos relacionales

Componentes esenciales de una base de datos relacional
- Tablas (Tables).
- Filas (Rows): Cada fila en una tabla representa un registro individual o una entrada única.
- Columnas (Columns): Cada columna representa un atributo o característica del registro.
<br><br>

Claves (Keys)  
💡 Las claves son un tipo especial de columna que nos permite conectar las tablas entre sí.
 Clave Primaria (Primary Key - PK) → columna que contiene un valor único para cada fila en una tabla, nunca se repite.
- Clave Foránea (Foreign Key - FK) → columna que conecta una tabla con otra, haciendo referencia a una clave primaria. Es el "enlace" que crea la relación.

SQL (Structured Query Language) es el lenguaje que usamos para consultar y trabajar con bases de datos relacionales. 
![alt text](image.png)

Recursos adicionales:
- [Introducción a SQL](https://www-w3schools-com.translate.goog/sql/sql_intro.asp?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=wapp)
<br><br>

### C1 - Lección 2: Identificar claves y relaciones entre tablas
- Clave Primaria (Primary Key - PK): es un identificador único para cada fila en una tabla.
- Clave Foránea (Foreign Key - FK): es una columna en una tabla que hace referencia a la clave primaria de otra tabla.

¿Por qué importan?  
por ejemplo, si no existieran claves, cada vez que un cliente hiciera una compra, deberías guardar su nombre, apellido, correo y demás datos en cada fila de la tabla de ventas. Esto es ineficiente y propenso a errores.
<br><br>

### C1 - Lección 3: Interpretar esquemas del mundo real
Un **Diagrama de Entidad-Relación** (ERD) es como un mapa visual de la base de datos. Muestra las tablas (entidades), sus columnas y las relaciones entre ellas. Leer un ERD te permite entender cómo fluye la información dentro de una empresa.

![alt text](image-1.png)
💡 El verdadero valor de este esquema es la capacidad de combinar datos de distintas tablas para responder preguntas de negocio complejas. Cada relación habilita un nuevo tipo de análisis.


Recursos adicionales
- YouTube: [Diagramas de Entidad-Relación (ERD) en Lucid Chart](https://www.youtube.com/watch?v=TKuxYHb-Hvc)
<br><br>

### C1 - Lección 4: Inspeccionar tablas con SQL

 Primer vistazo a los datos:
- `SELECT *`: el asterisco significa "muéstrame todas las columnas".
- `FROM nombre_tabla`: le indica a la base de datos de qué tabla quieres ver los datos.
- `LIMIT N`: limita la cantidad de filas que se muestran

💡 El orden importa
- Ejemplo: `SELECT * FROM fitness_trackers LIMIT 10;`
- Para seleccionar ciertas columnas:  `SELECT Titulo, Artista FROM Canciones;` 
<br><br>

Tipos de datos
- **Texto (TEXT/VARCHAR):** letras o caracteres especiales (ej. "Café Clásico", "clientes@email.com").
- **Números (INTEGER/FLOAT):** valores numéricos , pueden ser enteros (INTEGER) o números con decimales (FLOAT).
- **Fechas (DATE/TIMESTAMP):** valores que representan fechas y/o horas (ej. 01/01/2024, 2024-01-01 10:30:00).

💡 La correcta identificación del tipo de datos es crucial porque te dice qué tipo de análisis puedes realizar. No puedes sumar un texto, ni promediar una fecha.
<br><br>

Recursos adicionales:
- [SQL W3Schools:](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_columns) una herramienta gratuita y en línea para practicar tus consultas SQL sin necesidad de instalar un programa de base de datos
- [Tutoriales de SQL básico](https://www.w3schools.com/sql/sql_select.asp)
<br><br><br>

---
## Capitulo 2:  Consultas SQL para selección, filtrado y organización de datos
### C2 - Lección 1: Seleccionar columnas específicas
<br>

**🎯 Propósito de la lección**

Aprender a elegir solo las columnas relevantes de una tabla con SELECT, y a renombrarlas con `alias (AS)` para que el resultado sea claro y **“hable el idioma del negocio”**.

**🧠 Idea central**

En SQL siempre respondemos dos cosas, en este orden:

- Qué columnas mostrar → `SELECT` 

- De dónde traerlas → `FROM`

**1. Seleccionar todas las columnas (exploración)**

`SELECT *FROM fitness_trackers;`

Útil para un primer vistazo, pero no para reportes.

**Problemas de** `SELECT *``**:**

- 🔎 Legibilidad: demasiados campos no necesarios.

- 🐢 Rendimiento: más datos de los que usas = consultas más lentas.

- 🔐 Seguridad: puedes exponer información sensible.

- 💸 Costo: mover datos innecesarios encarece el procesamiento.

**2. Seleccionar columnas específicas (reporte)**

`SELECT brand_name, selling_price, rating FROM fitness_trackers;`

**Obtenemos solo lo pedido:** reporte limpio, comprensible y eficiente.

**Ventajas de limitar columnas**

- ✅ Eficiencia: menos E/S y menor tiempo de ejecución.

- ✅ Claridad: resultados sin “ruido”.

- ✅ Seguridad: reduces exposición de datos.

- ✅ Costo: menos transferencia y cómputo.

- 3. Hacer que el resultado “hable negocio” con alias (AS)

Los alias renombran las columnas en el resultado sin tocar la tabla.

`SELECT`
  `Brand_Name   AS marca,`
  `Selling_Price AS precio,`
  `Rating        AS calificacion`
`FROM fitness_trackers;`

**Cuándo usar alias**

- Para traducir nombres técnicos o en inglés.

- Para simplificar encabezados largos.

- Para desambiguar columnas con el mismo nombre (especialmente en JOIN).

**🔎 Nota:** El alias no cambia el esquema de la tabla; **solo el encabezado** mostrado por esa consulta.

**Practica guiada**

![alt text](image-2.png)

1. **Contexto:** El equipo quiere preparar un cuadro rápido con solo la marca (brand) y el precio de venta (selling price) de los productos.

**Tu objetivo:** Seleccionar las columnas Brand_Name y Selling_Price de la tabla fitness_trackers.
Usar alias Brand y Price_USD.

**Respuesta:**

`SELECT Brand_Name AS Brand,`
       `Selling_Price AS Price_USD`
`FROM fitness_trackers;`

2. **Contexto:** El equipo quiere ampliar el análisis anterior. Quieren ver una comparativa entre el precio de venta y el precio original, además de la marca. 

**Tu objetivo:** Seleccionar las columnas brand_name, original_price y selling_price de la tabla fitness_trackers.No uses alias.

**Respuesta:**

`SELECT Brand_Name,` `original_price,` `Selling_Price`
`FROM fitness_trackers;`

3. **Contexto:** El equipo de Calidad quiere un reporte el nombre de las marcas y el rating. Quieren revisar la reputación de cada una de las marcas que existen en la base de datos. 

**Tu objetivo:** Seleccionar esas dos columnas (Brand_Name, Rating) de la tabla fitness_trackers.
Usar alias claros: Marca, Puntaje.

**Respuesta:**

`SELECT Brand_Name AS Marca,`
       `Rating as Puntaje`
`FROM fitness_trackers;`

4. **Contexto:** El equipo de producto quiere un reporte con el modelo, el color y precio original.

**Tu objetivo:** Seleccionar esas tres columnas (Model_Name, Color, Original_Price) de la tabla fitness_trackers.
Usar alias claros: Modelo, Precio_Original.

**Respuesta:**

`SELECT Model_Name AS Modelo,`
       `Color,`
       `Original_Price AS Precio_Original`
`FROM fitness_trackers;`

<br>

### C2 - Lección 2: Filtrar datos con clausulas WHERE
<br>

**🎯 Propósito de la lección**

Pasar de **“verlo todo”** a **ver solo lo que importa**. se usa WHERE para:

- Enfocar el análisis en criterios específicos.

- Aplicar comparaciones `(=, >, <, >=, <=, <>/!=)`.

- Filtrar por rangos `(BETWEEN)`.

- Filtrar contra listas `(IN / NOT IN)`.

- Combinar condiciones `(AND / OR)` y entender su precedencia.

- Cuidar detalles con texto/fechas (comillas) y el impacto en agregaciones.

**🧠 Idea central**

Toda consulta responde dos cosas:

1. qué columnas mostrar `(SELECT …)` y de dónde traerlas `(FROM …)`.
2. Con `WHERE` decidimos qué filas cumplen nuestras condiciones.

**¿Qué pasa si no filtramos?**

`SELECT Brand_Name, Selling_Price, Rating`
`FROM fitness_trackers;`

Obtenemos todas las filas (p. ej. 610 dispositivos). El reporte queda ruidoso, mezcla productos baratos con mala calificación y carísimos sin contexto.

**Conclusión: en analítica, mostrar todo es mostrar nada útil. Aquí entra WHERE.**

**🧩 Sintaxis base**

`SELECT columnas`
`FROM   tabla`
`WHERE  condicion;`

- Primero SELECT, luego FROM, después WHERE.

- Las fechas y textos van entre comillas (p. ej., 'FitBit', '2024-01-01').

**1. Igualdades (=) con texto y fechas**

`SELECT Brand_Name, Selling_Price, Rating`
`FROM fitness_trackers`
`WHERE Brand_Name = 'FitBit';`

- Funciona para números, texto y fechas.

- Para texto/fecha: usa comillas simples.

**Pro tip:** algunos motores son case-insensitive por defecto, pero no todos. Si se necesita control, normalizar `(UPPER(Brand_Name) = 'FITBIT')`.

**2. Comparaciones (> , < , >= , <=)**

_“Muestra solo los mejor calificados”_

`SELECT Brand_Name, Selling_Price, Rating`
`FROM fitness_trackers`
`WHERE Rating > 4.7;`

Aplica a números y fechas `(created_at >= '2024-01-01')`.

**3. Rangos con BETWEEN**

`BETWEEN a AND b` es inclusivo (incluye límites `a` y `b`).

`SELECT Brand_Name, Selling_Price, Rating`
`FROM fitness_trackers`
`WHERE Selling_Price BETWEEN 28000 AND 29000;`

Equivalente a `Selling_Price >= 28000 AND Selling_Price <= 29000`.

**4. Listas de valores con IN / NOT IN**

`SELECT Brand_Name, Selling_Price, Rating`
`FROM fitness_trackers`
`WHERE Brand_Name IN ('FitBit', 'Xiaomi');`

- Útil cuando se filtra por conjuntos finitos (marcas, categorías, países).
- `NOT IN` excluye la lista.

**Pro tip:** si hay `NULL` en la columna, `NOT IN` puede comportarse distinto según motor. Prefiere `WHERE Brand_Name IS NULL OR Brand_Name NOT IN (…)` si necesitan incluir nulos explícitamente.

**5. Combinar condiciones: AND / OR (y paréntesis)**

**Caso:** “Modelos FitBit con precio entre 17.000 y 20.000”.

`SELECT brand_name, model_name, display, strap_material, selling_price`
`FROM fitness_trackers`
`WHERE brand_name = 'FitBit'`
  `AND selling_price BETWEEN 17000 AND 20000;`

**¿Y si el pedido fuera “FitBit o productos en ese rango de precio”?**

`SELECT brand_name, selling_price`
`FROM fitness_trackers`
`WHERE brand_name = 'FitBit'`
   `OR selling_price BETWEEN 17000 AND 20000;`

**Regla práctica**

- `AND` → todas las condiciones deben cumplirse.
- `OR` → basta con una.
- Siempre usar paréntesis para dejar claro el orden:

`WHERE (brand_name = 'FitBit' AND rating > 4.5)`
   `OR (brand_name IN ('Xiaomi','Garmin') AND selling_price < 20000)`

**Impacto en agregaciones**

Los filtros cambian los resultados de métricas (promedios, sumas, conteos).
Ejemplo: promedio de precio para marcas específicas:

`SELECT AVG(selling_price) AS avg_price`
`FROM fitness_trackers`
`WHERE brand_name IN ('FitBit','Xiaomi') AND rating > 4.5;`

**Errores comunes (y cómo evitarlos)**

- ❌ Mezclar `AND` y `OR` sin paréntesis → ✅ Agrupar con `()`.

- ❌ Olvidar comillas en texto/fecha → ✅ `'texto'`, `'YYYY-MM-DD'`.

- ❌ Confiar en `NOT IN` con posibles NULL → ✅ usar `IS NULL` explícito si aplica.

- ❌ Asumir que `BETWEEN` es exclusivo → ✅ es inclusivo.

- ❌ Filtrar después de agregar → ✅ recordar el orden:
    `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT.`

**Tarea práctica**

![alt text](image-3.png)

1. **Contexto:** El equipo de R&D quiere analizar únicamente los productos de la marca Fitbit o los que tengan rating entre 4 y 5.

**Tu objetivo:** 
- Seleccionar brand_name, model_name, rating.
- Filtrar por una de estas dos condiciones (debe cumplirse al menos una de las siguientes): 
    1. brand_name = 'FitBit'. 
    2. rating entre 4 y 5.

**Respuesta:**

`SELECT brand_name, model_name, rating`
`FROM fitness_trackers`
`WHERE brand_name = 'FitBit'`
`OR rating between 4 and 5`

2. **Contexto:** El equipo de producto quiere enfocarse en Fitbit, Garmin y Noise, pero solo en aquellos dispositivos con precio de venta mayor a 3000 y precio original menor a 10000.

**Tu objetivo:**

- Seleccionar model_name, brand_name, selling_rice y original_price.
- Filtrar por las marcas Fitbit, Garmin y Noise (brand_name) utilizando (IN).
- Filtrar por selling_price > 3000.
- Filtrar por original_price < 10000.

**Respuesta:**

`SELECT model_name, brand_name, selling_price, original_price`
`FROM fitness_trackers`
`WHERE brand_name IN ('FitBit', 'Garmin', 'Xiaomi')`
  `AND selling_price > 3000`
  `AND original_price < 10000;`

<br>

### C2 - Lección 3: Ordenar resultados con ORDER BY
<br>

**🎯 Propósito de la lección**

Aprender a usar ORDER BY para:

- Ordenar resultados en ascendente (ASC) o descendente (DESC).

- Crear rankings útiles (más caros, mejor calificados, etc.).

- Combinar ORDER BY con WHERE y LIMIT para informes claros y accionables.

- Ordenar por más de una columna (orden compuesto).

**🧠 Idea central**

`ORDER BY` define cómo mostrar las filas: primero decide qué traer `(SELECT ... FROM ... WHERE ...)` y luego cómo ordenarlas `(ORDER BY ...)`. Si además se quiere un Top N, aplicar LIMIT al final.

1. **Ordenar productos por precio (descendente)**

**Pedido:** _“Lista de productos Fitbit del más caro al más barato”._

`SELECT Brand_Name, Model_Name, Selling_Price, Rating`
`FROM fitness_trackers`
`WHERE Brand_Name = 'Fitbit'`
`ORDER BY Selling_Price DESC;`

**Claves:**

`ORDER BY Selling_Price` → define el criterio de orden.

`DESC` → orden descendente (más caros primero).

Si se omite `ASC/DESC`, el orden por defecto es ascendente `(ASC)`.

2. **Ordenar por más de una columna (orden compuesto)**

**Pedido:** _“Comparar Fitbit vs Xiaomi y ver los más caros dentro de cada marca”._

`SELECT Brand_Name, Model_Name, Selling_Price, Rating`
`FROM fitness_trackers`
`WHERE Brand_Name IN ('Fitbit', 'Xiaomi')`
`ORDER BY Brand_Name ASC, Selling_Price DESC;`

**¿Cómo leerlo?:**

- Primero agrupa por marca (A→Z).
- Dentro de cada marca, ordena por precio de mayor a menor.
- Este patrón resuelve empates (si dos filas empatan en la primera clave, usa la segunda).

**Pro tip:** añade una tercera clave si necesita orden estable (p. ej., Model_Name ASC).

3. **Ordenar y limitar la cantidad de resultados (Top N)**

**Pedido:** _“Top 5 precios más altos de Fitbit”._

`SELECT Brand_Name, Model_Name, Selling_Price, Rating`
`FROM fitness_trackers`
`WHERE Brand_Name = 'Fitbit'`
`ORDER BY Selling_Price DESC`
`LIMIT 5;`

**Notas prácticas:**

- `LIMIT` se aplica después de ordenar. Primero se ordena, luego se recorta el resultado.

- Según el motor SQL:

    - PostgreSQL/MySQL/SQLite → `LIMIT N`
    - SQL Server → `SELECT TOP (N)` ... (o `FETCH FIRST N ROWS ONLY` con `OFFSET/FETCH`)
    - Oracle → `FETCH FIRST N ROWS ONLY`

**Errores comunes (y cómo evitarlos)**

- ❌ Poner `ORDER BY` antes de `WHERE`. ✅ Orden correcto: `SELECT … FROM … WHERE … ORDER BY … LIMIT.`
- ❌ Esperar que `LIMIT` funcione igual en todos los motores. ✅ Revisar la sintaxis del motor (nota de compatibilidad arriba).
- ❌ Resultados “raros” por nulos. ✅ Revisar si hay `NULL` y usar `NULLS FIRST/LAST` si el motor lo soporta, o filtrar con `WHERE Rating IS NOT NULL`.
- ❌ Empates no deseados. ✅ Añadir claves secundarias: `ORDER BY Selling_Price DESC, Rating DESC, Model_Name ASC.`

**Actividad práctica**



<br>

### C2 - Lección 4: Agrupar y agregar datos
<br><br>

### C2 - Lección 5: Limpiar y preparar datos
<br><br>

### C2 - Lección 6: Asegurar la precisión con tipos de datos y funciones
<br><br><br>

---
## Capitulo 3: Cálculo de métricas financieras clave
### C3 - Lección 1:
<br><br><br>

---
## Capitulo 4: Estructurar, entregar y comunicar reportes financieros
### C4 - Lección 1: