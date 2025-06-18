from mistralai import Mistral

from config import config
from constants import SUMMARIZATION_PROMPT


async def analyze(text: str):
    client = Mistral(api_key=config.mistral_api_key)
    chat_response = client.chat.complete(
        model=config.model,
        messages=[
            {
                "role": "user",
                "content": f"Текст для суммаризации:\n{text}\n\nЗадание:\n{SUMMARIZATION_PROMPT}",
            },
        ]
    )
    return chat_response.choices[0].message.content


async def parse_analysis(analysed_text: str):
    ...