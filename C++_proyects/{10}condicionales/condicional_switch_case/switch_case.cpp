#include <iostream>
int main(){
    int mes_a;

    printf("ingrese el mes (1-12) \n");
    std::cin>>mes_a;

    switch (mes_a)
    {
        // en estos casos es comun editar varias lineas para ello usar ctrl+d para seleccionarlas y editarlas al mismo tiempo
        // es mas facil de leer que un if anidado
        case 1:
        printf(" es el mes de enero \n");
        break;//el break se usa en este caso para romper la comparacion y salir del switch
        case 2:
        printf(" es el mes de febrero \n");
        break;
        case 3:
        printf(" es el mes de marzo \n");
        break;
        case 4:
        printf(" es el mes de abril \n");
        break;
        case 5:
        printf(" es el mes de mayo \n");
        break;
        case 6:
        printf(" es el mes de junio \n");
        break;
        case 7:
        printf(" es el mes de julio \n");
        break;
        case 8:
        printf(" es el mes de agosto \n");
        break;
        case 9:
        printf(" es el mes de septiembre \n");
        break;
        case 10:
        printf(" es el mes de octubre \n");
        break;
        case 11:
        printf(" es el mes de noviembre \n");
        break;
        case 12:
        printf(" es el mes de diciembre \n");
        break;
    
        default://si no hay casos coincidentes se ejecuta esta sentencia,
        printf("caso de mes no valido (no es un numero entre 1-12) \n");
        break;
    }

    return 0;
}