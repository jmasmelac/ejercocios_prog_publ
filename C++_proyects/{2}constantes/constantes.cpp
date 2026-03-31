#include <iostream>

int main() {
   /*
   la palabra reservada const se utiliza para declarar una constante, 
   es decir, un valor que no puede ser modificado después de su inicialización. 
   En este caso, se declara una constante llamada pi_ con el valor de 3.1416.
   */
    const double pi_ = 3.1416;
    double radio_ = 5.0;
    double circunferencia = 2 * pi_ * radio_;

    printf("La circunferencia es: %.2f\n", circunferencia);

    printf("otro caso es el siguiente: \n");
    const double plank_constant = 6.62607015e-34; // constante de Planck en joules por segundo
    double frecuencia_foton = 5e14; // frecuencia de un fotón en hertz
    double energia_foton = plank_constant * frecuencia_foton; // energía del fotón en joules
    printf("La energía del fotón es: %.2e joules\n", energia_foton);
    printf("el principal uso de const es definir parametros fundamentales que son constantes universales\n");
    printf("normalmente se usan en códigos que hay caracteristicas que nunca cambian y se declaran al principio de los mismos\n");

    system("pause");
    return 0;
}