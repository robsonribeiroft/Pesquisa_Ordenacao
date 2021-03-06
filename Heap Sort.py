#Heap Sort 
#Princípio: Utiliza uma estrutura de dados chamada heap, para ordenar os elementos
#à medida que os insere na estrutura. O heap pode ser representado como uma árvore
#ou como um vetor.
#Complexidade no melhor e no pior caso: O(n log2n) é o mesmo que O(n lgn)

import random
lista = []

def heapSort(lista):
    #Função que implementa o método de ordenamento Heap Sort.
    def selet(inicio, contador):  
        raiz = inicio  
  
        while raiz * 2 + 1 < contador:  
            filho = raiz * 2 + 1  
            if filho < contador - 1 and lista[filho] < lista[filho + 1]:  
                filho += 1  
            if lista[raiz] < lista[filho]:  
                lista[raiz], lista[filho] = lista[filho], lista[raiz]  
                raiz = filho  
            else:  
                return

    contador = len(lista)  
    inicio = contador // 2 - 1  
    fim = contador - 1  
  
    while inicio >= 0:  
        selet(inicio, contador)  
        inicio -= 1  
  
    while fim > 0:  
        lista[fim], lista[0] = lista[0], lista[fim]  
        selet(0, fim)  
        fim -= 1 
    print("Lista Ordenada (Heap Sort):")
    print(lista)

def listaRan(tam, lista):
    #Função gera uma 'lista' com 'tam' valores aleatórios.
    random.seed()
    i=0
    while i<tam:
        num = random.randint(1, 10*tam)
        if num not in lista:
            lista.append(num)
            i+=1
    print("Lista Desordenada:")
    print(lista)


listaRan(20, lista)
heapSort(lista)

