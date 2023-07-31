def insertion_sort(arr, size):
    for i in range(1, size):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j = j-1
            arr[j] = key


array = [12, 45, 567, 67, 4, 15, 87, 4, 22, 7, 2, 9, 3, 0, 6]
size_of_array = len(array)

print(f'Array before sorting is: {array}')
insertion_sort(array, size_of_array)
print(f'Array after sorting is: {array}')


