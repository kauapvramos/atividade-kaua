from typing import Any,List

class Queue:

    def __init__(self, max_size: int = None) -> None:
     self.__data: List[Any] = []
     self.__max_size = max_size

    def __repr__(self) -> str:
     return str(self.__data)
    
    def is_full(self) -> bool:
        if self.__max_size is None:
            return False

        return len(self.__data) >= self.__max_size
    
    def enqueue(self, elemento: Any) -> None:
        if self.is_full():
          print("Lista cheia")
    
        else:
         self.__data.append(elemento)
    
    def dequeue(self) -> None:
        if len(self.__data) == 0:
         print("Lista Vazia")
        else:
          return print("Item removido: ",self.__data.pop(0))

    def is_empty(self) -> bool:
     if len(self.__data) == 0:
       return True
     else:
       return False     
    
    def peek(self) -> Any:
       if len(self.__data) == 0:
         print("Lista Vazia")
       else: 
          return print("Primeiro Item: ",self.__data[0])
     
    
    def size(self) -> Any:
      print("Tamanho da Lista:", len(self.__data))
      return len(self.__data)
    

    def clear(self) -> Any: 
      self.__data.clear()
      print("Metodo clear: lista foi limpa")

    ### metodo pop para indicar o indicie do elemento a ser removido no dequeue
    def pop(self) -> Any:
        if not self.__data:
            return None
        return self.__data.pop



  
  
   
   