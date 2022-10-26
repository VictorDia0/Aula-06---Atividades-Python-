#Dada uma matriz 5x5, elabore um algoritmo que escreva: d) Mostre a soma e a media dos elementos acima da diagonal principal

m = [[10,17,-3,40,22],[1,44,27,9,25],[14,0,62,13,34],[-5,-10,90,85,3],[2,77,39,16,56]]
cont = 0
soma = 0
for i in range(0,5):
    for l in range (0,5):
        if (i < l):
            cont = cont + 1
            soma = soma + m[i][l]
media = soma / cont

print(f'A soma dos elementos acima da diagonal principal é {soma}.')
print(f'A média dos elementos acima da diagonal principal é {media}')