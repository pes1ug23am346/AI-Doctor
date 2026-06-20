import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)


def ask_doctor(question):

    prompt = f"""
You are AI Doctor, a friendly healthcare assistant.

User Message:
{question}

First determine whether enough information is available.

If important information is missing:

DO NOT provide diagnosis, risk level, tests, or recommendations yet.

Instead ask 3-5 short follow-up questions that would help understand the condition better.

Examples:
- How old are you?
- How long have you had these symptoms?
- Do you have any medical conditions?
- Are you taking any medications?
- Do you have fever, chest pain, or breathing difficulty?

If enough information is available:

Provide:

## What Your Symptoms May Indicate
Explain possible causes in simple language.

## Risk Level
Low, Moderate, or High.

## What You Should Monitor
Important warning signs.

## Recommended Tests
Only if necessary.

## Which Specialist to Consult

## When to Seek Urgent Care

Important:
- This is not a diagnosis.
- Do not prescribe medications.
- Keep responses concise.
- Use bullet points.
- Avoid tables.
- Recommend consulting a healthcare professional.
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
