#include <stdio.h>
int main() {
    int opcion;
    float base, altura, lado1, lado2 ,radio,area;
    printf("Calculadora de área de figuras geométricas\n");
    printf("1. Triángulo\n");
    printf("2. Cuadrado\n");
    printf("3. Círculo\n");
    printf("Selecciona una figura (1-3): ");
    scanf("%d", &opcion);
    switch (opcion) {
        case 1:
            printf("Ingresa la base del triángulo: ");
            scanf("%f", &base);
            printf("Ingresa la altura del triángulo: ");
            scanf("%f", &altura);
            area = (base*altura)/2;
            printf("El área del triángulo es: %.2f\n", area);
            break;
        case 2:
            printf("Ingresa la base del cuadrado: ");
            scanf("%f", &lado1);
            printf("Ingresa la altura del cuadrado: ");
            scanf("%f", &lado2);
            area = (lado1*lado2);
            printf("El área del cuadrado es: %.2f\n", area);
            break;
        case 3:
            printf("Ingresa el radio del círculo: ");
            scanf("%f", &radio);
            area = 3.141593*(radio*radio);
            printf("El área del círculo es: %.2f\n", area);
            break;
        default:
            printf("Opción no válida.\n");
    }

    return 0;
}