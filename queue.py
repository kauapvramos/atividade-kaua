from typing import Any,List

class Queue:

    def __init__(self, max_size: int = None) -> None:
     self.__data: List[Any] = []
     self.__max_size = max_size

    def __repr__(self) -> str:
     return str(self.__data)
    
    def is_full(self) -> bool:
      if (self.size == self.__max_size ):
        return True
      else:
        return False
    
    def enqueue(self, elemento: Any) -> None:
        if self.is_full():
          print("Lista cheia")
    
        else:
         self.__data.append(elemento)
    
    def dequeue(self, elemento: Any) -> None:
        if len(self.__data) == 0:
         print("Lista Vazia")
        else:
         self.__data.pop(elemento[0])

    def is_emply(self) -> bool:
     if len(self.__data) == 0:
       return True
     else:
       return False     
    
    def peek(self) -> Any:
       if self.is_emply == True:
         print("Lista Vazia")
       return self.__data[0]
     
    
    def size(self) -> Any:
      print("Tamanho da Lista:", len(self.__data))
      return len(self.__data)
    

    def clear(self) -> Any: 
      self.__data.clear()
      print("Lista LIMPA")


if __name__ == "__main__":
   lista = Queue(3)
   lista.enqueue(5)
   lista.enqueue(3)
   print(lista)
   lista.dequeue
   lista.peek
   print(lista.is_emply())
   print(lista.size())

   print(lista)
