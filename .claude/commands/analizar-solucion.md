# Analizar Solución de Notebook

Analiza el notebook de solución especificado para identificar errores conceptuales y evaluar la calidad del código.

## Instrucciones

1. **Lee el notebook completo** especificado por el usuario (ruta proporcionada como argumento: $ARGUMENTS)

2. **Identifica la estructura del notebook:**
   - Secciones de markdown (títulos, explicaciones)
   - Celdas de código (imports, procesamiento, análisis)
   - Visualizaciones generadas
   - Conclusiones presentadas

3. **Evalúa errores conceptuales en estas categorías:**

### Errores Estadísticos
- [ ] ¿Se seleccionó la prueba estadística correcta?
- [ ] ¿Se interpretó correctamente el valor-p?
- [ ] ¿Se definió apropiadamente el nivel de significancia (alpha)?
- [ ] ¿Se confundió correlación con causalidad?
- [ ] ¿Se verificó el tamaño de muestra antes de concluir?

### Errores de Manejo de Datos
- [ ] ¿Se eliminaron datos sin justificación?
- [ ] ¿Se usó imputación contextual (por grupo) vs global?
- [ ] ¿Se convirtieron los tipos de datos correctamente?
- [ ] ¿Se detectaron duplicados implícitos (variantes de texto)?
- [ ] ¿Se manejaron los valores NaN apropiadamente?

### Errores Metodológicos
- [ ] ¿Las agregaciones son correctas (sum/mean/count)?
- [ ] ¿El groupby tiene la lógica correcta?
- [ ] ¿Los merge/join están bien aplicados?
- [ ] ¿Se filtraron outliers con metodología documentada?

### Errores de Visualización
- [ ] ¿El tipo de gráfico es apropiado para los datos?
- [ ] ¿Las escalas son correctas y no engañosas?
- [ ] ¿Los gráficos tienen títulos y etiquetas?
- [ ] ¿Las comparaciones visuales son justas?

### Errores en Conclusiones
- [ ] ¿Las afirmaciones están respaldadas por datos?
- [ ] ¿Se evitó la generalización excesiva?
- [ ] ¿Se documentaron limitaciones?
- [ ] ¿Se distinguió significancia estadística de práctica?

4. **Genera un reporte estructurado:**

```markdown
# Análisis de Solución: [Nombre del Notebook]

## Resumen Ejecutivo
[Evaluación general en 2-3 oraciones]

## Errores Conceptuales Identificados

### Críticos (deben corregirse)
1. [Error] - [Línea/Celda] - [Impacto]

### Menores (recomendaciones)
1. [Mejora sugerida] - [Ubicación]

## Buenas Prácticas Observadas
- [Práctica positiva identificada]

## Calidad del Código
- Legibilidad: [Alta/Media/Baja]
- Documentación: [Alta/Media/Baja]
- Eficiencia: [Alta/Media/Baja]

## Validación Metodológica
[Evaluación de la metodología estadística/analítica]

## Recomendaciones
1. [Recomendación prioritaria]
```

5. **Guarda el reporte** en la carpeta `local-assets/` del sprint correspondiente como `analisis-{nombre-notebook}.md`
