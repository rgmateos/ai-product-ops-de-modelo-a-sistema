
import streamlit as st

from utils.reporting
 
import generate_sdd_markdown,

markdown_to_pdf_bytes

st.title("Auditoría & Reporte (Entregable)")

st.subheader("Resumen de diseño (lo que se va a exportar)")

pipeline = st.session_state.get("pipeline_ordered", [])

roles = st.session_state.get("roles", {})

metrics = st.session_state.get("metrics", {})

guardrails = st.session_state.get("guardrails", {})

sim = st.session_state.get("sim", {})

col1, col2 = st.columns(2)

with col1:

st.markdown("### Pipeline")

st.write(pipeline if pipeline else "(no definido)")

st.markdown("### Roles")

st.json(roles)

with col2:

st.markdown("### Métricas")

st.json(metrics)

st.markdown("### Guardrails")

st.json(guardrails)

st.divider()

st.markdown
("## Generar especificación (SDD)")

md = generate_sdd_markdown(st.session_state)

st.code(md, language="markdown")

c1, c2 = st.columns(2)

with c1:

st.download_button(

"
 
Descargar SDD (.md)",

data=md.encode("utf
-
8"),

file_name="sdd_ai_product_ops.md",

mime="text/markdown",

use_container_width=True,

)

with c2:

pdf_bytes = markdown_to_pdf_bytes(md)

st.download_button(

"
 
Descargar SDD (.pdf)",

data=pdf_bytes,

file_name="sdd_ai_product_ops.pdf",

mime="application/pdf",

use_container_width=True,

)

st.caption("Nota: el PDF usa render básico; el .md es el “source of

truth” del entregable.")
