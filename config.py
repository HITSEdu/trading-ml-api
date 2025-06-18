import os
from dotenv import load_dotenv
from pydantic import BaseConfig


load_dotenv()


class Config(BaseConfig):
    mistral_api_key: str = os.getenv("MISTRAL_API_KEY")
    model: str = os.getenv("MODEL")


config = Config()
