import Tablero
import Estado
import copy

class Othello:
    def __init__(self):
        tablero_inicial = Tablero.Tablero()
        tablero_inicial.set_ficha(3, 3, False)
        tablero_inicial.set_ficha(4, 4, False)
        tablero_inicial.set_ficha(3, 4, True)
        tablero_inicial.set_ficha(4, 3, True)
        turno_inicial = True
        mov_iniciales = tablero_inicial.jugadas_posibles(turno_inicial)
        self.inicial = Estado.Estado(tablero_inicial, turno_inicial, \
                              self.evaluacion(tablero_inicial, turno_inicial), mov_iniciales)
        
    def actions(self, estado):
        return estado.tablero.jugadas_posibles(estado.turno)
    
    def resultado(self, estado, movimiento):
        if movimiento is None:
            nuevo_turno = not estado.turno
            nuevo_tablero = estado.tablero.copy()
            return Estado.Estado(nuevo_tablero, nuevo_turno,\
                            self.evaluacion(nuevo_tablero, nuevo_turno),\
                                nuevo_tablero.jugadas_posibles(nuevo_turno))
        if movimiento not in estado.movimientos:
            return estado 
        nuevo_turno = not estado.turno            
        nuevo_tablero = copy.deepcopy(estado.tablero)
        nuevo_tablero.set_ficha(movimiento[0], movimiento[1], estado.turno)
        fichas_a_rodear = estado.tablero.fichas_rodeadas(\
                            movimiento[0], movimiento[1], estado.turno)
        nuevo_tablero.invertir_fichas(fichas_a_rodear, estado.turno)
        nuevo_estado = Estado.Estado(nuevo_tablero, nuevo_turno,\
                              self.evaluacion(nuevo_tablero, nuevo_turno),\
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
        
    def coin_parity(self, tablero, turno):
        jugador = turno
        fichas_jugador = 0
        fichas_contrincante = 0
        fichas_en_tablero = tablero.cantidad_fichas()
        if jugador:
            fichas_jugador = int(fichas_en_tablero.x)
            fichas_contrincante = int(fichas_en_tablero.y)
        else:
            fichas_jugador = int(fichas_en_tablero.y)
            fichas_contrincante  = int(fichas_en_tablero.x)
        return 100 * \
                (fichas_jugador - fichas_contrincante) \
                / (fichas_jugador + fichas_contrincante)
    
    def actual_mobility(self, tablero, turno):
        max_player = turno
        min_player = not turno
        max = tablero.numero_jugadas_posibles(max_player)
        min = tablero.numero_jugadas_posibles(min_player)
        if max + min != 0:
            return 100 * (max - min) / (max + min)
        else:
            return 0
    
    def corners_captured(self, tablero, turno):
        jugador = turno
        contrincante = not jugador
        max = tablero.heuristica_esquinas(jugador)
        min = tablero.heuristica_esquinas(contrincante)
        if max + min != 0:
            return 100 * (max - min) / (max + min)
        else:
            return 0       
        
    def stability(self, tablero, turno):
        max_player = turno
        min_player = not turno
        max = tablero.heuristica_estabilidad(max_player)
        min = tablero.heuristica_estabilidad(min_player)

        if max + min != 0:
            return 100 * (max - min) / (max + min)
        else:
            return 0

    def evaluacion(self, tablero, turno):
        return 30 * self.corners_captured(tablero, turno) + \
                5 * self.actual_mobility(tablero, turno) + \
                25 * self.stability(tablero, turno) + \
                25 * self.coin_parity(tablero, turno)
        
    
        
        
        
        
