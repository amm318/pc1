class Meneses_Reservorio:

    def __init__(self, ubicacion, volumen_disponible=0):

        self.meneses_ubicacion = ubicacion

        self.meneses_volumen_disponible = volumen_disponible


    def meneses_llenar(self):

        self.meneses_volumen_disponible += 100


class Meneses_ReservorioResidencial(Meneses_Reservorio):

    def __init__(self, ubicacion, capacidad_maxima, volumen_disponible=0):

        super().__init__(ubicacion, volumen_disponible)

        self.meneses_capacidad_maxima = capacidad_maxima


    def meneses_llenar(self, volumen=100):

        if self.meneses_volumen_disponible + volumen <= self.meneses_capacidad_maxima:

            self.meneses_volumen_disponible += volumen

        else:

            self.meneses_volumen_disponible = self.meneses_capacidad_maxima


    def meneses_consumir(self):

        if self.meneses_volumen_disponible - 20 >= 0:

            self.meneses_volumen_disponible -= 20

        else:

            self.meneses_volumen_disponible = 0


    def meneses_calcular_consumo(self):

        return self.meneses_capacidad_maxima - self.meneses_volumen_disponible

