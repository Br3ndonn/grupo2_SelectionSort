from pathlib import Path
import csv
from lista import Lista

def carregar_lista_csv(caminho_arquivo) -> Lista:
    caminho = Path(caminho_arquivo)
    with caminho.open('r', newline='') as f:
        reader = csv.reader(f)
        row = next(reader, [])
    elementos = [int(x) for x in row if x.strip() != ""]
    return Lista(elementos)