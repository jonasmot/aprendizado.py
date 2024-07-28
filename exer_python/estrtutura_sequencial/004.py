#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeiro_bimestre_um = float(input("nota primeiro mês? : "))
primeiro_bimestre_dois = float(input("nota segundo mês? :"))

segundo_bimestre_um = float(input("nota primeiro mês? : "))
segundo_bimestre_dois = float(input("nota segundo mês? : "))

medias_bimestrais = int(primeiro_bimestre_um + primeiro_bimestre_dois + segundo_bimestre_um + segundo_bimestre_dois)/ 4

print(medias_bimestrais)