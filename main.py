from fastapi import FastAPI
from routes import usuarios, admin, estudiantes, profesores

app = FastAPI()

""" AGREGANDO RUTAS """

app.include_router(admin.router)
app.include_router(usuarios.router)
app.include_router(estudiantes.router)
app.include_router(profesores.router)


@app.get("/")
async def root():
    return {
        "mensaje": "Bienvenido"
    }