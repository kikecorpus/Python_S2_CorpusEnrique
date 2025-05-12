
miLista=[9,1,8,2,7,3,6,4,5]
print(miLista)
longitud= len(miLista)

for i in range (longitud-1):
    for j in range(longitud-1):
        if miLista[j+1]<miLista[j]:
            temporal= miLista[j]
            miLista[j] = miLista[j+1]
            miLista[j+1]= temporal
    
    print(miLista)