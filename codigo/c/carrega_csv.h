#ifndef CARREGA_CSV_H
#define CARREGA_CSV_H

#include "lista.h"

/**
 * Carrega uma lista de inteiros a partir de um arquivo CSV
 * O CSV deve conter uma única linha com valores separados por vírgula
 */
Lista* carregar_csv(const char* caminho);

#endif
