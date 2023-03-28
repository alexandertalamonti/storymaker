from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
print(API_KEY)