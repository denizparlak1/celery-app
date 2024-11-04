from fastapi import APIRouter,UploadFile,File,Depends,HTTPException
from tasks.uploads.upload_tasks import upload_file_to_s3
from service.s3.s3_service import get_s3_service
from service.s3.s3_config import get_s3_config
from service.s3.s3_config import S3Config
import logging
router = APIRouter()


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Upload a file and trigger a Celery task to process it."""
    file_content = await file.read()

    try:
        uploaded_file_path = upload_file_to_s3.delay(file_content, file.filename,file.content_type)
        return {"message": "File uploaded successfully!", "task_id": uploaded_file_path.id}
    except Exception as e:
        logging.error(f"Error during file upload: {e}")
        raise HTTPException(status_code=500, detail="File upload failed")