a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list2= []
for x in a:
    for y in b:
        if x == y:
            list2 = [x]+list2


print (list2)