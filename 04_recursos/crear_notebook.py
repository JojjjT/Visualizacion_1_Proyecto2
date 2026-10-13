# -*- coding: utf-8 -*-
"""
Genera el notebook base del Proyecto 2 (Visualización reproducible en Python)
con la estructura completa exigida por el enunciado:

  audiencia ⇒ pregunta ⇒ variables ⇒ preparación ⇒ visualizaciones
  ⇒ interpretación ⇒ conclusiones ⇒ reproducibilidad

Requisitos cubiertos por el esqueleto:
  - >= 4 visualizaciones estáticas con Seaborn (celdas marcadas)
  - >= 2 visualizaciones interactivas con Plotly (celdas marcadas)
  - Interpretación escrita después de cada visualización
  - Celdas Markdown que articulan el argumento (el notebook se lee como informe)

Uso:
  python crear_notebook.py
"""

import os
import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "02_notebook", "EquipoX_Proyecto2_Analisis.ipynb")

nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {"name": "python", "version": "3.11"},
}

md = lambda s: nbf.v4.new_markdown_cell(s)
code = lambda s: nbf.v4.new_code_cell(s)

cells = []

# ---------------------------------------------------------------- Portada
cells.append(md(r"""# Proyecto 2 — Visualización reproducible en Python
### Análisis exploratorio del *World Happiness Report 2024*

**Curso:** Visualización I — Universidad Externado de Colombia
**Equipo:** EquipoX — *\[completar integrantes\]*
**Docentes:** Adriana Pineda – Paola Moreno
**Entrega:** lunes 26 de octubre de 2026, 11:59 p.m.

---

> Este notebook se lee como un **informe analítico**: las celdas Markdown
> articulan el argumento y el código permite verificarlo.
"""))

# ---------------------------------------------------------------- 1. Audiencia y pregunta
cells.append(md(r"""## 1. Audiencia y pregunta analítica

**Audiencia técnica:** _\[identificar el tipo de investigador, equipo técnico o unidad
de análisis; explicar brevemente su interés en la problemática\]_

**Pregunta analítica:** _\[formular la pregunta concreta que orienta el análisis;
debe poder responderse con las variables disponibles en el WHR 2024\]_

**Acción esperada de la audiencia:**

1. Comprender la pregunta analítica y las variables empleadas.
2. Examinar distribuciones, relaciones y diferencias entre países o grupos.
3. Explorar interactivamente observaciones o comparaciones relevantes.
4. Distinguir resultados observados, limitaciones y nuevas preguntas.
5. Reproducir el análisis a partir de los archivos entregados.

> ⚠️ Las asociaciones observadas **no** se presentan como relaciones causales.
"""))

# ---------------------------------------------------------------- 2. Datos
cells.append(md(r"""## 2. Datos: fuente y variables

**Fuente obligatoria:** World Happiness Report 2024 – *Data for Figure 2.1*
**Archivo oficial:** `WHR24_Data_Figure_2.1.xls`
**Descarga:** <https://files.worldhappiness.report/WHR24_Data_Figure_2.1.xls>

El archivo original se conserva sin modificaciones en `01_datos_originales/`.
Todas las operaciones de preparación se documentan por separado, de modo que
el procedimiento sea reproducible.
"""))

cells.append(code("""# ============================================================
# Celda 1 — Importación de librerías
# ============================================================
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio

# Configuración general de estilo
sns.set_theme(style="whitegrid", context="notebook")
pio.templates.default = "plotly_white"
pd.set_option("display.max_columns", 50)

RANDOM_STATE = 42  # para cualquier operación estocástica
print("Librerías importadas correctamente.")"""))

cells.append(code("""# ============================================================
# Celda 2 — Importación del archivo oficial
# ============================================================
# Ruta relativa: el notebook se ejecuta desde 02_notebook/
DATA_PATH = os.path.join("..", "01_datos_originales", "WHR24_Data_Figure_2.1.xls")

df = pd.read_excel(DATA_PATH)
print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
df.head()"""))

cells.append(md(r"""### 2.1 Inspección de estructura, tipos y valores faltantes

_Primera verificación de reproducibilidad: qué hay en el archivo, de qué tipo es y
dónde faltan datos._"""))

cells.append(code("""# ============================================================
# Celda 3 — Inspección: tipos, faltantes y estadísticas descriptivas
# ============================================================
print("=== Tipos de datos ===")
print(df.dtypes.to_string())
print("\\n=== Valores faltantes ===")
faltantes = df.isna().sum()
print(faltantes[faltantes > 0].to_string() if (faltantes > 0).any() else "Sin valores faltantes")
print("\\n=== Estadísticas descriptivas ===")
df.describe().T"""))

