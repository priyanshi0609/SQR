import os
import traceback
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print("✅ llm_service.py is being loaded")
print("🔑 GEMINI_API_KEY Loaded:", bool(GEMINI_API_KEY))

# Configure API key
genai.configure(api_key=GEMINI_API_KEY)

# Try with 2.5-flash, but fallback to 1.5-flash if needed
MODEL_NAME = "gemini-2.5-flash"

async def ask_llm(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "❌ Gemini API key not found. Check your .env file."

    try:
        # Attempt to get the model (may fail if model doesn't exist)
        model = genai.GenerativeModel(model_name=MODEL_NAME)
        response = model.generate_content(prompt)

        # If you need async behavior, switch to sync-to-async bridge or use threads
        return response.text

    except Exception as e:
        print("🔥 Exception while generating content:")
        print(traceback.format_exc())

        # Optional fallback logic
        if "not found" in str(e).lower():
            return "❌ Model 'gemini-2.5-flash' not available. Try 'gemini-1.5-flash' or 'pro'."
        return f"❌ Exception: {str(e) or 'Unknown error'}"
