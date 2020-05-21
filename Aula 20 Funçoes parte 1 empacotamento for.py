def soma(* valores):                         # receber varios valores
    s = 0
    for num in valores:                      # para cada numero em valores
        s = s + num
    print(f'Somando os valores {valores} temos {s}')      # desempacotando


#progama principal
soma(5, 2)
soma(2, 9, 4)