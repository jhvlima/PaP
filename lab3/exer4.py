def last(lista):
    if len(lista) == 0:
        return None
    return lista[-1:]

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(last(lista))