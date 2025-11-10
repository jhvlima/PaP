from exer7 import temElemento

def SplitToken(separador, lista):
    if not temElemento(lista, separador):
        return lista
    
if __name__ == "__main__":
    print(SplitToken(2, [1,2,3,4,2,5,67,8,9,0,3]))