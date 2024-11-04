import logging
from fastapi import Depends
from config.celery.celery_config import celery_app
from service.s3.s3_config import S3Config
from service.s3.s3_service import S3Service


@celery_app.task
def upload_file_to_s3(file_content: bytes, filename: str,content_type: str):
    """Upload a file to S3 using the S3Service.

    Args:
        file_content (bytes): The content of the file to be uploaded.
        filename (str): The name of the file to be uploaded.

    Returns:
        str: The path of the uploaded file.
        :param filename:
        :param content_type:
    """
    s3_config = S3Config()
    s3_service = S3Service(s3_config)
    try:
        uploaded_file_path = s3_service.upload_file(filename, file_content,content_type)
        return uploaded_file_path
    except Exception as e:
        logging.error(f"Error during file upload: {e}")
        raise
