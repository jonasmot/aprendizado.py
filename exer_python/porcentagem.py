#Criar um programa que pede um valor e uma porcentagem desse valor, e mostre o resultados de quanto representa essa porcentagem
responde = 0

while responde < 5:
    valor = float(input("Digite sua quantia em R$: ").strip())

    porcento = float(input("Qual a porcentagem desse valor?").strip())

    resultado = valor * (porcento/100)

    print(f'{int(porcento)}% de {valor}, é R${resultado}')

    moedas = {'USD' : 'Dólar', 'EUR' : 'Euro', 'GBP' : 'Libra'}

    print("Responda com ! sim ou não !")
    escolha = input("Você deseja a conversão da moeda?").upper().strip()

    if (escolha != "sim" and escolha != "não"):
        print("Responda com ! sim ou não !")


    if(escolha == ''.strip()):
        print("!!!!!!!")
        print("programa encerrado")
        print("!!!!!!!")
        break

    if(escolha == "sim".upper().strip()):
        print("******************")
        print("C O N V E R S Ã O")
        print("******************")

        print(">", moedas['USD'], moedas['EUR'], moedas['GBP'], " ")
        moeda = input("Qual moeda deseja?").upper().strip()
        if(moeda in moedas):

            if(moeda == moedas['USD']):
                dolar_americano = (valor * 0.184711)
                conversao = dolar_americano * (porcento/100)
                print(f'R${valor} em dólar, fica: US${dolar_americano}')
                print(f'A porcentagem em Dólar fica : US${conversao}')

            if(moeda == moedas['GBP']):
                libras_esterlinas = (valor * 0.14624)
                conversao = libras_esterlinas * (porcento/100)
                print(f'R${valor} em Libras esterlinas, é: £{libras_esterlinas}')
                print(f'A porcentagem em Libras esterlinas fica: £{conversao}')

            if(moeda == moedas['EUR']):
                euro_europeu = (valor * 0.18)
                conversao = euro_europeu * (porcento/100)
                print(f'R${valor} em euro, converte: €{euro_europeu}')
                print(f'A porcentagem em Euro fica: €{conversao}')

        if(moeda not in moedas):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Digite uma moeda válida!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    if (escolha == "não"):
        print("Falou!!")
        break
    responde += 1
