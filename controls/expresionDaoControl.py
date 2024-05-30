from models.expresion import Expresion
from controls.dao.daoAdapter import DaoAdapter
from controls.tda.stack.stack import Stack

class ExpresionDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Expresion)
        self.__expresion = None

    @property
    def _expresion(self):
        if self.__expresion is None:
            self.__expresion = Expresion()
        return self.__expresion

    @_expresion.setter
    def _expresion(self, value):
        self.__expresion = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__expresion._id = self._lista._length +1
        self._save(self._expresion)

    

    def transform(self):
        stack = Stack(20)
        tokens = self.__expresion._expresion.split()

        for token in tokens:
            if token.isalpha():
                result = "No letras"
            
            elif token.isdigit():
                stack.push(int(token))
            else:
                B = stack.pop()
                A = stack.pop()

                a = float(A)
                b = float(B)

                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    result = a / b
                elif token == '^':
                    result = a ** b
                else:
                    result = "Operador no valido"
                stack.push(result)

        self._expresion._resultado = result


        self.save
        return result

    


