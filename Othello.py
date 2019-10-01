import Tablero
from Estado import Estado
import copy
from Heuristica import evaluacion

class Othello:
    def __init__(self):
        tablero_inicial = Tablero.Tablero()
        tablero_inicial.set_ficha(3, 3, False)
        tablero_inicial.set_ficha(4, 4, False)
        tablero_inicial.set_ficha(3, 4, True)
        tablero_inicial.set_ficha(4, 3, True)
        turno_inicial = True
        mov_iniciales = tablero_inicial.jugadas_posibles(turno_inicial)
        self.inicial = Estado(tablero_inicial, turno_inicial, \
                        evaluacion(tablero_inicial, turno_inicial), mov_iniciales)
        
    def actions(self, estado):
        return estado.tablero.jugadas_posibles(estado.turno)
    
    def resultado(self, estado, movimiento):
        if movimiento is None:
            nuevo_turno = not estado.turno
            nuevo_tablero = copy.deepcopy(estado.tablero)
            return Estado(nuevo_tablero, nuevo_turno,\
                            evaluacion(nuevo_tablero, nuevo_turno),\
                                nuevo_tablero.jugadas_posibles(nuevo_turno))
        if movimiento not in estado.movimientos:
            return estado 
        nuevo_turno = not estado.turno            
        nuevo_tablero = copy.deepcopy(estado.tablero)
        nuevo_tablero.set_ficha(movimiento[0], movimiento[1], estado.turno)
        fichas_a_rodear = estado.tablero.fichas_rodeadas(\
                            movimiento[0], movimiento[1], estado.turno)
        nuevo_tablero.invertir_fichas(fichas_a_rodear, estado.turno)
        nuevo_estado = Estado(nuevo_tablero, nuevo_turno,\
                              evaluacion(nuevo_tablero, nuevo_turno),\
                              nuevo_tablero.jugadas_posibles(nuevo_turno))
        return nuevo_estado
        
    def terminal_test(self, estado):
        fichas_en_tablero = estado.tablero.cantidad_fichas()
        fichas_negras = int(fichas_en_tablero.x)
        fichas_blancas = int(fichas_en_tablero.y)
        jugadas_posibles = estado.movimientos
        if fichas_negras + fichas_blancas == 64:
            return True
        elif len(jugadas_posibles) == 0:
            jugadas_posibles_contricante = estado.tablero.\
                jugadas_posibles(not estado.turno)
            if len(jugadas_posibles_contricante) == 0:
                return True
        else: return False
        
    def cutoff_test(self, estado, profundidad, limite):
        if profundidad > limite or self.terminal_test(estado):
            return True
        
    
        
    
        
        
        
        
