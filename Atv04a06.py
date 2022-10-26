#Atividade 4: Escreva um programa que receba como entrada uma matriz 3x3 de elementos inteiros. Calcule e mostre os elementos abaixo da diagonal principal da matriz. OBS.: não utilize funções.

m = [[0] * 3,[0] * 3,[0] * 3]

for i in range (0,3):
    for j in range (0,3):
        m[i][j] = int(input('Digite o número desejado: '))

for i in range (0,3):
    for j in range (0,3):
        if (i > j):
            print(m[i][j], end = ' ')