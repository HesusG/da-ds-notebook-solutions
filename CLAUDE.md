# Instrucciones del Proyecto: LATAM Bootcamp Data Analytics & Data Science

## Descripción General

Este repositorio contiene el currículo del bootcamp de Data Analytics y Data Science para LATAM. Incluye notebooks de proyectos, soluciones, y criterios de evaluación para revisores.

## Estructura de Directorios

```
projects-da-ds/
├── LATAM V7 DADS/           # Versión 7 - Data Analyst & Data Scientist combinado
│   └── 1-8 DA_DS/           # Sprints 1-8
│       ├── SP1 Basic Python/
│       ├── SP2 Continue Python/
│       ├── SP3 Data Wrangling - Music/
│       ├── SP4 Continue Data Wrangling - Instacart/
│       ├── SP5 Statistical Data Analysis - Megaline/
│       ├── SP6 Integrated Project 1 - Games/
│       ├── SP7 Software Development Tools/
│       └── SP8 SQL - Taxis/
├── LATAM V8 DA/             # Versión 8 - Data Analyst
├── Brasil/                  # Versión para Brasil
└── soluciones_ds/           # Soluciones de Data Science
```

## Convenciones de Nombres

### Idiomas
- **ESP** = Español (versión principal para LATAM)
- **EN** = English (versión en inglés)

### Tipos de Archivos
- **Sin sufijo** = Notebook del estudiante (proyecto base)
- **SOLV** = Solución verificada (principal)
- **SOL1/SOL2** = Soluciones alternativas o secuenciales
- **P** = Prefijo para carpetas de versión por idioma

### Estructura por Sprint
```
SP{N} {Nombre}/
├── P English version/
│   ├── S{N} EN {nombre}.ipynb          # Proyecto estudiante
│   └── S{N} EN SOLV {nombre}.ipynb     # Solución
├── P Spanish version/
│   ├── S{N} ESP {nombre}.ipynb         # Proyecto estudiante
│   └── S{N} ESP SOLV {nombre}.ipynb    # Solución
├── Reviewers_Assesment_Criteria/
│   └── criterios.md                     # Criterios de evaluación
├── local-assets/                        # Assets locales (scripts gitignored, SVGs tracked)
│   ├── generate_svgs.py                 # Script generador (gitignored)
│   └── svg*.svg                         # Visualizaciones de referencia
└── datasets/                            # Datos (gitignored)
```

## Guía para Criterios de Evaluación (criterios.md)

### Estructura Requerida

```markdown
# Criterios de Evaluación: {Nombre del Proyecto}

## Objetivo
[Descripción clara del objetivo de aprendizaje]

## Descripción del Proyecto
<details>
<summary>Task Statement</summary>
[Instrucciones detalladas del proyecto]
</details>

## Glosario de Términos Técnicos
[Definiciones de conceptos clave]

## Rúbrica de Evaluación - Checklist para Revisores

### BÁSICO
[Criterios mínimos - marcados con [OBLIGATORIO]]

### INTERMEDIO
[Criterios de nivel medio]

### AVANZADO
[Criterios de excelencia]

## Criterios de Aprobación General
[Niveles de aprobación: Básico, Intermedio, Avanzado]

## Ejemplos de Cumplimiento
[Código de ejemplo que demuestra buenas prácticas]

## Criterios de Descalificación
[Errores críticos que descalifican automáticamente]

## Errores Frecuentes
[Errores comunes identificados con explicación de:
- Qué es incorrecto
- Qué es correcto
- Consecuencia del error]
```

## Directrices para Identificación de Errores Conceptuales

### Categorías de Errores

1. **Errores Estadísticos**
   - Selección incorrecta de prueba estadística
   - Interpretación errónea del valor-p
   - Confusión entre correlación y causalidad
   - Nivel de significancia mal aplicado

2. **Errores de Manejo de Datos**
   - Eliminación masiva de datos sin justificación
   - Imputación sin contexto (usar media global vs. por grupo)
   - Conversión de tipos incorrecta
   - No detectar/tratar duplicados implícitos

3. **Errores Metodológicos**
   - Agregaciones incorrectas (sum vs mean vs count)
   - GroupBy con lógica equivocada
   - Merge/Join incorrecto de tablas
   - No verificar tamaño de muestra antes de conclusiones

4. **Errores de Visualización**
   - Tipo de gráfico inapropiado para los datos
   - Escalas engañosas
   - Falta de etiquetas o títulos
   - Comparaciones visuales injustas

5. **Errores en Conclusiones**
   - Afirmaciones no respaldadas por datos
   - Generalización excesiva
   - Omisión de limitaciones
   - Confundir significancia estadística con práctica

## Sprints con Múltiples Soluciones

| Sprint | Archivos SOL | Tipo |
|--------|-------------|------|
| SP5 | SOLV + SOL2 | Alternativas (diferentes enfoques) |
| SP6 | SOLV + SOL2 | Alternativas (diferentes enfoques) |
| SP8 | SOL1 + SOL2 | Secuenciales (partes 1 y 2) |

Para estos sprints, la solución de referencia debe combinar las mejores prácticas de ambos archivos.

## Comandos de Claude Disponibles

- `/analizar-solucion` - Analiza un notebook SOL para errores conceptuales
- `/generar-criterios` - Genera archivo criterios.md de evaluación
- `/crear-solucion-referencia` - Crea solución de referencia en local-assets
- `/comparar-soluciones` - Compara múltiples archivos SOL
