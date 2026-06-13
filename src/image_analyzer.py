import os
import torch

from PIL import Image
from dotenv import load_dotenv
from openai import OpenAI

from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration
)

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def analyze_image(image_file):

    image = Image.open(
        image_file
    ).convert("RGB")

    inputs = processor(
        image,
        return_tensors="pt"
    )

    with torch.no_grad():

        output = model.generate(
            **inputs,
            max_new_tokens=50
        )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    prompt = f"""
You are an AI healthcare assistant.

Image Description:
{caption}

Provide:

1. Visible Findings
2. Possible Concerns
3. Recommendations

Important:
- This is not a diagnosis.
- Recommend consulting a doctor.
- Mention if the image description is unclear.
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

    return f"""
### Image Description

{caption}

---

{response.choices[0].message.content}
"""
