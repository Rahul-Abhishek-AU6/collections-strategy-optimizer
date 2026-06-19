import os
import requests
import sys
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TOKEN = os.getenv("LLM_API_TOKEN")
URL = "https://llm-wrapper-741152993481.asia-south1.run.app/llm/query"

def test_connection():
    if not TOKEN:
        print("Error: LLM_API_TOKEN not found in environment variables.")
        print("Please export it or set it in your .env file.")
        return

    headers = {
        "Authorization": f"Bearer {TOKEN.strip()}", 
        "Content-Type": "application/json"
    }
    payload = {"prompt": "Hello. Reply in one short sentence."}
    
    print(f"Testing connection to: {URL}")
    try:
        response = requests.post(URL, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    test_connection()