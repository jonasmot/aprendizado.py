import random

def jogar_adivinhacao():
    print("********************")
    print("Jogo de Adivinhação!")
    print("********************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 100

    print("Qual o nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Escolha seu nível: "))
    if(nivel == 1):
        tentativas = 25
    elif (nivel == 2):
        tentativas = 15
    else:
        tentativas = 5;

    #while(rodadas <= tentativas):
    for rodadas in range(1, tentativas + 1):
       # print("Tentativa", rodadas, "de", tentativas) #
                    #string interpolation#
        print("Tentativa {} de {}".format(rodadas, tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou, seu chute foi maior que o número secreto.")
                if(rodadas == tentativas):
                    print("O número secreto era {} e perdeu {} pontos".format(numero_secreto, pontos_perdidos))
            elif (menor):
                print("Você errou, seu chute foi menor que o número secreto.")
                if(rodadas == tentativas):
                    print("O número secreto era {}, você perdeu {} pontos".format(numero_secreto, pontos_perdidos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("FIM")

if(__name__ == "__main__"):
    jogar_adivinhacao()
