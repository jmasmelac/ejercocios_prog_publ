#include <iostream>
int main(){
    
    //if es una condicion , donde si se cumple algo se ejecuta un segmento de codigo

    int edad;
    printf("ingrese su edad \n");
    std::cin>>edad;


    if (edad>0 && edad < 100){
        //los condicionales se pueden anidar pero es una mala practica anidarlos mucho ya que pierde legibilidad
        if(edad<18){
            printf("usted es menor de edad");
        }else{
            printf("usted es mayor de edad");
        }
        // otra cosa es tener mucho ojo con las condiciones, ya que lo ideal es que sean cortas, el uso de comparadores logicos se pueden abrebiar usando tablas de vedad
    }else{
        printf("valor de edad no valido");
    }
    if(edad>100 && edad < 120){
        printf("como que tiene mas de 100 años , pero usted deberia estar en un asilo");
    }else if(edad>120){
        printf("como que mas de 120 años deje de robar aire a este mundo");
    }else{
        printf("como que una edad negativa acaso esta tonto o que?");
    }


    return 0;
}