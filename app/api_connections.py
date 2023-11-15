"""
This file will make calls to external API => Needs modifications
External API URL: https://rapidapi.com/objectcut.api/api/background-removal/

---------------Discussed during the meeting---------------
1. Give user options to choose img output and input according to the api
2.  CRUD Operations
    Create: User img from our api will get converted to base64 from form and stored in db
    Read: Read from bd
    Update: External api call -> response output img will get stored in db
    Delete: Limit entries to 20 images; Use cookies (flask session) to store user id and limit entries. User can rm entries to add new ones.
"""

import requests
import base64
from PIL import Image
from io import BytesIO
from app.config import X_RAPID_API_KEY, X_RAPID_API_HOST


url = "https://background-removal.p.rapidapi.com/remove"


def remove_img_bg(img_base64):
    payload = {
        # "image_url": "https://objectcut.com/assets/img/raven.jpg",
        "image_base64": img_base64,
        "output_format": "base64"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": X_RAPID_API_KEY,
        "X-RapidAPI-Host": X_RAPID_API_HOST
    }

    response = requests.post(url, data=payload, headers=headers)

    image_output_base64 = response.json()["response"]["image_base64"]

    def base64_to_image(base64_string):
        base64_string = base64_string.split(',', 1)[-1]
        image_data = base64.b64decode(base64_string)
        image = Image.open(BytesIO(image_data))
        return image

    image = base64_to_image(image_output_base64)

    image.save("./test/output_image.png")
