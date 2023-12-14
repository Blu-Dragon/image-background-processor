# image-background-processor

A REST-API application built with Flask Framework

---

### Virtual Environment Setup

| **Windows Commands** | **Linux Commands** |
|----------------------|--------------------|
| 1. `py -m pip install --upgrade pip` | 1. `python3 -m pip install --user --upgrade pip` |
| 2. `py -m pip install --user virtualenv` | 2. `python3 -m pip install --user virtualenv` |
| 3. `py -m venv env` | 3. `python3 -m venv ./venv` |
| 4. `.\env\Scripts\activate` (command to activate venv) | 4. `source ./venv/bin/activate` (command to activate venv) |
| 5. `deactivate` (command to deactivate venv) | 5. `deactivate` (command to deactivate venv) |

---

### Installing Packages
`pip install -r requirements.txt`

### Create .env
Create a file named `.env` ; copy contents from `.env.example` and replace them with your key-value pairs

---

### Run Flask Application Using
1. `export FLASK_APP=app.py`
2. `export FLASK_ENV=development`  (Use this command in development phase)
3. `flask run`

---

##
Cloud Build Setup
1. Enable Google Build API: https://cloud.google.com/build/docs/api/reference/rest
2. Install `gcloud`: https://cloud.google.com/sdk/docs/install-sdk
3. Connect to REPO: https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github?generation=2nd-gen
4. Build REPO: https://cloud.google.com/build/docs/automating-builds/github/build-repos-from-github?generation=2nd-gen
5. Build triggers: https://cloud.google.com/build/docs/automating-builds/create-manage-triggers
6. Automate deployment: https://cloud.google.com/kubernetes-engine/docs/how-to/automated-deployment


---

# API Documentation

## Connection Health Check

### Endpoint

- **URL**: `/health`
- **Method**: GET

### Description

This endpoint checks the health status of the connection.

### Response

- **Status Code**: 200 OK
- **Response Body**:
    ```json
    {
        "status": "Healthy"
    }
    ```

---

## Read Data

### Endpoint

- **URL**: `/`
- **Method**: GET

### Description

This endpoint serves an index page. It performs the following actions:

1. If the user's cookies do not contain a `"user_id"`, it sets a new cookie with a generated user ID.
2. If the user data exists, it fetches the data associated with the user ID.
3. The fetched data is converted from a cursor object to a JSON string and then to a Python object.

### Request

- No specific request parameters.

### Response

- **Status Code**: 200 OK
- **Response Body** (example):
    ```json
    {
        "user_id": "123456",
        "username": "john_doe",
        "email": "john@example.com"
    }
    ```

## Create Data

### Endpoint

- **URL**: `/`
- **Method**: POST

### Description

This endpoint allows users to submit form data, including an image. It performs the following actions:

1. Fetches the form contents, including the user's name and the uploaded image.
2. Reads the user's cookies to retrieve the `"user_id"`.
3. Checks the user's records count to ensure it doesn't exceed a predefined limit (`USER_LIMIT`).
4. Converts the image to base64 format.
5. Calls an external API (`remove_img_bg`) to process the image.
6. If successful, creates a new record with the following data:
    - `user_id`: Unique identifier for the user.
    - `image_name`: Name associated with the image.
    - `original_image_base64`: Base64-encoded original image.
    - `processed_image_base64`: Base64-encoded processed image.
    - `created_on`: Timestamp of when the record was created.

### Request

- **Form Parameters**:
    - `name`: Image name (from the form).
    - `image`: Uploaded image file.

### Response

- **Status Code**: 302 Found (redirect)
- **Flash Messages**:
    - If the image is generated successfully: "Image generated successfully" (success message).
    - If there's an issue with image processing: "Failed to generate the image" (danger message).
    - If the user has reached the maximum limit: "Max limit reached. Please remove a record." (danger message).
    - If an unexpected error occurs: "Something went wrong" (danger message).

## Update Data

### Endpoint

- **URL**: `/update/<string:record_id>`
- **Method**: PUT

### Description

This endpoint allows users to update an existing record identified by its `record_id`. It performs the following actions:

1. Retrieves the `record_id` and the new `record_name` from the request JSON.
2. Edits the image name associated with the specified record.

### Request

- **URL Parameters**:
    - `record_id`: Unique identifier for the record to be updated.
- **Request Body** (JSON):
    ```json
    {
        "record_id": "123456",
        "record_name": "New Image Name"
    }
    ```

### Response

- **Status Code**: 200 OK
- **Response Body**:
    ```json
    {
        "message": "success"
    }
    ```

---

## Delete Data

### Endpoint

- **URL**: `/remove/<string:record_id>`
- **Method**: DELETE

### Description

This endpoint allows users to remove an existing record identified by its `record_id`. It performs the following actions:

1. Deletes the specified record from the database.

### Request

- **URL Parameters**:
    - `record_id`: Unique identifier for the record to be deleted.

### Response

- **Status Code**: 200 OK
- **Response Body**:
    ```json
    {
        "message": "success"
    }
    ```

---

# Image Data Schema

This schema represents the structure of an image data document stored in the MongoDB database.

| **Field**                | **Description**                                                                                     |
|--------------------------|-----------------------------------------------------------------------------------------------------|
| `_id`                    | Unique identifier for the image data document (automatically generated by MongoDB).                |
| `user_id`                | User ID associated with the image.                                                                  |
| `image_name`             | Name or label for the image.                                                                        |
| `original_image_base64`  | Base64-encoded representation of the original image.                                                |
| `processed_image_base64` | Base64-encoded representation of the processed image (after applying some operation or filter).   |
| `created_on`             | Timestamp indicating when the record was created (formatted as "YYYY-MM-DD HH:MM:SS").              |

---