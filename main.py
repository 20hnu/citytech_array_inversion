def array_inversion_count(arr):
    n = len(arr)
    count = 0
    for i in range(n - 1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count = count + 1
    return count

arr = [4,3,2]
print(array_inversion_count(arr))