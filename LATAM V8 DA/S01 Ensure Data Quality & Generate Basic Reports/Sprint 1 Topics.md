# Sprint 1: Asegura la calidad de los datos y genera reportes
🗓️ Fecha de creación: 4 septiembre 2025  
🗓️ Fecha de actualización: 4 septiembre 2025

## Capitulo 2: 
### Lección 1: Datos estructurados
- Datos estructurados: una tabla súper organizada, tiene filas y columnas bien definidas, y cada columna tiene un tipo de información específico
- Tipos de datos: Texto, Números, fecha, booleanos, etc
- Tipos de datos por estructura analítica: categóricos, numéricos, discretos, continuos, series temporales, transversales <br><br>

**Ejercicio 1** - Práctica guiada: Detectar problemas de estructura y formato
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/10yZMc0yH4x5Ubjmzz6qJqC-XGsrnx0yH0n2PrPUjYn0/edit?usp=sharing

**Ejercicio 2** - Actividad práctica: limpiar tipos de datos
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1MgdroGbCBGVDqh7vftSbXnW8xc2rH9YHuWlA8Tq-99U/edit?usp=sharing <br><br><br>


### Lección 2: Organización de datos para el análisis
- **Congelar filas**: menú “Ver”, elige “Congelar” y selecciona “1 fila”
- **Ordenar datos**: menú “Datos” y elige “Ordenar rango por columna A, de A a Z”, o por la columna que necesites.
- **Filtros**: Selecciona la fila de encabezados, ve a “Datos” y haz clic en “Crear un filtro”
- **Validación de Datos**: Selecciona la columna, luego ve al menú Datos y haz clic en Validación de datos. Cada vez que alguien quiera escribir algo en esa celda, tendrá que elegir entre las opciones dadas. <br><br>

**Ejercicio 1** - Práctica guiada: ordena y mejora la hoja de ventas
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1Ovhui9G1LQxusTJlW3KgSEorXEui0_bmGH_JfCynERQ/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): 

**Ejercicio 2** - Actividad práctica: Limpieza y validación de datos en suscripciones
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1pWhVHwqymE6AjSy0ysQW2Oz1PBhN4FN9kI8-0UXZdW8/edit?usp=sharing <br><br><br>


### Lección 3: Explorando Datasets con LLMs: Potencial y Limitaciones
- ¿Cómo pueden los LLMs ayudar en análisis de datos?: Análisis exploratorio inicial, Generación de insights, Documentación, Sugerencias metodológicas
  - Opción 1: Subir el dataset completo (menos de 10MB)
  - Opción 2: Compartir solo la estructura (recomendado para datos sensibles)
- Técnicas de prompting para análisis de datos: Contexto, Objetivo, Formato, Limitaciones
- Limitaciones críticas de los LLMs: Alucinaciones, Falta de acceso a datos reales, Sesgos en interpretaciones, Incapacidad para validar <br><br><br>


## Capitulo 3: 
### Lección 1: Identificación y corrección de errores en los datos
- **Quitar duplicados**: menú, elige "Limpieza de datos" y después selecciona "Quitar duplicados".
- **Valores ausentes**: menú, elige "Datos" y selecciona "Crear un filtro". En el menú del filtro, selecciona la opción  "(Vacío)"
- **Promedio**: `=PROMEDIO(A2:A100)` o `=AVERAGE(A2:A100)`
- **Mediana**: `=MEDIANA(A2:A100)` o `=MEDIAN(A2:A100)` <br><br>

**Ejercicio 1** - Práctica guiada: limpieza de datos de TecnoAll
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1B6W9eU7DcYiwa5id_PUONCBfQzErr6I2mCaLbnRceQk/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver):  https://docs.google.com/spreadsheets/d/1d2yyuk6SdusJyo7NDqO5D5UyZujcrHXTFvBGlZ0GUH8/edit?usp=sharing

**Ejercicio 2** - Actividad práctica: Aplicando EDA en nuestro negocio
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1qBk0JSXm_MgzdnyMsz9aUhnvI0xV-Hsp9aymgOI-nHY/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver):<br><br>


