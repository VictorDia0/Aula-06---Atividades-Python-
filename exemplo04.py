vet=[10,5,7,4,22]
i=0
soma=0
soma2=0
cont=0
while(i<5):
    soma2+=vet[i]
    if (vet[i]%2==0): # elementos pares
        soma+=vet[i]
        cont+=1
    i=i+1
media=soma/cont
print(f'A soma dos elementos pares {soma}')
print(f'A soma de todos elmentos {soma2}')
print(f'Media pares {media}')