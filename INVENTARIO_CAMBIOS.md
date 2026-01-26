# Inventario de Cambios - Repositorio projects-da-ds

## Fecha: 2026-01-24
## Branch: assesment-criteria

---

## Estado del Repositorio

### Resumen General
| Categoría | Cantidad | Notas |
|-----------|----------|-------|
| Total Notebooks | 121 | LATAM V7: 76, LATAM V8: 3, Brasil: 31 |
| Con Colab Badge | 5 | 4.1% del total |
| Criterios.md | 17+ | Solo en LATAM V7, ninguno en Brasil |
| Datasets S3 Yandex | 38 únicos | `code.s3.yandex.net/datasets/` |

---

## Cambios Realizados

### 1. Corrección de Naming de Carpetas

| Ruta Original | Ruta Nueva | Status |
|---------------|------------|--------|
| `LATAM V7 DADS/9-14 DA/SP 9 Business Analytics` | `SP9 Business Analytics` | [x] Completado |
| `LATAM V7 DADS/9-14 DA/SP 9 Deprecated - How to Tell a Story Using Data` | `SP9 Deprecated - How to Tell a Story Using Data` | [x] Completado |
| `LATAM V7 DADS/9-18 DS/SP 9 - Introduction to ML - Megaline` | `SP9 Introduction to ML - Megaline` | [x] Completado |
| `LATAM V7 DADS/9-18 DS/SP13 - Linear Algebra - Insurance` | `SP13 Linear Algebra - Insurance` | [x] Completado |

### 2. Archivos Eliminados

| Archivo/Carpeta | Razón | Status |
|-----------------|-------|--------|
| `SP5 Statistical Data Analysis - Megaline/Reviewers_Asessment_Criteria/` | Duplicado con typo ("Asessment" vs "Assesment") | [x] Completado |

### 3. Archivos Movidos

| Archivo | Origen | Destino | Status |
|---------|--------|---------|--------|
| `S16 ESP SOL3 Aprendizaje textos - Análisis sentimiento-COLAB.ipynb` | `SP16 Machine Learning for Texts/` (raíz) | `SP16 Machine Learning for Texts/P Spanish version/` | [x] Completado |

### 4. Criterios.md Renombrados

| Ruta | Nombre Original | Nombre Nuevo | Status |
|------|-----------------|--------------|--------|
| `9-14 DA/SP10 Making Business Decisions Based on Data/Reviewers_Assesment_Criteria/` | `criterios_DA_10_ab_test.md` | `criterios.md` | [x] Completado |
| `9-14 DA/SP11 Integrated Project 2/Reviewers_Assesment_Criteria/` | `criterios_DA_11_proyecto_integrado_2.md` | `criterios.md` | [x] Completado |

---

## Comparación LATAM V7 vs Brasil

### Estructura de Sprints

| Track | LATAM V7 | Brasil | Diferencia |
|-------|----------|--------|------------|
| DA_DS Base | SP1-SP8 (8 sprints) | SP1-SP7 (7 sprints) | Brasil tiene 1 menos |
| DA Avanzado | SP9-SP14 (6 sprints) | SP8-SP14 (7 sprints) | Numeración diferente |
| DS Avanzado | SP9-SP18 (10 sprints) | SP8-SP17 (9 sprints) | Brasil falta SP16 (ML Textos) |

### Criterios.md por Región

| Track | LATAM V7 ESP | LATAM V7 EN | Brasil |
|-------|--------------|-------------|--------|
| SP1-SP8 | 8 archivos | - | 0 archivos |
| SP9-SP14 DA | 4 archivos | - | 0 archivos |
| SP9-SP18 DS | 9 archivos | - | 0 archivos |
| **Total** | **21** | **0** | **0** |

### Sprint Faltante en Brasil DS
- **SP16 Machine Learning for Texts** (Análisis de Sentimiento con BERT)
- Contenido: TF-IDF, spaCy lemmatization, BERT embeddings, clasificación de reseñas IMDB

