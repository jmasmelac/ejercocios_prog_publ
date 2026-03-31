/*
Los alias de tipo son una forma de crear nombres alternativos para los tipos existentes en C++.
*/
#include <iostream>
#include <vector>

typedef std::vector<std::pair<std::string, int>> Pair_list_t;// alias de vector de pares de string e int
typedef std::string text_t;// alias de string
typedef int numero_t;// alias de int

using texto_t = std::string;// alias de string usando la palabra reservada using
using numero_alias_t = int;// alias de int usando la palabra reservada using

int main(){
    Pair_list_t my_list = {{"Alice", 30}, {"Bob", 25}}; // usando el alias de vector de pares
    text_t name = "Charlie"; // usando el alias de string
    numero_t age = 30; // usando el alias de int
    texto_t another_name = "Dave"; // usando el alias de string con using
    numero_alias_t another_age = 40; // usando el alias de int con using   
    printf("los nombres y edades son:\n");
    printf("%s: %d\n", my_list[0].first.c_str(), my_list[0].second);
    printf("%s: %d\n", my_list[1].first.c_str(), my_list[1].second);
    printf("el nombre es: %s\n", name.c_str());
    printf("la edad es: %d\n", age); 
    printf("el otro nombre es: %s\n", another_name.c_str());
    printf("la otra edad es: %d\n", another_age); 

    return 0;
}