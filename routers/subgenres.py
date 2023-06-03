from fastapi import APIRouter
from pydantic import BaseModel
from db.conection import getAllSubgenresFromDB
from db.schemas.subgenre import subgenre_schema, subgenres_schema

router = APIRouter(prefix="/api/subgenres")

  
@router.get("/")
async def getSubgenres():
  return subgenres_schema(getAllSubgenresFromDB())

 
  