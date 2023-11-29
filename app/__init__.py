# In-bulit lib imports
import base64
from datetime import datetime
from bson import ObjectId
from bson.json_util import dumps, loads

# Flask imports
from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    make_response,
    jsonify
)

# Application imports
from .api_connections import remove_img_bg
from .config import *

# Creating Flask instance
app = Flask(__name__)

# Secret key is needed for Flashing
app.secret_key = APP_SECRET_KEY

# Application imports
from .db_connections import DataBase

DataBase = DataBase()

# Logging: When required
# try:
#     logging.basicConfig(
#         filename="error_logs.log",
#         format="%(asctime)s %(levelname)-8s %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S",
#         level=logging.WARNING,
#     )
# except Exception as e:
#     print(f"Failed to initialize logging: {e}")


# Connection health check
@app.get("/health")
def health():
    return {"status": "Healthy"}


# Read
@app.get("/")
def index_page():
    # Set cookies if None
    if request.cookies.get("user_id") is None:
        resp = make_response(render_template("index.html"))
        user_id = str(ObjectId())
        resp.set_cookie("user_id", user_id)
        return resp

    # Check if user data exists
    user_id = request.cookies.get("user_id")

    # Fetch user data
    fetched_data = DataBase.read_data({'user_id': user_id})
    # Convert curser object to string
    json_string = dumps(fetched_data)
    # Convert the JSON string to a Python object
    data = loads(json_string)

    return render_template("index.html", data=data)


# Create
@app.post("/")
def index_form():
    try:
        # Fetching form contents
        name = request.form["name"]
        image = request.files["image"].read()

        # Reading cookies; user id
        user_id = request.cookies.get("user_id")

        # Check user records count
        count = DataBase.records_count({'user_id': user_id})

        # Setting max user limit
        if count >= USER_LIMIT:
            flash("Max limit reached. Please remove a record.", MESSAGE_TYPE_DANGER)
            return redirect(url_for("index_page"))

        # Converting image to base64
        img_base64 = base64.b64encode(image)

        # Function call to external api
        processed_image = remove_img_bg(img_base64)

        if processed_image:

            data = {
                "user_id": user_id,
                "image_name": name,
                "image_base64": processed_image,
                "created_on": str(datetime.today().replace(microsecond=0))
            }

            DataBase.create_data(data)

            flash("Image generated successfully", MESSAGE_TYPE_SUCCESS)
            return redirect(url_for("index_page"))

        flash("Failed to generate the image", MESSAGE_TYPE_DANGER)
        return redirect(url_for("index_page"))

    except Exception as e:
        print(f"Error: {e}")
        flash("Something went wrong", MESSAGE_TYPE_DANGER)
        return redirect(url_for("index_page"))


# Update
@app.put("/update/<string:record_id>")
def update_data(record_id):
    try:
        record_id = request.json.get("record_id")
        record_name = request.json.get("record_name")

        # Editing image name
        DataBase.update_processed_data(record_id, {"image_name": record_name})
        return jsonify({"message":"success"})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message":"error while editing"})

# Delete
@app.delete('/remove/<string:record_id>')
def remove_data(record_id):
    try:
        # Deleting entry from db
        DataBase.delete_processed_data(record_id)
        return jsonify({"message":"success"})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message":"error while deleting"})

if __name__ == "__main__":
    app.run(debug=True)