cells.append(md(r"""_**Observaciones de la inspección:** ¿cuántos países hay? ¿qué variables tienen
faltantes y en qué países? ¿las escalas son comparables entre sí?_

_\[completar tras ejecutar\]_

### 2.2 Diccionario de variables

| Variable | Significado | Uso en el análisis |
|----------|-------------|--------------------|
| `Country name` | País | Identificación / anotaciones |
| `Ladder score` | Evaluación de vida (0–10) | Variable de interés |
| `upperwhisker` / `lowerwhisker` | Intervalos del ladder score | Contexto de incertidumbre |
| `Explained by: Log GDP per capita` | Contribución del PIB per cápita | Indicador 1 |
| `Explained by: Social support` | Contribución del apoyo social | Indicador 2 |
| `Explained by: Healthy life expectancy` | Contribución de la esperanza de vida saludable | Indicador 3 |
| `Explained by: Freedom to make life choices` | Contribución de la libertad | Indicador 4 |
| `Explained by: Generosity` | Contribución de la generosidad | Indicador 5 |
| `Explained by: Perceptions of corruption` | Contribución de la percepción de corrupción | Indicador 6 |
| `Dystopia + residual` | Componente residual (Distopía + residual) | Contexto |

**Criterios de selección de variables, filtros y transformaciones** se documentan
en la celda de preparación (sección 3)."""))

# ---------------------------------------------------------------- 3. Preparación
cells.append(md(r"""## 3. Preparación y alcance

En esta sección se deja **trazabilidad** de cada operación:

- criterios de selección de variables,
- filtros, agrupaciones o transformaciones,
- justificación de cualquier agrupación de países o indicador derivado.

La fuente original (`df`) se mantiene separada del conjunto preparado (`df_analisis`)."""))

cells.append(code("""# ============================================================
# Celda 4 — Preparación documentada
# ============================================================
# 4.1 Renombrar columnas para trabajar con nombres cómodos (sin perder la trazabilidad)
renombrado = {
    "Country name": "pais",
    "Ladder score": "ladder_score",
    "Explained by: Log GDP per capita": "pib_percapita",
    "Explained by: Social support": "apoyo_social",
    "Explained by: Healthy life expectancy": "esperanza_vida",
    "Explained by: Freedom to make life choices": "libertad",
    "Explained by: Generosity": "generosidad",
    "Explained by: Perceptions of corruption": "corrupcion",
    "Dystopia + residual": "distopia_residual",
}

df_analisis = df.rename(columns=renombrado).copy()

# 4.2 Documentar filas con faltantes (NO se eliminan silenciosamente)
faltantes_mask = df_analisis.isna().any(axis=1)
print("Países con valores faltantes en indicadores:")
print(df_analisis.loc[faltantes_mask, ["pais"]].to_string(index=False))

# 4.3 Lista de indicadores que se usarán en el análisis
indicadores = ["pib_percapita", "apoyo_social", "esperanza_vida",
               "libertad", "generosidad", "corrupcion"]

# 4.4 Manejo explícito de faltantes: se documenta y se excluyen solo de las
#     visualizaciones que requieren valores completos (nunca en silencio).
n_faltantes = int(faltantes_mask.sum())
print(f"\\nFilas con algún faltante: {n_faltantes} de {len(df_analisis)}")
print("Se conservan en 'df_analisis' y se excluyen con dropna() en las gráficas "
      "que lo requieren (p. ej. Plotly con 'size').")

# 4.5 (Opcional) Crear grupos de países JUSTIFICADOS si la pregunta lo requiere.
#      Ejemplo: terciles de ladder_score — documentar siempre el criterio.
df_analisis["grupo_bienestar"] = pd.qcut(
    df_analisis["ladder_score"], q=3,
    labels=["Bajo", "Medio", "Alto"]
)

print(f"\\nConjunto preparado: {df_analisis.shape}")
df_analisis[["pais", "ladder_score", "grupo_bienestar"]].head()"""))

cells.append(md(r"""_**Justificación de transformaciones:** ¿por qué renombrar?, ¿por qué qcut en
terciles?, ¿qué se hizo con los faltantes y por qué?_

_\[completar con la justificación vinculada a la pregunta analítica\]_"""))

