from exer1 import head
from exer2 import tail
from exer7 import temElemento

def catListaUnicas(lista1, lista2):
    # se acabou a segunda lista, finaliza a recursao
    if lista2 == []:
        return lista1
    # se o elemento ja existe na lista1, entao vai para o proximo passo sem a inclusao o elemento
    if temElemento(lista1, head(lista2)):
        return catListaUnicas(lista1, tail(lista2))
    # se ele nao existe entao insere na lista
    return catListaUnicas(lista1 + [head(lista2)], tail(lista2))

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6]
    print(catListaUnicas(lista1, lista2))