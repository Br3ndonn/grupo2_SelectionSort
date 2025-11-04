"""
Script principal para executar experimentos do Selection Sort e gerar estatísticas
"""
from pathlib import Path
from time import perf_counter
import csv
import statistics
import sys
from carrega_lista import carregar_lista_csv
from selection_sort import selection_sort
from lista import Lista


def executar_experimento(caminho_csv, verbose=False):
    """
    Executa um único experimento: carrega CSV e ordena
    
    Args:
        caminho_csv: Path para o arquivo CSV
        verbose: exibe tempos detalhados de leitura e ordenação
        
    Returns:
        tempo_s: tempo de execução da ordenação em segundos (SEM incluir leitura)
    """
    # Tempo de leitura (NÃO contabilizado nas estatísticas)
    t_leitura_inicio = perf_counter()
    lista = carregar_lista_csv(caminho_csv)
    t_leitura_fim = perf_counter()
    tempo_leitura_ms = (t_leitura_fim - t_leitura_inicio) * 1000
    
    # Tempo de ordenação (ÚNICO tempo contabilizado)
    t_inicio = perf_counter()
    selection_sort(lista)
    t_fim = perf_counter()
    tempo_ordenacao_s = t_fim - t_inicio
    
    if verbose:
        print(f"    Leitura: {tempo_leitura_ms:.3f} ms | Ordenação: {tempo_ordenacao_s:.6f} s")
    
    # Retorna APENAS o tempo de ordenação em segundos
    return tempo_ordenacao_s


def executar_todos_experimentos(tamanhos_especificos=None):
    """
    Executa todos os experimentos e gera o arquivo de resultados
    
    Args:
        tamanhos_especificos: lista de tamanhos específicos para executar (opcional)
    """
    # Diretórios
    base_dir = Path(__file__).resolve().parents[2]
    dados_dir = base_dir / "dados"
    resultados_dir = base_dir / "resultados" / "estatisticas"
    resultados_dir.mkdir(parents=True, exist_ok=True)
    
    # Arquivo de saída
    arquivo_resultados = resultados_dir / "resultados_Python.csv"
    
    # Tamanhos dos vetores
    if tamanhos_especificos:
        tamanhos = tamanhos_especificos
    else:
        tamanhos = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    num_execucoes = 50
    
    print("="*60)
    print("EXPERIMENTOS - SELECTION SORT (PYTHON)")
    print("="*60)
    
    resultados = []
    
    for tamanho in tamanhos:
        dir_tamanho = dados_dir / f"n{tamanho:06d}"
        
        print(f"\nProcessando n={tamanho}...")
        
        tempos = []
        
        for execucao in range(1, num_execucoes + 1):
            arquivo_csv = dir_tamanho / f"run_{execucao:03d}.csv"
            
            if not arquivo_csv.exists():
                print(f"  AVISO: Arquivo {arquivo_csv} não encontrado!")
                continue
            
            try:
                tempo_s = executar_experimento(arquivo_csv)
                tempos.append(tempo_s)
                
                if execucao % 10 == 0:
                    print(f"  Progresso: {execucao}/{num_execucoes} execuções")
                    
            except Exception as e:
                print(f"  ERRO na execução {execucao}: {e}")
                continue
        
        if tempos:
            # Calcula estatísticas
            media_tempo = statistics.mean(tempos)
            desvio_padrao = statistics.stdev(tempos) if len(tempos) > 1 else 0.0
            
            resultados.append({
                'n': tamanho,
                'tempo_s': media_tempo,
                'desvio': desvio_padrao
            })
            
            print(f"  ✓ Concluído: média={media_tempo:.6f} s, desvio={desvio_padrao:.6f} s")
        else:
            print(f"  ✗ Nenhum tempo válido coletado para n={tamanho}")
    
    # Salva resultados em CSV
    print(f"\n{'='*60}")
    print("Salvando resultados...")
    
    with open(arquivo_resultados, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'tempo_s', 'desvio'])
        
        for resultado in resultados:
            writer.writerow([
                resultado['n'],
                f"{resultado['tempo_s']:.6f}",
                f"{resultado['desvio']:.6f}"
            ])
    
    print(f"✓ Resultados salvos em: {arquivo_resultados}")
    print("="*60)
    
    # Exibe resumo
    print("\nRESUMO DOS RESULTADOS:")
    print("-"*60)
    print(f"{'Tamanho (n)':<15} {'Tempo Médio (s)':<20} {'Desvio Padrão (s)':<20}")
    print("-"*60)
    for resultado in resultados:
        print(f"{resultado['n']:<15} {resultado['tempo_s']:<20.6f} {resultado['desvio']:<20.6f}")
    print("="*60)


if __name__ == "__main__":
    # Permite executar tamanhos específicos via linha de comando
    # Exemplo: python main.py 10000 20000 30000
    if len(sys.argv) > 1:
        tamanhos = [int(arg) for arg in sys.argv[1:]]
        print(f"Executando para tamanhos específicos: {tamanhos}")
        executar_todos_experimentos(tamanhos_especificos=tamanhos)
    else:
        print("AVISO: Selection Sort é O(n²). Tamanhos grandes demoram muito!")
        print("Exemplo de tempo estimado:")
        print("  n=10000:  ~17s")
        print("  n=20000:  ~68s")
        print("  n=50000:  ~425s (~7 min)")
        print("  n=100000: ~1700s (~28 min)")
        print("\nPara executar tamanhos específicos: python main.py 10000 20000")
        print("\nExecutando todos os tamanhos (isso pode levar horas)...")
        resposta = input("Continuar? (s/N): ")
        if resposta.lower() == 's':
            executar_todos_experimentos()
        else:
            print("Execução cancelada.")
