import json

with open('faturamento.json') as f:
    dados = json.load(f)

faturamento_diario = dados['faturamento_diario']

num_dias_zero = 0

for faturamento in faturamento_diario:
    if faturamento == 0:
        num_dias_zero += 1

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

media = sum(faturamento_diario) / (len(faturamento_diario) - num_dias_zero)


dias_acima_da_media = sum(1 for f in faturamento_diario if f > media)

print("Menor valor de faturamento diário: R$ {:.2f}".format(menor_valor))
print("Maior valor de faturamento diário: R$ {:.2f}".format(maior_valor))
print("Número de dias com faturamento diário acima da média mensal de {:.2f}: ".format(media)+ "{} dias".format(dias_acima_da_media))
