#Dada uma matriz 5x5, elabore um algoritmo que escreva: h) A soma e média dos elementos da diagonal secundaria
m = [[10,17,-3,40,22],[1,44,27,9,25],[14,0,62,13,34],[-5,-10,90,85,3],[2,77,39,16,56]]

for i in range(0,5):
    for j in range (0,5):
        if (i + j == 5 - 1):
            print(m[i][j])