#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input('Qual a medida da base do quadrado?'))
altura = float(input('Qual a medida da altura do quadrado?'))

area_quadrado = base * altura
dobro_area_quadrado = area_quadrado * 2

print(f'O dobro da área deste quadrado : {dobro_area_quadrado}')