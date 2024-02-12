/*
Escribe un programa en C para gestionar el inventario de productos de una tienda. El programa debe permitir al usuario realizar las siguientes acciones:

Agregar un nuevo producto al inventario.
Mostrar todos los productos en el inventario.
Buscar un producto por su nombre.
Actualizar la cantidad disponible de un producto en el inventario.
Eliminar un producto del inventario.
Cada producto debe tener los siguientes atributos:

Nombre del producto (cadena de caracteres).
Código del producto (entero).
Precio del producto (flotante).
Cantidad disponible en el inventario (entero).
El programa debe utilizar arreglos y punteros para almacenar y manipular la información del inventario. Puedes utilizar estructuras para representar cada producto y funciones para implementar cada acción mencionada anteriormente.
*/

#include <stdio.h>
#include <string.h>
typedef struct {//struct se utiliza para definir estructuras de datos, forma de agrupar múltiples variables bajo un solo nombre
    char nombre[50];
    int codigo;
    float precio;
    int cantidad;
} Producto;//nombre de la variable conjunto 
int main(){
    int MAX_PRODUCTOS =100;
    int numProductos = 0;
    Producto inventario_ [MAX_PRODUCTOS];
    int opcion;
    char nombreBuscado[50];
    do {
            printf("\n--- GESTION DE INVENTARIO ---\n");
            printf("1. Agregar producto\n");
            printf("2. Mostrar inventario\n");
            printf("3. Buscar producto\n");
            printf("4. Actualizar cantidad\n");
            printf("5. Eliminar producto\n");
            printf("0. Salir\n");
            printf("Seleccione una opcion: ");
            scanf("%d", &opcion);

            switch (opcion) {
            case 1://agrega un producto
                 if (numProductos >= MAX_PRODUCTOS) {
                    printf("No hay espacio disponible para agregar más productos.\n");
                    break;}

                printf("Ingrese el nombre del producto: ");
                scanf("%s", inventario_[numProductos].nombre);

                printf("Ingrese el código del producto: ");
                scanf("%d", &inventario_[numProductos].codigo);

                printf("Ingrese el precio del producto: ");
                scanf("%f", &inventario_[numProductos].precio);

                printf("Ingrese la cantidad disponible del producto: ");
                scanf("%d", &inventario_[numProductos].cantidad);
                (numProductos)++;
                break;
            case 2://visualiza los productos
                printf("nombre\t\tcodigo\t\tprecio\t\tcantidad \n");// los \t\t separan las palabras a la misma distancia
                for (int i = 0; i<numProductos ;i++){
                printf("%s\t\t%d\t\t%.2f\t\t%d\n", inventario_[i].nombre, inventario_[i].codigo, inventario_[i].precio, inventario_[i].cantidad);   
                }
                break;
            case 3://busca los nombres (mejorable)
                printf("Ingrese el nombre del producto que desea buscar: ");
                scanf("%s", nombreBuscado);
                for (int i = 0; i < numProductos; i++){
                    if (strcmp(nombreBuscado, inventario_[i].nombre) == 0){//La función strcmp compara las cadenas Devuelve un valor negativo si cadena1 es "menor" que cadena2.Devuelve cero si cadena1 es "igual" a cadena2.Devuelve un valor positivo si cadena1 es "mayor" que cadena2.
                        printf("Producto encontrado:\n");
                        printf("Nombre: %s\n", inventario_[i].nombre);
                        printf("Codigo: %d\n", inventario_[i].codigo);
                        printf("Precio: %.2f\n", inventario_[i].precio);
                        printf("Cantidad disponible: %d\n", inventario_[i].cantidad);
                        break; // Salimos de la función después de encontrar la compatibilidad
                    } else{printf("El producto con el nombre \"%s\" no se encuentra en el inventario.\n", nombreBuscado);break;}                  
                }
                
                break;
            case 4://actualizar cantidad
                printf("Ingrese el nombre del producto que desea buscar para remplazar la cantidad: ");
                scanf("%s", nombreBuscado);
                for (int i = 0; i < numProductos; i++){
                    if (strcmp(nombreBuscado, inventario_[i].nombre) == 0){
                        printf("Ingrese la nueva cantidad disponible del producto: ");
                        scanf("%d", &inventario_[i].cantidad);
                        break; // Salimos de la función después de cambiar la cantidad
                    }                   
                }
                break;
            case 5://borrar una variable
                printf("Ingrese el nombre del producto que desea borrar: ");
                scanf("%s", nombreBuscado);
                for (int i = 0; i < numProductos; i++){
                    
                    if (strcmp(nombreBuscado, inventario_[i].nombre) == 0){
                     for (int j = i; j < numProductos - 1; j++) {
                            inventario_[j] = inventario_[j + 1];
                        }
                        (numProductos)--;
                        break; 
                    }                   
                }
                break;
            case 0:
                printf("Saliendo del programa...\n");
                break;
            default:
                printf("Opcion no valida. Por favor, seleccione una opcion valida.\n");
            }
        }while (opcion != 0);
    
    return 0;
}