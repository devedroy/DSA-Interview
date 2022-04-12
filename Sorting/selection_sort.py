

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

A = [64, 25, 12, 22, 11]

print(selection_sort(A))