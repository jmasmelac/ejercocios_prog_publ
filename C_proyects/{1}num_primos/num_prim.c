//codigo para ver numeros primos en un rango
#include <stdio.h>
int main() {
  system("cls");
    int inicio, fin;
    printf("Ingrese el inicio del rango: ");
    scanf("%d", &inicio);
    printf("Ingrese el fin del rango: ");
    scanf("%d", &fin);
    system("cls");
    if (inicio <= 0 || fin <= 0 || inicio > fin) {
        printf("Error: rango no válido.\n");
        return 0;
    }
    for (int i = inicio; i <= fin; i++) {
        if (i <= 1) {
            continue;//interrumpe la ejecución del ciclo actual, quita el 1
        }
        int es_primo = 1;  // asume que es primo
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                es_primo = 0;  // i no es primo
                break;
            }
        }
        if (es_primo) {
            printf("%d ", i);
        }
    }
    return 0;
}