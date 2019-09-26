class Othello(Game):
    def __init__(self, dimension=8, dimension=8):
       
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
        
        
        
        
