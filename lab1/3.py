numeros = list()

for i in range(5): 
    n = input()
    numeros.append(n)
    
for i in range(5):
    for j in range(i, 5):
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux
        
print(numeros)