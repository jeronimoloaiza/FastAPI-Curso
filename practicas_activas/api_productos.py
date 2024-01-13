from typing import Optional
from fastapi import FastAPI, HTTPException
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
#    for p in product_list:
#        if p.id == product_id:
#            return pfrom http.client import 
    resultado = list(filter(lambda p: p.id == product_id, product_list ))

    if len(resultado): #Lo mismo que if len(resultado) > 0:
        return resultado

    raise HTTPException(status_code=404, detail=f'El producto con la id {product_id} no fue encontrado')


@app.delete('/producto/{product_id}')
def eliminar_profucto_por_id(product_id:str):
    resultado = list(filter(lambda p: p.id == product_id, product_list ))

    if len(resultado):
        producto = resultado[0]
        product_list.remove(producto)

        return {'Mensaje' : f'El producto con la id {product_id} fue eliminado'}
    
    raise HTTPException(status_code=404, detail=f'El producto con la id {product_id} no fue encontrado')
