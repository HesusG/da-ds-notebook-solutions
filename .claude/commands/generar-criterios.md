# Generar Criterios de Evaluación

Genera un archivo `criterios.md` completo para el sprint especificado, siguiendo la plantilla estándar.

## Instrucciones

1. **Identifica el sprint** a partir del argumento proporcionado: $ARGUMENTS

2. **Lee los notebooks de solución (SOL/SOLV)** del sprint para entender:
   - Objetivos de aprendizaje
   - Competencias requeridas
   - Pasos del análisis
   - Técnicas utilizadas
   - Resultados esperados

3. **Lee el notebook del estudiante** (si existe) para entender el punto de partida

4. **Genera el archivo criterios.md** con la siguiente estructura:

```markdown
# Criterios de Evaluación: [Nombre del Proyecto]

## Objetivo

[Descripción clara del objetivo en 2-3 oraciones]

**Requisitos previos**: [Conocimientos necesarios]

**Competencias que desarrollarás**: [Lista de competencias separadas por comas]

<details>
<summary>Task Statement</summary>

## Descripción del proyecto

[Contexto del proyecto - quién es el cliente, qué problema resuelve]

## Instrucciones del proyecto

1. **Prepara los datos:**
   - [Pasos de preparación específicos]

2. **Analiza los datos:**
   - [Pasos de análisis específicos]

3. **Genera conclusiones:**
   - [Qué debe contener la conclusión]

## Descripción de los datos

- `columna1` - descripción
- `columna2` - descripción
[...]

</details>

## Glosario de Términos Técnicos

**[Término 1]**: [Definición clara y concisa]

**[Término 2]**: [Definición clara y concisa]

[Incluir todos los términos técnicos relevantes al sprint]

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO

**[Categoría 1]**
- [ ] **[OBLIGATORIO]** [Criterio crítico]
- [ ] **[OBLIGATORIO]** [Criterio crítico]
- [ ] [Criterio adicional]

**[Categoría 2]**
- [ ] **[OBLIGATORIO]** [Criterio crítico]
- [ ] [Criterio adicional]

### INTERMEDIO

**[Categoría 1]**
- [ ] **[OBLIGATORIO]** [Criterio]
- [ ] [Criterio]

**[Categoría 2]**
- [ ] [Criterio]

### AVANZADO

**[Categoría 1]**
- [ ] **[OBLIGATORIO]** [Criterio de excelencia]
- [ ] [Criterio de excelencia]

**[Categoría 2]**
- [ ] [Criterio de excelencia]

## Criterios de Aprobación General

**Niveles de aprobación:**

- **BÁSICO (Aprobado mínimo)**:
  - Todos los criterios OBLIGATORIOS: X/X
  - Al menos Y criterios adicionales de los Z no obligatorios

- **INTERMEDIO (Aprobado satisfactorio)**:
  - Todos los criterios OBLIGATORIOS: X/X
  - Al menos Y criterios adicionales de los Z no obligatorios

- **AVANZADO (Aprobado con distinción)**:
  - Todos los criterios OBLIGATORIOS: X/X
  - Al menos Y criterios adicionales de los Z no obligatorios

## Ejemplos de Cumplimiento

**[Título del ejemplo]:**
```python
# Código de ejemplo que demuestra la buena práctica
[código]
```

**[Título del ejemplo 2]:**
```python
[código]
```

## Criterios de Descalificación

**Errores Críticos que descalifican automáticamente:**
- [Error crítico 1]
- [Error crítico 2]
- [...]

## Errores Frecuentes

*Esta sección identifica los errores más comunes observados en este proyecto.*

### [Categoría de Errores]

1. **[Nombre del error]**:
   - Incorrecto: `[código incorrecto]`
   - Correcto: `[código correcto]`
   - Consecuencia: [Qué pasa si se comete este error]

2. **[Nombre del error 2]**:
   - Incorrecto: [descripción]
   - Correcto: [descripción]
   - Consecuencia: [impacto]

[...]

**Formulario de Feedback**: [TBD - Google Form](enlace-por-definir)
```

5. **Guarda el archivo** en `{Sprint}/Reviewers_Assesment_Criteria/criterios.md`

## Notas Importantes

- Los criterios OBLIGATORIOS deben ser específicos y verificables
- Incluir ejemplos de código reales extraídos del notebook de solución
- Los errores frecuentes deben basarse en el análisis de las soluciones
- Mantener consistencia con el formato de SP4/criterios.md como referencia
