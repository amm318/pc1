import unittest
from pc1 import Meneses_Persona,Meneses_Atleta
class TestMenesesAtleta(unittest.TestCase): 

 def setUp(self): 
    self.atleta = Meneses_Atleta("Angelo Meneses")

 def test_caminar(self): 
    self.atleta.meneses_caminar() 
    self.assertEqual(self.atleta.meneses_distancia_recorrida, 2) 
 def test_entrenar(self):
    self.atleta.meneses_entrenar(5) 
    self.assertEqual(self.atleta.meneses_calorias_consumidas, 2500) 
    self.assertEqual(self.atleta.meneses_distancia_recorrida, 5)

 def test_competir(self): 
    self.atleta.meneses_competir(10) 
    self.assertEqual(self.atleta.meneses_calorias_consumidas, 7500) 
    self.assertEqual(self.atleta.meneses_distancia_recorrida, 10) 
    
if __name__ == '__main__': 
    unittest.main()








