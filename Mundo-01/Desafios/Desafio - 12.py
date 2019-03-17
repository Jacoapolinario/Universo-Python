preco = float(input('Digite o preço R$: '))
desconto = preco * 5 / 100
resultado = preco - desconto
print('O produto que custava {}, na promoção com 5% de desconto, vai custar {:.2f}'.format(preco, resultado))