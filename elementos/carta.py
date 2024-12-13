
# Descripción: Clase que representa una carta de la baraja francesa. Cada carta tiene un palo y un valor.
class Carta:
    palos = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def toString(self):
        return f'{self.valor} de {self.palo}'
    
    @staticmethod
    def getPalos():
        return Carta.palos
    
    @staticmethod
    def getValores():
        return Carta.valores