from typing import Any,List




class Stack:




    def __init__(self) -> None:
     self.__data: List[Any] = []




    def push(self, elemento: Any) -> None:
     self.__data.append(elemento)
   
    def __repr__(self) -> str:
      return str(self.__data)
   
    def remover(self) -> Any:
     if len(self.__data) == 0:
       return print("Lista Vaziza")
     else:
       print("Item removido: ", self.__data.pop())
     return self.__data
     
    def pop(self) -> Any:
        if not self.__data:
            return None
        return self.__data.pop
   
    def is_emply(self) -> Any:
     if len(self.__data) == 0:
       return print("Lista Vazia")
     else:
       print("Nao esta Vazia Lista tem: ",len(self.__data), "elementos")
     return self.__data
   
    def tamanho(self) -> Any:
       print("Tamanho: ",len(self.__data))
       return len(self.__data)
   
    def peek(self) -> Any:
      if not self.__data:
        return None
      return self.__data[-1]
   
     
if __name__ == "__main__":
  pilha = Stack()
  pilha.push("Livro 1")      
  pilha.push("Livro 2")      
  pilha.push("Livro 3")      
  pilha.push("Livro 4")      




  print(pilha)
  pilha.remover()
  print(pilha)
  pilha.tamanho()
  pilha.is_emply()
  print(pilha.peek())












       














 
