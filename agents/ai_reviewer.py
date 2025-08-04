# agents/ai_reviewer.py

import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "openai").lower()

# Set up model-specific client
if MODEL_PROVIDER == "openai":
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

elif MODEL_PROVIDER == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

else:
    raise ValueError("Unsupported MODEL_PROVIDER. Use 'openai' or 'gemini'.")

def review_chapter(original: str, rewritten: str) -> str:
    """
    Compares the original and rewritten content, returning constructive editorial feedback.

    Args:
        original (str): Original scraped content.
        rewritten (str): AI-generated rewritten content.

    Returns:
        str: Review feedback including score and suggestions.
    """
    if not original or not rewritten:
        return "❌ Missing original or rewritten content."

    prompt = f"""
You are a professional editor. Compare the following original and rewritten content.
Provide a score out of 10 and list clear suggestions for improving the rewritten version.

Original:
{original[:2000]}

Rewritten:
{rewritten[:2000]}
"""

    try:
        if MODEL_PROVIDER == "openai":
            print("🔍 Reviewing with OpenAI GPT...")
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a meticulous editor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5
            )
            return response['choices'][0]['message']['content'].strip()

        elif MODEL_PROVIDER == "gemini":
            print("🔍 Reviewing with Gemini model...")
            response = gemini_model.generate_content(prompt)
            return response.text.strip() if response and hasattr(response, "text") else "⚠️ No response from Gemini model."

    except Exception as e:
        return f"⚠️ Error during review: {e}"
