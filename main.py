import os
import json
import logging
from src.engine import get_recommendation
from src.llm_client import get_ai_message

# Setup professional logging for auditing
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("audit.log"),
        logging.StreamHandler()
    ]
)

# Robust path handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'data_schema.json')

def run():
    try:
        with open(DATA_PATH, 'r') as f:
            borrowers = json.load(f)
    except FileNotFoundError:
        logging.error(f"Data file not found at {DATA_PATH}. Please check the file path.")
        return

    logging.info("Starting Collections Strategy Optimization...")

    for b in borrowers:
        # 1. Get recommendation logic
        action, reason = get_recommendation(b)
        
        # 2. Build prompt for AI
        prompt = (f"Act as a professional collections agent. Borrower ID: {b['id']}. "
                  f"Days Past Due: {b['days_past_due']}. Action Required: {action}. "
                  f"Reason: {reason}. Generate a concise, empathetic, compliant message.")
        
        # 3. Get AI message
        message = get_ai_message(prompt)
        
        # 4. Log results
        logging.info(f"ID: {b['id']} | Action: {action} | Reason: {reason}")
        logging.info(f"Message: {message}\n")

    logging.info("Optimization complete. Check audit.log for full details.")

if __name__ == "__main__":
    run()