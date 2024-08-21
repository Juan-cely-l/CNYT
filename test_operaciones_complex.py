
import unittest
from operaciones_complex import *

class Test(unittest.TestCase):
    def testSuma(self):
        a,b = [5,5],[5,6]
        c,d = [1,10],[5,8]
        self.assertEqual(suma_complex(a,b),[10,11])
        self.assertEqual(suma_complex(c,d),[6,18])

    def testMult(self):
        a,b = [5,5],[5,6]
        c,d = [1,10],[5,8]
        self.assertEqual(mult_complex(a,b),[-5,55])
        self.assertEqual(mult_complex(c,d),[-75,58])

    def testResta(self):
        a,b = [5,5],[5,6]
        c,d = [1,10],[5,8]
        self.assertEqual(resta_complex(a,b),[0,-1])
        self.assertEqual(resta_complex(c,d),[-4,2])

    def testDiv(self):
        a,b = [5,5],[5,6]
        c,d = [1,10],[5,8]
        self.assertEqual(division_complex(a,b),[0.9016393442622951, -0.08196721311475409])
        self.assertEqual(division_complex(c,d),[0.9550561797752809, 0.47191011235955055])

    def testMod(self):
        a = [5,5]
        c = [1,10]
        self.assertEqual(modulo_complex(a),7.0710678118654755)
        self.assertEqual(modulo_complex(c),10.04987562112089)

    def testConjugado(self):
        a = [5,5]
        c = [1,10]
        self.assertEqual(conjugado_complex(a),[5,-5])
        self.assertEqual(conjugado_complex(c),[1,-10])

    def testPolarACartesiano(self):
        a = [6,0.52359]
        b = [11.180339887498949, 1.1071487177940904]
        self.assertEqual(polar_cartesiano(a), [5.196178749301447, 2.9999544005381225])
        
        
    
    def testCartesianoAPolar(self):
        a = [6,6]
        b = [5,10]
        self.assertEqual(cartesiano_polar(a),([8.48528137423857, 0.7853981633974483]))
        self.assertEqual(cartesiano_polar(b),[11.180339887498949, 1.1071487177940904])

        
if __name__ == "__main__":
    unittest.main()
