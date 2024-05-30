import sys
sys.path.append('../')

from controls.expresionDaoControl import ExpresionDaoControl
from models.expresion import Expresion

expresion1 = ExpresionDaoControl()


expresion1._expresion._expresion = "16 4 + 2 5 * + 6 /"
expresion1.transform()

expresion1._expresion._expresion = "16 10 + 2 5 * + 6 /"
expresion1.transform()

expresion1._expresion._expresion = "a"
expresion1.transform()

expresion1._expresion._expresion = "13 5 p"
expresion1.transform()



