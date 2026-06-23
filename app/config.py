from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+aiomysql://bob_user:bob_password@localhost:3306/bob_db"
    DATABASE_SYNC_URL: str = "mysql+pymysql://bob_user:bob_password@localhost:3306/bob_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    HOST: str = "0.0.0.0"
    PORT: int = 9102
    DEBUG: bool = True

    # RAG Settings
    RAG_API_URL: str = "https://aai.c-zentrixcloud.com/utils/query"
    RAG_ID: str = "c082962a-e522-4e94-a21b-6bb220dd3e89"

    # BoB URLs
    BOB_WEBSITE_URL: str = "https://www.bob.bt/"
    BOB_SUPPORT_URL: str = "https://www.bob.bt/service-and-support/"
    BOB_DOWNLOAD_FORMS_URL: str = "https://www.bob.bt/service-and-support/download-forms/"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
