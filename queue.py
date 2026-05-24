from typing import Any,List



class Queue:

    def __init__(self) -> None:
     self.__data: List[Any] = []

    def __repr__(self) -> str:
     return str(self.__data)
    
    def enqueue(self, elemento: Any) -> None:
     self.__data.append(elemento)


