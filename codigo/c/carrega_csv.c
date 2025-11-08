#include "carrega_csv.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

Lista* carregar_csv(const char* caminho) {
    FILE* arquivo = fopen(caminho, "r");
    if (!arquivo) return NULL;
    
    Lista* lista = lista_criar();
    char buffer[1048576];  // 1MB buffer
    
    if (fgets(buffer, sizeof(buffer), arquivo) == NULL) {
        fclose(arquivo);
        lista_destruir(lista);
        return NULL;
    }
    
    char* token = strtok(buffer, ",");
    while (token != NULL) {
        lista_adicionar(lista, atoi(token));
        token = strtok(NULL, ",");
    }
    
    fclose(arquivo);
    return lista;
}
