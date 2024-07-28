#suposto loop para calcular a quantidade de caracteres de uma frase/palavra#
total = 0
palavra = "python rocks!"
acabou = False

#while (not acabou):
#for letra in palavra :
    # esse código definirá True para a variável acabou apenas quando total for igual ao tamanho da palavra.
    #acabou = (total == len(palavra)-1)
    # comparações retornam verdadeiro ou false.

inteiros = [1,3,4,5,7,8,9]
#List Comprehension
pares = [x for x in inteiros if x % 2 == 0]
#print(pares)


arquivo = open("palavras.txt", "r")
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)
    print(linha)

arquivo.close()




#print(acabou)