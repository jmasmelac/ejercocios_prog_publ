/*
Este proyecto está licenciado bajo una Licencia Creative Commons Atribución-NoComercial 4.0 Internacional.
 Puedes:
 - Compartir: copiar y redistribuir el material en cualquier medio o formato.
 - Adaptar: remezclar, transformar y construir sobre el material.
 Bajo las siguientes condiciones:
 - Atribución: debes dar crédito adecuado, proporcionar un enlace a la licencia e indicar si se realizaron cambios.
    No puedes sugerir que el licenciante te respalda a ti o al uso que hagas del material.
 - NoComercial: no puedes utilizar el material con fines comerciales.
 Puedes encontrar una copia completa de la licencia en el siguiente enlace: http://creativecommons.org/licenses/by-nc/4.0/legalcode

 © Author: Luko (Dev)
gestor_pedidos.c (c) 2024  February 12 13:28
Version:2024-02-12T18:28:58.253Z
Desc: descripcion abajo
 */
/*
Se te pide que implementes un programa en C que simule este sistema de gestión de pedidos utilizando pilas y colas. El programa debe permitir realizar las siguientes operaciones:
Agregar Pedido: Agregar un nuevo pedido al sistema. El pedido debe tener un número de pedido único, una lista de platos solicitados y el estado inicial "pendiente".
Marcar Pedido como Listo: Marcar un pedido como "listo para servir". El pedido debe ser eliminado de la cola de pedidos pendientes y agregado a la pila de pedidos listos.
Servir Pedido: Servir el pedido más antiguo que esté listo para servir. El pedido debe ser eliminado de la pila de pedidos listos.
Mostrar Pedidos Pendientes: Mostrar todos los pedidos pendientes en orden de llegada.
Mostrar Pedidos Listos: Mostrar todos los pedidos listos para servir en orden de preparación.
Mostrar Último Pedido Servido: Mostrar el último pedido que fue servido.
*/
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include <time.h>//libreria para tomar el tiempo exacto para el id

#define tamaño_arreglo 10

typedef struct {//declaracion de pedidos donde se toma el id, la orden y el estado
  long long int Identificador;//variable que se le asgnara la fecha exacta como id
   char Orden_[200];//orden del cliente a cocinar
   char estado[20];//estado del pedido
} Pedidos;

long long Identificador_fecha_hora() {
    time_t tiempo_actual;
    struct tm *info_tiempo;
    
    time(&tiempo_actual);
    info_tiempo = localtime(&tiempo_actual);

    long long identificador = (((info_tiempo->tm_year + 1900) % 100) * 10000000LL) + 
                              ((info_tiempo->tm_yday + 1) * 10000LL) +
                              (info_tiempo->tm_hour * 100LL) +
                              info_tiempo->tm_min;
    return identificador;
}

int main(){
   Pedidos Orden_cliente[10];
   int opcion;
   int selector;//variable caso 2
   for(int i=0;i<11;i++){//ciclo que inicializa las variables en 0
      Orden_cliente[i].Identificador=0;
      strcpy(Orden_cliente[i].estado, " ");
      strcpy(Orden_cliente[i].Orden_, " ");
   }
   //int tamaño_arreglo=10;
   do{
    printf("\n--- GESTION DE PEDIDOS ---\n");
            printf("1. Agregar pedido \n");
            printf("2. Orden lista \n");
            printf("3. Servir pedido \n");
            printf("4. Pedidos pendientes \n");
            printf("5. Pedodos listos \n");
            printf("6. Ultimos pedidos servidos\n");
            printf("0. Salir\n");
            printf("Seleccione una opcion: ");
            scanf("%d", &opcion);
            switch (opcion) {
               case 1://Agregar pedido
               
               if (Orden_cliente[tamaño_arreglo - 1].Identificador != 0) {
                  printf("cocina a su capacidad maxima verifique si ya esta lista alguna orden\n");
                  break;
                  }else{
                     for(int i = tamaño_arreglo - 1; i >= 0; i--){
                           Orden_cliente[i] = Orden_cliente[i-1];
                     }
               }
                printf("Ingrese la orden del cliente: ");
                scanf("%s", Orden_cliente[0].Orden_);
                printf("\n");
                Orden_cliente[0].Identificador=Identificador_fecha_hora();
                strcpy(Orden_cliente[0].estado, "espera");
                printf("\nla orden es :\n %s\n id: %lld\n estado: %s\n",Orden_cliente[0].Orden_,Orden_cliente[0].Identificador,Orden_cliente[0].estado);
               break;
               case 2://Orden lista
               for(int i = 0; i < tamaño_arreglo; i++) {
                     
                        printf("%d %s %lld %s \n",i, Orden_cliente[i].Orden_, Orden_cliente[i].Identificador, Orden_cliente[i].estado);
                     
               }
               printf("que orden se encuentra lista (escriba el numero)");
               scanf("%d",selector);
               for(int i = 0; i < tamaño_arreglo; i++) {
                  if(selector==i){   
                       strcpy(Orden_cliente[selector].estado, "listo");
                  }
               }
               break;
               case 3://Servir pedido
               break;
               case 4://Pedidos pendientes
               printf("van de la orden mas nueva a la mas antigua\n");
                for(int i = 0; i < tamaño_arreglo; i++) {
                     if(strcmp(Orden_cliente[i].estado, "espera") == 0) {
                        printf("%s %lld %s \n", Orden_cliente[i].Orden_, Orden_cliente[i].Identificador, Orden_cliente[i].estado);
                     }
               }
               break;
               case 5://Pedodos listos
               break;
               case 6://Ultimos pedidos servidos
               break;
               case 0://Salir
               printf("Saliendo del programa...\n");
               break;
               default:
               printf("Opcion no valida. Por favor, seleccione una opcion valida.\n");
               break;
            }
    }while (opcion != 0);
    return 0;
}