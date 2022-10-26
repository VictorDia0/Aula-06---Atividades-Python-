#Atividade 1: Escreva um programa que receba como entrada uma matriz 3x3 de elementos inteiros. Calcule e mostre o maior e o menor elemento. OBS.: não utilize funções.

def new_func():
    m = [[0,0,0],[0,0,0],[0,0,0]]
    maior = m[0][0]
    menor = m[0][0]
    for linha in range(0,3) :
        for coluna in range (0,3) :
            m[linha][coluna] = int(input('Digite o número desejado: '))
            if (m[linha][coluna] > maior):
                maior = m[linha][coluna]
            if (m[linha][coluna] < menor):
                menor = m[linha][coluna]
    print(f'O maior elemento é = {maior}')
    print(f'O menor elemento é = {menor}')

new_func()