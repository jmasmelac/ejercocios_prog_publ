//ordenar conjunto de numeros de menor a mallor y de mallor a menor 
#include <stdio.h>
int main() {
 int numeros_[]={19,14,59,1,4,9,6,22,2,5};
 int tam_num= sizeof(numeros_) / sizeof(numeros_[0]);//sizeof calcular el tamaño en bytes de un tipo de dato
    for (int i = 0; i < tam_num - 1; i++) {
        for (int j = 0; j < tam_num - 1; j++){
                if(numeros_[j]>numeros_[j+1]){
                   int temp_ =numeros_[j];
                   numeros_[j]=numeros_[j+1];
                   numeros_[j+1]=temp_ ;
                }
        }
    }
      for (int k = 0; k < tam_num; k++) {
        printf("%d ", numeros_[k]); // Imprime cada elemento seguido de un espacio
    }
     printf(" haora pa atra pa ");
    for (int i = tam_num -1; i >0 ; i--) {
        for (int j = tam_num -1; j >0 ; j--){
                if(numeros_[j]<numeros_[j-1]){
                   int temp_ =numeros_[j];
                   numeros_[j]=numeros_[j-1];
                   numeros_[j-1]=temp_ ;
                }
        }
    }
      for (int k = tam_num -1; k >=0 ; k--) {
        printf("%d ", numeros_[k]); 
    }
 return 0;
}