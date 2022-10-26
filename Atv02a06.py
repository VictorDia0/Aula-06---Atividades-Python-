#Atividade 2: Escreva um programa que receba como entrada uma matriz 3x3 de elementos inteiros. Calcule e mostre a soma e média dos elementos pares. OBS.: não utilize funções.

matriz = [[0] * 3,[0] * 3, [0] * 3] #Matriz.
s = 0 # Variavel para somar os numeros inseridos.
c = 0 # Variavel para contar a quantidade de numeros inseridos.
for linha in range (0,3):
    for coluna in range (0,3):
        # Logo abaixo entramos com a mesma variavel para efetuar a inserção de dados no codigo.
        matriz[linha][coluna]= int(input('Digite um valor: '))
        if (matriz[linha][coluna] % 2 == 0):
            c +=  1
            s += matriz[linha][coluna]
media = s / c # Variavel para efetuar o calculo da media.
print(f'A soma dos elementos é: {s}')
print(f'A média dos elementos é: {media}')