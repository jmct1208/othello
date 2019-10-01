from Heuristica import *
class Estado:

    def __init__(self, tablero, turno, evaluacion, movimientos):
        self.tablero = tablero
        self.turno = turno
        self.evaluacion = evaluacion
        self.movimientos = movimientos

    def display(self):
        turno = "Humano" if self.turno else "Computadora"
        print("------------------------------------------------")
        print("Turno: %s" % turno)
        '''
        fichas_h = coin_parity(self.tablero, self.turno)
        mobilidad_h = actual_mobility(self.tablero, self.turno)
        estabilidad_h = stability(self.tablero, self.turno)
        esquinas_h = corners_captured(self.tablero, self.turno)
        print("Heuristica esquinas: %s" % str(esquinas_h))
        print("Estabilidad: %s" % str(estabilidad_h))
        print("Mobilidad: %s" % str(mobilidad_h))
        print("Heuristica fichas: %s" % str(fichas_h))
        '''
        print("Evaluacion: %s" % str(self.evaluacion))
        print("Movimientos posibles: %s" % str(self.movimientos))
        transpuesta = [list(i) for i in zip(*self.tablero.mundo)]
        for l in transpuesta:
            print(l)
