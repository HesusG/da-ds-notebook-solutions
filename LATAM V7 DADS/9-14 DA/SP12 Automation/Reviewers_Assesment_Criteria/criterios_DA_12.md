# Criterios de Evaluación: DA_12 - Dashboard Final en Tableau Public

> **ESTA ENTREGA NO ES EN UN NOTEBOOK**
> En esta entrega se espera la implementación técnica completa de un dashboard interactivo en Tableau Public.
> El dashboard debe ser funcional, estéticamente agradable y responder a preguntas de negocio sobre tendencias de video.

## Objetivo

Construir un dashboard interactivo que visualice la dinámica de los videos en tendencia en YouTube, permitiendo a los usuarios filtrar por fecha y país para obtener insights sobre categorías populares y distribución geográfica.

**Requisitos previos**: Conocimientos de Tableau Public (conexión de datos, creación de gráficos, dashboards, filtros, publicación).

**Competencias que desarrollarás**: Visualización de datos, diseño de dashboards interactivos, storytelling con datos, uso de filtros globales, publicación y distribución de reportes.

<details>
<summary>Requisitos del Entregable</summary>

## Contenido esperado del entregable

Para que tu entregable sea aprobado, deberás entregar un **enlace a un dashboard publicado en Tableau Public** que contenga:

### 1. Gráficos de Tendencias (Evolución Temporal)
- **Historial de tendencias (Área Apilada)**: Mostrar la evolución del número total de videos por categoría a lo largo del tiempo.
- **Historial de tendencias % (Área Apilada Normalizada)**: Mostrar la participación porcentual de cada categoría a lo largo del tiempo.

### 2. Gráficos de Distribución Geográfica
- **Trending by Country (Pie Chart)**: Mostrar la distribución total de videos por país.
- **Trending by Country and Category (Heatmap)**: Tabla de calor que cruce categorías (filas) y países (columnas) para mostrar la intensidad de videos.

### 3. Interactividad y Filtros
- **Filtro Global de Fecha-Hora**: Debe permitir seleccionar un rango de tiempo y afectar a **todos** los gráficos.
- **Filtro Global de País**: Debe permitir seleccionar uno o varios países y afectar a **todos** los gráficos.

### 4. Diseño y Accesibilidad
- **Layout organizado**: Los gráficos deben estar dispuestos de manera lógica (ej. temporales a la izquierda, geográficos a la derecha).
- **Títulos y Etiquetas**: Todo debe estar claramente etiquetado.
- **Alt-text**: El dashboard debe incluir un texto alternativo descriptivo para accesibilidad.

</details>

## Glosario de Términos Técnicos

**Dashboard**: Panel de control que combina múltiples visualizaciones en una sola vista para facilitar el análisis y la toma de decisiones.

**Filtro Global**: Filtro que se aplica a todas las hojas de trabajo (worksheets) dentro de un dashboard que comparten la misma fuente de datos.

**Área Apilada (Stacked Area)**: Gráfico que muestra la evolución de múltiples series a lo largo del tiempo, apiladas una sobre otra para mostrar el total.

**Heatmap (Mapa de Calor)**: Visualización tabular donde los valores se representan mediante colores de diferente intensidad.

**Tableau Public**: Plataforma gratuita para crear, publicar y compartir visualizaciones de datos en línea.

---

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO (10 criterios obligatorios)

**Componentes Visuales**
- [ ] **[OBLIGATORIO]** Incluye gráfico de Área Apilada (Total de videos por tiempo y categoría)
- [ ] **[OBLIGATORIO]** Incluye gráfico de Área Apilada % (Porcentaje por tiempo y categoría)
- [ ] **[OBLIGATORIO]** Incluye Pie Chart (Videos por país)
- [ ] **[OBLIGATORIO]** Incluye Heatmap (Categoría vs País)

**Interactividad**
- [ ] **[OBLIGATORIO]** Filtro de Fecha-Hora funciona globalmente (afecta a todos los gráficos)
- [ ] **[OBLIGATORIO]** Filtro de País funciona globalmente (afecta a todos los gráficos)

**Formato y Entrega**
- [ ] **[OBLIGATORIO]** El dashboard está publicado en Tableau Public
- [ ] **[OBLIGATORIO]** El enlace es accesible (visibilidad pública)
- [ ] **[OBLIGATORIO]** Incluye título claro ("Trending Videos Dashboard")
- [ ] **[OBLIGATORIO]** Incluye Alt-text descriptivo

### INTERMEDIO (6 criterios)

**Calidad Visual y Diseño**
- [ ] **[OBLIGATORIO]** Usa etiquetas de datos claras (porcentajes y totales en Pie Chart)
- [ ] **[OBLIGATORIO]** Los colores son consistentes entre gráficos (ej. misma leyenda para categorías)
- [ ] **[OBLIGATORIO]** El layout es ordenado (ej. 1200px ancho, alineación correcta)
- [ ] Usa tooltips informativos al pasar el mouse

**Configuración Avanzada**
- [ ] Configura correctamente el cálculo de tabla rápido (Percent of Total) para el gráfico 2
- [ ] El eje temporal muestra fecha y hora correctamente

### AVANZADO (4 criterios)

**Excelencia y Usabilidad**
- [ ] Diseño estético profesional (uso de espacios en blanco, fuentes legibles)
- [ ] Interactividad avanzada (ej. usar un gráfico como filtro para los demás)
- [ ] Tiempos de carga optimizados (no es excesivamente lento)
- [ ] Narrativa visual clara (el dashboard cuenta una historia)

---

## Criterios de Aprobación

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: 10/10
  - Al menos 1 criterio adicional de los 6 no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (incluye los 3 obligatorios de Intermedio)
  - Al menos 3 criterios adicionales de los 4 no obligatorios restantes

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: 13/13 (Básico + Intermedio)
  - Al menos 3 criterios de la sección AVANZADO

---

## Aspectos negativos a evitar en el entregable

- **Filtros rotos**: Filtros que solo afectan a un gráfico y no a todo el dashboard.
- **Gráficos ilegibles**: Demasiadas categorías en el Pie Chart sin agrupar, o etiquetas superpuestas.
- **Ejes incorrectos**: Usar fecha discreta en lugar de continua cuando se requiere ver la evolución detallada.
- **Falta de contexto**: No incluir títulos o leyendas que expliquen qué se está viendo.
- **Enlace privado**: Entregar un enlace que requiere login o no es público.

---
