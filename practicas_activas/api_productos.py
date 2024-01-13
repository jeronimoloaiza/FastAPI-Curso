from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class ProductClass(BaseModel):
    id: Optional[str] = None
    nombre: str
    precio_venta: float
    proveedor: str

app = FastAPI()

product_list = []

@app.get('/')
def index():
    return {'Mensaje' : 'Bienvenidos a la API de Productos'}

@app.get('/producto')
def obtener_productos():
    return product_list

@app.post('/producto')
def crear_producto(new_product: ProductClass):
    product_list.append(new_product)
    return {'Mensaje': 'Producto creado satisfactoriamente'}