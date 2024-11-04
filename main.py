from fastapi import FastAPI
from controller.s3 import s3_controller
app = FastAPI()


app.include_router(s3_controller.router, prefix="/api/content",tags=["File Upload"])
