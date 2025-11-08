#ifndef LISTA_H
#define LISTA_H

typedef struct Lista Lista;

/**
 * Cria uma nova lista vazia
 */
Lista* lista_criar();

/**
 * Adiciona um inteiro ao final da lista
 */
void lista_adicionar(Lista* lista, int valor);

/**
 * Retorna o tamanho da lista
 */
int lista_tamanho(const Lista* lista);

/**
 * Retorna o elemento no índice especificado
 */
int lista_get(const Lista* lista, int index);

/**
 * Define o valor no índice especificado
 */
void lista_set(Lista* lista, int index, int valor);

/**
 * Destrói a lista e libera memória
 */
void lista_destruir(Lista* lista);

#endif
