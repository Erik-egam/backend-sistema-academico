from fastapi import FastAPI
from routes import usuarios

app = FastAPI()

""" AGREGANDO RUTAS """

app.include_router(usuarios.router)

@app.get("/")
async def root():
    return {
        "mensaje": "Bienvenido"
    }