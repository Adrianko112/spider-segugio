# config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
 
    # Completamento
    ### ollama
    # LLM_MODEL = "llama3.2"
    # LLM_MODEL_LOW = "llama3.2"
    # AI_API_URL = "http://localhost:11434/v1"
    # AI_API_KEY = "ollama"

    ### openai
    LLM_MODEL = "gpt-4o-mini"       
    LLM_MODEL_LOW = "gpt-4o-mini"   
    AI_API_URL = "https://api.openai.com/v1/"
    AI_API_KEY = os.getenv("OPENAI_API_KEY")