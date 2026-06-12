import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def analyze_symptoms(symptoms):

    prompt = f"""
You are an AI healthcare assistant.

Analyze the following symptoms:

{symptoms}

Provide:

1. Possible Conditions
2. Risk Level
3. Recommendations

Keep the answer concise.

Important:
This is not a medical diagnosis.
Recommend consulting a doctor when necessary.
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
