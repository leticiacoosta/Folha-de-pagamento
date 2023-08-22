SALARIO= float(input('Digite o salário:'))
VALE= (SALARIO*0.06)
VALE=input('Descontar o Vale-Transporte?')
if VALE==('NAO'):
    VALE= SALARIO*0.06
    print('Não haverá desconto do Vale-Transporte')
elif VALE==('SIM'):
    VALE= SALARIO*0.06
    print('O desconto do Vale-Transporte foi de:',VALE)
    
if SALARIO <1302.00:
   INSS= SALARIO*0.075
   INSS-SALARIO*0.075
   print(f'Foi descontado R${INSS}do INSS')
   print('Seu salário com os descontos ficará R$:',(SALARIO-INSS-VALE))
elif SALARIO <2571.29:
    INSS= SALARIO*0.09
    INSS-SALARIO*0.09
    print(f'Foi descontado R${INSS}do INSS')
    print('Seu salário com os descontos ficará R$:',(SALARIO-INSS-VALE))
elif SALARIO <3856.94:
    INSS= SALARIO*0.12
    INSS-SALARIO*0.12
    print(f'Foi descontado R${INSS}do INSS')
    print('Seu salário com os descontos ficará R$:',(SALARIO-INSS-VALE))