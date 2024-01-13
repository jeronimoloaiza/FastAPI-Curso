from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id : int
    name: str = 'Jerónimo Loaiza'
    signup_ts: datetime | None = None
    friends: list[int] = []

#Desde el exterior podríamos recibir estos datos:
external_data = {
    'id': 1001,
    'signup_ts' : datetime.strptime('2024-1-12 16:46', '%Y-%m-%d %H:%M'), #Para formato datetime
    'friends' : [1002, 1003, 1004]
}
user = User(**external_data )

print('------------------------------------------------------')
print(user)
print('------------------------------------------------------')
print('id = ', user.id)
print('name = ',user.name)
print('time = ', user.signup_ts)
print('friends = ', user.friends)