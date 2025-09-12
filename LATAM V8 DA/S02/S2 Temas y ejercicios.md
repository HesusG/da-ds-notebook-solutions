# Sprint 2: Transformar datos para insights de negocio
🗓️ Fecha de creación: 10 septiembre 2025  
🗓️ Fecha de actualización: 11 septiembre 2025<br><br>

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
- [ventas_1000.csv](https://drive.google.com/file/d/1EMjltVRbWv5I7n0X_Tpw838iFK7jJfsm/view?usp=sharing)
- a
- a

Ejercicio resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1PIpZZkcKfjuAOgc57aW1derL2EOCPGcltrV3jDyEVek/edit?usp=sharing

No se han visto las tablas dinámicas, para responder el cuestionario, se pueden usar filtros. <br><br>

Recursos adicionales
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

### C2 - Lección 5:
<br><br><br>

---
## Capitulo 3: Resumir datos con funciones y filtros
### C3 - Lección :
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
- Ejercicio resuelto (cualquier persona de TT puede ver): 