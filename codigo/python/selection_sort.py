from lista import Lista

def selection_sort(lista: Lista) -> Lista:
    """
    Ordena uma Lista usando o algoritmo Selection Sort
    
    Args:
        lista: objeto Lista contendo inteiros
        
    Returns:
        Lista ordenada
    """
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista