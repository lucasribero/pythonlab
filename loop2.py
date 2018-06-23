#!/usr/bin/python3

#numero = 0
#while numero < 10:
#    print(numero)
#    numero += 1


nomes = []
while True:
    nome = input('Digite um nome ou sair: ')

    if nome.lower().strip() == 'sair':
        break
    nomes.append(nome)
print(nomes)



