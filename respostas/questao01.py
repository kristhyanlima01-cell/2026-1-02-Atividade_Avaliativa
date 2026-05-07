#Escreva um programa Python que exiba na tela uma sequência de 10 números inteiros aleatórios entre 1 e 100.
from random import randint


repeticoes = int(input("Digite um número inteiro positivo: "))

for i in range(repeticoes):
    numero = randint(1, 100)
    print(numero)
