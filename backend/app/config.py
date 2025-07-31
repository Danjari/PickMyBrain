from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    EMAIL_USER: str
    EMAIL_PASS: str
    API_SECRET_KEY: str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()