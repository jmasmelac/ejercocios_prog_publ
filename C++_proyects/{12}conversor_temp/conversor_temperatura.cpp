#include <iostream>

int main(){
    double temperatura_;
    char tipo_temperatura;
    double temperatura_convertida;
    printf("Ingrese si la temperatura es Farenegtie o Celsius escribiendo `C` ô `F` respectivamente \n");
    scanf("%c",&tipo_temperatura);
    printf("Ahora ingrese el valor de la temperatura a convertir \n");
    scanf("%lf",&temperatura_);
    switch (tipo_temperatura)
    {   case 'C':
        case 'c':
            temperatura_convertida = (temperatura_ * 9/5) + 32;
            printf("la temperatura convertida a Farenheit es: %.2f\n", temperatura_convertida);
        break;
        case 'F':
        case 'f':
            temperatura_convertida = (temperatura_ - 32) * 5/9;
            printf("la temperatura convertida a Celsius es: %.2f\n", temperatura_convertida);
        break;
        default:
            printf("caso de tipo de temperatura no valido, por favor ingrese `C` o `F` para indicar el tipo de temperatura a convertir \n");
    }
    printf("usando operadores lógicos, ");
    if(tipo_temperatura == 'F' || tipo_temperatura == 'F' ){
        temperatura_convertida = (temperatura_ - 32) * 5/9;
            printf("la temperatura convertida a Celsius es: %.2f\n", temperatura_convertida);
    }else if (tipo_temperatura == 'C' || tipo_temperatura == 'c'){
        temperatura_convertida = (temperatura_ * 9/5) + 32;
            printf("la temperatura convertida a Farenheit es: %.2f\n", temperatura_convertida);
    }else{
        printf("caso de tipo de temperatura no valido, por favor ingrese `C` o `F` para indicar el tipo de temperatura a convertir \n");
    }
    
    return 0;
}