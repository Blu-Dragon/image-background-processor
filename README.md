# image-background-processor

A REST-API application built with Flask Framework

### Virtual Environment Setup
* venv on Windows
1. `py -m pip install --upgrade pip`
2. `py -m pip install --user virtualenv`
3. `py -m venv env`
4. `.\env\Scripts\activate`
5. `deactivate`

* venv on Unix/macOS
1. `python3 -m pip install --user --upgrade pip`
2. `python3 -m pip install --user virtualenv`
3. `python3 -m venv ./venv`
4. `source ./venv/bin/activate`
5. `deactivate`

### Installing Packages
`pip install -r requirements.txt`

### Create .env
Create a file named `.env` ; which contents same as `.env.example`

### Run Flask Application Using
1. `export FLASK_APP=app.py`
2. `export FLASK_ENV=development`  (Use this command in development phase)
3. `flask run`

#### Note : 
Secret Key is needed for flashing purpose in flask. Make sure to add it in a seperate config or env file.