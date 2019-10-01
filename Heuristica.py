def coin_parity(tablero, turno):
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
        print("Fichas jugador: %s" % str(fichas_jugador))
        print("Fichas contrincante: %s" % str(fichas_contrincante))
        return 100 * \
                (fichas_jugador - fichas_contrincante) \
                / (fichas_jugador + fichas_contrincante)
    
def actual_mobility(tablero, turno):
        max_player = turno
        min_player = not turno
        max = tablero.numero_jugadas_posibles(max_player)
        min = tablero.numero_jugadas_posibles(min_player)
        print("Mobilidad jugador: %s" % str(max))
        print("Mobilidad contrincante: %s" % str(min))
        if max + min != 0:
            return 100 * (max - min) / (max + min)
        else:
            return 0
    
def corners_captured(tablero, turno):
        jugador = turno
        contrincante = not jugador
        max = tablero.heuristica_esquinas(jugador)
        min = tablero.heuristica_esquinas(contrincante)
        print("Esquinas jugador: %s" % str(max))
        print("Esquinas contrincante: %s" % str(min))
        if max + min != 0:
            return 100 * (max - min) / (max + min)
        else:
            return 0       
        
def stability(tablero, turno):
        max_player = turno
        min_player = not turno
        max = tablero.heuristica_estabilidad(max_player)
        min = tablero.heuristica_estabilidad(min_player)
        print("Estabilidad jugador: %s" % str(max))
        print("Estabilidad contrincante: %s" % str(min))
        if max + min != 0:
            return 100 * (max - min) / (max + min)
        else:
            return 0
'''
def evaluacion(tablero, turno):
        return 30 * corners_captured(tablero, turno) + \
                5 * actual_mobility(tablero, turno) + \
                25 * stability(tablero, turno) + \
                25 * coin_parity(tablero, turno)
'''
def evaluacion(tablero, turno):
    max_player = turno
    min_player = not turno
    max = tablero.heuristica_pesos(max_player)
    min = tablero.heuristica_pesos(min_player)
    
    return max - min
    
