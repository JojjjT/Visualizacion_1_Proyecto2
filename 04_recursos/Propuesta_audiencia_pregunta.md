# Propuesta — Proyecto 2 · Visualización I
## (Para aprobación de la docente — sesión siguiente a la asignación)

**Equipo:** Equipo 7 — Joshua Trujillo y Nicolás Figueroa
**Fecha de elaboración:** 12 de octubre de 2026

---

## 1. Audiencia técnica específica

**Destinatario:** Unidad de investigación comparativa sobre determinantes del
bienestar de una organización internacional (p. ej. grupo de investigación del
PNUD o Banco Mundial que estudia indicadores de desarrollo y calidad de vida).

**Interés en la problemática:** Este equipo de investigación necesita identificar
de manera fundamentada y reproducible **qué combinaciones de condiciones
(PIB, apoyo social, esperanza de vida, libertad, generosidad y percepción de
corrupción) se asocian con altos niveles de bienestar reportado**, y en qué
medida esas condiciones **no alcanzan a explicar** la evaluación de vida de
algunos países. El resultado orienta futuras investigaciones sobre los
"determinantes explicados y no explicados" del bienestar y sirve como base
verificable para estudios comparados.

## 2. Pregunta analítica

> **¿Qué "recetas" de bienestar predominan entre los países con mayor y menor
> evaluación de vida según el World Happiness Report 2024, y en qué medida el
> componente no explicado (Distopía + residual) altera o cuestiona esas recetas?**

### Subpreguntas de apoyo

1. ¿Qué combinación de los seis indicadores explicativos caracteriza a los
   países en los terciles superior e inferior del *ladder score*?
2. ¿Qué países presentan el componente `Dystopia + residual` más alto y qué
   tienen en común, sugiriendo que las variables disponibles **no bastan** para
   explicar su bienestar?
3. ¿Los países atípicos respecto de su "receta" esperada concentran altos o
   bajos niveles de residual, lo que indicaría que la explicación está
   incompleta?

## 3. Variables que se emplearán

| Variable (en el archivo) | Significado | Uso previsto |
|---------------------------|-------------|--------------|
| `Country name` | País | Identificación, anotaciones en gráficos |
| `Ladder score` | Evaluación de vida (0–10) | Variable de interés / eje de orden |
| `upperwhisker` / `lowerwhisker` | Intervalos del ladder score | Contexto de incertidumbre (bandas) |
| `Explained by: Log GDP per capita` | Contribución del PIB per cápita | Dimensión 1 de la "receta" |
| `Explained by: Social support` | Contribución del apoyo social | Dimensión 2 de la "receta" |
| `Explained by: Healthy life expectancy` | Contribución de la esperanza de vida saludable | Dimensión 3 de la "receta" |
| `Explained by: Freedom to make life choices` | Contribución de la libertad | Dimensión 4 de la "receta" |
| `Explained by: Generosity` | Contribución de la generosidad | Dimensión 5 de la "receta" |
| `Explained by: Perceptions of corruption` | Contribución de la percepción de corrupción | Dimensión 6 de la "receta" |
| `Dystopia + residual` | Componente residual no explicado | **Eje central de la subpregunta 2** |

**Criterio de selección:** se emplean las 10 variables numéricas disponibles en
el archivo oficial (se exclúyen `upper/lowerwhisker` solo de los modelos de
composición y se conservan como referencia de incertidumbre). No se crearán
indicadores derivados salvo la clasificación en terciles del `ladder_score`,
cuyo criterio (pandas `qcut`, q=3) se documentará en el notebook.

## 4. Coherencia esperada

audiencia (unidad de investigación comparativa) ⇒
pregunta (recetas de bienestar + componente no explicado) ⇒
variables (6 indicadores + residual + ladder score) ⇒
preparación (renombre documentado, terciles, manejo de 3 faltantes) ⇒
visualizaciones (composición por grupos, perfiles radar/heatmap, residual
vs. explicado, atípicos) ⇒
interpretación (tras cada gráfico) ⇒
conclusiones (qué recetas predominan y qué queda sin explicar)

---

**Estado:** ☐ Borrador → ☑ Enviado para aprobación → ☐ Aprobado
