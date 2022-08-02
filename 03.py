import xml.etree.ElementTree as et

arquivo = et.parse('dados.xml')
raiz = arquivo.getroot()

for filhas in raiz.findall('row'):
    d = filhas.find('dia').text
    v = filhas.find('valor').text
    vanterior = 0
    if v > vanterior:
        print("Maior valor")
        print(f'Dia: {d} | Valor: {v}')
    elif v == vanterior:
        print("valores iguais")
        print(f'Dia: {d} | Valor: {v}')
    else:
        print("Menor valor")
        print(f'Dia: {d} | Valor: {v}')
    vanterior = v
arquivo.write('novo_dados.xml')
