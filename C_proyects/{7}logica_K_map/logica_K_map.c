// ojo este código falta pulir la lógica , aun no esta completo hay detalles lógicos que falta por resolver

#include <stdio.h>

#define FILAS 2  // En C, los tamaños son constantes
#define COLUMNAS 2

// Función para verificar si un grupo es una potencia de 2
int esPotenciaDe2(int n) {
    return (n != 0) && ((n & (n - 1)) == 0);
}

// Función para encontrar grupos de 1 en la matriz
void encontrarGrupos(int K_map[FILAS][COLUMNAS], int asignados[FILAS][COLUMNAS]) {
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            if (K_map[i][j] == 1 && !asignados[i][j]) {
                // Marcar el elemento actual como asignado
                asignados[i][j] = 1;
                int grupo[FILAS][COLUMNAS] = {0};
                grupo[i][j] = 1;

                // Buscar adyacentes y formar el grupo
                int tamanoGrupo = 1;
                int cambios = 1;
                while (cambios > 0) {
                    cambios = 0;
                    for (int k = 0; k < FILAS; k++) {
                        for (int l = 0; l < COLUMNAS; l++) {
                            if (grupo[k][l] == 1) {
                                // Verificar adyacencia a la derecha
                                if (K_map[k][(l + 1) % COLUMNAS] == 1 && !asignados[k][(l + 1) % COLUMNAS]) {
                                    grupo[k][(l + 1) % COLUMNAS] = 1;
                                    asignados[k][(l + 1) % COLUMNAS] = 1;
                                    tamanoGrupo++;
                                    cambios++;
                                }
                                // Verificar adyacencia abajo
                                if (K_map[(k + 1) % FILAS][l] == 1 && !asignados[(k + 1) % FILAS][l]) {
                                    grupo[(k + 1) % FILAS][l] = 1;
                                    asignados[(k + 1) % FILAS][l] = 1;
                                    tamanoGrupo++;
                                    cambios++;
                                }
                                // Verificar adyacencia a la izquierda
                                if (K_map[k][(l - 1 + COLUMNAS) % COLUMNAS] == 1 && !asignados[k][(l - 1 + COLUMNAS) % COLUMNAS]) {
                                    grupo[k][(l - 1 + COLUMNAS) % COLUMNAS] = 1;
                                    asignados[k][(l - 1 + COLUMNAS) % COLUMNAS] = 1;
                                    tamanoGrupo++;
                                    cambios++;
                                }
                                // Verificar adyacencia arriba
                                if (K_map[(k - 1 + FILAS) % FILAS][l] == 1 && !asignados[(k - 1 + FILAS) % FILAS][l]) {
                                    grupo[(k - 1 + FILAS) % FILAS][l] = 1;
                                    asignados[(k - 1 + FILAS) % FILAS][l] = 1;
                                    tamanoGrupo++;
                                    cambios++;
                                }
                            }
                        }
                    }
                }

                // Verificar si el tamaño del grupo es una potencia de 2
                if (esPotenciaDe2(tamanoGrupo)) {
                    printf("Grupo de tamaño %d encontrado:\n", tamanoGrupo);
                    for (int k = 0; k < FILAS; k++) {
                        for (int l = 0; l < COLUMNAS; l++) {
                            if (grupo[k][l] == 1) {
                                printf("(%d, %d) ", k, l);
                            }
                        }
                    }
                    printf("\n");
                }
            }
        }
    }
}

int main() {
    // Declaración e inicialización de la matriz de 4x4
    int K_map[FILAS][COLUMNAS] = {
        {1, 1},
        {1, 0}
    };

    // Matriz auxiliar para marcar los elementos asignados a un grupo
    int asignados[FILAS][COLUMNAS] = {0};

    // Imprimir el tamaño de la matriz
    printf("Numero de filas: %d\n", FILAS);
    printf("Numero de columnas: %d\n", COLUMNAS);

    // Imprimir la matriz para verificar la inicialización
    printf("Matriz K_map de %dx%d:\n", FILAS, COLUMNAS);
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            printf("%d ", K_map[i][j]);
        }
        printf("\n");
    }

    // Encontrar grupos de 1
    encontrarGrupos(K_map, asignados);

    return 0;
}








