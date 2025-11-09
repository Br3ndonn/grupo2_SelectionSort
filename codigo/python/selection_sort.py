def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        if i != min_index:
            temp = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = temp
    return lista