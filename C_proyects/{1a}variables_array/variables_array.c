/*
variables dentro de un arreglo de caracteres
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
    char arreglo_[]={"ster siera,14.5,cuchillo,kenedy"};
    char *token = strtok(arreglo_, ",");// Dividir el arreglo en subcadenas usando la coma como delimitador
    float num;
    while (token != NULL) {
        if (sscanf(token, "%f", &num) == 1) { // Si el token es un número, almacenarlo como flotante
            printf("Numero: %.2f\n", num);
        }
        token = strtok(NULL, ",");// Obtener el siguiente token
        //en caso de querer almacenar todas las variables hacer swich case y al final del bucle la variable con el ++
    }
    printf("Numero: %.2f\n", num);
    return 0;
}