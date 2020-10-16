def bubbleSort(numsList):
    n = len(a)
    for x in range(n-1):
        for y in range(x+1, n):
            if(a[x] > a[y]):
                a[x], a[y] = a[y], a[x]
                
    return a
    
a = [500, 99, 10, 4, 100, 7, 9, -10, 11, 1, 200, 4]
a = bubbleSort(a)            
print("ASC- ", a)
# for x in range(n-1):
#     for y in range(x+1, n):
#         if(a[x] < a[y]):
#             a[x], a[y] = a[y], a[x]
            
# print("DESC- ", a)    