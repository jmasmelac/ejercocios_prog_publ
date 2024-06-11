#piedra papel o tijera
import random   #biblioteca para el valor de la maquina
contador = 0
while True:

    if contador == 3:
        break

    usuario_op=(input("piedra(1) papel(2) o tijera(3), o salir -> "))
    
    if (usuario_op.isdigit()):
        usuario_op=int(usuario_op)
        if usuario_op<1 or usuario_op>3:
            print("Perderás automáticamente")
    elif (usuario_op.lower()) == "piedra":
        usuario_op=1
    elif (usuario_op.lower()) == "papel":
        usuario_op=2
    elif (usuario_op.lower()) == "tijera":
        usuario_op=3
    elif ((usuario_op.lower()) == "salir"):
        break
    else:
        usuario_op=4

#la maquina escoge el valor
    pc_option=random.randint(1,3)

    if pc_option ==1:
        print('la maquina escogió piedra ')
    elif pc_option ==2:
        print('la maquina escogió papel ')
    elif pc_option ==3:
        print('la maquina escogió tijera ')
    else:
        print('la maquina escogió mal ')

# evaluación del resultado
    if usuario_op == pc_option:
        print("Empate")
    elif (usuario_op -pc_option == 1 or usuario_op - pc_option == -2):
        print("Ganador")
        contador += 1
    else:
        print("Perdedor")