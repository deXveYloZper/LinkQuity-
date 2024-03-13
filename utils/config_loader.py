# /utils/config_loader.py

from dotenv import load_dotenv
import os

load_dotenv()

def get_api_key(api_name):
    """Retrieves an API key from environment variables."""
    return os.getenv(api_name)
