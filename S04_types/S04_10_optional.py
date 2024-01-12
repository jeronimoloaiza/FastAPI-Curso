from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f'hi {name}!')
    else:
        print('Hello World')

#Esto hace que el parámetro name sea opcional ponerlo. En caso de no hacerlo se printea 'Hello world'
        
say_hi()
say_hi('Jero')