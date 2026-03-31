#include <iostream>
#include <cmath> // para usar las funciones matematicas como max() y min()
int main(){
    int numero_1 =3;
    int numero_2 =4;
    double numero_3;

    numero_3 = std::max(numero_1, numero_2); // max() devuelve el valor máximo entre dos valores
    std::cout << "el numero mayor es: " << numero_3 << "\n";
    numero_3 = std::min(numero_1, numero_2); // min() devuelve el valor mínimo entre dos valores
    std::cout << "el numero menor es: " << numero_3 << "\n";
    numero_3 = std::pow(numero_1, numero_2); // pow() devuelve el resultado de elevar el primer argumento a la potencia del segundo argumento
    std::cout << numero_1 << " elevado a la potencia de " << numero_2 << " es: " << numero_3 << "\n";
    numero_3 = std::sqrt(numero_2); // sqrt() devuelve la raíz cuadrada del argumento
    std::cout << "la raiz cuadrada de " << numero_2 << " es: " << numero_3 << "\n";
    numero_3 = std::abs(-5); // abs() devuelve el valor absoluto del argumento
    std::cout << "el valor absoluto de -5 es: " << numero_3 << "\n";
    numero_3 = std::round(3.14); // round() devuelve el valor redondeado al entero más cercano
    std::cout << "el valor redondeado de 3.14 es: " << numero_3 << "\n";
    numero_3 = std::ceil(3.14); // ceil() devuelve el valor redondeado hacia arriba al entero más cercano
    std::cout << "el valor redondeado hacia arriba de 3.14 es: " << numero_3 << "\n";
    numero_3 = std::floor(3.14); // floor() devuelve el valor redondeado hacia abajo al entero más cercano
    std::cout << "el valor redondeado hacia abajo de 3.14 es: " << numero_3 << "\n";
    std::cout << "estas funciones junto con la docuemtacion estan en cplusplus.com/reference/cmath/ \n";
    std::cout << "esto mismo aplica para cualquier libreria de la que se tenga dudas";

    return 0;
}