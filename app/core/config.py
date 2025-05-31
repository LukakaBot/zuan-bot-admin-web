from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=[".env", ".env.local", ".env.development", ".env.production"],
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    # 服务名称
    SERVICE_PROJECT_NAME: str
    # 服务地址
    SERVICE_HOST: str
    # 服务端口
    SERVICE_PORT: int
    # 接口前缀
    SERVICE_API_PREFIX: str


settings = Settings()
