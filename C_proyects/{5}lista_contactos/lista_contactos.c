/*
Este proyecto está licenciado bajo una Licencia Creative Commons Atribución-NoComercial 4.0 Internacional.
 Puedes:
 - Compartir: copiar y redistribuir el material en cualquier medio o formato.
 - Adaptar: remezclar, transformar y construir sobre el material.
 Bajo las siguientes condiciones:
 - Atribución: debes dar crédito adecuado, proporcionar un enlace a la licencia e indicar si se realizaron cambios.
    No puedes sugerir que el licenciante te respalda a ti o al uso que hagas del material.
 - NoComercial: no puedes utilizar el material con fines comerciales.
 Puedes encontrar una copia completa de la licencia en el siguiente enlace: http://creativecommons.org/licenses/by-nc/4.0/legalcode

 © Author: Luko (Dev)
lista_contactos.c (c) 2024  February 12 12:41
Version:2024-02-12T17:41:54.413Z
Desc: descripcion abajo
 */

/*
Este proyecto está licenciado bajo una Licencia Creative Commons Atribución-NoComercial 4.0 Internacional.
 Puedes:
 - Compartir: copiar y redistribuir el material en cualquier medio o formato.
 - Adaptar: remezclar, transformar y construir sobre el material.
 Bajo las siguientes condiciones:
 - Atribución: debes dar crédito adecuado, proporcionar un enlace a la licencia e indicar si se realizaron cambios.
    No puedes sugerir que el licenciante te respalda a ti o al uso que hagas del material.
 - NoComercial: no puedes utilizar el material con fines comerciales.
 Puedes encontrar una copia completa de la licencia en el siguiente enlace: http://creativecommons.org/licenses/by-nc/4.0/legalcode

 © Author: Luko (Dev)
lista_contactos.c (c) 2024  February 10 14:03
Version:2024-02-10T19:03:16.447Z
Desc: descripcion abajo
 */
/*
Agregar contacto: Permitir al usuario agregar un nuevo contacto. Cada contacto debe tener los siguientes campos:

Nombre (cadena de caracteres)
Teléfono (cadena de caracteres)
Email (cadena de caracteres)
Categoría (cadena de caracteres)
Mostrar contactos: Mostrar todos los contactos almacenados en la lista, ordenados alfabéticamente por nombre.

Buscar contacto: Permitir al usuario buscar un contacto por su nombre y mostrar la información completa del contacto encontrado.

Eliminar contacto: Permitir al usuario eliminar un contacto de la lista.

Filtrar por categoría: Permitir al usuario filtrar la lista de contactos por categoría y mostrar solo los contactos que pertenecen a esa categoría.

Guardar y cargar desde archivo: Implementar la funcionalidad de guardar la lista de contactos en un archivo y cargarla nuevamente en el programa en sesiones posteriores.
*/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {//struct se utiliza para definir estructuras de datos, forma de agrupar múltiples variables bajo un solo nombre
    char nombre[50];
    int telefono;
    char email_[50];
    char categria_[50];
} contacto;//nombre de la variable conjunto 


void inicializa_archivo(){
    FILE *archivo;
    archivo = fopen("contactos.csv", "r");// Intentar abrir el archivo en modo lectura

    if (archivo == NULL) {
        printf("\nEl archivo no existe. Creando uno nuevo...\n");

        archivo = fopen("contactos.csv", "w");// Si el archivo no existe, crear uno nuevo en modo escritura

        if (archivo == NULL) {
            printf("Error al crear el archivo.\n");
            exit(1);
        }

        fprintf(archivo, "Nombre,Telefono,Email,Categoria,100\n");// Escribir encabezado en el archivo nuevo
        fprintf(archivo, "maria,5553246,maria@Email.com,reina\n");
        fprintf(archivo, "pedro,5553246,pedro@Email.com,rey\n");
    } else {
        printf("\nArchivo cargado correctamente\n");
        fclose(archivo);// Si el archivo ya existe, cerrarlo y abrirlo en modo de lectura y escritura
    }
    fclose(archivo);
}

