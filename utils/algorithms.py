def quick_sort(arr, key_func, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (key_func(x) > key_func(pivot) if reverse else key_func(x) < key_func(pivot))]
    middle = [x for x in arr if key_func(x) == key_func(pivot)]
    right = [x for x in arr if (key_func(x) < key_func(pivot) if reverse else key_func(x) > key_func(pivot))]
    return quick_sort(left, key_func, reverse) + middle + quick_sort(right, key_func, reverse)

def filtrar_por_data_recursivo(registros, data_alvo, index=0):
    if index >= len(registros):
        return []
    match = [registros[index]] if registros[index].get("data") == data_alvo else []
    return match + filtrar_por_data_recursivo(registros, data_alvo, index + 1)