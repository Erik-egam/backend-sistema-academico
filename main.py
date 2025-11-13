from fastapi import FastAPI
from routes import usuarios, admin, estudiantes, profesores
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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