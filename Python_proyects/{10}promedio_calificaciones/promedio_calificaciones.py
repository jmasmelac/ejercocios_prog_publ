
estudiantes={}
for i in range(1, 11):
    new_student=input(f"ingresa el nombre del estudiante {i}-> ")
    edad_=int(input(f"ingresa la edad del estudiante {i}-> "))
    nota_=int(input(f"ingresa la calificación del estudiante {i}-> "))
    estudiantes[new_student] = {"edad": edad_, "nota": nota_}

#promedio de notas
total_notas = 0
num_estudiantes = len(estudiantes)
for estudiante in estudiantes:
    total_notas += estudiantes[estudiante]["nota"]

promedio_notas = total_notas / num_estudiantes

#promedio de edades
total_edades = 0
for estudiante in estudiantes:
    total_edades += estudiantes[estudiante]["edad"]

promedio_edades = total_edades / num_estudiantes

#visualización de datos
print("| {:^8} | {:^5} | {:^12} | {:^10} | {:^10} |".format("Nombre", "Edad", "Calificación", "Promedio", "edades"))

for estudiante in estudiantes:
    print("| {:^8} | {:^5} | {:^12} | {:^10.2f} | {:^10.2f} |".format(estudiante, estudiantes[estudiante]["edad"], estudiantes[estudiante]["nota"], promedio_notas,promedio_edades))