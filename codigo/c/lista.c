#include "lista.h"
#include <stdlib.h>
#include <stdio.h>

struct Lista {
    int* elementos;
    int tamanho;
    int capacidade;
};

Lista* lista_criar() {
    Lista* lista = (Lista*)malloc(sizeof(Lista));
    lista->elementos = (int*)malloc(10 * sizeof(int));
    lista->tamanho = 0;
    lista->capacidade = 10;
    return lista;
}

void lista_adicionar(Lista* lista, int valor) {
    if (lista->tamanho >= lista->capacidade) {
        lista->capacidade *= 2;
        lista->elementos = (int*)realloc(lista->elementos, lista->capacidade * sizeof(int));
    }
    lista->elementos[lista->tamanho++] = valor;
}

int lista_tamanho(const Lista* lista) {
    return lista->tamanho;
}

int lista_get(const Lista* lista, int index) {
    return lista->elementos[index];
}

void lista_set(Lista* lista, int index, int valor) {
    lista->elementos[index] = valor;
}

void lista_destruir(Lista* lista) {
    if (lista) {
        free(lista->elementos);
        free(lista);
    }
}
