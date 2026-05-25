from queue import Queue

if __name__ == "__main__":

   ## Definindo o tamanho da Lista 
   lista = Queue(3)

   ## Adicionando elementos com a funcao def enquere
   lista.enqueue(1)
   lista.enqueue(2)
   lista.enqueue(3)
   
   ## Lista no momento 01
   print("Lista no momento: ", lista)

   ## Verificando tamanho da Lista
   print("Tamanho da Lista: ", lista.size())
   
   ## Verificando se a Lista esta Cheia
   print(lista.is_full())

   ## Verificando se esta Vazia 01
   print(lista.is_empty())

   ## Adicionado mais um valor a Lista mostrando que esta cheia 
   lista.enqueue(4)

   ## removendo e retorna o primeiro elemento
   lista.dequeue()

    ## retornando o primeiro item sem remover 
   lista.peek()


    ## Lista no momento 02
   print("Lista no momento: ", lista)

   ## removendoi itens da Lista
   lista.clear()

    ## Lista no momento 03
   print("Lista no momento: ", lista)

   ## Verificando se esta Vazia 02
   print(lista.is_empty())



 
   