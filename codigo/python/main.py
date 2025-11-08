from pathlib import Path
from time import perf_counter
import csv
import statistics
import sys
from carrega_lista import carregar_lista_csv
from selection_sort import selection_sort

def executar_experimento(caminho_csv):
    lista = carregar_lista_csv(caminho_csv)
    t_inicio = perf_counter()
    selection_sort(lista)
    t_fim = perf_counter()
    return (t_fim - t_inicio) * 1000  # Retorna em milissegundos

if __name__ == "__main__":
    tamanhos = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    num_execucoes = 50
    
    if len(sys.argv) > 1:
        tamanhos = [int(arg) for arg in sys.argv[1:]]
    
    print("EXPERIMENTOS - SELECTION SORT (PYTHON)")
    
    base_dir = Path(__file__).resolve().parents[2]
    dados_dir = base_dir / "dados"
    resultados_dir = base_dir / "resultados" / "estatisticas"
    resultados_dir.mkdir(parents=True, exist_ok=True)
    
    with open(resultados_dir / "resultados_Python.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'tempo_ms', 'desvio'])
        
        for n in tamanhos:
            print(f"\nProcessando n={n}...")
            tempos = []
            
            for exec in range(1, num_execucoes + 1):
                caminho = dados_dir / f"n{n:06d}" / f"run_{exec:03d}.csv"
                tempo = executar_experimento(caminho)
                tempos.append(tempo)
                
                if exec % 10 == 0:
                    print(f"  {exec}/{num_execucoes}")
            
            media = statistics.mean(tempos)
            desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0
            writer.writerow([n, f"{media:.6f}", f"{desvio:.6f}"])
            print(f"  Media: {media:.3f} ms, Desvio: {desvio:.3f} ms")
    
    print("\nResultados em: resultados/estatisticas/resultados_Python.csv")
