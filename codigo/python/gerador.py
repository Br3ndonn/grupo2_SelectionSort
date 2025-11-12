import os
import random
import csv
from pathlib import Path

def gerar_dados():
    base_dir = Path(__file__).resolve().parents[2] / "dados"
    base_dir.mkdir(parents=True, exist_ok=True)
    print(f"Saída base: {base_dir}")

    tamanhos = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    num_execucoes = 50
    seed_base = 1000
    
    print("Iniciando geração de dados...")
    
    for tamanho in tamanhos:
        dir_tamanho = base_dir / f"n{tamanho:06d}"
        dir_tamanho.mkdir(parents=True, exist_ok=True)
        
        print(f"\nGerando dados para n={tamanho}...")
        
        for execucao in range(1, num_execucoes + 1):
            seed = seed_base + (tamanho // 10000 - 1) * num_execucoes + execucao
            random.seed(seed)
            
            vetor = [random.randint(1, 1000000) for _ in range(tamanho)]
            
            nome_arquivo = f"run_{execucao:03d}.csv"
            caminho_arquivo = dir_tamanho / nome_arquivo
            
            with open(caminho_arquivo, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(vetor)
            
            if execucao % 10 == 0:
                print(f"  Progresso: {execucao}/{num_execucoes} execuções")
        
        print(f"✓ Concluído: {num_execucoes} arquivos gerados em {dir_tamanho}")
    
    print("\n" + "="*50)
    print("✓ GERAÇÃO COMPLETA!")
    print(f"Total de arquivos gerados: {len(tamanhos) * num_execucoes}")
    print("="*50)


if __name__ == "__main__":
    gerar_dados()