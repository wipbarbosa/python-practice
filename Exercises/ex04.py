#4. Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores:
#(1) a vista com 5% de desconto; 
#(2) o valor da parcela em 2x; 
#(3) o valor da parcela em 3x com acréscimo de 5% no valor total.

print("===== CÁLCULO DE ACORDO COM O TIPO DE PAGAMENTO =====")

valor_produto = float(input("Digite o valor do produto: \n"))

print(
"(1) a vista com 5 porcento de desconto\n"
"(2) o valor da parcela em 2x\n"
"(3) o valor da parcela em 3x com acréscimo de 5% no valor total.\n"
)


avista = valor_produto - (valor_produto * 0.05)
parcelado = valor_produto / 2
produto_com_juros = (valor_produto * 0.05) + valor_produto
parcela_com_juros = produto_com_juros / 3

tipo_de_pagamento = int(input("Digite o numero do tipo de pagamento: "))

if tipo_de_pagamento == 1:
    print(f"O valor a vista com desconto será de R$ {avista:.2f}")

elif tipo_de_pagamento == 2:
    print(
    f"O pagamento será em 2 parcelas de R$ {parcelado:.2f}\n"
    f"Valor total: R$ {valor_produto:.2f}"
)
elif tipo_de_pagamento == 3:
    print(f"O pagamento será em 3 parcelas de R${parcela_com_juros}\n"
          f"Valor toral: R$ {produto_com_juros}"
          )
else:
    print("Opção inválida tente novamente")