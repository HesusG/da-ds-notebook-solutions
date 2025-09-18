# Sprint 2: Transformar datos para insights de negocio
🗓️ Fecha de creación: 10 septiembre 2025  
🗓️ Fecha de actualización: 17 septiembre 2025<br><br>

---
## Capitulo 1: Preguntas analíticas en contexto de negocio
### C1 - Lección 1: Formular preguntas a partir del negocio

Cómo identificar y priorizar Stakeholders
- Decisión – “¿Qué necesitas decidir exactamente con estos datos?”
- Plazo – “¿Para cuándo debes tener la respuesta?”
- Involucrados – “¿Quién más participa o puede bloquear/impulsar la acción y cómo prefieren recibir actualizaciones?” <br><br>
  
**1. Definir Tarea:** Definir el éxito antes de medir  
- ¿Cuál es la meta concreta? → **Identificar el canal que más vende Accesorios en Primavera–Verano para redirigir presupuesto.
- ¿Cómo se mide ese éxito? → Ventas netas y ticket promedio por canal.
- ¿Cuál es la ruta de medición? → Históricos mar–ago 2025 y entrega antes de la reunión del miércoles.

**2. Plantea la tarea:** Mini-Framework 4Q (Qué, Cuánto, Cuándo, Quién)  
- ¿Cómo varió `[métrica -qué-]` en `[dimensión-cuánto ]` durante `[periodo -cuándo-]` para ayudar a `[stakeholder -quién-]` a decidir?`

**3 Selecciona los datos:** Definir qué campos del conjunto de datos se van a usar

Guía rápida
1. Parte del objetivo → escoger canal líder.
2. Define la decisión → aumentar o recortar inversión.
3. Elige las dimensiones relevantes → canal, fecha, categoría.
4. Verifica que los datos existan: si faltan, ajusta la pregunta.
<br><br>

### C1 - Lección 2: Vincular preguntas con métricas clave

Una **métrica** es un cálculo que transforma datos aislados en información útil 
- Ejemplo métrica absoluta: Total  
- Ejemplos métricas relativas: Promedios, Crecimiento, ratio, variación, percentil, etc. 
<br><br>

KPIs y OKR
- El Objetivo (O) marca hacia dónde queremos ir.
- Los Resultados Clave (KRs) miden si lo estamos logrando.
- Y esos KRs se cuantifican con KPIs, es decir, métricas específicas (absolutas o relativas).
🎯 Los OKR definen los objetivos estratégicos, y los KPI permiten monitorear si se están cumpliendo.
<br><br>

KPIs vs. Guardrails (métricas de control)
- Guardrails: métricas de control que se monitorean en paralelo a los KPIs para alertar sobre posibles problemas para el negocio. 
💡 Los KPIs dicen si avanzas, los guardrails se aseguran de que avances sin generar un problema mayor.
<br><br>

Términos clave
- **Crecimiento** (MoM/YoY): Cambio entre dos periodos.
- **KPI**: Métrica clave ligada a un objetivo con umbral y frecuencia.
- **Métrica**: Cálculo que resume o compara datos.
- **Promedio**: Representa el desempeño típico.
- **Ratio**: Relación entre dos valores; mide eficiencia o proporción.
- **Valor absoluto vs. relativo**: Tamaño total vs. eficiencia o tendencia.

<br><br>

### C1 - Lección 3: Indicadores que predicen y confirman

Dos tipos de métricas:
- **Indicadores lagging** → miden el resultado final, no puedes cambiarlo. Por ejemplo, las ventas logradas al cierre del trimestre.
- **Indicadores leading** → actúan como palancas de cambio porque se pueden influir a diario, mide para decidir si se cambia algo, para obtener un mejor resultado final. Por ejemplo, el número de clientes saludados personalmente en tienda, que según el libro antecede a un aumento en las ventas.

<br><br>

### C1 - Lección 4: Usar LLMs para el análisis de stakeholders y métricas

LLMs como aliados: Utiliza la IA
- como Subject Matter Expert (SME): pide explicación sobre conceptos desconocidos
- para construir una pregunta 4Q 
- Selector de métrica con guardrails en el prompt
- para generar las funciones de Google Sheets

💡 Diseña una vez, reutiliza siempre: guarda tus prompts SME, conversación 4Q y selector con guardrails para el próximo canal “caótico”.

<br><br><br>

---
## Capitulo 2: Preparar y explorar el dataset
### C2 - Lección 1: Cómo importar datos y unirlos con LEFT JOIN

- Importar un nuevo dataset: File > Import
- Explorando la estructura del conjunto de datos: Revisar encabezados, tipos de datos correctos, cantidad de renglones, etc.
- Comparando los datasets: identificar clave compartida, una columna que funciona como un “punto en común” que permite combinar la información de dos o más hojas de cálculo.   
💡 Regla de oro: si la clave no es única en la hoja de lookup (por ejemplo Tiendas), el join generará duplicados y métricas infladas.

Cómo unir las hojas de transactions y stores
- Tipos de JOIN: LEFT, RIGHT, INNER y FULL

1. Tener los datos en un solo libro de sheets.
2. Posicionarse en una tabla/hoja, en columna nueva, escribe la formula de VLOOKUP. Syntax: 
`=VLOOKUP(search_key, range, index, [is_sorted])`
2. Revisa algunas filas al azar para confirmar que los datos sean correctos.

**Ejercicio** - 
Datos crudos (cualquier persona con el link puede ver):
- [stores.csv](https://drive.google.com/file/d/1UajQdAnrhWP19uBnWIRM7BxZBZPM-96H/view?usp=sharing)
- [transactions.csv](https://drive.google.com/file/d/1Ei3CKnP7LPLb2aqrygVzyqE7s7fnOCx_/view?usp=sharing)

- Ejercicio resuelto (aparece en la plataforma, cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1wnYElfJBinIjvNsZOlkn17k3BgG2YDWM1VLwRTGbTwI/edit?usp=sharing
<br><br>

### C2 - Lección 2: Cómo combinar datasets con XLOOKUP

- Tabla transaccional: cada fila representa una transacción individual, es decir, una venta específica.  
-  Tabla de consulta: también conocidos como tablas de lookup, no se repiten registros: simplemente se listan los valores únicos.

💡 Regla de oro: la tabla “larga” (transaccional) recibe la información de las tablas “cortas” (lookup).

Fórmulas comparadas:
- `=VLOOKUP(lo_que_busco (clave primaria), donde busco, número de columna a regresar, ¿coincidencia exacta?)`
  - Ejemplo`=VLOOKUP(B2, Productos!A:D, 3, FALSE)`
- `=XLOOKUP(lo_que_busco (clave primaria), dónde_busco, columna a regresar, [si_no_encuentra], [match_mode])`
  - Opciones de [match_mode]:
    - 0 → Coincidencia exacta (es el valor por defecto).
    - -1 → Coincidencia exacta o el siguiente menor.
    - 1 → Coincidencia exacta o el siguiente mayor.
    - 2 → Coincidencia con comodines ( o ?).
  - Ejemplo `=XLOOKUP(B2, Productos!A:A, Productos!C:C, "No existe")` <br><br>


**Ejercicio 1** - Mi Súper Almacén

Datos crudos (cualquier persona con el link puede ver):
- Tabla transaccional: [ventas.csv](https://drive.google.com/file/d/1IjzdM3J2ulxc22K01NDI2QoDgNOuc8Ev/view?usp=sharing)
- Tabla de consulta: [Productos.csv](https://drive.google.com/file/d/1taE0tQ8tErCaMxZ7RV_G0mg4LU4unzxK/view?usp=sharing)
- Tabla de consulta: [sucursales.csv](https://drive.google.com/file/d/1s5A0jVeMMk1wGorqGTVpFRLRC5_hXrt_/view?usp=sharing)  
  
Ejercicio resuelto: https://docs.google.com/spreadsheets/d/1bZGJNBsCFrxvNe8Di1TMK0g0Vm8anc6SaeAFnosLg-s/edit?usp=sharing <br><br>

**Ejercicio 2** - Ejercicios Aplicados – Facturación por categoría y región
Datos crudos (cualquier persona con el link puede ver):
- [ventas_2000.csv](https://drive.google.com/file/d/1EMjltVRbWv5I7n0X_Tpw838iFK7jJfsm/view?usp=sharing)
- productos_2000.csv
- sucursales_2000.csv

Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1PIpZZkcKfjuAOgc57aW1derL2EOCPGcltrV3jDyEVek/edit?usp=sharing

No se han visto las tablas dinámicas, para responder el cuestionario, se pueden usar filtros. <br><br>

Recursos adicionales (Google Sheets)
- [Documentación oficial XLOOKUP](https://support.google.com/docs/answer/12405947)
<br><br>

### C2 - Lección 3: Cómo organizar hojas de cálculo para análisis
Crear un cuaderno limpio y profesional, con reglas claras y documentación mínima:
- Renombrar y colorear pestañas para identificarlas rápido.
  - Para renombrar: doble clic en nombre de la hoja
  - Para colorear: Clic derecho en nombre de la hoja > Cambiar color
- Escribir nombres claros en cada columna.
- Seguir una convención estándar de nombres (pestañas, columnas, rangos).
- Aplicar un código de colores para diferenciar tipos de datos (brutos, limpios, análisis).
- Incluir un README.
  -  un archivo README es una guía rápida para entender el proyecto: 
     -  qué información contiene cada dataset
     -  cómo fue procesada
     -  cuál es el objetivo del análisis

**Ejercicio** - Practica aplicada - Crea tu propio README - empresa Mi Che
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/18pXwhiRwo7ZsV3F9EHudanjdnX9_Cria/edit?usp=sharing&rtpof=true&sd=true
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1ZhEXh6oTxoc6VQOiHVEAbDSQydyEtQYp/edit?usp=sharing&ouid=105341058430000280825&rtpof=true&sd=true
<br><br>

### C2 - Lección 4: Cómo preparar datos categóricos para agrupar

Funciones de Limpieza:
| Paso | Fórmula | Original → Resultado |
|-----------|-----------|-----------|
| Quitar basura + espacios |  `=TRIM(CLEAN(A2))`        | `" Electronics "` → `"Electronics"`  |
| Capitalizar cada palabra | `=PROPER(TRIM(CLEAN(A2)))` | `"electronics"` → `"Electronics"`  |
| Mayúsculas globales      | `=UPPER(...)`              | `"Electronics"` → `"ELECTRONICS"` |
| Separar y tomar 1ᵉʳ ítem | `=INDEX(SPLIT(A2,"/"),1)`  | `"ELECTRONICS/COMPUTERS"` → `"ELECTRONICS"`  |
| Reemplazar cadena        | `=SUBSTITUTE(A2,"AND KITCHEN","")`  | `"HOME AND KITCHEN"` → `"HOME"` |
| Recodificar variantes    | `=SWITCH(A2,"NA","NO CATEGORY","N/A","NO CATEGORY",A2)`  | `"N/A"` → `"NO CATEGORY"`  |
| Todo-en-uno | `=UPPER(TRIM(CLEAN(SUBSTITUTE(A2,"AND KITCHEN",""))))`  | Limpieza completa  |

💡 Mentalidad clave: no limpies manualmente; diseña el proceso una vez y reutilízalo.

Plantilla reutilizable: 
- crea una hoja formuleada, cada vez que aparece mas info en los datos crudos, la plantilla corrige todo de forma automática.
- Protege las hojas para hacer la plantilla a prueba de errores: clic derecho > Proteger hoja
<br><br>

Quality Assurance checks (Control de Calidad)
- Nombrar rangos: seleccionar rango > Data > Named ranges > poner nombre
- Formato condicional: Seleccionar columna > Format > Conditional format rules
- Registrar cambios en la hoja README <br><br>

**Ejercicio** - Práctica aplicada
empresa Mi Che quiere conocer:  
Cual es la region con el mayor numero de ventas totales para todos los productos pertenecientes a dos unidades:  panadería y snacks
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/15TfduxFqRFtP0uv7OR2w8aOmczq5Qb-f/edit?usp=sharing&ouid=105341058430000280825&rtpof=true&sd=true
- Ejercicio resuelto (cualquier persona de TT puede ver): 

### C2 - Lección 5: Cómo usar LLMs para fórmulas y errores en hojas de cálculo

Detectar errores comunes en las fórmulas (#N/A, #NUM, #VALUE!).
- `#VALUE!`: cuando intentas operar con rangos incompatibles, tipos de dato distintos o inexistentes.
- `#N/A`: cuando la búsqueda no encuentra coincidencias.
- `#NUM!`: cuando una referencia apunta a una celda/columna fuera de Rango.<br><br>

