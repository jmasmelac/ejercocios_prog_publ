#include <iostream>
#include <iomanip>//este header es para usar std::fixed y std::setprecision, que permiten controlar el formato de salida de los números de punto flotante.

int main() {
    int a = 5; // Declaración e inicialización de una variable entera
    double b = 3.14; // Declaración e inicialización de una variable de punto flotante (15 decimales)
    char c = 'A'; // Declaración e inicialización de una variable de carácter, solo con comillas simples''
    std::string d = "Hola, mundo!"; // Declaración e inicialización de una variable de cadena, la cadena en comillas dobles""
    bool e = true; // Declaración e inicialización de una variable booleana
    float f = 0.1f; // Declaración e inicialización de una variable de punto flotante de precisión simple (7 decimales)
    long double g = 0.1L; // Declaración e inicialización de una variable de punto flotante de precisión extendida (18 decimales)

    /*
    ojo con las variables ya que 
    se están inicializando y 
    asignando al mismo tiempo
    */

    std::cout << "Valor de a: " << a << std::endl;
    std::cout << "Valor de b: " << b << std::endl;
    std::cout << "Valor de c: " << c << std::endl;
    std::cout << "Valor de d: " << d << std::endl;
    std::cout << "Valor de e: " << e << std::endl;

    /*
    lo siguiente es
    hacer operaciones
    con los valores
    */

    std::cout << "Suma de a y b: " << a + b << std::endl;
    // otro detalle con los flotantes es el siguiente
    double decimal_a = 0.09999999999999999; // Esto puede causar problemas de precisión
    std::cout << "Valor de decimal_a: " << decimal_a << std::endl;
    std::cout << "los valores están redondeados a 0.1 debido a la precisión limitada de los números de punto flotante" << std::endl;
    std::cout << "para estos casos hay otros tipos de variables" << std::endl;
    std::cout << "tampoco imprime caracteres especiales por defecto" << std::endl;
    std::cout << "valor de decimal_a con formato de punto flotante extendido: " << std::fixed << decimal_a << std::endl;
    std::cout << std::fixed << std::setprecision(2)<< "una cadena concatenada con los valores de a y b: "<< "El valor de a es " << a << " y el valor de b es " << b << " pero también esta d que es " << d << std::endl;
    printf("otra forma de imprimir con formato es usando printf: El valor de a es %d y el valor de b es %.2f\n", a, b);

    return 0;
}