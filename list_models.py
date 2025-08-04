# list_models.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load your GOOGLE_API_KEY from .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    models = genai.list_models()
    for model in models:
        print(f"✅ Model Name: {model.name}")
        print(f"   Supported Methods: {model.supported_generation_methods}")
        print("-" * 50)
except Exception as e:
    print("❌ Error while listing models:", e)
