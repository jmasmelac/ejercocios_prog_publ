// calculadora basica ejercicio de ejemplo y pruebas
#include <iostream>
int main(){
    int operacion_mat;
    double num_1;
    double num_2;
    double resultado_;
    printf("ingrese la operacion a hacer (suma(1) , resta(2) , multiplicacion(3) , division(4) )\n");
    std::cin>>operacion_mat;
    printf("ahora ingrese el primer valor a ser operado (numero)\n");
    std::cin>>num_1;
    printf("ahora ingrese el segundo valor a ser operado (numero)\n");
    std::cin>>num_2;
    switch (operacion_mat)
    {
        case 1:
         resultado_ = num_1 + num_2;
        printf("el resultado de la operacion de sumar es %.2f\n",resultado_);
        break;
        case 2:
         resultado_ = num_1 - num_2;
        printf("el resultado de la operacion de restar es %.2f\n",resultado_);
        break;
        case 3:
         resultado_ = num_1 * num_2;
        printf("el resultado de la operacion de multiplicar es %.2\nf",resultado_);
        break;
        case 4:
         // ojo num_2 no puede ser 0 eso esta indeterminado
            if (num_2==0){
                printf("ojo manito las divisiones entre 0 no dan, por ende su resultado se lo pongo en 0");
                resultado_ =0;
            }else{
                resultado_ = num_1 / num_2;
                 printf("el resultado de la operacion de dividir es %.2f\n", resultado_);
            }
         
        break;
    
    default:
        printf("caso de operacion no valido para esta calculadora");
        break;
    }

    std::cout<<"para poner mas bonitos los resultados en terminal se puede usar esta sentencia, el resultado de la operacion fue: "<<resultado_<<std::endl;

    return 0;
}