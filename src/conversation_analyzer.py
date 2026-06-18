import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def analyze_conversation(conversation):

    prompt = f"""
You are an AI healthcare assistant.

Analyze the following doctor-patient conversation.

Conversation:

{conversation}

Provide:

1. Symptoms Identified
2. Duration of Symptoms
3. Possible Medical Concerns
4. Important Observations
5. Recommended Follow-up Questions
6. Recommendations

Important:
This is not a diagnosis.
Always recommend consulting a healthcare professional.
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
