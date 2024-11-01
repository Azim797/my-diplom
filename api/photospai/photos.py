from  fastapi import APIRouter,UploadFile,File
import random


photo_router = APIRouter(prefix="/photo",tags=["photos"])

@photo_router.post("/add_photo")
async def add_photo_api(post_id:int,photo_file:UploadFile = File(...)):
    file_id = random.randint(1,1000000)
    if photo_file:
        with open(f"db/photo/photo_{file_id}_{post_id}.jpg","wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
            return {"status":1,"message":"vse ok"}
    return {"status":0,"message":"error"}