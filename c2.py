list1 = [x for x in range(1, 30)]
for x in list1:
  if (x%2==0):
     print( x)



list2 = [x*2 for x in range(1, 14)]
print(list2)


list2 = [x*2 for x in range(0, 31, 2)]
print(list2)

list2 = [x*2 for x in range(1, 31) if x%2==0]
print(list2)