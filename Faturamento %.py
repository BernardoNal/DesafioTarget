faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'SE' : 5041.75,
    'Outros': 19849.53
}

total = sum(faturamento_mensal.values())

percentuais = {}

faturamento_por_estado = [(estado, valor) for estado, valor in faturamento_mensal.items()]
faturamento_por_estado = sorted(faturamento_por_estado, key=lambda x: x[1], reverse=True)

for estado, valor in faturamento_por_estado:
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")
