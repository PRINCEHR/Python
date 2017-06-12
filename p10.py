n1 = input("Enter the no 1")
n2 = input("Enter the no 2")
n3 = input("Enter the no 3")

if (n1<n2 and n1<n3):
    l1 = n1
elif (n2<n1 and n2<n3):
    l1 = n2
elif (n3<n1 and n3<n2):
    l1 = n3

print ("Small   est Number", l1)