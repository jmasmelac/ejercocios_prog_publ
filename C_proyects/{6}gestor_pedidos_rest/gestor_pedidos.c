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
