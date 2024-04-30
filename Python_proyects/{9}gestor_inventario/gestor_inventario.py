#inventario en python
productos_tienda={'papa':30,
                  'yuca':21}

while True :
    print("agrega un producto con 1")
    print("edita  un producto con 2")
    print("elimina un producto con 3")
    print("muestra todos los productos 4")
    print("salir con 5")

    opción_cliente=int(input("-> "))

    if (opción_cliente==1):
        nuevo_producto_name=input("ingresa el nombre del nuevo producto -> ")
        nuevo_producto_val=int(input("ingresa la cantidad del nuevo producto -> "))
        productos_tienda[nuevo_producto_name]=nuevo_producto_val
    elif(opción_cliente==2):
        producto_act=input("escriba el nombre del valor a actualizar ")
        if producto_act in productos_tienda:
            productos_tienda[producto_act]=int(input("ingresa el valor nuevo del producto -> "))
        else:
            print("la palabra recibida no coincide con el inventario ")
    elif(opción_cliente==3):
        eliminar_product=input("ingrese el producto a eliminar -> ")
        if eliminar_product in productos_tienda:
            del productos_tienda[eliminar_product]
        else:
            print("la palabra recibida no coincide con el inventario ")
    elif(opción_cliente==4):
        print(productos_tienda)
    elif(opción_cliente==5):
        break
    else:
        print("opción no valida, escriba otra ves el numero")