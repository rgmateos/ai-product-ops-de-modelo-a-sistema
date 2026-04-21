
import streamlit as st

import plotly.graph_objects as go

st.title("AI Product Ops: De Modelo a Sistema")

st.caption("Regla de oro: si no puedes medirlo, no puedes operarlo.")

st.subheader("Framework: People · Process · Data · Tech · Policy")

with st.expander
("Definiciones rápidas (para discusión en clase)",

expanded=True):

st.markdown("""

-
 
**People**: roles obligatorios (Owner/PO, SRE, Data Steward).

-
 
**Process**: flujo operable (HITL, escalado, runbooks).

-
 
**Data**: métricas (valor/coste/riesgo), observabilidad, calidad.

-
 
**Tech**: arquitectura (RAG, validación, trazabilidad, latencia).

-
 
**Policy**: kill switch, auditoría, PII, controles, cumplimiento.

""")

st.markdown("### Radar de madurez (ajusta y discute trade
-
offs)")

colA, colB = st.columns([1, 2], vertical_alignment="top")

with colA:

people = st.slider("People", 0, 5, 3)

process = st.slider("Process", 0, 5, 3)

data = st.slider("Data", 0, 5, 3)

tech = st.slider("Tech", 0, 5, 3)

policy = st.slider
("Policy", 0, 5, 3)

with colB:

categories = ["People", "Process", "Data", "Tech", "Policy"]

values = [people, process, data, tech, policy]

fig
 
= go.Figure(

data=[
go.Scatterpolar(r=values + [values[0]], theta=categories

+ [categories[0]], fill="toself")]

)

fig.update_layout(

polar=dict(radialaxis=dict(visible=True, range=[0, 5])),

showlegend=False,

margin=dict(l=10, r=10, t=10, b=10),

)

st.plotly_chart(fig, use_container_width=True)

st.info("Objetivo didáctico: antes de “tocar prompts”, forzar

decisiones de sistema (roles, flujos, métricas y políticas).")
