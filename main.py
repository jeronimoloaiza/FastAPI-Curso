from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

#Creación de una aplicación en FastAPI:
app = FastAPI()

class item(BaseModel):
    name: str
    price: float
    is_in_offer: Union[bool, None] = None

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