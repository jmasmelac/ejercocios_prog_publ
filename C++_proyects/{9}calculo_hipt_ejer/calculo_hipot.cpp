//calculo de una hipotenusa usando la funcion sqrt() de la libreria cmath
#include <iostream>
#include <cmath> // para usar la funcion sqrt()
int main(){
    double cateto_1 ;
    double cateto_2 ;
    double hipotenusa;

    std::cout << "ingrese el valor del primer cateto: (numero mayor a 1)\n";
    std::cin >> cateto_1;
    std::cout << "ingrese el valor del segundo cateto: (numero mayor a 1)\n";
    std::cin >> cateto_2;
    // cateto_1^2 + cateto_2^2 = hipotenusa^2
    hipotenusa = std::sqrt(std::pow(cateto_1, 2) + std::pow(cateto_2, 2)); // sqrt() devuelve la raíz cuadrada del argumento, pow() devuelve la potencia al 2 como en la formula
    std::cout << "la hipotenusa es: " << hipotenusa << "\n";

    return 0;
}