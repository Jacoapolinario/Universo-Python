km = float(input('Km pecorridos: '))
dias = float(input('Quantidade de dias: '))
km_pecorridos = km * 0.15
dias_alugados = dias * 60
resultado = km_pecorridos + dias_alugados
print('O total a pagar é R${:.2f}'.format(resultado))