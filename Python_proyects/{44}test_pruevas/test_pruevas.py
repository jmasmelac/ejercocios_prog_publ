def calculo_total(products):
    total = 0
    for product in products:
        total += product['price'] 
    return total

def test_calculo_total_lista_vacía():
    print('test_calculo_total_lista_vacía')
    assert calculo_total([]) == 0

def calculo_total_productos():
    products = [
        {'name': 'Jabón', 'price': 10},
        {'name': 'Shampoo', 'price': 20},
        {'name': 'Crema', 'price': 30},
    ]
    print(calculo_total(products))
    assert calculo_total(products) == 60

if __name__ == '__main__':
    test_calculo_total_lista_vacía()