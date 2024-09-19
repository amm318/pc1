class Meneses_Persona: 
    def __init__(self, nombre): 
        self.meneses_nombre = nombre 
        self.meneses_distancia_recorrida = 0 
    def meneses_caminar(self): 
        self.meneses_distancia_recorrida += 2 


class Meneses_Atleta(Meneses_Persona): 
    def __init__(self, nombre): 
        super().__init__(nombre) 
        self.meneses_calorias_consumidas = 0 
    def meneses_entrenar(self, distancia=None): 
        if distancia is None: distancia = 10 
         
        self.meneses_calorias_consumidas += distancia * 500 
        self.meneses_distancia_recorrida += distancia 
        
    def meneses_competir(self, distancia=None): 
        if distancia is None: distancia = 20  
        self.meneses_calorias_consumidas += distancia * 750