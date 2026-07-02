from dotenv import load_dotenv
import os
load_dotenv()
DEEPSEEK_API_KEY=os.getenv("DEEPSEEK_API_KEY")
BASE_URL="https://api.deepseek.com"