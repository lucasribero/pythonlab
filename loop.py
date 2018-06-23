#!/usr/bin/python3

numeros = list(range(1,11))
nomes = ['daniel', 'joao', 'maria', 'ana']

#for variavel in nomes:
#    print(variavel.title())
#print (numeros)

num = int(input('Digite um numero: '))
for numero in range(0, num, 2):
    print(numero)
