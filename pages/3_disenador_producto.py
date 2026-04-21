import pandas as pd
import streamlit as st

st.title("Diseñador de Producto (Wizard)")

steps = ["1) Flujo", "2) Roles", "3) Métricas & Guardrails"]
step = st.radio("Paso", steps, horizontal=True)

# --- Paso 1
if step == steps[0]:
    st.subheader("Paso 1 — Definir el flujo (Process & Tech)")

    available = [
        "Auth",
        "RAG",
        "Inferencia",
        "Validación Humana",
        "Filtro PII",
        "Auditoría",
    ]
    selected = st.multiselect(
        "Selecciona componentes del pipeline",
        options=available,
        default=st.session_state.get(
            "pipeline_selected", ["Auth", "RAG", "Inferencia", "Auditoría"]
        ),
    )
    st.session_state["pipeline_selected"] = selected

    st.markdown("#### Ordena el pipeline (edita la columna **Orden**)")

    df = pd.DataFrame({"Paso": selected, "Orden": list(range(1, len(selected) + 1))})
    edited = st.data_editor(
        df,
        hide_index=True,
        use_container_width=True,
        num_rows="fixed",
    )
    ordered = edited.sort_values("Orden")["Paso"].tolist()
    st.session_state["pipeline_ordered"] = ordered

    if "Validación Humana" not in selected:
        st.warning(
            "Peligro: estás diseñando un sistema sin Human-in-the-loop (Validación Humana)."
        )
    if "Auditoría" not in selected:
        st.warning("Peligro: estás diseñando un sistema sin trazabilidad (Auditoría).")

# --- Paso 2
elif step == steps[1]:
    st.subheader("Paso 2 — Asignación de roles (People)")
    roles = st.session_state["roles"]

    col1, col2 = st.columns(2)

    with col1:
        kill_switch_options = ["", "SRE", "Product Owner", "Dev Lead"]
        data_policy_options = ["", "Legal", "Data Steward", "CISO"]

        current_kill_switch = roles.get("kill_switch_owner", "")
        current_data_policy = roles.get("data_policy_owner", "")

        if current_kill_switch not in kill_switch_options:
            current_kill_switch = ""
        if current_data_policy not in data_policy_options:
            current_data_policy = ""

        roles["kill_switch_owner"] = st.selectbox(
            "¿Quién pulsa el Kill Switch?",
            options=kill_switch_options,
            index=kill_switch_options.index(current_kill_switch),
        )

        roles["data_policy_owner"] = st.selectbox(
            "¿Quién define política de datos?",
            options=data_policy_options,
            index=data_policy_options.index(current_data_policy),
        )

    with col2:
        roles["service_owner"] = st.text_input(
            "Service Owner (nombre)", value=roles.get("service_owner", "")
        )
        roles["sre_owner"] = st.text_input(
            "SRE Owner (nombre)", value=roles.get("sre_owner", "")
        )
        roles["data_steward"] = st.text_input(
            "Data Steward (nombre)", value=roles.get("data_steward", "")
        )

    st.session_state["roles"] = roles

# --- Paso 3
else:
    st.subheader("Paso 3 — Métricas y Guardrails (Data & Policy)")
    metrics = st.session_state["metrics"]
    guardrails = st.session_state["guardrails"]

    st.markdown("#### Tabla guía (ejemplo)")
    guide = pd.DataFrame(
        [
            {
                "Tipo": "Outcome (Valor)",
                "Ejemplo": "FCR, CSAT, tiempo a resolución",
            },
            {
                "Tipo": "Efficiency (Coste)",
                "Ejemplo": "€/ticket, tokens/ticket, % escalados",
            },
            {
                "Tipo": "Safety (Riesgo)",
                "Ejemplo": "tasa alucinación, fuga PII, errores críticos",
            },
        ]
    )
    st.table(guide)

    metrics["outcome"] = st.text_input(
        "Métrica de Valor (Outcome)", value=metrics.get("outcome", "")
    )
    metrics["efficiency"] = st.text_input(
        "Métrica de Coste (Efficiency)", value=metrics.get("efficiency", "")
    )
    metrics["safety"] = st.text_input(
        "Métrica de Riesgo (Safety)", value=metrics.get("safety", "")
    )

    guardrails["slo_latencia_s"] = st.number_input(
        "SLO Latencia p95 (seg)",
        min_value=0.1,
        value=float(guardrails.get("slo_latencia_s", 2.0)),
        step=0.1,
    )
    guardrails["max_halluc_rate"] = st.number_input(
        "Umbral alucinación (0..1)",
        min_value=0.0,
        max_value=1.0,
        value=float(guardrails.get("max_halluc_rate", 0.02)),
        step=0.01,
    )

    st.session_state["metrics"] = metrics
    st.session_state["guardrails"] = guardrails

    st.info("Mínimo exigible: 3 métricas (valor/coste/riesgo) + 1 SLO con umbral numérico.")
