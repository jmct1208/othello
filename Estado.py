# -*- coding: utf-8 -*-
class Estado:
    def __init__(self, tablero, turno, evaluacion, movimientos):
        self.tablero = tablero
        self.turno = turno
        self.evaluacion = evaluacion
        self.movimientos = movimientos
        
    def display(self):
        turno = "Humano" if self.turno else "Computadora"
        print("Turno: %s" % turno)
        print("Evaluacion: %s" % str(self.evaluacion))
        print("Movimientos posibles: %s" % str(self.movimientos))
        
        
