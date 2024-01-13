from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_venta: float
    proveedor: str

app = FastAPI()

productos = []

@app.get('/')
def index():
    return {'Mensaje' : 'Bienvenidos a la API de Productos'}