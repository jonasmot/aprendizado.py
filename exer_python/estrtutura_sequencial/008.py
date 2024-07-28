#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input("Quanto você ganha por hora?"))
horas_trabalhadas = int(input("Quantas horas você trabalha na semana?"))

horas_mensais = horas_trabalhadas * 4



salario_mes = ganho_por_hora * horas_mensais

print(f'Você receberá {salario_mes} por mês!')
