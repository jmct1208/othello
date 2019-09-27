inf = float('inf')
class Othello(Game):
    def __init__(self):
        tablero_inicial = Tablero()
        tablero_inicial.setFicha(3, 3, "blanco")
        tablero_inicial.setFicha(4, 4, "blanco")
        tablero_inicial.setFicha(3, 4, "negro")
        tablero_inicial.setFicha(4, 3, "negro")
        turno_inicial = true
        mov_iniciales = tablero_inicial.jugadas_posibles(turno_inicial)
        self.inicial = Estado(tablero, turno_inicial, 0, mov_iniciales)
        
    def actions(self, estado):
        return estado.tablero.jugadas_posibles(estado.turno)
    
    def resultado(self, estado, movimiento):
        if movimiento not in estado.movimientos:
            return state 
        tablero = estado.tablero.copy()
        tablero.setFicha(movimiento[0], movimiento[1], estado.turno)
        fichas_a_rodear = estado.tablero.fichas_rodeadas(movimiento[0], movimiento[1], estado.turno)
        tablero.invertir_fichas(fichas_a_rodear, estado.turno)
        nuevo_estado = Estado(tablero, !estado.turno, 0, tablero.jugadas_posibles(!estado.turno))
        
    def terminal_test(self, estado):
        fichas_en_tablero = estado.tablero.cantidad_fichas()
        fichas_negras = int(fichas_en_tablero.x)
        fichas_blancas = int(fichas_en_tablero.y)
        jugadas_posibles = estado.movimientos
        if fichas_negras + fichas_blancas == 64:
            return true
        elif len(jugadas_posibles) == 0:
            jugadas_posibles_contricante = estado.tablero.jugadas_posibles(!estado.turno)
            if len(jugadas_posibles_contricante) == 0:
                return true
        else return false

    def evaluacion(self, estado):
        
    def cutoff_test(self, estado, profundidad, limite):
        if profundidad > limite or self.terminal_test(estado):
            return True
        
    def coin_parity(self, estado):
        jugador = estado.turno
        fichas_jugador = 0
        fichas_contrincante = 0
        fichas_en_tablero = estado.tablero.cantidad_fichas()
        if jugador:
            fichas_jugador = int(fichas_en_tablero.x)
            fichas_contrincante = int(fichas_en_tablero.y)
        else:
            fichas_jugador = int(fichas_en_tablero.y)
            fichas_contrincante  = int(fichas_en_tablero.x)
        return 100 * (fichas_jugador - fichas_contrincante) / (fichas_jugador - fichas_contrincante)
    
    def actual_mobility(self, estado):
        max_player = estado.turno
        min_player = !estado.turno
        max_player_actual_mobility = estado.tablero.numero_jugadas_posibles(max_player)
        min_player_actual_mobility = estado.tablero.numero_jugadas_posibles(min_player)
        if max_player_actual_mobility + min_player_actual_mobility != 0:
            return (max_player_actual_mobility - min_player_actual_mobility) / (max_player_actual_mobility + min_player_actual_mobility)
        else:
            return 0

def max_value(state, alpha, beta, profundidad):
        if juego.cutoff_test(state, profundidad, d):
            return juego.evaluacion(estado)
        v = -inf
        for a in juego.actions(estado):
            v = max(v, min_value(juego.resultado(estado, a), alpha, beta, profundidad))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def min_value(state, alpha, beta, profundidad):
        if juego.cutoff_test(estado, profundidad, d):
            return juego.evaluacion(estado)
        v = inf
        for a in juego.actions(state):
            v = min(v, max_value(juego.result(state, a), alpha, beta, profundidad + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v 
       
def alphabeta_cuttoff_search(estado, juego, d=4):
    best_score = -inf
    beta = inf
    best_action = None
    for a in juego.actions(estado):
        v = min_value(juego.resultado(estado, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action
        
    
        
        
        
        
