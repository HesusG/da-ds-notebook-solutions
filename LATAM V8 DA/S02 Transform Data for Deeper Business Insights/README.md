# Sprint 2: Transform Data for Deeper Business Insights: Project
## ESP: Transformar datos para insights de negocio
📅 Fecha de actualización: 20 Octubre 2025

💻 Herramienta: Google Sheets o Excel

✅ El proyecto tiene plantilla o precodigo para el estudiante.

### Descripción del proyecto
---
**Proyecto 2: Resumen Ejecutivo de Ventas Walmart**

Imagina que eres analista en Walmart: la Dirección Comercial necesita un resumen ejecutivo para decidir determinados ajustes de presupuesto e inventario.
---
- Plantilla inicial de Proyecto (cualquier persona con el link puede ver): https://docs.google.com/spreadsheets/d/1PlqJH8t5q_Jwpf8K4mBEXnPUY3cyywAJ/edit?usp=sharing&ouid=105341058430000280825&rtpof=true&sd=true
- Proyecto resuelto (cualquier persona de TT puede ver): https://docs.google.com/spreadsheets/d/1B4PHq1kNPAwRc1z0U_q78TmH6dpSl8bU/edit?usp=sharing&ouid=105341058430000280825&rtpof=true&sd=true <br><br><br>

- Instrucciones (link a plataforma): https://tripleten.com/trainer/data-analyst/lesson/a979922b-959c-4720-9896-aa53ffe20c00/
- Información: https://coding-bootcamps.notion.site/6-Proyecto-2-Resumen-Ejecutivo-de-Ventas-Walmart-26b6ed1efc93804e93befda4d68f7c21
- Criterios de evaluación: https://coding-bootcamps.notion.site/Grading-Rubric-26b6ed1efc9381fa92a3ecf51f7c0e9b


## 💡 Tips
_Para los primeros pasos, basta con seguir las instrucciones del Sprint, para los siguientes, aquí unos consejos._

### Parte 3: Resumen con tablas dinámicas
#### Dinamica kpi 1

- En el campo calculado creado Ventas por m² ($/m²) poner este tipo de formato personalizado para que el resultado se vea mucho más profesional $"#,##0.00"/m²
<br><br>

### Parte 4: Dashboard
#### Formula para traer el campo Ventas x metro
```
=SI.ERROR(
  TEXTO(
    INDICE(pivot_kpi1!$D:$D; COINCIDIR($B$2; pivot_kpi1!$A:$A; 0));
    "$ #,##0.00" 
       ) 
    & " /m²";
    "—"
)
```

#### Formula para traer el campo Participación del depto
```
=SI.ERROR(
  TEXTO(
    INDICE(pivot_kpi2!$B:$B; COINCIDIR($B$2; pivot_kpi2!$A:$A; 0));
    "0.00%"
  );
 "—"
)
```

#### Formula para traer el campo KPI Volatilidad
```
=IFERROR(
  TEXT(
    INDEX(pivot_kpi3!$E:$E, MATCH($B$2, pivot_kpi3!$A:$A, 0)),
    "0.00"
  ),
 "—"
)
```