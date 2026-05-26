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

    def is_empty(self) -> bool:
        return len(self.__data) == 0

    def enqueue(self, elemento: Any) -> None:
        if self.is_full():
            raise OverflowError("Fila cheia! Tamanho máximo: ",self.__max_size)
        self.__data.append(elemento)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("não é possível remover: a fila está vazia.")
        return self.__data.pop(0)

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError(" a fila está vazia.")
        return self.__data[0]

    def size(self) -> int:
        return len(self.__data)

    def clear(self) -> None:
   
        self.__data.clear()

    def pop(self) -> Any:
        if not self.__data:
            return None
        return self.__data.pop()
