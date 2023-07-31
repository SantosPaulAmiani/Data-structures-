def selection_sort(arr, size):
    for i in range(size):
        min = i

        for j in range(i+1, size):
            if arr[j] < arr[min]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp


array = [12, 5, 6, 3, 34, 432 ]
size_of_array = len(array)
print(f'Array before sorting is: {array}')
selection_sort(array, size_of_array)
print(f'Size of array after sorting is: {array}')
