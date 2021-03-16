from fastapi import APIRouter, UploadFile, File

from database.models import ForceAccountPackage

router = APIRouter()


@router.post('/packages', response_model=ForceAccountPackage)
async def create_package(file: UploadFile = File(...)):
    return {"filename": file.filename}
