# desafio076 Lista de preço com tupla
# Crie um progama que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.
# No final mostre uma listagem de preço, organizando os dados em forma tabular.
tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20
         , 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
for posicao in range(0, len(tupla)): # Equanto a posição estiver em 0 ate comprimento da tupla, mostre posicao
    if posicao % 2 == 0: # Se a posição for par, vai mostrar o nome do produto
        print(f'{tupla[posicao]:.<40}', end='') # O conteudo da tupla na posição
    elif posicao % 2 == 1:
        print(f'R$ {tupla[posicao]:>7.2f}')
print('-'*50)