int total_contactos(){
    FILE *archivo = fopen("contactos.csv", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        exit(1);
    }
    char linealeida[100];
    int contador=0;
    if (fgets(linealeida, sizeof(linealeida), archivo) == NULL) {// omite la primera fila
        printf("Error: archivo vacio.\n");
        fclose(archivo);
        exit(1);
    }
    while (fgets(linealeida, sizeof(linealeida), archivo) != NULL) {
            contador++;
        }
        fclose(archivo);
        return contador;
}

int contactos_totales_lec(){
  char primeralinea_[100] ;
  FILE *archivo = fopen("contactos.csv", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        exit(1);
    }
    if (fgets(primeralinea_, 100, archivo) == NULL) {
        printf("Error: archivo vacío.\n");
        fclose(archivo);
        exit(1);
    }

    fclose(archivo);
    char *token = strtok(primeralinea_, ",");// Dividir el arreglo en subcadenas usando la coma como delimitador
    int num;
    while (token != NULL) {
        if (sscanf(token, "%d", &num) == 1) { // Si el token es un número, almacenarlo 
            //printf("Numero: %d\n", num);
        }
        token = strtok(NULL, ",");// Obtener el siguiente token
        //en caso de querer almacenar todas las variables hacer swich case y al final del bucle la variable con el ++
    }
    return num;
}

void leerCSV(char *nombreArchivo, contacto *personas_, int num_contac_ex) {
     FILE *archivo = fopen(nombreArchivo, "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        exit(1);
    }
    char linealeida[100];
    // Omitir la primera fila
    if (fgets(linealeida, sizeof(linealeida), archivo) == NULL) {
        printf("Error: archivo vacio.\n");
        fclose(archivo);
        exit(1);
    }
    // Eliminar el carácter de nueva línea si está presente
        size_t longitud = strlen(linealeida);
        if (linealeida[longitud - 1] == '\n')
            linealeida[longitud - 1] = '\0';
    // Leer los contactos restantes
    for (int i = 0; i < num_contac_ex; i++) {
        fgets(linealeida, sizeof(linealeida), archivo);
        // Tokenizar la línea para obtener los campos
        char *token = strtok(linealeida, ",");
        strcpy(personas_[i].nombre, token);
        token = strtok(NULL, ",");
        personas_[i].telefono = atoi(token);
        token = strtok(NULL, ",");
        strcpy(personas_[i].email_, token);
        token = strtok(NULL, ",");
        strcpy(personas_[i].categria_, token);
    }

    fclose(archivo);

}

contacto *llenar_personas(){
    FILE *archivo;
    archivo = fopen("contactos.csv", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        exit(1);
    }
    char linea[100];
    int primera_linea=1;
    int coontador=0;
    contacto *conocido=(contacto*)malloc(100 * sizeof(contacto));//malloc asignar memoria dinámicamente durante la ejecución del programa
    //para este caso se usa devido a que en ningun momento le asigne tamaño a esa variable, solo le asignava el valor
    while (fgets(linea, sizeof(linea), archivo) != NULL) {
        if (primera_linea) {primera_linea = 0;continue;}//se uso para saltar la primera linea
        contacto personajes;
        char *token;
        // Usar strtok para dividir la línea en tokens usando la coma como delimitador
        token = strtok(linea, ",");
        strcpy(personajes.nombre,token); //Copia la cadena apuntada por token (incluyendo el carácter nulo) a la cadena apuntada
        token = strtok(NULL, ",");
        personajes.telefono = atoi(token); // Convertir el segundo token a entero/// se usa atof para datos .flotante
        token = strtok(NULL, ",");
        strcpy(personajes.email_,token);
        token = strtok(NULL, ",");
        strcpy(personajes.categria_,token);

        conocido[coontador++]=personajes;
    }
    fclose(archivo);
    return conocido;
}

