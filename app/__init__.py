from flask import Flask
import base64
from .api_connections import remove_img_bg

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

    app = Flask(__name__)
    
    # Healthy Connection 
    @app.route('/')
    def health():
        return {"status": "Healthy"}


    # Testing api_connections integration
    @app.route("/test-bg-remover")
    def test_bg_remover():
        try:
            with open("test/raven.jpg", "rb") as img_file: 
                img_data = img_file.read()
                img_base64 = base64.b64encode(img_data)
            
            remove_img_bg(img_base64)
            return {"status": "Success"}

        except Exception as e:
            return {"error": f"{e}"}

    return app
