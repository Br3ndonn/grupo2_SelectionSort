from lista import Lista
from carrega_lista import carregar_lista_csv
from pathlib import Path
from selection_sort import selection_sort
from time import perf_counter

if __name__ == "__main__":
    # Exemplo usando a nova classe Lista
    """print("=== Usando a classe Lista ===")
    minha_lista = Lista([64, 25, 12, 22, 11, 40, 11])
    print("Lista original:", minha_lista)
    
    lista_ordenada = selection_sort(minha_lista)
    print("Lista ordenada:", lista_ordenada)"""

    base_dados = Path(__file__).resolve().parents[2] / "dados" / "n010000" / "run_001.csv"

    # Tempo de leitura do CSV
    t0 = perf_counter()
    lista_csv = carregar_lista_csv(base_dados)
    t1 = perf_counter()
    tempo_leitura = t1 - t0
    print(f"Tamanho lido do CSV: {len(lista_csv)}")
    print(f"Tempo de leitura: {tempo_leitura*1000:.3f} ms ({tempo_leitura:.6f} s)")

    # Tempo de ordenação (Selection Sort)
    t2 = perf_counter()
    lista_ordenada_csv = selection_sort(lista_csv)  # ordena in-place
    t3 = perf_counter()
    tempo_sort = t3 - t2
    print(f"Tempo de ordenação: {tempo_sort*1000:.3f} ms ({tempo_sort:.6f} s)")

    # Resumo
    print("Primeiros 10 elementos ordenados do CSV:", lista_ordenada_csv.obter_elementos()[:10])
    print("Últimos 10 elementos ordenados do CSV:", lista_ordenada_csv.obter_elementos()[-10:])
