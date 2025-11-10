#include "carrega_csv.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* carregar_csv(const char* caminho, int* tamanho) {
    FILE* arquivo = fopen(caminho, "r");
    if (!arquivo) return NULL;
    
    // Alocar buffer dinamicamente para evitar stack overflow
    char* buffer = (char*)malloc(1048576);
    if (!buffer) {
        fclose(arquivo);
        return NULL;
    }
    
    if (fgets(buffer, 1048576, arquivo) == NULL) {
        fclose(arquivo);
        free(buffer);
        return NULL;
    }
    fclose(arquivo);
    
    // Primeira passagem: contar elementos
    int count = 0;
    char* temp_buffer = (char*)malloc(1048576);
    if (!temp_buffer) {
        free(buffer);
        return NULL;
    }
    strcpy(temp_buffer, buffer);
    char* token = strtok(temp_buffer, ",");
    while (token != NULL) {
        count++;
        token = strtok(NULL, ",");
    }
    free(temp_buffer);
    
    // Alocar array
    int* arr = (int*)malloc(count * sizeof(int));
    if (!arr) {
        free(buffer);
        return NULL;
    }
    
    // Segunda passagem: preencher array
    int idx = 0;
    token = strtok(buffer, ",");
    while (token != NULL) {
        arr[idx++] = atoi(token);
        token = strtok(NULL, ",");
    }
    free(buffer);
    
    *tamanho = count;
    return arr;
}
