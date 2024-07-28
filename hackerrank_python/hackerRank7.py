if __name__ == '__main__':
    n = int(input().strip())  # tamanho da lista

    numero = []

    contador = 0
    while contador < n:
        arr = list(map(int, input().rstrip().split()))
        numero.append(arr)
        contador += 1

    numero.reverse()
    print(numero)