# ---------------------------------------------------------------- 4. EDA
cells.append(md(r"""## 4. Análisis exploratorio (EDA) y planificación de comparaciones

Antes de graficar, se planifica: **¿qué necesita examinar el analista con cada
visualización?, ¿por qué es adecuada para las variables?, ¿qué aporta que no se
haya mostrado ya?**"""))

cells.append(code("""# ============================================================
# Celda 5 — EDA numérico: distribuciones y correlaciones base
# ============================================================
# 5.1 Estadísticas por indicador
resumen = df_analisis[indicadores + ["ladder_score"]].describe().T
display(resumen)

# 5.2 Matriz de correlación (base para elegir qué relaciones graficar)
corr = df_analisis[indicadores + ["ladder_score"]].corr()
display(corr.round(2))

# 5.3 Ranking extremos del ladder score (contexto para anotaciones)
print("Top 5 países:")
display(df_analisis.nlargest(5, "ladder_score")[["pais", "ladder_score"]])
print("Bottom 5 países:")
display(df_analisis.nsmallest(5, "ladder_score")[["pais", "ladder_score"]])"""))

cells.append(md(r"""### 4.1 Plan de visualizaciones

| # | Tipo | Librería | Qué examina | Propósito analítico |
|---|------|----------|-------------|---------------------|
| 1 | Distribución | Seaborn | Ladder score global | Forma y dispersiones iniciales |
| 2 | Relación | Seaborn | Indicador vs ladder score | Asociaciones individuales |
| 3 | Comparación de grupos | Seaborn | Grupos de bienestar × indicadores | Diferencias entre grupos |
| 4 | Matriz / anotaciones | Seaborn | Correlaciones + casos extremos | Panorama general con lectura |
| 5 | Interactiva 1 | Plotly | Exploración país-indicador | Profundizar en observaciones |
| 6 | Interactiva 2 | Plotly | Comparación multivariable | Exploración con filtro/agrupación |

_Cada visualización se acompaña inmediatamente de su interpretación escrita,
vinculada a la pregunta analítica._"""))

# ---------------------------------------------------------------- 5. Seaborn
cells.append(md(r"""## 5. Visualizaciones estáticas con Seaborn

> **Mínimo requerido: 4 gráficos.** Cada uno responde: ¿qué necesita examinar el
> analista?, ¿por qué esta forma es adecuada?, ¿qué aporta que no se mostró ya?"""))

cells.append(md(r"""### 5.1 — Visualización estática 1: distribución del ladder score"""))

cells.append(code("""# ============================================================
# Celda 6 — Seaborn 1: distribución del ladder score
# ============================================================
fig, ax = plt.subplots(figsize=(9, 5))

sns.histplot(data=df_analisis, x="ladder_score", kde=True, bins=20,
             color="#2E86AB", ax=ax)

ax.set_title("Distribución de la evaluación de vida (ladder score), WHR 2024",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Ladder score (0–10)")
ax.set_ylabel("Países")

plt.tight_layout()
plt.show()"""))

cells.append(md(r"""**Interpretación (Visualización 1):**

_¿Cómo se distribuye la evaluación de vida entre los 143 países? ¿Hay sesgo,
valores atípicos o diferencias claras? ¿Qué indica esto para la pregunta
analítica?_

_\[escribir aquí la lectura, conectada explícitamente con la pregunta\]_"""))

cells.append(md(r"""### 5.2 — Visualización estática 2: asociación entre un indicador y el ladder score"""))

cells.append(code("""# ============================================================
# Celda 7 — Seaborn 2: indicador vs ladder score
# ============================================================
# AJUSTAR: elegir el indicador más pertinente para la pregunta analítica
VAR_X = "pib_percapita"   # <- cambiar según la pregunta

fig, ax = plt.subplots(figsize=(9, 6))

sns.regplot(data=df_analisis, x=VAR_X, y="ladder_score",
            scatter_kws={"alpha": 0.6, "s": 50},
            line_kws={"color": "#D1495B"}, ax=ax)

ax.set_title(f"Asociación entre {VAR_X.replace('_', ' ')} y la evaluación de vida",
             fontsize=13, fontweight="bold")
ax.set_xlabel(VAR_X.replace("_", " ").title())
ax.set_ylabel("Ladder score")

plt.tight_layout()
plt.show()"""))

cells.append(md(r"""**Interpretación (Visualización 2):**

_¿La asociación es positiva/negativa?, ¿cuál es su fuerza?, ¿hay países atípicos?
Esto es una **asociación observada, no causalidad**. ¿Qué aporta para responder
la pregunta?_

_\[escribir aquí\]_"""))

