from queue import Queue

if __name__ == "__main__":

    ## Definindo o tamanho da Lista
    lista = Queue(3)

    ## Adicionando elementos com a funcao enqueue
    lista.enqueue(1)
    lista.enqueue(2)
    lista.enqueue(3)

    ## Lista no momento 01
    print("Lista no momento:", lista)

    ## Verificando tamanho da Lista
    print("Tamanho da Lista:", lista.size())

    ## Verificando se a Lista esta Cheia
    print("Está cheia?", lista.is_full())

    ## Verificando se esta Vazia 01
    print("Está vazia?", lista.is_empty())

    ## Tentando adicionar mais um valor (fila cheia → captura o erro)
    try:
        lista.enqueue(4)
    except OverflowError as e:
        print("OverflowError:", e)

    ## Removendo e retornando o primeiro elemento
    print("Dequeue:", lista.dequeue())

    ## Retornando o primeiro item sem remover
    print("Peek:", lista.peek())

    ## Lista no momento 02
    print("Lista no momento:", lista)

    ## Removendo todos os itens da Lista
    lista.clear()

    ## Lista no momento 03
    print("Lista no momento:", lista)

    ## Verificando se esta Vazia 02
    print("Está vazia?", lista.is_empty())