# Sprint 3: Explorar KPIs con SQL
🗓️ Fecha de creación: 9 octubre 2025  
🗓️ Fecha de actualización: 10 octubre 2025<br><br>

---
## Capitulo 1: Entender la estructura de una base de datos relacional
### C1 - Lección 1: Explorar bases de datos relacionales

Componentes esenciales de una base de datos relacional
- Tablas (Tables)
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

Ejemplo: `SELECT * FROM fitness_trackers LIMIT 10;`  
<br><br>

Tipos de datos
- **Texto (TEXT/VARCHAR):** letras o caracteres especiales (ej. "Café Clásico", "clientes@email.com").
- **Números (INTEGER/FLOAT):** valores numéricos , pueden ser enteros (INTEGER) o números con decimales (FLOAT).
- **Fechas (DATE/TIMESTAMP):** valores que representan fechas y/o horas (ej. 01/01/2024, 2024-01-01 10:30:00).

💡 La correcta identificación del tipo de datos es crucial porque te dice qué tipo de análisis puedes realizar. No puedes sumar un texto, ni promediar una fecha.


<br><br><br>

---
## Capitulo 2:  Consultas SQL para selección, filtrado y organización de datos
### C2 - Lección 1:
<br><br>

### C2 - Lección 2:
<br><br>

### C2 - Lección 3:
<br><br>

### C2 - Lección 4:
<br><br>

### C2 - Lección 5:
<br><br>

### C2 - Lección 6:
<br><br><br>

---
## Capitulo 3: Cálculo de métricas financieras clave
### C3 - Lección 1:
<br><br><br>

---
## Capitulo 4: Estructurar, entregar y comunicar reportes financieros
### C4 - Lección 1: