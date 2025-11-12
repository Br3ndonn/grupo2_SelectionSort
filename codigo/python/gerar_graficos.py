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
    plt.plot(df["n"], df["tempo_ms"], marker='o', linestyle='-', color='steelblue')
    # plt.xscale("log")
    # plt.yscale("log")
    plt.title(titulo)
    plt.xlabel("Tamanho do vetor (n)")
    plt.ylabel("Tempo médio (ms)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(arquivo_saida, dpi=300)
    plt.close()
    print(f"✅ Gráfico salvo em {arquivo_saida}")

def gerar_comparativo(dados):
    """Gera um gráfico comparativo entre as três linguagens."""
    plt.figure(figsize=(8, 5))
    for nome, df in dados.items():
        plt.plot(df["n"], df["tempo_ms"], marker='o', linestyle='-', label=nome)
    # plt.xscale("quadratic")
    # plt.yscale("quadratic")
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

if __name__ == "__main__":
    main()
    