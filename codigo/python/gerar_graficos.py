import os
import pandas as pd
import matplotlib.pyplot as plt

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ESTAT_DIR = os.path.join(BASE_DIR, "../../resultados/estatisticas")
GRAF_DIR = os.path.join(BASE_DIR, "../../resultados/graficos")

# Garante que a pasta de saída exista
os.makedirs(GRAF_DIR, exist_ok=True)

def carregar_dados(caminho_csv):
    """Lê um CSV de resultados e retorna um DataFrame ordenado por n."""
    if not os.path.exists(caminho_csv):
        print(f"[AVISO] Arquivo não encontrado: {caminho_csv}")
        return None
    df = pd.read_csv(caminho_csv)
    df = df.sort_values("n")
    return df

def gerar_grafico(df, titulo, arquivo_saida):
    """Gera gráfico log-log de desempenho para uma linguagem."""
    plt.figure(figsize=(8, 5))
    
    # Plota os dados reais
    plt.plot(df["n"], df["tempo_ms"], marker='o', linestyle='-', color='steelblue', label='Tempo real', linewidth=2)
    
    # Adiciona sombra do desvio padrão
    plt.fill_between(df["n"], 
                     df["tempo_ms"] - df["desvio"], 
                     df["tempo_ms"] + df["desvio"],
                     alpha=0.2, color='steelblue', label='± Desvio padrão')
    
    # Adiciona linha de referência O(n²)
    n_ref = df["n"].values
    # Ajusta a constante para que a curva O(n²) fique visível no gráfico
    # Usa o primeiro ponto para calibrar
    c = df["tempo_ms"].iloc[0] / (n_ref[0] ** 2)
    tempo_teorico = c * (n_ref ** 2)
    plt.plot(n_ref, tempo_teorico, linestyle='--', color='red', alpha=0.7, linewidth=2, label='O(n²) teórico')
    
    plt.xscale("log")
    plt.yscale("log")
    plt.title(titulo)
    plt.xlabel("Tamanho do vetor (n)")
    plt.ylabel("Tempo médio (ms)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(arquivo_saida, dpi=300)
    plt.close()
    print(f"✅ Gráfico salvo em {arquivo_saida}")

def gerar_comparativo(dados):
    """Gera um gráfico comparativo entre as três linguagens."""
    plt.figure(figsize=(10, 6))
    
    # Define cores para cada linguagem
    cores = {'C': 'blue', 'Java': 'orange', 'Python': 'green'}
    
    # Plota dados de cada linguagem com sombra de desvio
    for nome, df in dados.items():
        cor = cores.get(nome, 'gray')
        plt.plot(df["n"], df["tempo_ms"], marker='o', linestyle='-', color=cor, label=nome, linewidth=2)
        
        # Adiciona sombra do desvio padrão
        plt.fill_between(df["n"], 
                         df["tempo_ms"] - df["desvio"], 
                         df["tempo_ms"] + df["desvio"],
                         alpha=0.15, color=cor)
    
    # Adiciona linha de referência O(n²)
    # Usa o primeiro dataset para calibrar a constante
    primeiro_df = list(dados.values())[0]
    n_ref = primeiro_df["n"].values
    c = primeiro_df["tempo_ms"].iloc[0] / (n_ref[0] ** 2)
    tempo_teorico = c * (n_ref ** 2)
    plt.plot(n_ref, tempo_teorico, linestyle='--', color='black', alpha=0.5, linewidth=2, label='O(n²) referência')
    
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Comparativo de Desempenho - Selection Sort")
    plt.xlabel("Tamanho do vetor (n)")
    plt.ylabel("Tempo médio (ms)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    saida = os.path.join(GRAF_DIR, "comparativo_linguagens.png")
    plt.savefig(saida, dpi=300)
    plt.close()
    print(f"✅ Gráfico comparativo salvo em {saida}")

def gerar_razao_crescimento(dados):
    """Gera gráfico comparando razão de crescimento empírica vs teórica O(n²)."""
    plt.figure(figsize=(10, 6))
    
    # Define cores para cada linguagem
    cores = {'C': 'blue', 'Java': 'orange', 'Python': 'green'}
    
    # Para cada linguagem, calcula a razão de crescimento
    for nome, df in dados.items():
        if len(df) < 2:
            continue
            
        cor = cores.get(nome, 'gray')
        n_values = df["n"].values
        tempo_values = df["tempo_ms"].values
        
        # Calcula razão de crescimento empírica: T(n) / T(n0)
        # Normaliza pelo primeiro valor
        n0 = n_values[0]
        t0 = tempo_values[0]
        razao_empirica = tempo_values / t0
        
        # Plota razão empírica
        plt.plot(n_values, razao_empirica, marker='o', linestyle='-', 
                color=cor, label=f'{nome} (empírico)', linewidth=2)
    
    # Calcula e plota razão teórica O(n²): (n/n0)²
    primeiro_df = list(dados.values())[0]
    n_values = primeiro_df["n"].values
    n0 = n_values[0]
    razao_teorica = (n_values / n0) ** 2
    
    plt.plot(n_values, razao_teorica, linestyle='--', color='black', 
            alpha=0.7, linewidth=3, label='O(n²) teórico')
    
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Validação Empírica da Complexidade O(n²)\nRazão de Crescimento: T(n)/T(n₀)")
    plt.xlabel("Tamanho do vetor (n)")
    plt.ylabel("Razão de crescimento (normalizado)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    saida = os.path.join(GRAF_DIR, "razao_crescimento_empirico_vs_teorico.png")
    plt.savefig(saida, dpi=300)
    plt.close()
    print(f"✅ Gráfico de razão de crescimento salvo em {saida}")

def main():
    arquivos = {
        "C": os.path.join(ESTAT_DIR, "resultados_C.csv"),
        "Java": os.path.join(ESTAT_DIR, "resultados_Java.csv"),
        "Python": os.path.join(ESTAT_DIR, "resultados_Python.csv"),
    }

    dados = {}

    for nome, caminho in arquivos.items():
        df = carregar_dados(caminho)
        if df is not None:
            dados[nome] = df
            gerar_grafico(
                df,
                f"Desempenho do Selection Sort em {nome}",
                os.path.join(GRAF_DIR, f"desempenho_{nome}.png"),
            )

    if len(dados) >= 2:
        gerar_comparativo(dados)
    
    if len(dados) >= 1:
        gerar_razao_crescimento(dados)

if __name__ == "__main__":
    main()
    