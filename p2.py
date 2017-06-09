list = [1,2,3,4,5,6,7,8,9,10]
liste =[]
listo =[]


for x in list:
    if x%2==0:
        liste=[x]+liste
    else:
        listo= [x]+listo

print (liste)
print (listo)
