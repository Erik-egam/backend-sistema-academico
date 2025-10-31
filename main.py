from fastapi import FastAPI
from routes import usuarios, admin

app = FastAPI()

""" AGREGANDO RUTAS """

app.include_router(usuarios.router)
app.include_router(admin.router)

@app.get("/")
async def root():
    return {
        "mensaje": "Bienvenido"
    }