void agregar_contacto(contacto *personas_, int *num_contac_ex, int num_max_contactos) {
        // Buscar el primer índice vacío
    int indice_vacio = -1;
    for (int i = 0; i < num_max_contactos; i++) {
        if (personas_[i].telefono == 0) {  // Verificar si el teléfono es 0 (valor predeterminado)
            indice_vacio = i;
            break;
        }
    }
    
    if (indice_vacio == -1) {
        printf("No se encontró un espacio vacío para agregar el nuevo contacto.\n");
        return;
    }

    if (indice_vacio >= num_max_contactos) {
        printf("No hay espacio disponible para agregar más contactos.\n");
        return;
    }

    printf("indice vacio %d\n",indice_vacio);
    //printf("numcontactos %d",numContactos);
    printf("nummax %d\n",num_max_contactos);
    printf("Ingrese el nombre del nuevo contacto: \n");
    scanf("%s", personas_[indice_vacio].nombre);

    printf("Ingrese el numero telefonico del contacto: \n");
    scanf("%d", &personas_[indice_vacio].telefono);

    printf("Ingrese el email del nuevo contacto: \n");
    scanf("%s", personas_[indice_vacio].email_);

    printf("Ingrese la categoria a la que pertenece el nuevo contacto: \n");
    scanf("%s", personas_[indice_vacio].categria_);

    (*num_contac_ex)++;
}

void guardarCSV(char *nombreArchivo, contacto *lista_contactos, int total_contactos,int contactosTotales) {
    FILE *archivo = fopen(nombreArchivo, "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo para escribir.\n");
        exit(1);
    }

    // Escribir la primera línea de encabezados
    fprintf(archivo, "Nombre,Telefono,Email,Categoria,%d\n",contactosTotales);

    // Escribir cada contacto en el archivo en formato CSV
    for (int i = 0; i < total_contactos; i++) {
        fprintf(archivo, "%s,%d,%s,%s", lista_contactos[i].nombre, lista_contactos[i].telefono,
                lista_contactos[i].email_, lista_contactos[i].categria_);
                 // Verificar si la última categoría ya contiene un salto de línea
        if (i == total_contactos - 1 && lista_contactos[i].categria_[strlen(lista_contactos[i].categria_) - 1] != '\n') {
            fprintf(archivo, "\n");
        } 
    }
    printf("total contactos final %d\ntotal contactos almacenables %d",total_contactos,contactosTotales);
    fclose(archivo);
}



