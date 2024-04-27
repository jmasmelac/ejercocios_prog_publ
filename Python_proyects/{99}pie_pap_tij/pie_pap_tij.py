#piedra papel o tijera
usuario_op=int(input("piedra(1) papel(2) o tijera(3) -> "))
pc_option=2
if usuario_op == pc_option:
    print("Empate")
elif (usuario_op -pc_option == 1 or usuario_op - pc_option == -2):
    print("Ganador")
else:
    print("Perdedor")