---

## Notebooks con Colab Badge

### Ya Implementados (5)
| Notebook | Sprint | Idioma |
|----------|--------|--------|
| S3 EN SOLV Let_me_hear_the_Music.ipynb | SP3 | English |
| S16 ESP SOL3 Aprendizaje textos - COLAB.ipynb | SP16 | Spanish |
| S17 ESP SOL3 Vision artificial - Colab GPU.ipynb | SP17 | Spanish |
| S18 ESP SOL Proyecto_final.ipynb | SP18 | Spanish |
| S18 ESP SOL2 Proyecto final.ipynb | SP18 | Spanish |

### Pendientes (116)
- Todos los notebooks de LATAM V8 DA (3)
- Todos los notebooks de Brasil (31)
- Mayoría de notebooks LATAM V7 (71)

### Prioridad para Colab Badge
1. Notebooks SOLV/SOL de sprints con datasets grandes
2. SP5 (Megaline - 5 CSVs)
3. SP6 (Games)
4. SP9-SP15 DS (modelos ML)

---

## URLs de Datasets

### S3 Yandex (Fuente Principal)
Base URL: `https://code.s3.yandex.net/datasets/`

| Dataset | Sprints que lo usan |
|---------|---------------------|
| megaline_*.csv (5 archivos) | SP5, SP9 DS |
| games.csv | SP6 |
| taxi.csv | SP8, SP15 DS |
| Churn.csv | SP10 DS |
| geo_data_*.csv (3 archivos) | SP11 DS |
| gold_recovery_*.csv (3 archivos) | SP12 DS |
| insurance_us.csv | SP13 DS |
| car_data.csv, autos.csv | SP14 DS |
| imdb_reviews.tsv | SP16 DS |

### GitHub Releases (Alternativa para Colab)
| Release | Dataset | Notebook |
|---------|---------|----------|
| `imdb` | imdb_reviews.csv | SP16 SOL3 COLAB |
| `faces` | faces.zip | SP17 SOL3 COLAB |

---

## Cambios Pendientes para Brasil

### Fase 1: Crear Criterios.md Básicos
Basarse en los criterios de LATAM V7 y traducir/adaptar:

| Sprint Brasil | Basarse en | Prioridad |
|---------------|------------|-----------|
| SP1-SP7 | LATAM V7 SP1-SP8 | Alta |
| SP8-SP14 DA | LATAM V7 SP9-SP14 DA | Media |
| SP8-SP17 DS | LATAM V7 SP9-SP18 DS | Media |

### Fase 2: Agregar Sprint Faltante
- Crear SP16 en Brasil DS (Aprendizado Automático para Textos)
- Traducir notebook de LATAM V7 SP16 a portugués

---

## Historial de Actualizaciones

| Fecha | Cambio | Autor |
|-------|--------|-------|
| 2026-01-24 | Creación del documento de inventario | Claude |
| 2026-01-24 | Renombrado carpetas SP 9 → SP9 (3 carpetas) | Claude |
| 2026-01-24 | Renombrado SP13 - → SP13 (1 carpeta) | Claude |
| 2026-01-24 | Eliminada carpeta duplicada SP5/Reviewers_Asessment_Criteria | Claude |
| 2026-01-24 | Movido S16 COLAB notebook a P Spanish version | Claude |
| 2026-01-24 | Renombrados criterios SP10 DA y SP11 DA a criterios.md | Claude |

---

## Notas Adicionales

### Archivos .py en SP17 English
Existen archivos Python (.py) en `SP17/P English version/`:
- P16_0.py, P16_1.py, P16_2.py, P16_3.py
- Revisar si son scripts auxiliares o deben convertirse a notebooks

### AWS RDS (Solo para SQL)
- Host: `yp-trainers-practicum.cluster-czs0gxyx2d8w.us-east-1.rds.amazonaws.com`
- Uso: Base de datos para proyectos SQL (SP8, SP14 DA)
- No es almacenamiento de datasets
