def bubble_sort(arr, size):
    for i in range(size):
        swaps = 0
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swaps = 1

        if swaps == 0:
            break


array = [12, 14, 87, 57, 97, 1.1, 44, 0]
array_size = len(array)

print(f"Array before sorting is:  {array}")
bubble_sort(array, array_size)
print(f'Array after sorting is: {array}')


