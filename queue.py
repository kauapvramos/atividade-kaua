from typing import Any,List



class Queue:

    def __init__(self) -> None:
     self.__data: List[Any] = []

    def __repr__(self) -> str:
     return str(self.__data)
    
    def enqueue(self, elemento: Any) -> None:
     self.__data.append(elemento)
    
    def peek(self) -> Any:
      if not self.__data:
        return None
      return self.__data[-1]
    

    def is_emply(self) -> Any:
     if len(self.__data) == 0:
       return print("Lista Vazia")
     else:
       print("Nao esta Vazia Lista tem: ",len(self.__data), "elementos")
     return self.__data
    
    def tamanho(self) -> Any:
       print("Tamanho: ",len(self.__data))
       return len(self.__data)
    

    def clear(self) -> Any: 
      self.__data.clear()
      print("Lista LIMPA")

    