int main() {
    inicializa_archivo();//esta funcion verifica si existe el archivo, si no lo crea y añade la primera linea
    int num_contac_ex =total_contactos();//numero del total de contactos existentes

    int contactos_totales_ = contactos_totales_lec();//esta fucion lee la primera linea donde se almacena el valor del limite final del total de contactos
    
    contacto personas_[contactos_totales_ ];
    leerCSV("contactos.csv", personas_, num_contac_ex);

    char nombreBuscado[50];//variable de busqueda por nombre

    char categoriaBuscada[50];//variable para categoria

    printf("%d %d ",num_contac_ex,contactos_totales_);

    int opcion;

    do {
            printf("\n--- GESTION DE CONTACTOS ---\n");
            printf("1. Agregar contacto\n");
            printf("2. Mostrar contactos\n");
            printf("3. Buscar contacto\n");
            printf("4. Eliminar contacto\n");
            printf("5. filtro por cartegoria\n");
            printf("6. editar total de contactos\n");
            printf("0. Salir\n");
            printf("Seleccione una opcion: ");
            scanf("%d", &opcion);
            switch (opcion) {
            case 1://agrega contacto
                agregar_contacto(personas_, &num_contac_ex, contactos_totales_ );

            break;
            case 2://mostrar los contactos
                printf("nombre\t\ttelefono\t\temail\t\tcategoria\n");// los \t\t separan las palabras a la misma distancia
                for (int i = 0; i<num_contac_ex ;i++){
                    if(personas_[i].telefono<=0){break;}//rompe el ciclo con un valor ilogico o atipico
                printf("%s\t\t%d\t\t%s\t\t%s\n", personas_[i].nombre, personas_[i].telefono, personas_[i].email_, personas_[i].categria_);   
                }
            break;
            case 3://buscar contacto

                printf("Ingrese el nombre de la persona que desea buscar: \n");
                scanf("%s", nombreBuscado);
                int encontrado = 0;
                printf("nombe buscado: %s\n",nombreBuscado);
                for (int i = 0; i < num_contac_ex; i++){printf("%s ", personas_[i].nombre);}
                printf("\n");
                for (int i = 0; i < num_contac_ex; i++){
                    if (strcmp(personas_[i].nombre,nombreBuscado) == 0){//La función strcmp compara las cadenas Devuelve un valor negativo si cadena1 es "menor" que cadena2.Devuelve cero si cadena1 es "igual" a cadena2.Devuelve un valor positivo si cadena1 es "mayor" que cadena2.
                        printf("Contacto encontrado:\n");
                        printf("Nombre: %s\n", personas_[i].nombre);
                        printf("telefono: %d\n", personas_[i].telefono);
                        printf("email: %s\n", personas_[i].email_);
                        printf("Categoria: %s\n", personas_[i].categria_);
                        encontrado = 1;
                        break; // Salimos de la función después de encontrar la compatibilidad
                    }                  
                }if (!encontrado){printf("El contacto con el nombre \"%s\" no se encuentra en la lista.\n", nombreBuscado);break;} 

            break;
            case 4://elimina contacto
            printf("Ingrese el nombre del contacto que desea borrar: ");
            scanf("%s", nombreBuscado);
            int encontrado4 = 0;
                for (int i = 0; i < num_contac_ex; i++) {
                    if (strcmp(nombreBuscado, personas_[i].nombre) == 0) {
                        encontrado4 = 1;
                        // Eliminar el contacto encontrado moviendo los contactos hacia la izquierda
                        for (int j = i; j < num_contac_ex - 1; j++) {
                            personas_[j] = personas_[j + 1];
                        }
                        // Reducir el número total de contactos
                        num_contac_ex--;
                        printf("El contacto \"%s\" ha sido eliminado exitosamente.\n", nombreBuscado);
                        break;
                    }
                }
                if (!encontrado4) {
                    printf("No se encontró ningún contacto con el nombre \"%s\".\n", nombreBuscado);
                }
            break;
            case 5://buscar por categoria
                  printf("Ingrese el nombre de la categoria a buscar: "); 
                  scanf("%s",categoriaBuscada);
                  strcat(categoriaBuscada, "\n");//concatena con un salto de linea para poder buscar
                  int encontrado5 =0;
                  //for (int i = 0; i < num_contac_ex; i++){printf("%s ", personas_[i].categria_);}
                for (int i = 0; i < num_contac_ex; i++) {
                    // Comparar la categoría ingresada por el usuario con las categorías almacenadas
                    if (strcmp(categoriaBuscada, personas_[i].categria_) == 0) {
                        printf("Nombre: %s\n", personas_[i].nombre);
                        encontrado5 = 1;
                    }
                } if (!encontrado5){printf("la categoria con el nombre \"%s\" no se encuentra en la lista.\n", categoriaBuscada);break;}
                break;
            case 6://cambia el total de contactos
                printf("El total de contactos es de %d\n",contactos_totales_);
                printf("El nuevo valor sera :");
                scanf("%d",&contactos_totales_);
                break;
            case 0:
                printf("Saliendo del programa...\n");
                guardarCSV("contactos.csv", personas_, num_contac_ex,contactos_totales_ );
                break;
            default:
                printf("Opcion no valida. Por favor, seleccione una opcion valida.\n");
                break;
            }
        }while (opcion != 0);

    

    return 0;
}
