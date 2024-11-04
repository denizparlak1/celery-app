# Celery S3 File Upload Service

## Overview
This is a sample FastAPI project for uploading files to Amazon S3 asynchronously using **Celery** and **Poetry** for dependency management.

## Project Structure
```plaintext
celery-app/
├── config
│   ├── celery
│   │   ├── __init__.py
│   │   └── celery_config.py        # Celery configuration
│   ├── environment
│   │   └── env_config.py           # Environment configurations
├── controller
│   └── s3
│       └── s3_controller.py        # FastAPI route for file upload
├── service
│   └── s3
│       ├── s3_config.py            # S3 connection configuration
│       └── s3_service.py           # S3 upload logic
├── tasks
│   └── uploads
│       ├── __init__.py
│       └── upload_tasks.py         # Celery tasks for file upload
├── .env                            # Environment variables
├── docker-compose.yaml             # Docker Compose configuration
├── Dockerfile                      # Docker configuration
├── main.py                         # FastAPI entry point
├── poetry.lock                     # Poetry lock file
└── pyproject.toml                  # Poetry project configuration


```
### Requirements
- Docker and Docker Compose (for running containers)
- Redis as a Celery broker
- Amazon S3 credentials in the .env file

# Setup
Clone the Repository and navigate to the project:


 
Copy code
```plaintext
 git clone https://github.com/yourusername/celery-s3-app.git
 cd celery-s3-app
``` 
Add Environment Variables in .env:

```plaintext
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
S3_BUCKET_NAME=your_s3_bucket_name
```
Install Dependencies with Poetry:

```plaintext
poetry install
```
Start Services using Docker Compose:

```plaintext
docker-compose up --build
```