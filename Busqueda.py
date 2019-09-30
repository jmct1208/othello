inf = float('inf')
def alphabeta_cutoff_search(estado, juego, d=4):
    tablero = estado.tablero
    turno = estado.turno
    def max_value(estado, alpha, beta, profundidad):
        if juego.cutoff_test(estado, profundidad, d):
            return juego.evaluacion(tablero, turno)
        v = -inf
        for a in juego.actions(estado):
            v = max(v, min_value(juego.resultado(estado, a), \
                    alpha, beta, profundidad))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def min_value(estado, alpha, beta, profundidad):
        if juego.cutoff_test(estado, profundidad, d):
            return juego.evaluacion(tablero, turno)
        v = inf
        for a in juego.actions(estado):
            v = min(v, max_value(juego.resultado(estado, a), \
                    alpha, beta, profundidad + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v 
    best_score = -inf
    beta = inf
    best_action = None
    for a in juego.actions(estado):
        v = min_value(juego.resultado(estado, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action
