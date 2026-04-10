#include <iostream>
int main(){
    std::string nombre_completo;
    nombre_completo = "Máximo Décimo Meridio, comandante de los ejércitos del norte, general de las legiones Félix, leal servidor del verdadero emperador Marco Aurelio";
    printf("la cadena de texto es: %s\n", nombre_completo.c_str());
    printf("el tamaño de la cadena de texto es: %ld\n", nombre_completo.length());
    printf("el tamaño de la cadena de texto es: %lu\n", nombre_completo.size());

    /*
    ojo la diferencia entre length y size es que length devuelve el numero de caracteres de la cadena, 
    mientras que size devuelve el numero de bytes que ocupa la cadena en memoria, 
    esto es importante porque en algunos casos una cadena puede tener caracteres especiales que ocupan mas de un byte, 
    por ejemplo los emojis, entonces en ese caso length y size pueden devolver valores diferentes, pero en este caso como no hay caracteres especiales ambos devuelven el mismo valor
    en la terminal los resultados son ->
    "el tama├▒o de la cadena de texto es: ö
    el tama├▒o de la cadena de texto es: 148"
    esto se debe a que "ö" es el ascii 148 (usando %lu), si se cambia a %ld en el printf se obtiene el resultado correcto,
    ya que %ld es el formato de long int, pero %lu es el formato de unsigned long int
    */

    printf("el nombre esta vacio? %s\n", nombre_completo.empty() ? "si" : "no");
    //la ? se llama operador ternario, es una forma de escribir un if en una sola linea, la sintaxis es -> condicion ? valor_si_verdadero : valor_si_falso
    //el metodo empty() devuelve true si la cadena esta vacia, y false si no lo esta, entonces en este caso como la cadena no esta vacia devuelve false, por lo tanto se imprime "no"

    printf("el metodo clear() borra el contenido de la cadena, no lo hago pero seira como \n");
    //nombre_completo.clear();

    printf("añadamos el final de la frase:\n %s\n", nombre_completo.append(" Padre de un hijo asesinado, marido de una mujer asesinada y alcanzaré mi venganza, en esta vida o en la otra").c_str());
    // el .c_str() se usa para convertir la cadena a algo inprimible en consola, no hace falta si se usa std::cout

    printf("miremos que hay en la poscion 20 de la cadena: %c\n", nombre_completo.at(20));
    // el metodo at() devuelve el caracter en la posicion indicada

    printf("cambiemos el caranter en la poscicion 1 a `a`:\n");
    nombre_completo[1] = 'a';
    nombre_completo.insert(9, "e");// el metodo insert() inserta una cadena en la posicion indicada
    printf("la cadena de texto es: %s\n", nombre_completo.c_str());

    printf("la pralablra 'general' esta en la  posicion: %ld\n", nombre_completo.find("general"));
    // el metodo find() devuelve la posicion de la "primera" ocurrencia de la cadena indicada,

    printf("esta muy largo el nombre, recortemoslo y que quede en : %s\n",nombre_completo.erase(24, 235).c_str());
    // el metodo erase() borra una parte de la cadena (lo que uno indique, depende de caracteres especiales y de la lonngitud de la cadena)

    printf("los metodos para manejar cadenas de texto son muchos, solo es poner . en la variable y identificar que hace cada uno");

    return 0;
}