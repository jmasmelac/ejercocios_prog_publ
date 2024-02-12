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
contactos.c (c) 2024  February 10 13:56
Version:2024-02-10T18:56:40.061Z
Desc: description
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

void guardarCSV(char *nombreArchivo, contacto *lista_contactos, int total_contactos) {
    FILE *archivo = fopen(nombreArchivo, "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo para escribir.\n");
        exit(1);
    }

    // Escribir la primera línea de encabezados
    fprintf(archivo, "Nombre,Telefono,Email,Categoria,100\n");

    // Escribir cada contacto en el archivo en formato CSV
    for (int i = 0; i < total_contactos; i++) {
        fprintf(archivo, "%s,%d,%s,%s", lista_contactos[i].nombre, lista_contactos[i].telefono,
                lista_contactos[i].email_, lista_contactos[i].categria_);
    }

    fclose(archivo);
}


void borrarContacto(contacto *lista_contactos, int *total_contactos, char *nombre_a_borrar) {
  int indice = -1;
    // Buscar el índice del contacto con el nombre especificado
    for (int i = 0; i < *total_contactos; i++) {
        if (strcmp(lista_contactos[i].nombre, nombre_a_borrar) == 0) {
            indice = i;
            break;
        }
    }
    if (indice == -1) {
        printf("No se encontró ningún contacto con el nombre especificado.\n");
        return;
    }
    // Eliminar el contacto moviendo los contactos posteriores una posición hacia atrás
    for (int i = indice; i < (*total_contactos - 1); i++) {
        lista_contactos[i] = lista_contactos[i + 1];
    }
    // Reducir el número total de contactos
    (*total_contactos)--;  
}

void leerCSV(char *nombreArchivo, contacto *lista_contactos, int total_contactos) {
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
    for (int i = 0; i < total_contactos; i++) {
        fgets(linealeida, sizeof(linealeida), archivo);
        // Tokenizar la línea para obtener los campos
        char *token = strtok(linealeida, ",");
        strcpy(lista_contactos[i].nombre, token);
        token = strtok(NULL, ",");
        lista_contactos[i].telefono = atoi(token);
        token = strtok(NULL, ",");
        strcpy(lista_contactos[i].email_, token);
        token = strtok(NULL, ",");
        strcpy(lista_contactos[i].categria_, token);
    }

    fclose(archivo);

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

int total_contactos(){
    FILE *archivo = fopen("contactos.csv", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        exit(1);
    }
    char linealeida[100];
    int contador=0;
    // Omitir la primera fila
    if (fgets(linealeida, sizeof(linealeida), archivo) == NULL) {
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
    } else {
        printf("\nArchivo cargado correctamente\n");
        fclose(archivo);// Si el archivo ya existe, cerrarlo y abrirlo en modo de lectura y escritura
    }
    fclose(archivo);
}

int main() {
    inicializa_archivo();//esta funcion verifica si existe el archivo, si no lo crea y añade la primera linea
    //primero se crea el archivo, si ya existe solo afirma si se carga correctamente
    int numero_contactos =total_contactos();//numero del total de contactos
    printf("numero de contactos existentes %d\n",numero_contactos);
    printf("hola");

    int contactos_totales_ = contactos_totales_lec();//esta fucion lee la primera linea donde se almacena el valor del limite final del total de contactos
    printf("Numero total de contactos a almacenar: %d\n", contactos_totales_ );

    contacto lista_contactos[100];
    leerCSV("contactos.csv", lista_contactos, numero_contactos);
    // Mostrar los contactos leídos como tabla
    printf("Tabla de contactos:\n");
    printf("%-20s %-15s %-30s %-20s\n", "Nombre", "Telefono", "Email", "Categoria");
    for (int i = 0; i < numero_contactos; i++) {
        printf("%-20s %-15d %-30s %-20s\n", lista_contactos[i].nombre, lista_contactos[i].telefono,
               lista_contactos[i].email_, lista_contactos[i].categria_);
    }


    // Borrar un contacto por su nombre
    char nombre_a_borrar[50];
    printf("\nIngrese el nombre del contacto que desea borrar: ");
    fgets(nombre_a_borrar, sizeof(nombre_a_borrar), stdin);
    nombre_a_borrar[strcspn(nombre_a_borrar, "\n")] = '\0'; // Eliminar el salto de línea del final

    borrarContacto(lista_contactos, &numero_contactos, nombre_a_borrar);

    printf("%-20s %-15s %-30s %-20s\n", "Nombre", "Telefono", "Email", "Categoria");
    for (int i = 0; i < numero_contactos; i++) {
        printf("%-20s %-15d %-30s %-20s\n", lista_contactos[i].nombre, lista_contactos[i].telefono,
               lista_contactos[i].email_, lista_contactos[i].categria_);
    }

    guardarCSV("contactos.csv", lista_contactos, numero_contactos);


    return 0;
}