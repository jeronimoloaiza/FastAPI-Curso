from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 as uuid

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
    new_product.id = str(uuid())
    product_list.append(new_product)
    return {'Mensaje': 'Producto creado satisfactoriamente'}

@app.get('/producto/{product_id}')
def obtener_producto_por_id(product_id: str):
    for p in product_list:
        if p.id == product_id:
            return p
    return {'Mensaje' : f'El producto con el id {product_id} no fue encontrado'}
