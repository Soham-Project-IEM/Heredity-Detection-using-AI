import streamlit as st
from chatbot_backend import get_ai_response
import base64
import os

st.set_page_config(page_title="🧬 Heredity Detection System", layout="centered")

st.title("🧬 Heredity Detection System")
st.markdown("Provide patient details for AI-based medical diagnostic support.")

# Form Inputs
with st.form("heredity_form", clear_on_submit=True):
    name = st.text_input("Patient's Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])

    family_history = st.radio("Family history of disease?", ["Yes", "No"])
    family_details = ""
    if family_history == "Yes":
        family_details = st.text_area("Describe family history")

    traits = st.multiselect(
        "Genetic Traits (select one or more)",
        ["Diabetes", "Hypertension", "Cancer", "Thalassemia", "Hemophilia",
         "Sickle Cell", "Cystic Fibrosis", "Huntington's Disease",
         "Muscular Dystrophy", "Color Blindness"]
    )

    symptoms = st.text_area("Describe symptoms")

    uploaded_file = st.file_uploader("Upload DNA Report (PDF or Image)", type=["pdf", "png", "jpg", "jpeg"])

    submitted = st.form_submit_button("Get Diagnosis")

if submitted:
    with st.spinner("Generating diagnostic response..."):

        # Prepare content for AI
        prompt = f"""
        Patient Name: {name}
        Age: {age}
        Sex: {sex}
        Family History of Disease: {family_history}
        Family Details: {family_details}
        Genetic Traits: {', '.join(traits)}
        Symptoms: {symptoms}
        """
        if uploaded_file:
            file_details = f"DNA Report: {uploaded_file.name}"
        else:
            file_details = "DNA Report: Not uploaded"

        prompt += f"\n{file_details}"

        # Get AI response
        response = get_ai_response(prompt)

        # Save recent response (you can extend this to save in a DB/file)
        if "history" not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append({
            "name": name,
            "age": age,
            "sex": sex,
            "traits": traits,
            "symptoms": symptoms,
            "diagnosis": response
        })

        st.success("AI Diagnostic Response:")
        st.write(response)

# Show recent history
if "history" in st.session_state and st.session_state.history:
    st.markdown("---")
    st.header("📄 Recent Submissions")
    for idx, record in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**{idx}. {record['name']}** (Age: {record['age']}, Sex: {record['sex']})")
        st.markdown(f"- Traits: {', '.join(record['traits'])}")
        st.markdown(f"- Symptoms: {record['symptoms']}")
        st.markdown(f"- **Diagnosis**: {record['diagnosis']}")
        st.markdown("---")
