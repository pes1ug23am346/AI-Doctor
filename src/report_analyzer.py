import os

from pypdf import PdfReader
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def analyze_report(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    text = text[:5000]

    prompt = f"""
You are an AI healthcare assistant.

Analyze this medical report.

Provide:

1. Summary
2. Important Findings
3. Abnormal Values
4. Recommendations

Medical Report:

{text}
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
