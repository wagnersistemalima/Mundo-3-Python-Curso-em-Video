# desfio074 Maior e menor valores em tupla
# Crie um progama que vai gerar cinco números aleatorios e colocar em uma tupla. depois disso
# mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) # Colocando () vira tupla
print(tupla)
print(f'O maior valor gerado dentro da tupla foi {max(tupla)}')
print(f'O menor valor gerado dentro da tupla foi {min(tupla)}')