import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(f"Key: {GEMINI_API_KEY[:5]}...{GEMINI_API_KEY[-5:] if GEMINI_API_KEY else 'None'}")

if not GEMINI_API_KEY:
    print("No key found")
    exit(1)

try:
    genai.configure(api_key=GEMINI_API_KEY)
    with open('models.txt', 'w') as f:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                f.write(m.name + '\n')
    print("Models listed to models.txt")
except Exception as e:
    print(f"Error: {e}")
