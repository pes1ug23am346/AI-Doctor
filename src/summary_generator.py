import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def generate_summary(
    age,
    symptoms,
    medical_history,
    vitals
):

    prompt = f"""
You are an AI healthcare assistant.

Generate a professional hospital-style patient report.

Patient Information:

Age: {age}

Symptoms:
{symptoms}

Medical History:
{medical_history}

Vitals:
{vitals}

Format exactly like this:

AI DOCTOR HEALTH REPORT

PATIENT INFORMATION
- Age:
- Medical History:

SYMPTOMS
- ...

VITAL SIGNS
- ...

RISK ASSESSMENT
- Low / Moderate / High

RECOMMENDED TESTS
- ...

SUGGESTED SPECIALIST
- ...

CLINICAL NOTES
- ...

DISCLAIMER
This is not a diagnosis.
Consult a qualified healthcare professional.

Keep the report professional, concise, and easy to read.
"""
