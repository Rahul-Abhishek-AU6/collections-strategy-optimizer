import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("LLM_API_TOKEN")
URL = "https://llm-wrapper-741152993481.asia-south1.run.app/llm/query"

def get_ai_message(prompt_context):
    headers = {"Authorization": f"Bearer {TOKEN.strip()}", "Content-Type": "application/json"}
    payload = {"prompt": prompt_context}
    
    response = requests.post(URL, json=payload, headers=headers)
    if response.status_code == 201:
        return response.json().get("response")
    return "Fallback: Please contact our support team regarding your account."