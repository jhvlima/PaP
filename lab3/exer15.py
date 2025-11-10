from exer1 import head
from exer2 import tail
from exer7 import temElemento
from exer13 import tamanhoLista


def strip(lista1, lista2):
    print(lista1, lista2)
    if lista1 == []:
        return lista2
   
    if not temElemento(lista2, head(lista1)):
        return strip(tail(lista1), lista2)
    
    return [x for x in range(1, tamanhoLista(lista1)) if head(lista1) != lista2[x]]

if __name__ == "__main__":
    lista1 = [2, 3, 4]
    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(strip(lista1, lista2))