from src.medical_rag import ask_medical_rag
from src.image_analyzer import analyze_image
import sys
import os

sys.path.append(os.path.abspath("src"))

import streamlit as st

from symptom_analyzer import analyze_symptoms
from report_analyzer import analyze_report
from vital_analyzer import analyze_vitals

st.set_page_config(
    page_title="AI Doctor",
    page_icon="🩺",
    layout="wide"
)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🩺 AI Doctor")

module = st.sidebar.radio(
    "Select Module",
    [
        "Symptom Analysis",
        "Medical Report Analysis",
        "Medical Image Analysis",
        "Vital Analysis",
        "Medical RAG"
    ]
)

st.sidebar.success("AI Healthcare Assistant")

# ==========================
# HEADER
# ==========================

st.title("🩺 AI Doctor")

st.subheader(
    "AI-Powered Smart Healthcare Assistant"
)

st.divider()

# ==========================
# DASHBOARD
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Modules", "5")

with col2:
    st.metric("AI Engine", "Hugging Face")

with col3:
    st.metric("Status", "Active")

st.divider()

# ==========================
# SYMPTOM ANALYSIS
# ==========================

if module == "Symptom Analysis":

    st.header("🩺 Symptom Analysis")

    symptoms = st.text_area(
        "Enter Symptoms",
        placeholder="Example: Fever, headache, cough for 3 days"
    )

    if st.button("Analyze Symptoms"):

        if symptoms.strip():

            with st.spinner("Analyzing symptoms..."):

                result = analyze_symptoms(symptoms)

            st.success("Analysis Complete")

            st.markdown(result)

# ==========================
# MEDICAL REPORT ANALYSIS
# ==========================

elif module == "Medical Report Analysis":

    st.header("📄 Medical Report Analysis")

    uploaded_file = st.file_uploader(
        "Upload Medical Report PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )

        if st.button("Analyze Report"):

            with st.spinner(
                "Analyzing Medical Report..."
            ):

                result = analyze_report(
                    uploaded_file
                )

            st.success(
                "Report Analysis Complete"
            )

            st.markdown(result)

# ==========================
# IMAGE ANALYSIS
# ==========================
elif module == "Medical Image Analysis":

    st.header("🖼️ Medical Image Analysis")

    image_file = st.file_uploader(
        "Upload Medical Image",
        type=["png", "jpg", "jpeg"]
    )

    if image_file:

        st.image(
            image_file,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button(
            "Analyze Image"
        ):

            with st.spinner(
                "Analyzing image..."
            ):

                result = analyze_image(
                    image_file
                )

            st.success(
                "Image Analysis Complete"
            )

            st.markdown(result)
# ==========================
# VITAL ANALYSIS
# ==========================
elif module == "Vital Analysis":

    st.header("❤️ Vital Analysis")

    heart_rate = st.number_input(
        "Heart Rate (bpm)",
        min_value=30,
        max_value=250,
        value=72
    )

    systolic_bp = st.number_input(
        "Systolic BP",
        min_value=50,
        max_value=250,
        value=120
    )

    diastolic_bp = st.number_input(
        "Diastolic BP",
        min_value=30,
        max_value=150,
        value=80
    )

    spo2 = st.number_input(
        "SpO2 (%)",
        min_value=50,
        max_value=100,
        value=98
    )

    temperature = st.number_input(
        "Temperature (°F)",
        min_value=90.0,
        max_value=110.0,
        value=98.6
    )

    if st.button("Analyze Vitals"):

        with st.spinner("Analyzing vitals..."):

            result = analyze_vitals(
                heart_rate,
                systolic_bp,
                diastolic_bp,
                spo2,
                temperature
            )

        st.success("Vital Analysis Complete")

        st.markdown(result)
# ==========================
# MEDICAL RAG
# ==========================
elif module == "Medical RAG":

    st.header("📚 Medical RAG Assistant")

    question = st.text_input(
        "Ask a Medical Question",
        placeholder="Example: What are symptoms of anemia?"
    )

    if st.button("Ask AI Doctor"):

        if question.strip():

            with st.spinner(
                "Searching medical knowledge..."
            ):

                result = ask_medical_rag(
                    question
                )

            st.success(
                "Answer Generated"
            )

            st.markdown(result)
