# desafio081 Extraindo dados de uma lista
# Crie um progama que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
status = True
cont = 0
lista = []
while status:
    numeros = int(input(f'Digite o {cont}º número:'))
    opcao = ' '
    while opcao not in 'SN':     # se a opção estiver em 'S' continuar adicionando numeros a lista
        opcao = str(input('Quer continuar?[S/N]:').strip().upper()[0])
        if opcao in 'N':    # se opcao estiver em 'N' encerrar progama
            status = False
    lista.append(numeros)
    lista.sort(reverse=True)
    print(lista)
    cont = cont + 1
if 5 in lista: # Fora do laço. Se o numero 5 faz parte da lista?
    print('O valor 5 faz parte da lista')
else:          # Se não
    print('O valor 5 não foi encontrado na lista')

print(f'foram digitados {cont} numeros')   # Letra A
print(f'A lista ordenada de forma decrecente {lista}')