from fastapi import FastAPI
from routers import subgenres
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Routers
app.include_router(subgenres.router)

@app.get("/")
async def root():
    return {"message": "Rythmiq API working on port 8000"}
