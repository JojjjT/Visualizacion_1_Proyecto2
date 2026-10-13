# Proyecto 2 — Visualización reproducible en Python

**Curso:** Visualización I · Quinto Semestre 2026 · Universidad Externado de Colombia
**Docentes:** Adriana Pineda – Paola Moreno
**Herramienta principal:** Python (Seaborn y Plotly)
**Fecha máxima de entrega:** lunes 26 de octubre de 2026, 11:59 p.m.
**Peso en la nota final:** 20 %

## Objetivo

Análisis exploratorio reproducible con Python sobre el **World Happiness Report 2024**,
comunicando hallazgos mediante visualizaciones estáticas (Seaborn) e interactivas (Plotly).

## Estructura del proyecto

```
Proyecto_2/
├── 00_Instrucciones_Proyecto_2.pdf      ← enunciado oficial
├── 01_datos_originales/
│   └── WHR24_Data_Figure_2.1.xls        ← fuente oficial descargada (NO modificar)
├── 02_notebook/
│   └── EquipoX_Proyecto2_Analisis.ipynb ← notebook principal (por crear)
├── 03_entregables/
│   ├── EquipoX_Proyecto2_Notebook.ipynb
│   ├── EquipoX_Proyecto2_Interactivos.html
│   ├── EquipoX_Proyecto2_Informe.pdf    (máx. 3 páginas)
│   └── EquipoX_Proyecto2_Anexo_IA.pdf   (máx. 1 página)
├── 04_recursos/                         ← paletas, imágenes, plantillas
└── README.md                            ← este archivo
```

## Requisitos clave (checklist)

### Notebook
- [ ] Código completamente reproducible, organizado y comentado
- [ ] **≥ 4 visualizaciones estáticas con Seaborn**
- [ ] **≥ 2 visualizaciones interactivas con Plotly** (propósitos diferenciados)
- [ ] Títulos informativos, ejes, etiquetas, leyendas y paletas legibles
- [ ] Interpretación escrita después de **cada** visualización, vinculada a la pregunta
- [ ] Conclusiones fundamentadas + limitaciones (sin causalidad)
- [ ] Ejecutar de principio a fin sin correcciones manuales

### Entregables
- [ ] Notebook .ipynb o enlace a Colab, completo y ejecutado
- [ ] Archivo HTML con las visualizaciones interactivas de Plotly
- [ ] Documento PDF (máx. 3 páginas): pregunta, audiencia, datos, hallazgos, conclusiones
- [ ] Carpeta con el archivo original de datos y recursos de reproducción
- [ ] Anexo técnico de uso de IA (máx. 1 página): herramientas, prompts (incl. paleta de colores), reflexión

**Convención de nombres:** `EquipoX_Proyecto2_NombreArchivo`

### Sustentación oral (10 min, desde el Notebook)
| Tiempo | Contenido |
|--------|-----------|
| 1 min  | Contexto, audiencia y pregunta analítica |
| 1 min  | Fuente, variables y transformaciones |
| 3 min  | Seaborn: patrones, relaciones y diferencias |
| 3 min  | Plotly: interacción en vivo y valor analítico |
| 2 min  | Síntesis: hallazgos, limitaciones y respuesta |

## Rúbrica (50 puntos)

| Criterio | Puntos |
|----------|--------|
| Reproducibilidad completa del código | 10 |
| Visualizaciones estáticas con Seaborn (≥4) | 9 |
| Visualizaciones interactivas con Plotly (≥2) | 9 |
| Interpretación escrita de cada visualización | 8 |
| Conclusiones fundamentadas en la evidencia | 5 |
| Documento PDF | 4 |
| Sustentación oral | 5 |

## Hitos

- [ ] **Paso 1 — Propuesta:** audiencia técnica concreta + pregunta analítica → aprobación de la docente (sesión siguiente a la asignación)
- [ ] **Paso 2 — Datos:** importar WHR24, inspeccionar estructura, tipos y faltantes
- [ ] **Paso 3 — Preparación:** documentar selección de variables, filtros y transformaciones
- [ ] **Paso 4 — EDA:** análisis exploratorio y planificación de comparaciones
- [ ] **Paso 5 — Seaborn:** 4+ visualizaciones estáticas con interpretación escrita
- [ ] **Paso 6 — Plotly:** 2+ visualizaciones interactivas con propósito analítico
- [ ] **Paso 7 — Síntesis:** integrar hallazgos y conclusiones que respondan la pregunta
- [ ] **Paso 8 — Reproducibilidad:** ejecutar notebook completo desde cero
- [ ] **Paso 9 — Entregables:** HTML, PDF (3 pág.), anexo IA (1 pág.)
- [ ] **Paso 10 — Sustentación:** preparar narrativa de 10 min

## Datos

- **Fuente obligatoria:** World Happiness Report 2024 – Data for Figure 2.1
- **Archivo:** `01_datos_originales/WHR24_Data_Figure_2.1.xls` (ya descargado)
- **Estructura:** 143 países × 11 columnas — Ladder score + 6 variables explicativas
  (Log GDP per capita, Social support, Healthy life expectancy, Freedom, Generosity,
  Perceptions of corruption) + Dystopia + residual + intervalos whisker
- **Nota:** 3 filas con valores faltantes en las variables explicativas (identificar países)
- ⚠️ No sustituir por versiones de Kaggle ni datos de otros años