cells.append(md(r"""### 5.3 — Visualización estática 3: comparación entre grupos de países"""))

cells.append(code("""# ============================================================
# Celda 8 — Seaborn 3: indicadores por grupo de bienestar
# ============================================================
# Comparación de TODOS los indicadores entre grupos justificados (terciles)
melted = df_analisis.melt(
    id_vars=["pais", "grupo_bienestar", "ladder_score"],
    value_vars=indicadores,
    var_name="indicador", value_name="contribucion"
)

fig, ax = plt.subplots(figsize=(11, 6))

sns.boxplot(data=melted, x="indicador", y="contribucion",
            hue="grupo_bienestar", palette="viridis", ax=ax)

ax.set_title("Contribución de los indicadores por grupo de bienestar",
             fontsize=13, fontweight="bold")
ax.set_xlabel("")
ax.set_ylabel("Contribución al ladder score")
ax.tick_params(axis="x", rotation=25)
ax.legend(title="Grupo de bienestar")

plt.tight_layout()
plt.show()"""))

cells.append(md(r"""**Interpretación (Visualización 3):**

_¿Qué indicadores varían más entre grupos bajos, medios y altos? ¿Hay solapamiento?
¿La comparación de grupos está justificada por la pregunta analítica?_

_\[escribir aquí\]_"""))

cells.append(md(r"""### 5.4 — Visualización estática 4: panorama de correlaciones con anotaciones"""))

cells.append(code("""# ============================================================
# Celda 9 — Seaborn 4: heatmap de correlaciones
# ============================================================
cols_corr = ["ladder_score"] + indicadores
corr = df_analisis[cols_corr].corr()

fig, ax = plt.subplots(figsize=(9, 7))

sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .8}, ax=ax)

ax.set_title("Correlación entre el ladder score y los seis indicadores",
             fontsize=13, fontweight="bold")

plt.tight_layout()
plt.show()"""))

cells.append(md(r"""**Interpretación (Visualización 4):**

_¿Qué indicadores tienen la correlación más fuerte con el ladder score?, ¿hay
colinealidad entre indicadores?, ¿qué relaciones merecen explorarse en detalle
con Plotly?_

_\[escribir aquí\]_"""))

# ---------------------------------------------------------------- 6. Plotly
cells.append(md(r"""## 6. Visualizaciones interactivas con Plotly

> **Mínimo requerido: 2 gráficos** con propósitos analíticos diferenciados. La
> interactividad debe **aportar valor** a la interpretación: permitir profundizar
> en observaciones o comparaciones, no solo añadir efectos visuales.

### 6.1 — Interactiva 1: exploración país-indicador"""))

cells.append(code("""# ============================================================
# Celda 10 — Plotly 1: burbujas (o scatter interactivo) país-indicador
# ============================================================
# AJUSTAR: elegir ejes y variable de tamaño según la pregunta analítica
# Se excluyen filas con faltantes SOLO para este gráfico (dropna documentado)
df_plot1 = df_analisis.dropna(subset=["esperanza_vida", "ladder_score", "pib_percapita"])

fig1 = px.scatter(
    df_plot1,
    x="esperanza_vida",           # <- ajustar
    y="ladder_score",
    size="pib_percapita",         # <- ajustar (tamaño = tercer indicador)
    color="grupo_bienestar",
    hover_name="pais",
    hover_data={"ladder_score": ":.2f", "esperanza_vida": ":.2f"},
    labels={
        "esperanza_vida": "Contribución esperanza de vida saludable",
        "ladder_score": "Ladder score",
        "grupo_bienestar": "Grupo de bienestar",
        "pib_percapita": "PIB per cápita (log)",
    },
    title="Evaluación de vida vs. esperanza de vida saludable (tamaño: PIB per cápita)",
    color_discrete_sequence=px.colors.qualitative.Set2,
    size_max=22,
    opacity=0.75,
)

fig1.update_layout(height=560, legend_title_text="Grupo de bienestar")
fig1.show()"""))

cells.append(md(r"""**Interpretación (Interactiva 1):**

_¿Qué permite examinar la interacción que un gráfico estático no mostraba?
(hover por país, tamaño como tercer indicador, filtro por grupo). ¿Qué patrones
o casos atípicos aparecen al explorar? ¿Qué aporta para la pregunta?_

_\[escribir aquí\]_"""))

