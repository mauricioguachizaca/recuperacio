from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedListExeption import LinkedEmptyException

class StackOperation(Linked_List):
    def __init__(self, tope):
        super().__init__()
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTop(self):
        return self._length < self.__tope

    def push(self, data):
        if self.verifyTop:
            self.add(data, 0)
        else:
            raise LinkedEmptyException("Stack is Full")

    def pop(self):
        if self.isEmpty:
            raise LinkedEmptyException("Stack is Empty")
        else:
            num = self.get(0)
            self.delete(0)  # Corregir el nombre del método de delete
            return num
