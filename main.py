def array_inversion(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr

arr = [1, 2, 3, 5]
print(array_inversion(arr))