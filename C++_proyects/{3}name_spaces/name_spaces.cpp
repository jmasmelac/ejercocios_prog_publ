/*
los nombres de espacios o namespaces son una forma de organizar el código en C++. 
Permite declarar variables que compartan el mismo nombre.
*/
#include <iostream>
namespace primero{
    int numero = 10;
}
namespace segundo{
    int numero = 20;
}
int main(){
    int numero = 30;
    //si no estubiera declarada la variable numero aca usando
    //usin namespace primero;
    //using namespace segundo;
    //tomaria el valor declarado en esos namespaces
    printf("El numero dentro de main es: %d\n", numero);
    printf("El numero dentro del namespace primero es: %d\n", primero::numero);
    printf("El numero dentro del namespace segundo es: %d\n", segundo::numero);
    // usualmente se usa esta sentencia para lo siguiente
    using namespace std;
    cout<<"el using namespace std; es para no tener que escribir std:: antes de cada elemento del espacio de nombres std"<<endl;

    

    return 0;
}