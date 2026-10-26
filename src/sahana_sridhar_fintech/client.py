import requests
from .config import config


def fetch_live_data() -> dict:
    config.validate()

    url = "https://api.stripe.com/v1/balance"
    headers = {
        "Authorization": f"Bearer {config.api_key}"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    available = data.get("available", [{}])[0]

    return {
        "status": "LIVE_SUCCESS",
        "currency": available.get("currency", "usd").upper(),
        "available_balance": available.get("amount", 0) / 100.0,
        "livemode": data.get("livemode", False),
    }