El LLM ayuda a corregir problemas como fórmulas rotas o mejorar formulas existentes. Para ello, hay que redactar prompts claros para que el LLM corrija correctamente. Por ejemplo, en ChatGPT escribir un buen prompt e incluir: 
- una explicación detallada de tu problema
- la fórmula que estás usando
- los detalles del error que aparece o mejora que se desea hacer <br><br>

Documentar la causa y la solución en README
- crea un rastro de conocimiento
- sirven de guía y referencia: muestran cómo se planteó el problema, contexto y solución de la IA


<br><br><br>

---
## Capitulo 3: Resumir datos con funciones y filtros
### C3 - Lección 1: Filtrar y explorar patrones en los datos

💡 Un **filtro** permite mostrar solo las filas que cumplen con ciertos criterios que tú defines. Todo lo demás se oculta, lo que ayuda a ver patrones y tendencias mucho más rápido.
- Todos los datos deben de tener encabezados, es decir, nombres para cada columna.
- Activar filtro: Clic en tabla > Clic en el icono de embudo o filtro en la barra de herramientas
- Aparece un ícono junto a cada encabezado. Haz clic en el de la columna que quieras filtrar
- Desmarca Seleccionar todo y 
    - marca únicamente la categoría de interés
    - filtra por condición, por ejemplo un rango de fechas
