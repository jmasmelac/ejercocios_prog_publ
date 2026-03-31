#include <iostream>
int main(){
    int a = 10;
    int b = 5;
    int suma = a + b; // suma de a y b
    int resta = a - b; // resta de a y b
    int multiplicacion = a * b; // multiplicación de a y b
    int division = a / b; // división de a y b
    int modulo = a % b; // módulo de a y b

    printf("los valores de a y b son: %d y %d\n", a, b);
    printf("la suma es: %d\n", suma);
    printf("la resta es: %d\n", resta);
    printf("la multiplicación es: %d\n", multiplicacion);
    printf("la división es: %d\n", division);
    printf("el módulo es: %d\n", modulo);
    printf("el modulo es la operación que devuelve el residuo de la división entre dos números\n");
    //reasignacion de variables
    a += 5; // a = a + 5
    b -= 2; // b = b - 2
    printf("después de la reasignación:\n");
    printf("el nuevo valor de a es: %d\n", a);
    printf("el nuevo valor de b es: %d\n", b);
    printf("otra reasignacion se hace con ++ y --\n");
    a++; // a = a + 1
    b--; // b = b - 1
    printf("después de la reasignación con ++ y --:\n");
    printf("el nuevo valor de a es: %d\n", a);
    printf("el nuevo valor de b es: %d\n", b);
    printf("este tipo de reasignacion solo suma o resta 1");

    printf("el orden de operaciones es importante\n");
    int resultado = a + b * 2/2; //el orden de operaciones es: primero division, luego multiplicación y finalmente suma
    printf("siendo a = %d y b = %d\n", a, b);
    printf("el resultado de a + b * 2/2 es: %d\n", resultado);
    printf("el orden fue: division, multiplicación y suma\n");
    printf("para los casos en los que queremos ver los decimales de la división, debemos usar el tipo de dato float o double\n");
    float division_float = (float)a / (b+1); // división de a y b con dec
    printf("la división de a y b con decimales es: %.2f\n", division_float);


    return 0;
}