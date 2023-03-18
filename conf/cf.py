from os import environ

from dotenv import load_dotenv
from pydantic import BaseModel
from logzero import loglevel


class AppConfig(BaseModel):
    APP_NAME: str = 'stock-api'
    APP_HOST: str = '0.0.0.0'
    APP_PORT: int = 2100
    LOG_LEVEL: int = 10

    REDIS_URL: str
    PSQL_URL: str
    GATEWAY_URL: str


def load_config() -> AppConfig:
    load_dotenv()
    config = AppConfig(**environ)
    loglevel(level=config.LOG_LEVEL)
    return config


CONFIG = load_config()
