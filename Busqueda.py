from Heuristica import evaluacion
inf = float('inf')
def alphabeta_cutoff_search(estado, juego, d=4):
    tablero = estado.tablero
    turno = estado.turno
    def max_value(estado, alfa, beta, profundidad):
        if juego.cutoff_test(estado, profundidad, d):
            print("d: %s" % str(d))
            print("profundidad: %s" % str(profundidad))
            estado.display()
            return evaluacion(tablero, turno)
        v = -inf
        for a in juego.actions(estado):
            nodo_a_expander = juego.resultado(estado, a)
            #nodo_a_expander.display()
            v = max(v, min_value(nodo_a_expander, \
                    alfa, beta, profundidad))
            if v >= beta:
                return v
            alfa = max(alfa, v)
        return v
    
    def min_value(estado, alfa, beta, profundidad):
        if juego.cutoff_test(estado, profundidad, d):
            return evaluacion(tablero, turno)
        v = inf
        for a in juego.actions(estado):
            nodo_a_expander = juego.resultado(estado, a)
            #nodo_a_expander.display()
            v = min(v, max_value(nodo_a_expander, \
                    alfa, beta, profundidad + 1))
            if v <= alfa:
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
