from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str
    AWS_REGION: str

    class Config:
        env_file = ".env"

settings = Settings()
