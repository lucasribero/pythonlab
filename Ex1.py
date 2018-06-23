#!/usr/bin/python3

nome = input("Digite Seu nome: ")
nota1 = int(input("Digite sua nota1: "))
nota2 = int(input("Digite sua nota2: "))

soma = nota1 + nota2
media = soma / 2

print ("O Aluno {0} tem a media{1}".format(nome.title(), media))