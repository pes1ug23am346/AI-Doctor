import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def analyze_vitals(
    heart_rate,
    systolic_bp,
    diastolic_bp,
    spo2,
    temperature
):

    prompt = f"""
You are an AI healthcare assistant.

Analyze the following patient vitals:

Heart Rate: {heart_rate} bpm
Blood Pressure: {systolic_bp}/{diastolic_bp} mmHg
SpO2: {spo2}%
Temperature: {temperature} °F

Provide:

1. Risk Level
2. Findings
3. Recommendations

Important:
This is not a diagnosis.
Recommend consulting a doctor if necessary.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
