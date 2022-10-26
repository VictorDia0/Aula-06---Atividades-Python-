# *** soma de elmentos ***
m = [[1,2,3],[2,1,4],[3,4,1]]
s = 0
for i in range(0,3) :
    for j in range (0,3) :
        s+= m[i][j]
        #print(m[i][j], end = ' ')
    #print('\n')
print(f'A soma = {s}')

''' *** Contando elementos ***
m = [[1,2,3],[2,1,4],[3,4,1]]
cont = 0
for i in range(0,3) :
    for j in range (0,3) :
        cont = cont+ 1
print(f'A quantidade = {cont}')'''

''' *** Mostrar elementos Pares ***
m = [[1,2,3],[2,1,4],[3,4,1]]
cont = 0
for i in range(0,3) :
    for j in range (0,3) :
        if (m[i][j] % 2 == 0) :
            print(m[i][j], end = ' ')'''

''' *** Calcular a média dos elementos ***
m = [[1,2,3],[2,1,4],[3,4,1]]
soma = 0
cont = 0
for i in range(0,3) :
    for j in range (0,3) :
        cont = cont + 1
        soma = soma + m[i][j]
media = soma / cont
print(f'A média = {media :.2f}') '''

''' **** Mostrar o maior elemento ****
m = [[1,2,3],[2,1,4],[3,4,1]]
maior = m[0][0]
for i in range(0,3) :
    for j in range (0,3) :
        if (m[i][j] > maior) :
            maior = m[i][j]
print(f'O maior elemento = {maior}') '''