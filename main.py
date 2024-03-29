from fastapi import FastAPI
from typing import Union
from models.item_model import Item


#Creación de una aplicación en FastAPI:
app = FastAPI()

#Métodos get
@app.get('/')
def read_root():
    return {"Hello": "World!"}

@app.get('/hola')
def hola_mundo():
    return {"hola":"mundo"}

@app.get('/items/{item_id}') #Lo que va en corchetes es algo variable
def read_item(item_id: int, name:Union[str, None] = None):
    return {'item_id': item_id, 'name': name}

@app.get('/calculadora')
def calcular(operando_1: float, operando_2: float):
    return {'suma': operando_1 + operando_2}

#Métodos put
@app.put('/items/{item_id}') #Put, para actualizar datos
def update_item(item_id: int, item: Item):
    return {'item_name' : item.name, 'item_id': item_id, 'item_price': item.price}