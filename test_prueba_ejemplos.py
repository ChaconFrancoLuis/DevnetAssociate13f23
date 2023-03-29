
"""#libreria pytest para pruebas de unidad
import pytest

#unidad de prueba o unittest
def add5(v):
    myval = v + 5
    return myval

# Caso de Prueba o testcase
#caso de prueba funcion add5, todas las pruebas fueron exitosas
def tests_add5():
    r = add5(1)
    assert r == 6
    r = add5(5)
    assert r == 10
    r = add5(10.102645)
    assert r == 15.102645"""

"""
#libreria unittest para pruebas de unidad
import unittest

#unit test
def add5(v):
    myval = v + 5
    return myval

#test case
class tests_add5(unittest.TestCase):
    def test_add5(self):
        self.assertEqual(add5(1),6)
        self.assertEqual(add5(5),10)
        self.assertEqual(add5(10.102645),15.102645)


# condicion que se cumple cuando se ejecuta archivo directamente y no por medio de importarlo a otro archivo
if __name__ == '__main__':
    unittest.main()"""

#ejemplo unittest con pytest y funciones para resolver el area de un circulo
"""
import pytest
#test units
def Area(radius):
    pi = 3.1416
    miArea = pi * radius **2
    return miArea

def mostrarArea(radius):
    mostrar = Area(radius)
    print(f"area de un ciruclo con radio{str(radius)} es {str(mostrar)}")

# Test Case
def tests_add5():
    r = Area(8)
    assert r == 201.0624"""

#ejemplo unittest con libreria unittest.testcase y funciones para resolver el area de un circulo

"""
import unittest

#test unit
def add5(v):
    myval = v + 5
    return myval 

#test case
class tests_add5(unittest.TestCase):
    def test_add5(self):
        self.assertEqual(add5(1),6)
        self.assertEqual(add5(5),10)
        self.assertEqual(add5(10.102102),15.102102)


if __name__ == '__main__':
    unittest.main()"""

