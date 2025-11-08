#include "selection_sort.h"

void selection_sort(Lista* lista) {
    int n = lista_tamanho(lista);
    
    for (int i = 0; i < n; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            if (lista_get(lista, j) < lista_get(lista, min_index)) {
                min_index = j;
            }
        }
        if (i != min_index) {
            int temp = lista_get(lista, i);
            lista_set(lista, i, lista_get(lista, min_index));
            lista_set(lista, min_index, temp);
        }
    }
}
