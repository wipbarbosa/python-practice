# 10. Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um algoritmo que leia o
# código da moeda que o cliente quer comprar e qual o montante que ele quer adquirir nessa moeda.
# Mostre então quanto ele deverá pagar em reais para concretizar a operação. Além da cotação, a empresa
# cobra uma comissão de 5% (quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a R$1.000). Considere o câmbio do dia



print("===== CÂMBIO PARA REAIS =====")
print("\n== Selecione a opção desejada ==")
print("1 - Dólar (R$ 5.10)")
print("2 - Libra (R$ 6.88)")
print("3 - Euro  (R$ 5.90)")

tipo_moeda = int(input("\nDigite o código da moeda desejada: "))

multiplicador = 0

if tipo_moeda == 1:
    multiplicador = 5.10
    nome_moeda = "Dólares"
elif tipo_moeda == 2:
    multiplicador = 6.88
    nome_moeda = "Libras"
elif tipo_moeda == 3:
    multiplicador = 5.90
    nome_moeda = "Euros"
else:
    print("Opção inválida!")
    exit() 


montante = float(input(f"\nDigite o montante em {nome_moeda} que deseja adquirir: "))

valor_base_reais = montante * multiplicador

if valor_base_reais < 1000:
    taxa_comissao = 0.05
else:
    taxa_comissao = 0.03

valor_comissao = valor_base_reais * taxa_comissao
valor_total = valor_base_reais + valor_comissao

print("\n" + "="*30)
print(f"Montante desejado: {montante:.2f} em {nome_moeda}")
print(f"Valor convertido (bruto): R$ {valor_base_reais:.2f}")
print(f"Taxa de comissão ({taxa_comissao * 100:.0f}%): R$ {valor_comissao:.2f}")
print(f"VALOR TOTAL A PAGAR: R$ {valor_total:.2f}")
print("="*30)
