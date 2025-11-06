# slice em python: lista[inicio:fim:passo]
# ex: lista[1:5:2] -> do indice 1 ao 4, pulando de 2 em 2

def tail(lista):
    if len(lista) == 0:
        return None
    return lista[1:]

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(tail(lista))