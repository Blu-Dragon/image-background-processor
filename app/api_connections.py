"""
This file will make calls to external API
External API URL: https://rapidapi.com/objectcut.api/api/background-removal/
"""

import requests
import base64
from PIL import Image
from io import BytesIO
from app.config import X_RAPID_API_KEY, X_RAPID_API_HOST


url = "https://background-removal.p.rapidapi.com/remove"


def remove_img_bg(img_base64):
    payload = {
        "image_base64": img_base64,
        "output_format": "base64"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": X_RAPID_API_KEY,
        "X-RapidAPI-Host": X_RAPID_API_HOST
    }

    res = requests.post(url, data=payload, headers=headers)

    if res.status_code == 400:
        return False

    try:
        response = res.json().get("response")
        image_output_base64 = response.get("image_base64")
        
    except Exception as e:
        print(e)
        return False

    # Return False if response is Null/None
    if image_output_base64 is None:
        return False

    return image_output_base64
