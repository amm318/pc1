import unittest
from ejer2 import Meneses_Reservorio,Meneses_ReservorioResidencial
import unittest


class TestMenesesReservorioResidencial(unittest.TestCase):

    

    def setUp(self):

        self.reservorio = Meneses_ReservorioResidencial("Ubicación X", 500)


    def test_llenar(self):

        self.reservorio.meneses_llenar(300)

        self.assertEqual(self.reservorio.meneses_volumen_disponible, 300)

        self.reservorio.meneses_llenar(250)

        self.assertEqual(self.reservorio.meneses_volumen_disponible, 500)  # No debe superar la capacidad máxima


    def test_consumir(self):

        self.reservorio.meneses_volumen_disponible = 100

        self.reservorio.meneses_consumir()

        self.assertEqual(self.reservorio.meneses_volumen_disponible, 80)

        self.reservorio.meneses_consumir()

        self.assertEqual(self.reservorio.meneses_volumen_disponible, 60)

    

    def test_calcular_consumo(self):

        self.reservorio.meneses_llenar(400)

        consumo = self.reservorio.meneses_calcular_consumo()

        self.assertEqual(consumo, 100)


if __name__ == '__main__':

    unittest.main()