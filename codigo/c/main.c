#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <windows.h>
#include "selection_sort.h"

int* ler_csv(const char* caminho, int* tamanho) {
    FILE* arquivo = fopen(caminho, "r");
    if (!arquivo) {
        printf("Erro ao abrir arquivo: %s\n", caminho);
        return NULL;
    }
    
    int num, count = 0;
    
    /* Contar elementos primeiro */
    while (fscanf(arquivo, "%d,", &num) == 1) {
        count++;
    }
    
    if (count == 0) {
        fclose(arquivo);
        *tamanho = 0;
        return NULL;
    }
    
    /* Alocar tamanho exato */
    int* arr = (int*)malloc(count * sizeof(int));
    if (!arr) {
        fclose(arquivo);
        printf("Erro de memoria\n");
        return NULL;
    }
    
    /* Voltar ao inicio e ler valores */
    rewind(arquivo);
    int i = 0;
    while (i < count && fscanf(arquivo, "%d,", &num) == 1) {
        arr[i++] = num;
    }
    
    fclose(arquivo);
    *tamanho = i;
    return arr;
}

double calcular_media(double* valores, int n) {
    double soma = 0.0;
    int i;
    for (i = 0; i < n; i++) {
        soma += valores[i];
    }
    return soma / n;
}

double calcular_desvio(double* valores, int n, double media) {
    double soma = 0.0;
    double diff;
    int i;
    
    if (n <= 1) return 0.0;
    
    for (i = 0; i < n; i++) {
        diff = valores[i] - media;
        soma += diff * diff;
    }
    return sqrt(soma / (n - 1));
}

int main() {
    int exec, t;
    LARGE_INTEGER freq, inicio, fim;
    double tempos[50];
    double media, desvio;
    int tamanhos[] = {10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
    int num_tamanhos = 10;
    FILE* resultado;
    
    QueryPerformanceFrequency(&freq);
    
    resultado = fopen("../../resultados/estatisticas/resultados_C.csv", "w");
    if (!resultado) {
        printf("Erro ao criar arquivo de resultados\n");
        return 1;
    }
    
    fprintf(resultado, "n,tempo_ms,desvio\n");
    
    for (t = 0; t < num_tamanhos; t++) {
        int n = tamanhos[t];
        
        printf("\nProcessando n=%d...\n", n);
        
        for (exec = 1; exec <= 50; exec++) {
            char caminho[256];
            int tamanho;
            int* arr;
            
            sprintf(caminho, "../../dados/n%06d/run_%03d.csv", n, exec);
            
            arr = ler_csv(caminho, &tamanho);
            if (!arr) continue;
            
            QueryPerformanceCounter(&inicio);
            selection_sort(arr, tamanho);
            QueryPerformanceCounter(&fim);
            
            tempos[exec - 1] = ((double)(fim.QuadPart - inicio.QuadPart) / freq.QuadPart) * 1000.0;
            
            if (exec == 25) {
                printf("  25/50 concluidos\n");
            } else if (exec == 50) {
                printf("  50/50 concluidos\n");
            }
            
            free(arr);
        }
        
        media = calcular_media(tempos, 50);
        desvio = calcular_desvio(tempos, 50, media);
        
        printf("  Media: %.6f ms | Desvio: %.6f ms\n", media, desvio);
        
        fprintf(resultado, "%d,%.6f,%.6f\n", n, media, desvio);
    }
    
    fclose(resultado);
    
    printf("\nResultados salvos em: resultados/estatisticas/resultados_C.csv\n");
    
    return 0;
}