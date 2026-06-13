import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def retrieve_document(question):

    question = question.lower()

    if "anemia" in question:
        return "anemia.txt"

    elif "diabetes" in question:
        return "diabetes.txt"

    elif "hypertension" in question or "blood pressure" in question:
        return "hypertension.txt"

    elif "asthma" in question:
        return "asthma.txt"

    return None


def ask_medical_rag(question):

    file_name = retrieve_document(question)

    if not file_name:
        return """
⚠️ No Relevant Medical Document Found

Your question is outside the current medical knowledge base.

Available Topics:
• Anemia
• Diabetes
• Hypertension
• Asthma

Please ask a question related to one of these conditions.
"""

    file_path = os.path.join(
        "data/medical_docs",
        file_name
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        context = file.read()

    prompt = f"""
You are an AI healthcare assistant.

Use ONLY the information below.

Medical Information:

{context}

Question:
{question}

Provide:
1. Answer
2. Important Notes
3. When to Consult a Doctor

Important:
This is not a diagnosis.
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
