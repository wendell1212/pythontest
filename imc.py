# calcular seu imc, e te informar, o quanto de peso precisa perder ou ganhar.

peso = float(input())
altura = float(input())

imc = peso / altura ** 2
imc_ideal = 24.9
imc_geral = imc_ideal * altura ** 2

imc_geral2 = peso - imc_geral

peso_ideal = imc_geral2 * (-1)
print('IMC atual = {:.2f}'.format(imc))
print('Peso a ser ganho/perdido = {:.2f}'.format(peso_ideal))
