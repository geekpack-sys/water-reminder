import os
import requests

NTFY_URL = f"https://ntfy.sh/{os.environ['NTFY_TOPIC']}"
DOG_API = "https://dog.ceo/api/breeds/image/random"


def get_dog_image():
    try:
        r = requests.get(DOG_API, timeout=10)
        r.raise_for_status()
        return r.json()["message"]
    except (requests.RequestException, KeyError, ValueError):
        return None


def drinkWater():
    headers = {
        "Priority": "4",
        "Tags": "potable_water,dog",
        "Title": "Drink water!",
    }

    dog = get_dog_image()
    if dog:
        headers["Attach"] = dog

    r = requests.post(
        NTFY_URL,
        data="Time to drink water! 🚰".encode("utf-8"),
        headers=headers,
        timeout=10,
    )
    r.raise_for_status()


if __name__ == "__main__":
    drinkWater()