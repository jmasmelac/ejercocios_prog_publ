"""
Este proyecto está licenciado bajo una Licencia Creative Commons Atribución-NoComercial 4.0 Internacional.
 Puedes:
 - Compartir: copiar y redistribuir el material en cualquier medio o formato.
 - Adaptar: remezclar, transformar y construir sobre el material.
 Bajo las siguientes condiciones:
 - Atribución: debes dar crédito adecuado, proporcionar un enlace a la licencia e indicar si se realizaron cambios.
    No puedes sugerir que el licenciante te respalda a ti o al uso que hagas del material.
 - NoComercial: no puedes utilizar el material con fines comerciales.
 Puedes encontrar una copia completa de la licencia en el siguiente enlace: http://creativecommons.org/licenses/by-nc/4.0/legalcode

 © Author: jmasmelac (Dev)
batalla_naval.py (c) 2024  July 22 11:29
Version:2024-07-22T16:29:54.883Z
Para ver el diagrama de flujo (si hay) mira el archivo .drawio en el proyecto
Desc: juego de batalla naval
 """

#mapa

def crear_tablero(tamaño=10):#creación del tablero, tamaño 10x10
    return [[' ' for _ in range(tamaño)] for _ in range(tamaño)]

def mostrar_tablero(tablero, oculto=False):
    
    print('    ' + ' '.join([str(i) for i in range(len(tablero))]))# Imprimir los números de las columnas, 4 espacios por ajuste con la interfaz
    
    for i, fila in enumerate(tablero):  # Imprimir cada fila , el enumerate numera los elementos en la variable tablero
        print(f'{i:2d} |' + '|'.join([' ' if oculto and celda != 'O' and celda != 'X' else celda for celda in fila]) + '|')# el join junta las palabras y el {i:2d} es para los elementos del bucle
                                                                                                                            #el if verifica si se puede ver el tablero, si falla o acierta el tiro
#barcos 

def colocar_barco(tablero, barco, x, y, orientación):#posiciona el barco en x y indicada
    tamaño = len(tablero)#tamaño del tablero
    if orientación == 'horizontal':
        if y + barco['tamaño'] > tamaño:#verifica el tamaño del barco no se salga del mapa
            return False
        for i in range(barco['tamaño']):#verifica si la posición esta vacía
            if tablero[x][y+i] != ' ':
                return False
        for i in range(barco['tamaño']):#pone el símbolo correspondiente al barco
            tablero[x][y+i] = barco['símbolo']
    elif orientación == 'vertical':
        if x + barco['tamaño'] > tamaño:
            return False
        for i in range(barco['tamaño']):
            if tablero[x+i][y] != ' ':
                return False
        for i in range(barco['tamaño']):
            tablero[x+i][y] = barco['símbolo']
    return True


import random # se usa la librería random para decir la posición de los barcos

def colocar_barcos_aleatoriamente(tablero, barcos):#recibe el tablero y la lista de los barcos ya definidos
    for barco in barcos:
        colocado = False
        while not colocado:
            x = random.randint(0, len(tablero) - 1)#random del eje x
            y = random.randint(0, len(tablero) - 1)#random del eje y 
            orientación = random.choice(['horizontal', 'vertical'])#random entre horizontal y vertical
            colocado = colocar_barco(tablero, barco, x, y, orientación)#llamado a la función de colocar barco

#gameplay

def disparar(tablero, x, y):
    if tablero[x][y] == ' ':
        tablero[x][y] = 'O'  # Agua
        return False
    elif tablero[x][y] in ['P', 'A', 'C', 'D']:#letras correspondientes a los barcos
        tablero[x][y] = 'X'  # Golpe
        return True
    else:
        return None  # Ya se ha disparado aquí
    

def turno_jugador(tablero_enemigo):
    while True:
        try:
            x = int(input("Ingrese la fila para disparar (0-9): "))
            y = int(input("Ingrese la columna para disparar (0-9): "))
            if 0 <= x < 10 and 0 <= y < 10:
                resultado = disparar(tablero_enemigo, x, y)#llamado a la función disparar
                if resultado is None:
                    print("Ya has disparado en esa posición. Intenta de nuevo.")
                else:
                    return resultado
            else:
                print("Coordenadas fuera del tablero. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa números válidos.")

def turno_computadora(tablero_jugador):#mejorable, ver que mas denotar de la ia del juego
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        resultado = disparar(tablero_jugador, x, y)#llamado a la función disparar de la maquina
        if resultado is not None:#verifica si el tiro de la maquina es valido
            print(f"El enemigo dispara en ({x}, {y})")
            return resultado

#bucle del juego

def juego():

    barcos = [#lista de barcos
    {'nombre': 'Portaaviones', 'tamaño': 5, 'símbolo': 'P'},#elementos de un barco
    {'nombre': 'Acorazado', 'tamaño': 4, 'símbolo': 'A'},
    {'nombre': 'Crucero', 'tamaño': 3, 'símbolo': 'C'},
    {'nombre': 'Destructor', 'tamaño': 2, 'símbolo': 'D'}]
    total_barcos_aliados=14
    total_barcos_enemigos=14

    tablero_jugador = crear_tablero()# Crear un tablero de 10x10 para jugador
    tablero_enemigo = crear_tablero()#crea tablero enemigo

    colocar_barcos_aleatoriamente(tablero_jugador, barcos)
    colocar_barcos_aleatoriamente(tablero_enemigo, barcos)

    while True:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador)
        print("\nTablero enemigo:")
        mostrar_tablero(tablero_enemigo, oculto=True)

        print("\nTu turno:")
        if turno_jugador(tablero_enemigo):
            print("¡Has acertado!")
            total_barcos_enemigos=total_barcos_enemigos-1
        else:
            print("Agua.")

        if total_barcos_enemigos==0:
            print("¡Felicidades! Has ganado.")
            break

        print("\nTurno del enemigo:")
        if turno_computadora(tablero_jugador):
            print("El enemigo ha acertado.")
            total_barcos_aliados=total_barcos_aliados-1
        else:
            print("El enemigo ha fallado.")

        if total_barcos_aliados==0:
            print("Lo siento, has perdido.")
            break

juego()#llamado a la función del juego