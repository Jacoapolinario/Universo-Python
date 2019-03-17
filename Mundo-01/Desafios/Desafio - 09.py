numero = int(input('Digite um valor: '))

for valor in range(10):
   resultado = valor * numero
   print('{}X{} = {}'.format(numero, valor, resultado))