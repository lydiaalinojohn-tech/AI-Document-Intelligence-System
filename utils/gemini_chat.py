import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def ask_gemini(question, context):

    prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the information below.

DOCUMENT:

{context}

QUESTION:

{question}

ANSWER:
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text