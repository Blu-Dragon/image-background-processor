from flask import Flask, render_template, request
import base64
from .api_connections import remove_img_bg
from flask_bootstrap import Bootstrap

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
    bootstrap = Bootstrap(app)

    # # Healthy Connection 
    # @app.route('/')
    # def health():
    #     return render_template('index.html')
    #     # return {"status": "Healthy"}

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            name = request.form['name']
            image = request.files['image'].read()
            img_base64 = base64.b64encode(image)
            remove_img_bg(img_base64)

        return render_template('index.html')

    # Testing api_connections integration
    @app.route("/test-bg-remover")
    def test_bg_remover():
        try:
            with open("test/jarvis.jpg", "rb") as img_file: 
                img_data = img_file.read()
                img_base64 = base64.b64encode(img_data)
            
            remove_img_bg(img_base64)
            return {"status": "Success"}

        except Exception as e:
            return {"error": f"{e}"}

    return app
