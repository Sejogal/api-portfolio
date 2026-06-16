from fastapi import FastAPI
from routes import formulario_router

app = FastAPI()

app.include_router(formulario_router)


