from typing import Union
from pydantic import BaseModel

#Creación de modelo personalizado
class Item(BaseModel):
    name: str
    price: float
    is_in_offer: Union[bool, None] = None