frase = str(input('Digite uma frase: ')).upper().strip()
aparece = frase.count('A')
print(aparece)
primeira_posicao = frase.find('A')+1
print(primeira_posicao)
ultima_posicao = frase.rfind('A')+1
print(ultima_posicao)




