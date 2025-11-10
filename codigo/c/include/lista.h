#ifndef LISTA_H
#define LISTA_H

typedef struct Lista Lista;

Lista* lista_criar();

void lista_adicionar(Lista* lista, int valor);

int lista_tamanho(const Lista* lista);

int lista_get(const Lista* lista, int index);

void lista_set(Lista* lista, int index, int valor);

void lista_destruir(Lista* lista);

#endif
