def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + 'is this old:' + age
    return name_with_age

print(get_name_with_age('jeronimo', 5))