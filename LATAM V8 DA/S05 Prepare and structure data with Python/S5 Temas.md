# Sprint 5: Prepara y estructura datos con Python
🗓️ Fecha de creación: 2 Diciembre 2025  
🗓️ Fecha de actualización: 2 Diciembre 2025<br><br>

---
## Capitulo 1: Introducción a Python y Pandas
### C1 - Lección 1: Python para el análisis de datos
<br>

**🎯 Propósito de la lección**

Dar el salto desde análisis “manual” (Sheets/Excel) a un enfoque automatizable y escalable usando Python, entendiendo por qué es el estándar en analítica cuando empiezan a crecer los datos, la frecuencia de actualización y la necesidad de reproducibilidad.

**🧠 Idea central**

El valor no está solo en calcular, sino en poder repetir el mismo análisis cada semana (con archivos nuevos), sin errores humanos, dejando un proceso documentado, trazable y reutilizable.

**Tematicas trabajadas**

1) **Contexto del caso (motivación realista)**

    - Te pones en el rol de Data Analyst Jr. en una organización ambiental que monitorea contaminación (PM2.5).
    - Cada lunes llegan archivos nuevos y hoy el proceso se hace “a mano” (copiar/pegar/filtrar/calcular promedios).
    - La jefa pide automatización: “No podemos depender de pasos manuales. Quiero que empieces a usar Python.”

**Mensaje clave:** cuando el proceso se repite semanalmente, ya no es un análisis, es un proceso… y eso se automatiza.

2) **Qué es Python (y por qué se volvió el idioma universal)**

- Python se presenta como lenguaje simple, versátil y con comunidad.

- Se aterriza a analítica: Python sirve para

    - Limpieza y transformación (ordenar, limpiar, preparar datos)
    - Visualización (gráficos y dashboards)
    - Automatización (scripts reproducibles)
    - (y más adelante) Machine Learning

3) **Por qué Sheets se queda corto (y dónde entra Python)**

Se explican 3 límites típicos de hojas de cálculo:

- Repetición manual → más tiempo + más probabilidad de error
- Dificultad para escalar → archivos grandes se ponen lentos o fallan
- Poca trazabilidad → cuesta saber “cómo se generó” el reporte

Python entra como solución porque:

- te deja automatizar lo repetitivo,
- repetir el flujo con nuevos datos,
- documentar el proceso (y que otro lo ejecute igual).

4) **Cómo se usa Python en Data Analytics (librerías)**

Se introduce la idea de librerías: paquetes que ya traen herramientas listas.

- **pandas:** tablas tipo Excel, pero programables
- **numpy / scipy:** matemáticas/estadística
- **matplotlib / seaborn:** visualización

5) **Comparación práctica: Sheets vs SQL vs Python**

Se ubica cada herramienta en el ciclo de análisis:

- **SQL:** extraer datos y agrupar en bases corporativas
- **Sheets/Excel:** revisión rápida, compartir con negocio, outputs manuales
- **Python:** limpieza robusta, análisis reproducible, automatización, visualización programable

6) **Pensamiento programático (structured thinking)**

Se enseña que programar no es memorizar comandos: es pensar en pasos.

- Analogía “receta”: pasos claros y en orden.
- Se plantea un flujo típico de analítica:
    1. definir el problema
    2. ubicar datos
    3. cargar dataset
    4. explorar columnas/errores
    5. limpiar (nulos/duplicados/inconsistencias)
    6. calcular
    7. visualizar
    8. responder la pregunta

**Mini-pseudocódigo:** promedio de PM2.5 por país (agrupar → promedio → ordenar → gráfico → reporte).

7) **Ejemplo de lógica “si-entonces” (para automatizar)**

Se cuenta el caso de Sofía (inventario) para explicar:

- cómo un proceso manual se vuelve reglas + bucles:

    - “si stock > 0”
    - “y si fecha última venta > 90 días”
    - entonces “agregar a olvidados”

Se muestra la equivalencia “manual vs pseudocódigo”.

8) **Conexión con el flujo real que se usará en el sprint**

Se deja instalado el pipeline mental que se repetirá en las siguientes lecciones:
Cargar → Explorar → Limpiar → Analizar → Visualizar → Comunicar (aplicado al dataset de PM2.5).

**Errores comunes y cómo evitarlos**

- ❌ Creer que Python “reemplaza” SQL y Sheets → ✅ Pensar en combo: SQL extrae, Python transforma/analiza, Sheets comparte/visualiza rápido.
- ❌ Empezar a “tirar código” sin plan → ✅ Escribir primero pasos/pseudocódigo (qué hago, en qué orden, con qué reglas).
- ❌ No estandarizar nombres/unidades del dataset (PM2.5) → ✅ Definir una convención y repetirla en todo el sprint.
- ❌ Pensar que “librería = magia” y no entender qué hace → ✅ Conectar cada librería con una tarea (tablas, estadística, gráficos).
- ❌ Hacer el análisis una sola vez y no prepararlo para repetirse → ✅ Diseñar desde el inicio como proceso semanal: cargar → limpiar → calcular → reportar.

<br>

### C1 - Lección 2: Configurando tu entorno de análisis
<br>

**🎯 Propósito de la lección**

