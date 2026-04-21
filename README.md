# AI Product Ops: De Modelo a Sistema (Streamlit)

App didáctica para obligar decisiones de diseño (trade-offs) en sistemas IA:

- Framework (People / Process / Data / Tech / Policy)
- Simulador TI vs SI (coste API vs retrabajo humano)
- Wizard de diseño (pipeline, roles, métricas, guardrails)
- Auditoría y reporte (SDD en Markdown/PDF)

## Estructura

```text
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
