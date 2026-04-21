# AI Product Ops: De Modelo a Sistema (Streamlit)

App didáctica para obligar decisiones de diseño (trade-offs) en sistemas IA:

- Framework (People / Process / Data / Tech / Policy)
- Simulador TI vs SI (coste API vs retrabajo humano)
- Wizard de diseño (pipeline, roles, métricas, guardrails)
- Auditoría y reporte (SDD en Markdown/PDF)

## Estructura

    /
    ├─ app.py
    ├─ requirements.txt
    ├─ README.md
    ├─ .gitignore
    ├─ .streamlit/
    │  └─ config.toml
    ├─ pages/
    │  ├─ 1_home_framework.py
    │  ├─ 2_simulador_ti_vs_si.py
    │  ├─ 3_disenador_producto.py
    │  └─ 4_auditoria_reporte.py
    └─ utils/
       ├─ __init__.py
       ├─ economics.py
       └─ reporting.py

## Ejecutar en local

    pip install -r requirements.txt
    streamlit run app.py

## Desplegar en Streamlit Community Cloud

1. Ve a share.streamlit.io
2. Pulsa Create app
3. Selecciona tu repositorio y rama
4. En File path / entrypoint pon app.py
5. Pulsa Deploy

## Qué hace la app

### 1. Home · Framework
Permite revisar el marco People / Process / Data / Tech / Policy y ajustar la madurez de cada dimensión.

### 2. Simulador · TI vs SI
Compara coste TI (API) frente a coste operativo humano para visualizar trade-offs entre precio y calidad.

### 3. Diseñador · Wizard
Permite definir:
- pipeline
- roles
- métricas
- guardrails

### 4. Auditoría · Reporte
Genera un SDD exportable en:
- Markdown
- PDF

## Dependencias

- streamlit
- plotly
- pandas
- reportlab