Es posible filtrar diferentes columnas, para evaluar diferentes escenarios.
<br><br>

#### Visualizar patrones
Las visualizaciones dentro de la hoja nos permiten encontrar patrones de negocio de un vistazo.

- Mapas de Calor (Heatmaps): Asigna colores según los valores en tus datos
  - Seleccionar el rango > Menu Fórmato > Formato Condicional > Seleccionar Escala de Colores
- Barras de Datos (Stack Bar / Barras de Progreso en Celda): los gráficos en celdas (sparklines), rellenan las celdas con barras horizontales cuya longitud refleja el valor de cada dato.
  - Sintaxis: `SPARKLINE(datos, [opciones])`. 
  - Ejemplo: Gráfico de barras con color y tamaño `=SPARKLINE(A1:A10, {"charttype","bar"; "color","blue"; "max",100})`  
    - `"max",100` → define el valor máximo de referencia, se toma el valor 100 como tope para escalar todas las barras proporcionalmente.
  
    Tipos de graficos:
    - Línea `{"charttype","line"}`
    - Barra	`{"charttype","bar"}`
    - Columna `{"charttype","column"}`
    - Win/Loss `{"charttype","winloss"}`
<br><br>

**Ejercicio** - Práctica Individual - Ventas por producto en una región específica - Ventas Cafetería
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1jNrlAoN4UCTcI_V7T7w1DHCwAgb2Er83bgHi6gESmuI/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1_YXQIyEoD-iwwTpp5xiqiZtAJpFg9_D9w7EPpVazdts/edit?usp=sharing <br><br>
💡 Pistas:
- Pregunta 1: menú de filtro > Filtrar por condición > Texto contiene "01/2024"
- Ejercicio 1: menú de filtro > Filtrar por condición > Valores entre "01/04/2024" y "30/06/2024"
- Ejercicio 2: menú de filtro > Filtrar por condición > Mayor a (Greater than) 65
<br><br>
Recursos adicionales (Google Sheets)
- [Documentación oficial  Sparkline](https://support.google.com/docs/answer/3093289?hl=es) <br><br>

### C3 - Lección 2: Funciones condicionales

Las funciones de agregación condicional te permiten sumar, contar o promediar valores solo si estos cumplen con una o más condiciones.
- `SUMIF` (SUMAR.SI): Suma si se cumple una condición
  - Sintaxis: `=SUMIF(rango_criterio, criterio, [rango_suma])`
    - rango criterio: columna donde está el elemento a buscar
    - criterio: lo que estamos buscando
    - rango_suma (opcional): la columna de los que queremos sumar, si no se especifica, toma "rango criterio"
  - Ejemplo: `=SUMIF(A2:A6, "Café*", B2:B6)`
    - El asterisco se usa como comodín, la fórmula sumará cualquier producto que empiece con la palabra `Café`.

- `COUNTIF` (CONTAR.SI): Cuenta si se cumple una condición
  - Sintaxis: `=COUNTIF(rango, criterio)`
    - rango: columna donde vamos a buscar
    - criterio: lo que queremos contar
  - Ejemplo: `=COUNTIF(C:C, "Té Verde")`
  - Ejemplo: `=COUNTIF(A:A,">18")` la condición van entre comillas

- `AVERAGEIF` (PROMEDIO.SI): Promedio si se cumple una condición
  - Sintaxis: `= AVERAGEIF(rango_criterio, criterio, [rango_promedio]))`    
    - rango criterio: columna donde está el elemento a buscar
    - criterio: lo que estamos buscando
    - rango_promedio (opcional): la columna de los que queremos promediar, si no se especifica, toma "rango criterio"
  - Ejemplo: `= AVERAGEIF(C:C, "Café Clásico", G:G)`   
<br><br>

Referencias en fórmulas  
**Referencia relativa**: Cuando copias o arrastras una fórmula hacia otras celdas, las referencias cambian automáticamente, ajusta la fórmula a la nueva posición.
- Ejemplo: si tienes `=A2+B2` en la fila 2 y la copias a la fila 3, automáticamente se convierte en `=A3+B3`.
Para que la referencia no cambie, se necesitan **referencias absolutas**.

👉 Referencia relativa (dinámica): `A2` → se adapta al mover la fórmula (`A3`, `A4`,…).  
👉 Referencia absoluta (fija): 
- `$A$2` → siempre apunta exactamente a la celda `A2`.
- `$A2` → fija la columna `A`, pero la fila cambia.
- `A$2` → fija la fila `2`, pero la columna cambia. <br><br>

💡 TIP: En Google Sheets, el atajo para fijar una celda o rango (poner los $ para referencias absolutas):
- Windows: F4
- Mac: ⌘ + T  
Cada vez que presionas el atajo mientras editas una referencia, va ciclando entre:
  - `A2` → relativo
  - `$A$2` → columna y fila fijas
  - `A$2` → fila fija
  - `$A2` → columna fija 

**Ejercicio** - Práctica Guiada: 
- Ejercicio sin resolver - mismo que lección anterior (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1jNrlAoN4UCTcI_V7T7w1DHCwAgb2Er83bgHi6gESmuI/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): <br><br>

Recursos adicionales (Google Sheets)
- [SUMAR.SI (SUMIF)](https://support.google.com/docs/answer/3093583?hl=es)
  - más funciones, en misma página, barra de la derecha
- [CONTAR.SI (COUNTIF)](https://support.google.com/docs/answer/3093480?hl=es)
- [PROMEDIO.SI (AVERAGEIF)](https://support.google.com/docs/answer/3256529?hl=es-419) <br><br><br>
  
### C3 - Lección 3: Identificar datos “sucios”
Los registros suelen venir con errores de entrada, duplicados, valores fuera de rango o categorías mal escritas.

- **Duplicados**: registros que aparecen más de una vez en un conjunto de datos. Aparecen por errores de entrada, fallas en la importación o problemas en la recolección de datos.
  - Por ejemplo: `=COUNTIF($A$2:$A$100, A2) > 1` → cuenta cuántas veces aparece el valor de la celda A2 dentro del rango de A2 a A100. Importante: usa referencias absolutas en el rango para poder arrastrar la fórmula.
- **Outliers** o valores atípicos: dato que se aleja considerablemente del resto de valores. Aparecen porque alguien cometió un error al registrar la información o porque realmente hubo un evento poco común.
  - Es importante detectarlos? Porque pueden distorsionar los cálculos como el promedio.<br><br>

Encontrar Valores duplicados y outliers  
El formato condicional también permite cambiar el color de las celdas o del texto automáticamente si cumplen una condición.
- Seleccionar columna > Formato (Format) > Formato condicional (Conditional formatting)
- Escribir la fórmula: 
  - Resaltar valores duplicados: “La fórmula personalizada es” > `=COUNTIF($A$2:$A$101, A2) > 1`
  - Resaltar valores atípicos: “Mayor que” > escribir número sin sentido
- Selecciona un color de relleno

Valores inconsistentes o inesperados  
Datos que no coinciden con las categorías definidas  
Ejemplo, tenemos unicamente 4 regiones: Norte, Sur, Este y Oeste.  
Regla que resalte cualquier otro valor:
- Seleccionar columna > Formato (Format) > Formato condicional (Conditional formatting)
- “La fórmula personalizada es” > `=AND($E$2:$E$101<>"Sur", $E$2:$E$101<>"Norte", $E$2:$E$101<>"Este", $E$2:$E$101<>"Oeste")`
  - Si una celda en esta columna no es Sur y no es Norte y no es Este y no es Oeste, entonces márcala como error.
  - usamos el signo de pesos para indicar referencias absolutas <br><br>

**Ejercicio** Práctica guiada - Ejercicio 1: Valores Extremos - Ventas Cafetería   
**Ejercicio** Práctica Aplicada - Ejercicio 1: Análisis de datos y detección de errores  
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1jNrlAoN4UCTcI_V7T7w1DHCwAgb2Er83bgHi6gESmuI/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1K_Kplc2xCtL0pYZnQiTEW1IrJqBmscEK5sXD07M0ys4/edit?usp=sharing
  - Valor no esta entre (Is not between) 0 y 180.
  - Fórmula personalizada: `=AND($D$2:$D$101<>"Té", $D$2:$D$101<>"Café", $D$2:$D$101<>"Jugo")` <br><br>

### C3 - Lección 4: Comparar segmentos con múltiples condiciones

Funciones de agregación condicional con múltiples condiciones  
- `SUMIFS` (SUMAR.SI.CONJUNTO): Suma si se cumplen múltiples condiciones:
  - Sintaxis: `SUMAR.SI.CONJUNTO(rango_suma; rango_criterios1; criterios1; [rango_criterios2; criterios2];...)`
  - Ejemplo: `SUMAR.SI.CONJUNTO(A2:A9;B2:B9;"=A*";C2:C9;"Juan")`

- `COUNTIFS` (CONTAR.SI.CONJUNTO)   
  - Sintaxis: `CONTAR.SI.CONJUNTO(rango_criterios1; criterios1; [rango_criterios2; criterios2];…)`
    - Ejemplo: `=CONTAR.SI.CONJUNTO(B:B;"=Sí"; D:D;"=Sí")`

-  `AVERAGEIFS` (PROMEDIO.SI.CONJUNTO):
   - Sintaxis: `PROMEDIO.SI.CONJUNTO(rango_promedio; rango_criterio1; criterio1; [rango_criterio2; criterio2]; ...)`
   - Ejemplo: `=PROMEDIO.SI.CONJUNTO(B2:B;B2:B;">=70";B2:B;"<=90")`
<br><br>

Tablas de resumen usando funciones
Ejemplo: 
- En las filas, los productos (Café Clásico, Café con Leche, Té Verde).
- En las columnas, las regiones (Norte, Sur, Oeste, Este).

Fórmula `=SUMIFS($G:$G, $C:$C, $J5, $E:$E, K$4)`
- `$G:$G` → Ventas Totales
- `$C:$C` → Productos
- `$J5` → fijamos columna J (productos) pero dejamos libre la fila, para poder arrastrar hacia abajo y cambiar el producto.
- `$E:$E` → Región
- `K$4` → fijamos la fila 4 (regiones) pero dejamos libre la columna, para poder arrastrar hacia la derecha y cambiar la región

Arrastrar la fórmula hacia la derecha, cambiará automáticamente la región.
Arrastrar hacia abajo, cambiará automáticamente el producto.
<br>

Ventas Totales
| Producto        | Norte | Sur   | Oeste | Este  |
|-----------------|-------|-------|-------|-------|
| Café Clásico    | 575   | 462.5 | 250   | 237.5 |
| Café con Leche  | 345   | 270   | 510   | 460   |
| Té Verde        | 0     | 80    | 0     | 705   |
<br><br>

¿Cuándo usar SUMIFS/COUNTIFS/AVERAGEIFS ?
![alt text](image.png)

**Ejercicio** - Ejercicio 1: Ventas por Región y Tipo de Producto
- Ejercicio sin resolver (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1m_xfKbcCZTkbyT-dBRqYfo7t4j_MucMphzmczh7QBaM/edit?usp=sharing
- Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1OqVf7HiqEXVACEp_57nGmHW3BAMXCesnRRzN_8ph0qo/edit?usp=sharing <br><br>

Recursos adicionales
- `SUMIFS` (SUMAR.SI.CONJUNTO):
  - [Google Sheets](https://support.google.com/docs/answer/3238496?hl=es)
  - [Microsoft Excel](https://support.microsoft.com/es-es/office/funci%C3%B3n-sumar-si-conjunto-c9e748f5-7ea7-455d-9406-611cebce642b)
- `COUNTIFS` (CONTAR.SI.CONJUNTO)
  - [Google Sheets](https://support.google.com/docs/answer/3256550?hl=es)
  - [Microsoft Excel](https://support.microsoft.com/es-es/office/funci%C3%B3n-contar-si-conjunto-dda3dc6e-f74e-4aee-88bc-aa8c2a866842)
- `AVERAGEIFS` (PROMEDIO.SI.CONJUNTO)
  - [Google Sheets](https://support.google.com/docs/answer/3256534?hl=es)
  - [Microsoft Excel](https://support.microsoft.com/es-es/office/funci%C3%B3n-promedio-si-conjunto-48910c45-1fc0-4389-a028-f7c5c3001690)
<br><br><br>

### C3 - Lección 5: Hojas resumen con métricas clave 
<br><br><br>

---
## Capitulo 4: Analizar datos con tablas dinámicas
### C4 - Lección :
<br><br><br>

---
## Capitulo 5: Visualizar y destacar hallazgos clave
### C5 - Lección :


**Ejercicio** - 
- Ejercicio sin resolver (cualquier persona con el link puede ver):
- Ejercicio resuelto (cualquier persona de TT puede ver): <br><br>