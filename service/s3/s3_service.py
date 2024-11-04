import io
import boto3
from fastapi import Depends
from service.s3.s3_config import S3Config
from service.s3.s3_config import get_s3_config


class S3Service:
    """Service for handling operations with Amazon S3."""

    def __init__(self, config: S3Config):
        """Initialize the S3 client and set the bucket name."""
        self.client = boto3.client(
            's3',
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_access_key,
            region_name=config.region_name
        )
        self.bucket_name = config.bucket_name

    def upload_file(self, file_path: str, file_content: bytes, content_type: str = None) -> str:
        """Upload a file to S3.

        Args:
            file_path (str): The path where the file will be stored in the S3 bucket.
            file_content (bytes): The content of the file to be uploaded.
            content_type (str, optional): The content type of the file.

        Returns:
            str: The path of the uploaded file.

        Raises:
            Exception: If the upload fails.
        """
        try:
            self.client.upload_fileobj(
                io.BytesIO(file_content),
                self.bucket_name,
                file_path,
                ExtraArgs={"ContentType": content_type}
            )
            return file_path
        except Exception as e:
            raise Exception(f"Failed to upload file to S3: {e}") from e


def get_s3_service(config: S3Config = Depends(get_s3_config)) -> S3Service:
    """Dependency injection for S3Service.

    Args:
        config (S3Config): The S3 configuration object.

    Returns:
        S3Service: An instance of the S3Service.
    """
    return S3Service(config)
