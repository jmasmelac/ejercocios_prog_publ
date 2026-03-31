#include <iostream>
int main(){
    std::string nombre;
    int edad;
    std::cout <<"las entradas de texto puede ser: \n";
    std::cout << "tu nombre es: \n";
    std::cin >> nombre;
    std::cout << "Hola, " << nombre << "!\n";
    std::cout << "cual es tu edad? \n";
    std::cin >> edad;
    std::cout << "tu edad es: " << edad << " aunque sea grosero preguntar\n";

    //si se ingresa una frase con espacios, solo se tomara la primera palabra,los espacios se consideran delimitadores
    // la funcion getline() se puede usar para leer una linea completa de texto, incluyendo espacios, hasta que se presione enter
    std::string frase;
    std::cout << "escribe una frase: \n";
    std::getline(std::cin, frase);
    std::cout << "la frase que escribiste es: " << frase << "\n";
    std::cout << "lo notaste hay un problema ya que con el salto de linea anterior, el getline() no funciona correctamente \n";
    std::cout << "para solucionar esto, se puede usar ";
    std::cout << "ingrese otra frase: \n";
    std::getline(std::cin>>std::ws, frase); // std::ws se usa para ignorar los espacios en blanco antes de la entrada
    std::cout << "la frase que escribiste es: " << frase << "\n";

    char nombre_[100];
    int edad_;
    char frase_[200];
    
    printf("las entradas de texto puede ser: \n");
    printf("tu nombre es: \n");
    scanf("%99s", nombre_);//el %99s se usa para evitar el desbordamiento de buffer, ya que el tamaño del array es 100, se deja un espacio para el caracter nulo '\0'
    printf("Hola, %s!\n", nombre_);
    printf("cual es tu edad? \n");
    scanf("%d", &edad_);
    printf("tu edad es: %d aunque sea grosero preguntar\n", edad_);
    
    // si se ingresa una frase con espacios, solo se tomara la primera palabra,
    // los espacios se consideran delimitadores
    // fgets() se puede usar para leer una linea completa de texto,
    // incluyendo espacios, hasta que se presione enter
    
    printf("escribe una frase: \n");
    //getchar(); // Limpiar el buffer del salto de linea anterior (otro metodo de solucionar el problema del salto de linea)
    fgets(frase_, sizeof(frase_), stdin);
    printf("la frase que escribiste es: %s", frase_);
    printf("lo notaste hay un problema ya que con el salto de linea anterior, el fgets() no funciona correctamente \n");
    printf("para solucionar esto, se puede usar ");
    printf("ingrese otra frase: \n");
    fgets(frase_, sizeof(frase_), stdin);
    printf("la frase que escribiste es: %s", frase_);

}