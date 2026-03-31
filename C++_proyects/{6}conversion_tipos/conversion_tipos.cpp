#include <stdio.h>
int main(){

    printf("hay dos caso la conversion implícita y la conversión explícita\n");
    printf("la conversión implícita es cuando el compilador convierte automáticamente un tipo de dato a otro tipo de dato compatible\n");
    printf("la conversión explícita es cuando el programador convierte un tipo de dato a otro tipo de dato compatible usando un operador de conversión\n");
    double pi_ = 3.14159; //forma inplicita
    printf("el valor de pi es: %.5f\n", pi_);
    int pi_entero = (int)pi_; // conversión explícita de double a int
    printf("el valor de pi convertido a entero es: %d\n", pi_entero);
    printf("un caso tipico es el siguiente:\n");
    int numerador_ = 10;
    int denominador_ = 3;
    printf("tenemos 2 valores para dividirlos  un numerador de %d y un denominador de %d\n", numerador_, denominador_);
    double resultado_division = numerador_ / denominador_; // división de enteros, resultado entero
    printf("ojo con ese resultado ya que dio un numero entero pese a que esta definido como double, resultado_division es: %.2f\n", resultado_division);
    printf("este resultado se da porque los valores del numerador y denominador son enteros, toca hace la conversion explicita a double o floar segun el caso\n");
    resultado_division = (double)numerador_ / (double)denominador_;//ojo la conversion es en ambos
    printf("ahora el resultado de la división es: %.2f\n", resultado_division);
    printf("para el caso de variables tipo char hay que tener cuidado\n");
    char letra = 100; // forma implícita
    printf("el valor de letra es: %c\n", letra);
    printf("el numero represnta el código ASCII de la letra %c\n", letra);
    printf("es lo mismo que mostrar %c\n", (char)100);

}