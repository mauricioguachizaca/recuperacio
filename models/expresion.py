class Expresion():
    def __init__(self):
        self.__id = 0
        self.__expresion = ""
        self.__resultado = 0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _expresion(self):
        return self.__expresion

    @_expresion.setter
    def _expresion(self, value):

        self.__expresion = value

    @property
    def _resultado(self):
        return self.__resultado

    @_resultado.setter
    def _resultado(self, value):
        self.__resultado = value

    @property
    def serialize(self):
        return {
            "id": self._id,
            "expresion": self._expresion,
            "resultado": self._resultado
        }
    
    def deserializar(self, data):
        expresion = Expresion()
        expresion._id = data["id"]
        expresion._expresion = data["expresion"]
        expresion._resultado = data["resultado"]
        return expresion
   