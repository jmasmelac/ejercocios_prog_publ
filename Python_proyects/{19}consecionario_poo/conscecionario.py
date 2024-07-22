# creación de concesionario
# se compran y venden vehículos de toda clase
# un usuario puede preguntar cuales están disponibles y cuales no y el precio
# el usuario puede comprar un vehículo

# asi se define un objeto, este debe poseer atributos y métodos
class vehículo:  
    def __init__(self, modelo , precio, tipo): #asi se definen los atributos(características de un objeto)
        self.modelo = modelo # modelo del vehículo
        self.precio = precio # precio en $$
        self.tipo = tipo     # si es carro o moto o camioneta
        self.disponible = True #disponibilidad
    
    def vender(self): # asi se definen los métodos (que se puede hacer con ese objeto)
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.tipo} de la marca {self.modelo} ha sido vendido.")
        else:
            print(f"El vehículo {self.tipo} de la marca {self.modelo} no está disponible.")

    def hacer_disponible(self):
        self.disponible = True
        print(f"El vehículo {self.tipo} de la marca {self.modelo} está disponible para la venta.")

    def __str__(self): #El método __str__ te permite definir cómo quieres que se vea tu objeto cuando se convierta a una cadena de texto
        return f"{self.tipo} {self.modelo}"
    

class cliente:
    def __init__(self,nombre,id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.vehículos_comprados = []

    def comprar_vehículo(self, vehículo):
        if vehículo.disponible:
            vehículo.vender()
            self.vehículos_comprados.append(vehículo)
        else:
            print(f"El vehículo {self.tipo} de la marca {vehículo.modelo} no está disponible.") 

    def devolver_vehículo(self, vehículo):
        if vehículo in self.vehículos_comprados:
            vehículo.hacer_disponible()
            self.vehículos_comprados.remove(vehículo)
        else:
            print(f"El vehículo {self.tipo} de la marca {vehículo.modelo} no está en la lista de comprados.")

    def ver_vehículos_cliente(self):
        print(f"El nombre del cliente es {self.nombre}\n y sus vehículos son: {[str(v) for v in self.vehículos_comprados]}.")#un ciclo for para llamar a todos los miembros de la lista
                                                                                                                             #la función de str es para expresarlo en texto y no en dirección de memoria

#inicializamos de las variables vehículo
vehículo1=vehículo("Toyota",900000,"camioneta")
vehículo2=vehículo("Nisan",450000,"carro")
vehículo3=vehículo("Bugatti",1900999,"carro")
vehículo4=vehículo("boxer",9000,"moto")
vehículo5=vehículo("Renault",900000,"carro")

#variables clientes
cliente1=cliente("caimito dais",34)
cliente2=cliente("Gerry ford",54)

#las acciones correspondientes al cliente
cliente1.comprar_vehículo(vehículo1)
cliente1.ver_vehículos_cliente()

cliente1.devolver_vehículo(vehículo1)
cliente1.ver_vehículos_cliente()

vehículo1.vender()
vehículo1.hacer_disponible()

cliente1.comprar_vehículo(vehículo4)
cliente1.comprar_vehículo(vehículo5)

cliente1.ver_vehículos_cliente()

vehículo1.hacer_disponible()
cliente2.comprar_vehículo(vehículo1)
cliente2.comprar_vehículo(vehículo2)
cliente2.comprar_vehículo(vehículo3)

cliente2.ver_vehículos_cliente()