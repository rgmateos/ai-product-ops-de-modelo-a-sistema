import streamlit as st
from utils.economics import CostInputs, compute_costs

st.title("Simulador: La trampa de la optimización (TI vs SI)")
st.write(
    "Demuestra cómo bajar el coste de API (TI) puede disparar el coste total (SI) por retrabajo humano."
)

presets = {
    "Nano (barato)": {"eur_por_1k_tokens": 0.20, "fcr": 0.55},
    "Pro (equilibrado)": {"eur_por_1k_tokens": 0.80, "fcr": 0.72},
    "Ultra (caro)": {"eur_por_1k_tokens": 2.50, "fcr": 0.85},
    "Custom": None,
}

with st.sidebar:
    st.header("Inputs")
    preset = st.selectbox("Preset de modelo", list(presets.keys()), index=1)

    tickets = st.number_input("Tickets / periodo", min_value=1, value=1000, step=100)
    tokens_por_ticket = st.slider(
        "Tokens por ticket (estimado)", 50, 6000, 800, step=50
    )

    if preset != "Custom":
        eur_por_1k_tokens = presets[preset]["eur_por_1k_tokens"]
        fcr = presets[preset]["fcr"]
        st.caption(f"Precio fijo: {eur_por_1k_tokens} €/1k — FCR fijo: {fcr}")
    else:
        eur_por_1k_tokens = st.number_input(
            "Coste modelo (€/1k tokens)",
            min_value=0.0,
            value=0.80,
            step=0.05,
        )
        fcr = st.slider("Calidad (FCR estimado)", 0.10, 0.95, 0.72, step=0.01)

    coste_hora_agente = st.number_input(
        "Coste hora agente humano (€)", min_value=0.0, value=25.0, step=1.0
    )
    aht_min = st.slider(
        "AHT (min) por ticket que rebota", 1.0, 60.0, 15.0, step=1.0
    )

x = CostInputs(
    tickets=int(tickets),
    tokens_por_ticket=int(tokens_por_ticket),
    eur_por_1k_tokens=float(eur_por_1k_tokens),
    fcr=float(fcr),
    coste_hora_agente=float(coste_hora_agente),
    aht_min=float(aht_min),
)

r = compute_costs(x)

col1, col2, col3 = st.columns(3)
col1.metric("Coste TI (API)", f"{r['coste_ti']:.2f} €")
col2.metric("Coste Operativo (humanos)", f"{r['coste_operativo']:.2f} €")
col3.metric("COSTE TOTAL", f"{r['coste_total']:.2f} €")

st.divider()

if fcr < 0.65 and r["coste_operativo"] > r["coste_ti"]:
    st.error(
        "⚠️ ALERTA: estás ahorrando en TI, pero el retrabajo humano domina el coste total (SI)."
    )
elif r["coste_operativo"] > r["coste_ti"]:
    st.warning(
        "Atención: el coste operativo ya supera el coste TI. Revisa FCR/HITL/guardrails."
    )
else:
    st.success(
        "Buen balance: el coste TI domina (o está equilibrado) y el retrabajo está contenido."
    )

st.caption(
    "Interpretación: los tickets que la IA no resuelve (1-FCR) los paga el humano (AHT * €/hora)."
)

# Persistir en session_state para el reporte final
st.session_state["sim"] = {
    "preset": preset,
    "tickets": int(tickets),
    "tokens_por_ticket": int(tokens_por_ticket),
    "eur_por_1k_tokens": float(eur_por_1k_tokens),
    "fcr": float(fcr),
    "coste_ti": float(r["coste_ti"]),
    "coste_operativo": float(r["coste_operativo"]),
    "coste_total": float(r["coste_total"]),
}
