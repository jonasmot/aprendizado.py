if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        s = str(input())
        n = len(s)

        numero_par = []
        numero_impar = []

        index = 0
        while index < n:
            indice = s[index]

            if (index % 2 == 0):
                numero_par.append(indice)
            if (index % 2 == 1):
                numero_impar.append(indice)
            index += 1

        pares = "".join(numero_par)
        impares = "".join(numero_impar)
        print(pares, impares)

