'''list1 = [(c*9/5+32) for c in range(50, 101) ]
print list'''

dx = [ f for f in [((x*9/5.0)+32) for x in range(0, 101)] if f>150]
print (dx)


