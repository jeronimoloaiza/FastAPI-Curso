def process_items(prices: dict[str, float]):
    for name, price in prices.items(): #La función .items() para diccionarios entrega la llave y el valor
        print(name, price)