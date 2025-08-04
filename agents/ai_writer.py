# agents/ai_writer.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "openai").lower()

# Set up model-specific clients
if MODEL_PROVIDER == "openai":
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

elif MODEL_PROVIDER == "gemini":
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

else:
    raise ValueError("Unsupported MODEL_PROVIDER. Use 'openai' or 'gemini'.")

def generate_chapter(content: str) -> str:
    """
    Rewrites the given content creatively using either OpenAI or Gemini.
    """
    if not content:
        return "❌ No content provided."

    prompt = f"Rewrite this content creatively:\n\n{content[:3000]}"

    try:
        if MODEL_PROVIDER == "openai":
            print("✍️ Rewriting with OpenAI GPT...")
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative ghostwriter."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response['choices'][0]['message']['content'].strip()

        elif MODEL_PROVIDER == "gemini":
            print("✍️ Rewriting with Gemini model...")
            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text.strip() if response and hasattr(response, "text") else "⚠️ No response from Gemini."

    except Exception as e:
        return f"⚠️ Error in generate_chapter: {e}"
