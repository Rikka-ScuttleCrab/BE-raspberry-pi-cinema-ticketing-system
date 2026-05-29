import os

from dotenv import load_dotenv

load_dotenv()

SECRET_ROLE_KEY = os.getenv(
    "SECRET_ROLE_KEY"
)