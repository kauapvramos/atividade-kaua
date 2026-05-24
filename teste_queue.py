from queue import Queue

if __name__ == "__main__":
   lista = Queue(3)
   lista.enqueue(1)
   lista.enqueue(2)
   lista.enqueue(3)
   print(lista)
   print(lista.is_full())