Dejarte listo para trabajar en un entorno reproducible usando Jupyter Notebook, de forma que puedas empezar a construir el reporte mensual de PM2.5 por país (máx, mín, promedio) sin depender de pasos manuales.

**🧠 Idea central**

El “entorno” no es solo instalar cosas: es tener un espacio de trabajo donde puedas (1) ejecutar código por bloques, (2) ver resultados inmediatamente, y (3) documentar el análisis como si fuera un reporte. Jupyter Notebook funciona como el puente entre “programar” y “comunicar”.

**Tematicas trabajadas**

1) **Contexto de negocio y plan por capítulos**

- El problema que plantea tu jefa: reporte mensual de PM2.5 por país (máximo, mínimo, promedio).

La lección se enfoca en que puedas empezar el trabajo desde un notebook y dejarlo “bien armado” desde el inicio.

2) **Qué es Jupyter Notebook y por qué se usa**

- **Qué es:** un documento interactivo que mezcla código + texto + visualizaciones en un solo lugar.
- Por qué sirve en analítica:

    - Documentas paso a paso (no queda “mágico” como a veces pasa en Sheets).
    - Experimentas sin “romper” el dataset original.
    - Te queda un artefacto compartible (el notebook) para tu equipo/stakeholders técnicos.

3) **Conociendo la interfaz (lo mínimo indispensable)**

- **Celdas de código:** ejecutas Python y ves output debajo (tablas, prints, errores, gráficos).
- **Celdas de texto (Markdown):** escribes títulos, subtítulos, explicaciones y conclusiones.
- **Menú superior:** ejecutar celdas, insertar, mover, convertir tipo de celda, etc.
La idea es que el notebook no sea “solo código”, sino una historia.

4) **Ejecutando tu primer código (y entendiendo el “estado” del notebook)**

- **Cómo ejecutar:** botón Run/Ejecutar o atajo Shift + Enter.
- **Variables:** se guardan en memoria (kernel).

    - Si defines ciudad = "Buenos Aires" en una celda, puedes usarla más adelante en otras celdas.
    - Si borras la celda que crea la variable, la variable puede seguir existiendo si el kernel no se reinició (esto es clave para entender por qué a veces “funciona” algo y luego no).

5) Organizando tu notebook como un reporte profesional

Tres prácticas que se remarcan:

1. Usar títulos claros (Markdown)

    - _#_ Título principal
    - _##_ Secciones
    - _###_ Subsecciones

Esto actúa como “índice” y guía de lectura.

2. Comentarios breves en el código

    - Explican intención: qué haces y por qué (ej. “reemplazo nulos”, “cargo datos”, “calculo promedio”).

3. Variables con nombres con sentido

    - Mejor df_pm25, clean_df, mean_value que x, df1, etc.

**Errores comunes y cómo evitarlos**

- ❌ Creer que “reiniciar el notebook” borra todo (incluyendo outputs) automáticamente → ✅ Aclara: Restart Kernel limpia variables/memoria; para borrar outputs usa Clear All Outputs (o “Restart & Clear Output” si existe en tu interfaz).
- ❌ Ejecutar celdas “salteadas” y después no entender por qué algo falla → ✅ Ejecuta de arriba hacia abajo (Run All) y valida que el notebook sea reproducible.
- ❌ Escribir títulos con # dentro de una celda de código esperando que sea un encabezado → ✅ Los encabezados van en celda Markdown (en código # es comentario).
- ❌ Dejar un notebook como “pared de código” → ✅ Alterna: código → resultado → 2–3 líneas de explicación.
- ❌ Usar nombres genéricos (df1, x, temp) y perder el hilo → ✅ Nombres que describan contenido/estado: df_raw, df_clean, df_summary.

<br>

### C1 - Lección 3: Cargando datos con Pandas
<br>

<br>

### C1 - Lección 4: Entendiendo esquemas y diccionarios de datos
<br>

<br>


## Capitulo 2: Limpieza y transformación de datos

### C2 - Lección 1: Detectar y manejar valores faltantes o invalidos
<br>

<br>

### C2 - Lección 2: Eliminar duplicados y filas irrelevantes
<br>

<br>

### C2 - Lección 3: Convertir y formatear tipos de dato
<br>

<br>

### C2 - Lección 4: IA para categorización de datos
<br>

<br>

## Capitulo 3: Filtrar, ordenar y resumir datos

### C3 - Lección 1: Filtrando datos con condiciones
<br>

<br>

### C3 - Lección 2: Calculando estadisticas resumidas
<br>

<br>

### C3 - Lección 3: Agrupando y agregando datos
<br>

<br>

### C3 - Lección 4: Ordenando datos para identificar patrones
<br>

<br>

### C3 - Lección 5: IA Usando Claude Code para agrupar y resumir datos
<br>

<br>

## Capitulo 4: Combinación y estructuración de datasets

### C4 - Lección 1: Identificación de claves de unión y preparación de tablas
<br>

<br>

### C4 - Lección 2: Validación del conjunto de datos con herramientas visuales
<br>

<br>

### C4 - Lección 3: Combinación de datasets y verificación de resultados
<br>

<br>

### C4 - Lección 5: Limpieza y organización del dataset
<br>

<br>