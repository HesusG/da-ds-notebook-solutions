# Comparar Soluciones

Compara múltiples archivos de solución (SOL) para identificar diferencias, fortalezas y errores únicos de cada uno.

## Instrucciones

1. **Identifica los notebooks a comparar** a partir del argumento: $ARGUMENTS
   - Pueden ser 2 o más notebooks SOL del mismo sprint

2. **Lee cada notebook completamente** y documenta:
   - Estructura general (secciones, orden)
   - Técnicas utilizadas
   - Enfoques de limpieza de datos
   - Métodos de análisis
   - Visualizaciones creadas
   - Conclusiones alcanzadas

3. **Genera un reporte de comparación:**

```markdown
# Comparación de Soluciones: [Sprint]

## Resumen

| Aspecto | SOL1/SOLV | SOL2 |
|---------|-----------|------|
| Estructura | [descripción] | [descripción] |
| Enfoque principal | [descripción] | [descripción] |
| Fortaleza principal | [descripción] | [descripción] |
| Debilidad principal | [descripción] | [descripción] |

## Diferencias en Preparación de Datos

### Manejo de Valores Ausentes
- **SOLV**: [enfoque usado]
- **SOL2**: [enfoque usado]
- **Mejor práctica**: [cuál es preferible y por qué]

### Detección de Duplicados
- **SOLV**: [enfoque usado]
- **SOL2**: [enfoque usado]
- **Mejor práctica**: [recomendación]

### Conversión de Tipos
- **SOLV**: [enfoque usado]
- **SOL2**: [enfoque usado]
- **Mejor práctica**: [recomendación]

## Diferencias en Análisis

### [Tipo de análisis 1]
- **SOLV**: [metodología]
- **SOL2**: [metodología]
- **Mejor práctica**: [recomendación]

### [Tipo de análisis 2]
[...]

## Diferencias en Visualizaciones

| Visualización | SOLV | SOL2 | Preferida |
|--------------|------|------|-----------|
| [tipo] | [descripción] | [descripción] | [cuál y por qué] |

## Errores Conceptuales Únicos

### En SOLV
1. [Error identificado] - [Impacto] - [Corrección]

### En SOL2
1. [Error identificado] - [Impacto] - [Corrección]

### Comunes a Ambos
1. [Error compartido] - [Impacto] - [Corrección]

## Buenas Prácticas a Adoptar

### De SOLV
- [Práctica 1]: [por qué es buena]
- [Práctica 2]: [por qué es buena]

### De SOL2
- [Práctica 1]: [por qué es buena]
- [Práctica 2]: [por qué es buena]

## Conclusiones de la Comparación

### Aspectos para la Solución de Referencia
1. Adoptar de SOLV: [lista]
2. Adoptar de SOL2: [lista]
3. Mejorar en ambos: [lista]

### Recomendación para Criterios de Evaluación
- [Qué criterios agregar basado en esta comparación]
- [Qué errores frecuentes documentar]
```

4. **Casos especiales:**

### SP5 y SP6 (Soluciones Alternativas)
- Comparar enfoques metodológicos
- Identificar si ambos llegan a conclusiones similares
- Evaluar claridad pedagógica de cada uno

### SP8 (Soluciones Secuenciales)
- SOL1 y SOL2 son partes de un todo
- Evaluar continuidad entre partes
- Verificar que la transición es lógica

5. **Guarda el reporte** en:
   `{Sprint}/local-assets/comparacion-soluciones.md`

## Notas Importantes

- Ser objetivo en la comparación
- No hay "ganador" - identificar lo mejor de cada uno
- El objetivo es crear una solución de referencia superior
- Documentar errores sin juicio, con foco en mejora
