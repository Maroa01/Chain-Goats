from pydantic import BaseSettings
from decouple import config
from pathlib import Path

# Use this to build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Class to hold application's configuration values."""

    API_V1_STR: str = "/api/v1"
    APP_NAME: str = "ChainGoats"

    # Database
    DB_HOST: str = config("DB_HOST")
    DB_PORT: int = config("DB_PORT", cast=int)
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = config("DB_PASSWORD")
    DB_NAME: str = config("DB_NAME")
    TEST_DB_NAME: str = config("TEST_DB_NAME", default="chain_goats_test_db")
    DB_TYPE: str = config("DB_TYPE")





settings = Settings()