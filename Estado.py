class Estado:

    def __init__(self, tablero, turno, evaluacion, movimientos):
        self.tablero = tablero
        self.turno = turno
        self.evaluacion = evaluacion
        self.movimientos = movimientos

    def display(self):
        import Othello as j
        juego = j.Othello()
        turno = "Humano" if self.turno else "Computadora"
        fichas_h = juego.coin_parity(self.tablero, self.turno)
        mobilidad_h = juego.actual_mobility(self.tablero, self.turno)
        estabilidad_h = juego.stability(self.tablero, self.turno)
        esquinas_h = juego.corners_captured(self.tablero, self.turno)
        print("Turno: %s" % turno)
        print("Heuristica esquinas: %s" % str(esquinas_h))
        print("Estabilidad: %s" % str(estabilidad_h))
        print("Mobilidad: %s" % str(mobilidad_h))
        print("Heuristica fichas: %s" % str(fichas_h))
        print("Evaluacion: %s" % str(self.evaluacion))
        print("Movimientos posibles: %s" % str(self.movimientos))
        for l in self.tablero.mundo:
            print l
