
import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path.cwd() / ".env")


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    api_key: str = os.getenv("STRIPE_API_KEY", "")

    debug: bool = os.getenv("DEBUG", "False").lower() in (
        "true", "1", "yes"
    )

    def validate(self):
        if not self.api_key or self.api_key == "STRIPE_API_KEY":
            raise ValueError(
                "Stripe API key is missing. Check your .env file."
            )


config = Settings()