cells.append(md(r"""### 6.2 — Interactiva 2: comparación con filtro"""))

cells.append(code("""# ============================================================
# Celda 11 — Plotly 2: barras interactivo con selector de indicador
# ============================================================
# Versión larga con el indicador como NIVEL (para el slider de animation_frame)
melted2 = df_analisis.melt(
    id_vars=["pais", "grupo_bienestar", "ladder_score"],
    value_vars=indicadores,
    var_name="indicador", value_name="contribucion"
)

# Top 15 por indicador (sin drop de la columna 'indicador')
top_por_indicador = (
    melted2.dropna(subset=["contribucion"])
    .sort_values("contribucion", ascending=False)
    .groupby("indicador", group_keys=True, observed=True)
    .head(15)
    .reset_index(drop=True)
)

fig2 = px.bar(
    top_por_indicador,
    x="contribucion", y="pais",
    color="grupo_bienestar",
    animation_frame="indicador",          # <- filtro/selector: recorre indicadores
    labels={"contribucion": "Contribución", "pais": "País",
            "grupo_bienestar": "Grupo de bienestar"},
    title="Top 15 países por contribución — seleccione el indicador",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    orientation="h",
)

fig2.update_layout(height=600, yaxis={"categoryorder": "total ascending"},
                   legend_title_text="Grupo de bienestar")
fig2.show()"""))

cells.append(md(r"""**Interpretación (Interactiva 2):**

_¿Qué comparación habilita el filtro/selector que no era posible en estático?
¿Qué hallazgos emergen al recorrer los indicadores? ¿La interactividad aporta
valor analítico o solo decoración?_

_\[escribir aquí\]_"""))

# ---------------------------------------------------------------- 7. Síntesis
cells.append(md(r"""## 7. Síntesis de hallazgos y conclusiones

**Respuesta a la pregunta analítica:**

_\[integrar la evidencia de las seis visualizaciones para responder la pregunta
planteada en la sección 1. Cada hallazgo debe estar sustentado en los gráficos
anteriores.\]_

**Limitaciones del análisis:**

- _[alcance de la fuente: un solo año, indicadores agregados]_
- _[asociación ≠ causalidad]_
- _[faltantes / agrupaciones utilizadas]_
- _[otras que identifique el equipo]_

**Nuevas preguntas de investigación:**

- _[1]_
- _[2]_"""))

# ---------------------------------------------------------------- 8. Reproducibilidad
cells.append(md(r"""## 8. Comprobación de reproducibilidad

Ejecutar **Run All** desde el inicio: el notebook debe correr completo, sin
ajustes manuales, con rutas relativas y sin dependencias ocultas."""))

cells.append(code("""# ============================================================
# Celda 12 — Verificación final de reproducibilidad
# ============================================================
print("Reproducibilidad — verificación final")
print(f"  1. Datos originales leídos: {os.path.exists(DATA_PATH)}")
print(f"  2. Filas en el dataset:    {df.shape[0]}")
print(f"  3. Filas preparadas:       {df_analisis.shape[0]}")
print(f"  4. Seaborn (mín. 4):       [indicar cuáles celdas] ")
print(f"  5. Plotly (mín. 2):        [indicar cuáles celdas] ")
print("  6. Entregables: notebook + HTML Plotly + PDF (3 pág.) + anexo IA (1 pág.)")
print("\\n✓ Notebook ejecutado de principio a fin.")"""))

# ---------------------------------------------------------------- 9. Anexo IA
cells.append(md(r"""## 9. Anexo técnico de uso de IA (resumen)

> **Nota:** el anexo completo se entrega como PDF de máximo **una página**
> (`EquipoX_Proyecto2_Anexo_IA.pdf`). Este bloque es el borrador de trabajo.

**Herramientas y propósito:** _\[cuál y para qué\]_

**Prompts empleados (incluido al menos uno sobre la paleta de colores):**

1. _\[prompt sobre paleta de colores\]_
2. _\[otros prompts\]_

**Reflexión sobre revisión crítica:** _\[qué se verificó, qué se corrigió, qué se
rechazó de la salida de la IA\]_

_Si no se utilizó IA, declararlo expresamente._"""))

nb.cells = cells

os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print(f"Notebook creado: {OUT}")
print(f"Celdas: {len(cells)} (Markdown: {sum(1 for c in cells if c.cell_type=='markdown')}, "
      f"código: {sum(1 for c in cells if c.cell_type=='code')})")
