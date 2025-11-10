from exer2 import tail

def tamanhoLista(lista):
    if lista == []:
        return 0
    return tamanhoLista(tail(lista)) + 1

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(tamanhoLista(lista))