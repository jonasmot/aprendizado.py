import adivinhacao
import forca

def escolher_jogo():
    print("********************")
    print("***Decida o Jogo***!")
    print("********************")

    print("(1)Adivinhação (2)Forca")

    escolha = int(input("Sua Escolha: "))

    if(escolha == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogar_adivinhacao()
    elif(escolha == 2):
        print("Jogando Forca")
        forca.jogar_forca()

if(__name__ == "__main__"):
    escolher_jogo()