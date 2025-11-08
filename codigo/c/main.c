#include "lista.h"
#include "selection_sort.h"
#include "carrega_csv.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#ifdef _WIN32
#include <windows.h>
#include <direct.h>
#else
#include <sys/stat.h>
#endif

// Função simples para obter tempo em segundos
double obter_tempo() {
#ifdef _WIN32
    LARGE_INTEGER freq, counter;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&counter);
    return (double)counter.QuadPart / freq.QuadPart;
#else
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
#endif
}

// Calcula média
double calcular_media(double* valores, int n) {
    double soma = 0.0;
    for (int i = 0; i < n; i++) soma += valores[i];
    return soma / n;
}

// Calcula desvio padrão
double calcular_desvio(double* valores, int n, double media) {
    if (n <= 1) return 0.0;
    double soma = 0.0;
    for (int i = 0; i < n; i++) {
        double diff = valores[i] - media;
        soma += diff * diff;
    }
    return sqrt(soma / (n - 1));
}

// Executa experimento: carrega CSV e mede tempo de ordenação
double executar_experimento(const char* caminho_csv) {
    Lista* lista = carregar_csv(caminho_csv);
    if (!lista) return -1.0;
    
    double t_inicio = obter_tempo();
    selection_sort(lista);
    double t_fim = obter_tempo();
    
    lista_destruir(lista);
    return (t_fim - t_inicio) * 1000.0;  // Retorna em milissegundos
}

int main(int argc, char* argv[]) {
    int tamanhos[] = {10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
    int num_tamanhos = 10;
    int num_execucoes = 50;
    
    // Usa tamanhos passados por argumento
    if (argc > 1) {
        num_tamanhos = argc - 1;
        for (int i = 0; i < num_tamanhos; i++) {
            tamanhos[i] = atoi(argv[i + 1]);
        }
    }
    
    printf("EXPERIMENTOS - SELECTION SORT (C)\n");
    
    // Cria diretórios
#ifdef _WIN32
    _mkdir("..\\..\\resultados");
    _mkdir("..\\..\\resultados\\estatisticas");
#else
    mkdir("../../resultados", 0777);
    mkdir("../../resultados/estatisticas", 0777);
#endif
    
    FILE* resultado = fopen("../../resultados/estatisticas/resultados_C.csv", "w");
    if (!resultado) {
        printf("Erro ao criar arquivo\n");
        return 1;
    }
    fprintf(resultado, "n,tempo_ms,desvio\n");
    
    for (int t = 0; t < num_tamanhos; t++) {
        int n = tamanhos[t];
        printf("\nProcessando n=%d...\n", n);
        
        double tempos[50];
        int validos = 0;
        
        for (int exec = 1; exec <= num_execucoes; exec++) {
            char caminho[256];
            sprintf(caminho, "../../dados/n%06d/run_%03d.csv", n, exec);
            
            double tempo = executar_experimento(caminho);
            if (tempo >= 0) tempos[validos++] = tempo;
            
            if (exec % 10 == 0) printf("  %d/%d\n", exec, num_execucoes);
        }
        
        if (validos > 0) {
            double media = calcular_media(tempos, validos);
            double desvio = calcular_desvio(tempos, validos, media);
            fprintf(resultado, "%d,%.6f,%.6f\n", n, media, desvio);
            printf("  Media: %.3f ms, Desvio: %.3f ms\n", media, desvio);
        }
    }
    
    fclose(resultado);
    printf("\nResultados em: resultados/estatisticas/resultados_C.csv\n");
    return 0;
}
