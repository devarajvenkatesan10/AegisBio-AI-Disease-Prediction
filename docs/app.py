import streamlit as st

st.set_page_config(page_title="AegisBio AI - Disease Prediction", page_icon="🏥")

st.title("🛡️ AegisBio AI: Health Risk Assistant")
st.subheader("Team Honey Bios | PEC Techathon 4.0")

st.markdown("---")

# Input Section
st.header("1. Patient Symptoms & Biometrics Intake")
symptoms = st.text_area("Log Current Symptoms", "Experiencing mild fatigue and elevated heart rate after moderate activity.")
hrv = st.slider("Heart Rate Variability (HRV)", 20, 100, 45)
rhr = st.slider("Resting Heart Rate (BPM)", 50, 120, 78)

# Risk Prediction Engine Simulation
if st.button("Generate Health Risk Assessment"):
    st.markdown("---")
    st.header("2. AI Risk Assessment & Explainability")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Cardiovascular Risk Score", value="Moderate (38%)", delta="+12%")
    with col2:
        st.metric(label="Metabolic Risk Score", value="Low (14%)", delta="-3%")
        
    st.info("💡 **Explainable AI (SHAP) Analysis:** Elevated Resting Heart Rate (78 BPM) and lowered HRV contributed most to the moderate cardiovascular rating.")
    
    st.header("3. Preventive Recommendations")
    st.success("✔ Recommended Action 1: Increase daily hydration target to 2.8 Liters.")
    st.success("✔ Recommended Action 2: Perform 20 minutes of low-impact aerobic exercise.")
