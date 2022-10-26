lista = ['abacaxi','banana','morango','manga','caju']
lista.append('pera') #Adiciona um novo item no final da lista
lista.insert(0,'uva') # Adiciona um novo item escolhendo a posição
lista.pop() # Remove um item no final da lista
lista.remove('uva') # Remove um item desejado

for x in range(0,len(lista)) :
    print(lista[x], end = ' ')