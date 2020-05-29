milhas = float(input())
aliquota = float(input())

passagem = milhas * aliquota + 51.00
com_25_porcen = (passagem / 100) * 25
avista = passagem - com_25_porcen
com_5_porcen = (passagem / 100) * 5
parcelado_desconto = passagem - com_5_porcen
parcelas_6vezes = parcelado_desconto / 6
parcelas_10vezes = passagem / 10
print(f'Valor da passagem: R$ {passagem:.2f}\n')

print('Pagamento:')
print(f'1. À vista. R$ {avista:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {parcelado_desconto:.2f}')
print(f'   6 x R$ {parcelas_6vezes:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {passagem:.2f}')
print(f'   10 x R$ {parcelas_10vezes:.2f}')
~                                                  
