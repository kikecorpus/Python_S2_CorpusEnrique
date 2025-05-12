
miLista=[9,1,8,2,7,3,6,4,5]
print(miLista)
longitud= len(miLista)
cambios= True
i=0

while cambios and i < longitud-1:
    cambios= False
    
    for j in range(longitud-i-1):
        if miLista[j+1]<miLista[j]:
            temporal= miLista[j]
            miLista[j] = miLista[j+1]
            miLista[j+1]= temporal

            cambios= True
            print(miLista)
    i+=1
       