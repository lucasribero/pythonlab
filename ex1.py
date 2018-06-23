#!/usr/bin/python3

nome = input("Digite Seu nome: ")
nota1 = int(input("Digite sua nota1: "))
nota2 = int(input("Digite sua nota2: "))

soma = nota1 + nota2
media = soma / 2

if media >= 7:
    result = ('Aprovado')
    print('Aluno' , result , nome.title() , 'Parabens sua media foi:' , media)
else:
    result = ('Reprovado')
    print ('Aluno' , result , nome.title(), 'Estude Mais sua media foi:' , media)
