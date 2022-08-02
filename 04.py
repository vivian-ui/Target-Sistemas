estados = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}
total = 180759.98

for chave in estados:
    valor = estados[chave]
    percentage = (100*valor)/total
    print('A percentage de %s é %g' % (chave, percentage))

