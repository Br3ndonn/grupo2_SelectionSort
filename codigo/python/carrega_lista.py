import csv

def carregar_lista_csv(caminho_arquivo):
    """Carrega uma lista de inteiros a partir de um arquivo CSV"""
    with open(caminho_arquivo, 'r') as f:
        reader = csv.reader(f)
        row = next(reader)
        return [int(x) for x in row if x.strip()]
    