Recursos adicionales
- [Centro de Ayuda de Google Sheets: Quitar duplicados](https://support.google.com/docs/answer/6325535)
- [Centro de Ayuda de Google Sheets: Filtrar y ordenar tus datos](https://support.google.com/docs/answer/3540681)<br><br><br>

### Lección 2: Modificación de columnas
- **Dividir campos**: `SPLIT` permite dividir el contenido de una celda en múltiples columnas utilizando un "delimitador" 
  - Sintaxis: `=SPLIT(texto_a_dividir, delimitador)`
  - 📢 El delimitador debe ir entre comillas dobles.
- **Recortar espacios** sobrantes:  `TRIM` (recortar) elimina todos los espacios al principio y al final del texto, y reduce los espacios múltiples entre palabras a un solo espacio. 
  - Sintaxis: `=TRIM(texto_a_limpiar)`
- **Unir columnas** en una sola: La función `JOIN` (unir) permite combinar el contenido de varias celdas o un rango de celdas en una sola celda, utilizando un "delimitador" 
  - Sintaxis: `=JOIN(delimitador, valor1, [valor2, ...]) `
  - Sintaxis para un rango: `=JOIN(delimitador, rango)`
- **Transformar el texto:**
  - La función `UPPER` convierte todo el texto de una celda a mayúsculas: Sintaxis: `=UPPER(texto)`
  - La función `LOWER` convierte todo el texto de una celda a minúsculas: Sintaxis: `=LOWER(texto)`(no visto en esta lección)
  - La función `PROPER` convierte solo la primera letra a mayúscula: Sintaxis: `=PROPER(texto)`

- **Smart Fill** (Relleno Inteligente): ¿No te aparece la sugerencia? menú Datos > Relleno inteligente > Relleno inteligente para forzarla.
- **Smart Cleanup** (Limpieza Inteligente): Puede detectar y sugerir soluciones para problemas comunes como espacios extra, errores de mayúsculas/minúsculas, o incluso algunos formatos de fecha/número inconsistentes. Menú Datos > Limpieza de datos > Sugerencias de limpieza <br><br>

**Ejercicio 1** - Práctica guiada: Actualizando nuestra lista de clientes - MercatoHogar
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1PFKQL6onWY2jtNYcU1gtjXXK9CmbxPkqY-3SMnNM_xI/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1WfCglNLTmMRVK37RmfxisY3Nnyua0r3sYC31wUU0qC4/edit?usp=sharing

**Ejercicio 2** - Actividad Práctica: trabajando en nuestro inventario
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1ue0MRmOFtwS-nqdO0rqBAJh_8od5Yljm03TwE8le1fQ/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): <br><br>

Recursos adicionales
- [Lista de funciones de hoja de cálculo de Google](https://support.google.com/docs/table/25273?hl=es&ref_topic=9054531&sjid=3658440564594165918-SA)  
- [Centro de Ayuda de Google Sheets: Relleno inteligente](https://support.google.com/docs/answer/75509?hl=es&co=GENIE.Platform%3DDesktop&sjid=3658440564594165918-SA) <br><br><br>



### Lección 3: Diseño de flujos de trabajo ordenados
Flujos de trabajo ordenados
- **Cambiar el nombre de las pestañas:** hacer doble clic en el nombre de la pestaña o hacer clic en la flecha y seleccionar Renombrar en el menú desplegable.
- **Añadir una hoja** de resumen (tu bitácora de datos): muestra la información clave y documenta el trabajo realizado
  - Incluye: Descripción del proyecto, Fuente de los datos, Fecha de última actualización, Contacto, Registro de cambios, Suposiciones clave
  - ¿Cómo la creamos? Para crear una nueva hoja: Haz clic en el signo + en la esquina inferior izquierda, renómbrala,  introduce la información sugerida
- **Documentar las columnas:** crear una tabla que explique cada columna o característica del dataset, es decir un diccionario de datos
- **Añadir notas** breves o **comentarios** (pistas para el futuro): 
  - **Notas:** Pequeños textos que aparecen cuando pasas el ratón por encima de una celda. Son para información breve y contextual. Para insertar una nota, haz clic derecho en la celda donde quieres añadirla. Selecciona Agregar nota y escríbela.
  - **Comentarios:** Permiten una discusión o un hilo de conversación sobre una celda. Son ideales para la colaboración. Para añadir un comentario, haz clic derecho en la celda. Selecciona Insertar comentario y escribe tu comentario. Puedes mencionar a otros usuarios para notificarles.
- **Organizar el diseño**
  - Formato y encabezados
    - Usa fuente y tamaño consistentes para los datos, y otro para los encabezados
    - Aplica negrita a los títulos.
    - Mantén la misma alineación
    - Emplea bordes sutiles y colores suaves para separar o destacar, sin abusar.
  - **Espaciado**
    - Ajusta el ancho de las columnas para mostrar todo el contenido.
    - Modifica la altura de las filas si hay texto envuelto.
    - Usa filas o columnas vacías (o con color suave) para separar secciones grandes
    - Congelar filas/columnas: seleccionar la fila 1 > "Ver" > "Inmovilizar" > seleccionar "una fila". <br><br>

**Ejercicio 1** Práctica guiada: Clientes e Inventario
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1HfXzMgF09i4Tp4UpXTeyfJujOJkpuMR7YsW9W3n_sXQ/edit?usp=sharing 
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1JfL_3itCwBGmPOzcvxd92-P0N2Q-W9rQfLMw95aLliU/edit?usp=sharing <br><br><br>

## Capitulo 4: Convertir datos en insights
### Lección 1: Calculando estadísticas básicas
- Las **métricas clave** son números específicos que nos ayudan a entender el desempeño
  - Por ejemplo: Ventas totales del mes, Promedio de ventas por pedido, etc
  - Las 5 funciones fundamentales para calcular métricas:
    - SUM: Suma todos los valores en un rango de celdas. Sintaxis: `=SUM(rango)`
    - COUNT: Cuenta cuántas celdas contienen **números** en un rango e ignora celdas con texto o vacías. Sintaxis: `=COUNT(rango)`
    - AVERAGE: Calcula el promedio (media aritmética) de un rango de números. Sintaxis: `=AVERAGE(rango)`
    - MIN y MAX: Encuentra el valor mínimo y máximo en un rango. Sintaxis: `=MIN(rango)` y `=MAX(rango)`

Consejos para usar las funciones efectivamente:
- Verifica tus rangos: Asegúrate de que estás incluyendo todas las celdas necesarias.
- Usa referencias absolutas cuando sea necesario: Cambia A2 por $A$2:$A$10 si no quieres que el rango cambie al copiar la fórmula.
- Nombra tus cálculos: Agrega etiquetas claras junto a tus fórmulas (ej: "Ventas Totales:", "Promedio Diario:")<br><br>

**Ejercicio 1** Práctica guiada: análisis de ventas mensuales - Farma Mucho
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/19OMQo2kRsHPb-u9xbBV33Xya0wSd6DNi3ljIDLdywyA/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1Nu1gIoRP-pLwtoOidXbGXkHsCibRXxNvRqT9nQ0AvB0/edit?usp=sharing

**Ejercicio 2** Actividad práctica: informe ejecutivo de ventas - MercaRapido
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/13dqXYIQuCABVoP904B2_AbogbY1a-jO6aYXPjH34w7A/edit?usp=sharing 
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1kT7lq7Qba1YWTtmb-Y-ciOKgPLMFJW0Fzl4AlnEyHFM/edit?usp=sharing <br><br><br>

### Lección 2: Comunicando resultados con gráficos
- Gráfico de líneas: para mostrar tendencias en el tiempo
- Gráfico de barras: para comparar categorías

Cómo crear gráficos
1. **Preparar tus datos:** información organizada en columnas o filas contiguas
2. **Seleccionar los datos:** Haz clic en la primera celda de tu rango (incluyendo encabezados) y arrastra hasta la última celda con datos. Deberías ver un rectángulo azul rodeando toda tu selección.
3. **Insertar el gráfico:** menú "Insertar" > Selecciona "Gráfico" > Google Sheets creará automáticamente un gráfico sugerido y aparecerá el "Editor de gráficos" en el panel derecho.
4. **Elegir el tipo correcto:** En Editor de gráficos, sección "Configuración": 
   - Para comparar categorías: Selecciona "Gráfico de columnas"
   - Para mostrar tendencias: Selecciona "Gráfico de líneas" (el correcto)
5. **Personalizar para claridad:** En la pestaña "Personalizar" del Editor:
  - Modificar Título del gráfico - El título debe responder "¿Qué estoy viendo?"
  - Ejes (etiquetas):
  - Formato básico: 
    - Cambia colores si es necesario.
    - Ajusta el tamaño de fuente para legibilidad
    - Considera agregar una grilla para facilitar la lectura
6. **Interpretar y resumir** lo que muestra el gráfico. <br><br>

**Ejercicio 1** 
- Ejercicio sin resolver (cualquier persona con el link puede ver):<br><br><br>

### Lección 3: Cómo utilizar un LLM para crear visualizaciones de Google Sheets

Necesitas una presentación visual rápidamente
1. El poder de un prompt bien estructurado con Chat GPT
   - información clave: el tipo de datos que tenemos,  objetivo principal y el contexto de uso (audiencia).
2. Solicitar configuraciones específicas para Google Sheets
   - especifica que trabajas con Google Sheets para obtener instrucciones más precisas
3. Mejorar las visualizaciones existentes
  - ChatGPT puede ayudarte a mejorar los gráficos que ya creaste: puedes describir tu gráfico o simplemente cargar una foto de tu gráfico.
  
Técnicas avanzadas de prompting
- Solicita alternativas: No te conformes con una sola sugerencia. Pide que te dé múltiples opciones
- Pide el "por qué": Solicita una justificación para sus recomendaciones
- Incluye restricciones: Menciona algunas limitaciones técnicas o de formato

Errores comunes a evitar
- Prompts demasiado vagos
- Omitir el contexto de negocio
- No especificar la herramienta
- Ignorar a la audiencia<br><br>

Recursos adicionales  
[Guía de gráficos de Google Sheets](https://support.google.com/docs/answer/190718)<br><br>

**Ejercicio 1 y 2**  
Práctica guiada: Gráfico de barras - Ventas por producto - Gimnasio  
Actividad práctica: Dashboard de Desempeño por sucursal:

- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1__2gw-vJwyCelnZL1QExzdwd-682MTW2-RT2zmGffiA/edit?usp=sharing 
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/15mJPab01s2pgn_1LK5XclJSMvqGA3x_n4PIXoli4xNo/edit?usp=sharing <br><br><br>

