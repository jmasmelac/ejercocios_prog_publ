#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nombre[50];
    int edad;
    char profesion[50];
} Persona;
#define MAX_LINE_LENGTH 100

int main() {
    //////////////////////////////////////////////////////////////////////Abrir el archivo en modo escritura
    printf("\ncrea el archivo\n");
    //https://www.tutorialspoint.com/c_standard_library/c_function_fopen.htm
    //"w" Crea un archivo vacío para escribir. Si ya existe un archivo con el mismo nombre, su contenido se borra y el archivo se considera como un nuevo archivo vacío.
    FILE *archivo = fopen("datos.csv", "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    // Escribir las líneas de datos en el archivo CSV
    fprintf(archivo, "Nombre,Edad,Profesion\n");
    fprintf(archivo, "Light,30,Ingeniero\n");
    fprintf(archivo, "Luffy,25,Doctor\n");
    fprintf(archivo, "Uzumaki,40,Abogado\n");

    // Cerrar el archivo
    fclose(archivo);
    ///////////////////////////////////////////////////////////////////// Abrir el archivo en modo lectura
    printf("\ncarga datos al archibo\n");
    //"r"Abre un archivo para leer. El archivo debe existir.
    archivo = fopen("datos.csv", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    // Leer y mostrar cada línea del archivo
    char linea[MAX_LINE_LENGTH];
    while (fgets(linea, sizeof(linea), archivo) != NULL) {
        printf("%s", linea);
    }

    // Cerrar el archivo
    fclose(archivo);
    /////////////////////////////////////////////////////////////////// lectura y asignacion en variable
    printf("\nlectua del archivo\n");
    int primera_linea =1;//variable de control, salta primera linea
    char *token;
    int coontador =0;
    Persona conocido[MAX_LINE_LENGTH];
    archivo = fopen("datos.csv", "r");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

     printf("\nleyo el archivo\n");// lectura del archivo   
    while (fgets(linea, sizeof(linea), archivo) != NULL) {
        if (primera_linea) {primera_linea = 0;continue;}//se uso para saltar la primera linea
        Persona personajes;
        // Usar strtok para dividir la línea en tokens usando la coma como delimitador
        token = strtok(linea, ",");
        strcpy(personajes.nombre,token); //Copia la cadena apuntada por token (incluyendo el carácter nulo) a la cadena apuntada
        token = strtok(NULL, ",");
        personajes.edad = atoi(token); // Convertir el segundo token a entero
        /// se usa atof para datos .flotante
        token = strtok(NULL, ",");
        strcpy(personajes.profesion,token);
        conocido[coontador++]=personajes;
    }
    // Cerrar el archivo
    fclose(archivo);
    printf("\nnombre: %s , edad: %d , profesion: %s \n", conocido[1].nombre , conocido[1].edad , conocido[1].profesion );

    int vara_ =sizeof(conocido);//este limite se tiene que estimar apopiadamente
        for (int i = 0; i<=vara_ ;i++){
            if(conocido[i].edad<=0){break;}//rompe el ciclo con un valor ilogico
                printf("%s\t\t%d\t\t%s \n", conocido[i].nombre, conocido[i].edad, conocido[i].profesion);   
        }
        printf("\nedicion de datos\n");// lectura del archivo   
        conocido[2].edad=15;//edito edad
        strcpy(conocido[3].nombre,"gohan");//añado un nuevo valor al conjunto
        conocido[3].edad=20;
        strcpy(conocido[3].profesion,"entomologo\n");//ojo la ultima variable salta de linea
        strcpy(conocido[4].nombre,"asuna");//añado un nuevo valor al conjunto
        conocido[4].edad=14;
        strcpy(conocido[4].profesion,"Cazarecompensas\n");

        for (int i = 0; i<=vara_ ;i++){
            if(conocido[i].edad<=0){break;}//rompe el ciclo con un valor ilogico
                printf("%s\t\t%d\t\t%s\n", conocido[i].nombre, conocido[i].edad, conocido[i].profesion);   
        }
        /////////////////////////////////////////////////////////////////////////////cargar archibo
        printf("\n carga los datos al archibo \n");

    archivo = fopen("datos.csv", "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }
    fprintf(archivo, "Nombre,Edad,Profesionn\n");//aca se modifica el archibo cabecera
     // Escribir los datos actualizados de los empleados en el archivo
    for (int i = 0; i < vara_; i++) {
        if(conocido[i].edad<=0){break;}//rompe el ciclo con un valor ilogico
        printf("\n el bucle dura %d ciclos\n",i+1);
        
        fprintf(archivo, "%s,%d,%s", conocido[i].nombre, conocido[i].edad, conocido[i].profesion);
    }

    // Cerrar el archivo de escritura
    fclose(archivo);

    return 0;
}
