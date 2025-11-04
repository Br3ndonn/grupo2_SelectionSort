from lista import Lista

def selection_sort(lista: Lista) -> Lista:
    """
    Ordena uma Lista usando o algoritmo Selection Sort
    
    Args:
        lista: objeto Lista contendo inteiros
        
    Returns:
        Lista ordenada
    """
    for i in range(lista.tamanho()):
        min_index = i
        for j in range(i + 1, lista.tamanho()):
            if lista[j] < lista[min_index]:
                min_index = j
        if(i != min_index):
            temp = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = temp
    return lista