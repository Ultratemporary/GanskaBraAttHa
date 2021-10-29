def adderaIntLista(lista : list[int]) -> int:
    sum = 0
    for tal in lista:
        sum = sum + tal
    return sum

if __name__ == "__main__":
    print("Testing")
    lista = [2,3,4]
    print(adderaIntLista(lista))