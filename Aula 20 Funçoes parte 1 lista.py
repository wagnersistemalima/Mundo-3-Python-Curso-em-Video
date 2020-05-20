def dobra(lista):              # neste momento temos duas listas na memoria / lista e valores
    cont = 0                            # tudo que fizer em lista, interfere em valores diretamente
    while cont < len(lista):             # enquanto o cont for menor que o tamanho da lista
        lista[cont] = lista[cont] * 2
        cont = cont + 1



                                        # função para dobrar os numeros de valores


#progama principal
valores = [6, 3, 9, 1, 0, 2]          # vai dobrar cada numero da lista valores
dobra(valores)
print(valores)