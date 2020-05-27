# calcúlo de potência em kWh de aparelhos.
# para trasnformar kWh em Joules só mudar para 3,6 * 10^6

potencia = int(input())
minutos_ligado = int(input())

tempo = minutos_ligado * 60
gasto = potencia * tempo
kwh = gasto * 2.778 * 10 ** - 7
print(f'{kwh:.1f} kWh')
