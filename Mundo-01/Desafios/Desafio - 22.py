nome_completo = str(input('Nome Completo: ')).strip()
maiuscula = nome_completo.upper()
print(maiuscula)

minuscula = nome_completo.lower()
print(minuscula)


quantidade_caracteres = len(nome_completo) - nome_completo.count(' ')
print(quantidade_caracteres)

separador = nome_completo.split()
primeiro_nome = separador[0]
quantidade_primeiro_nome = len(primeiro_nome)
print(quantidade_primeiro_nome)
