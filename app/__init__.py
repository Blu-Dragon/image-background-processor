# In-bulit lib imports
import base64

# Flask imports
from flask import Flask, render_template, request, flash, redirect, url_for

# Application imports
from .api_connections import remove_img_bg
from .config import *

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


def create_app():
    # Creating Flask instance
    app = Flask(__name__)
    # Secret key is needed for Flashing
    app.secret_key = APP_SECRET_KEY

    # Connection health check
    @app.get('/health')
    def health():
        return {"status": "Healthy"}

    # Read
    @app.get('/')
    def index_page():
        return render_template('index.html')

    # Create
    @app.post('/')
    def index_form():
        try:
            # Fetching form contents
            name = request.form['name']
            image = request.files['image'].read()

            # Converting image to base64
            img_base64 = base64.b64encode(image)

            # Function call to external api
            if remove_img_bg(img_base64):
                flash("Image generated successfully", MESSAGE_TYPE_SUCCESS)
                return render_template('index.html')

            flash("Failed to generate the image", MESSAGE_TYPE_DANGER)
            return redirect(url_for('index_page'))
        
        except Exception as e:
            print(f"Error: {e}")
            flash("Something went wrong", MESSAGE_TYPE_DANGER)
            return redirect(url_for('index_page'))

    # Update
    @app.put('/update')
    def update_data():
        pass

    # Delete
    @app.delete('/remove')
    def remove_data():
        pass

    # Testing api_connections integration
    # @app.route("/test-bg-remover")
    # def test_bg_remover():
    #     try:
    #         with open("test/jarvis.jpg", "rb") as img_file: 
    #             img_data = img_file.read()
    #             img_base64 = base64.b64encode(img_data)
            
    #         remove_img_bg(img_base64)
    #         return {"status": "Success"}

    #     except Exception as e:
    #         return {"error": f"{e}"}

    return app
