#Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)


print(f'===== TABELA DE MULTIPLICAÇÃO =====')
for fator_multiplicando in range (1,11):
    print('=' * 25)
    print(f'Tabuada do:  {fator_multiplicando}')
    for fator_multiplicador in range(1,11):

        produto = fator_multiplicando * fator_multiplicador 

        print (f'{fator_multiplicando} x {fator_multiplicador} = {produto}')