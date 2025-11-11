# Selection Sort em C - Versão Modular Otimizada

## 📁 Estrutura Modular

O projeto foi completamente modularizado para ganho de desempenho e manutenibilidade:

```
c/
├── main.c                  # Programa principal (orquestração)
├── selection_sort.h/c      # Implementação do algoritmo
├── csv_loader.h/c          # Carregamento otimizado de CSV
├── timer.h/c               # Medição de tempo de alta precisão
├── estatisticas.h/c        # Cálculos estatísticos
├── experimento.h/c         # Execução dos experimentos
└── Makefile                # Compilação otimizada
```

## 🚀 Otimizações Implementadas

### 1. **Modularização**
- Separação de responsabilidades em módulos independentes
- Facilita compilação separada e cache de objetos
- Permite otimizações específicas por módulo

### 2. **Flags de Compilação (-O3)**
- `-O3`: Otimização agressiva do compilador
- `-march=native`: Código otimizado para a CPU local
- `-flto`: Link Time Optimization (otimiza entre módulos)

### 3. **Otimizações de Código**
- **restrict**: Garante que ponteiros não se sobrepõem (selection_sort)
- **const**: Permite otimizações em funções estatísticas
- **static**: Funções privadas podem ser inlined
- **I/O otimizado**: Leitura de arquivo inteiro em memória

### 4. **Timer de Alta Precisão**
- Windows: QueryPerformanceCounter
- Linux: clock_gettime(CLOCK_MONOTONIC)
- Precisão de microssegundos

## 📊 Ganhos de Desempenho Esperados

| Otimização | Ganho Estimado |
|------------|----------------|
| -O3 vs -O2 | 5-15% |
| -march=native | 3-10% |
| -flto | 2-5% |
| restrict keyword | 1-5% |
| I/O otimizado | 10-20% (carregamento) |

**Ganho total esperado: 15-30% de melhoria**

## 🔨 Compilação

```bash
# Compilar com todas as otimizações
make clean
make

# Executar experimentos
make run
```

## 📝 Observações Técnicas

### Link Time Optimization (LTO)
O LTO permite que o compilador otimize através das fronteiras dos módulos, como se fossem um único arquivo, mas mantendo os benefícios da modularização.

### march=native
Gera instruções específicas para o processador onde está sendo compilado. **Atenção**: O binário pode não funcionar em CPUs diferentes.

### restrict
Informa ao compilador que o ponteiro é a única referência à memória, permitindo otimizações como vetorização de loops.

## 🎯 Benefícios da Modularização

1. **Compilação Incremental**: Recompila apenas módulos alterados
2. **Manutenibilidade**: Código organizado e fácil de entender
3. **Testabilidade**: Cada módulo pode ser testado independentemente
4. **Reutilização**: Módulos podem ser usados em outros projetos
5. **Desempenho**: Otimizações específicas por módulo

## 📄 Descrição dos Módulos

### selection_sort.h/c
Implementação pura do algoritmo Selection Sort com ponteiro restrict para otimização.

### csv_loader.h/c
Carrega CSV de forma otimizada:
- Lê arquivo inteiro na memória (uma única operação de I/O)
- Conta vírgulas para alocar memória exata
- Converte strings para inteiros em um único passo

### timer.h/c
Medição de tempo multiplataforma de alta precisão.

### estatisticas.h/c
Cálculo de média e desvio padrão otimizados com const.

### experimento.h/c
Coordena a execução: carrega dados, ordena e mede tempo.

### main.c
Orquestra os experimentos, processa resultados e salva estatísticas.

## 🔍 Comparação: Monolítico vs Modular

| Aspecto | Monolítico | Modular |
|---------|------------|---------|
| Linhas por arquivo | ~200 | ~20-80 |
| Compilação | Tudo sempre | Incremental |
| Manutenção | Difícil | Fácil |
| Otimizações | Genéricas | Específicas |
| Reuso | Impossível | Total |
