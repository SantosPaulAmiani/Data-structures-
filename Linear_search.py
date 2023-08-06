def linear_search(a, n, key):
   count = 0
   for i in range(n):
      if(a[i] == key):
         print("The element is found at position", (i+1))
         count = count + 1
   if(count == 0):
      print("Unsuccessful Search")

a = [14, 56, 77, 32, 84, 9, 32, 10]
n = len(a)
key = 32
linear_search(a, n, key)
key = 32
linear_search(a, n, key)
