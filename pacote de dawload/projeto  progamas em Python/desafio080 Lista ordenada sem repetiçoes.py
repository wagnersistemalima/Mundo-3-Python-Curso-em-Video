# desafio080 Lista ordenada sem repetiçoes
# Crie um progama onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista. Ja
# na posição correta de inserção ( sem usar o (sort). No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    numero = int(input(f'Digite o {c}º numero:'))
    if c == 0:                        # condiçoes para adicionar numero no final da lista
        lista.append(numero)
        print(f'Numero adcionado ao final da lista')
    elif numero > len(lista) - 1:     # condiçoes para adicionar numero no final da lista
        lista.append(numero)
        print(f'Numero adcionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):       # condição para adicionar numero no inicio ou meio
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao = posicao + 1
print('-'*30)
print(f'Os valores digitados em ordem foram {lista}')