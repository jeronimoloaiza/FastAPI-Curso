def say_hi(name: str|None = None):
    if name is not None:
        print(f'hi {name}!')
    else:
        print('Hello World')

