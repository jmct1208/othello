class Tablero:
    ''' Definicion de un tablero para el juego de Othello '''
    def __init__(self, dimension=8, tam_casilla=60):
        ''' Constructor base de un tablero
        :param dimension: Cantidad de casillas en horizontal y vertical del tablero
        :type dimension: int
        :param tamCasilla: El tamano en pixeles de cada casilla cuadrada del tablero
        :type tamCasilla: int
        '''
        self.dimension = dimension
        self.tam_casilla = tam_casilla
        self.numeroDeTurno = 0 # Contador de la cantidad de turnos en el tablero
        self.mundo = [[0 for i in range(self.dimension)] \
            for j in range(self.dimension)] # Representacion logica del tablero. Cada numero representa: 0 = vacio, 1 = ficha jugador1, 2 = ficha jugador 2
            
    def display(self):
        ''' Dibuja en pantalla el tablero, es decir, dibuja las casillas y las fichas de los jugadores '''
        fondo = color(63, 221, 24) # El color del fondo del tablero
        linea = color(0) # El color de linea del tablero
        grosor = 2 # Ancho de linea (en pixeles)
        jugador1 = color(0) # Color de ficha para el primer jugador
        jugador2 = color(255) # Color de ficha para el segundo jugador
        
        # Doble iteracion para recorrer cada casilla del tablero
        for i in range(self.dimension):
            for j in range(self.dimension):
                # Dibujar cada casilla del tablero:
                fill(fondo)
                stroke(linea)
                strokeWeight(grosor)
                rect(i*self.tam_casilla, j*self.tam_casilla, \
                    self.tam_casilla, self.tam_casilla)
                # Dibujar las fichas de los jugadores:
                if not self.mundo[i][j] == 0 and \
                    (self.mundo[i][j] == 1 or self.mundo[i][j] == 2): # en caso de que la casilla no este vacia
                    fill(jugador1 if self.mundo[i][j] == 1 else jugador2) # establecer el color de la ficha
                    noStroke() # quitar contorno de linea
                    ellipse(i*self.tam_casilla+(self.tam_casilla/2), \
                        j*self.tam_casilla+(self.tam_casilla/2), \
                        self.tam_casilla*3/5, self.tam_casilla*3/5)
    
    def set_ficha(self, pos_x, pos_y, turno):
        ''' Coloca o establece una ficha en una casilla especifica del tablero.
        Nota: El eje vertical esta invertido y el contador empieza en cero.
        :param posX: Coordenada horizontal de la casilla para establecer la ficha
        :type posX: int
        :param posY: Coordenada vertical de la casilla para establecer la ficha
        :type posY: int
        :param turno: Representa el turno o color de ficha a establecer
        :type turno: bool
        '''
        if turno:
            self.mundo[pos_x][pos_y] = 1
        else:
            self.mundo[pos_x][pos_y] = 2
   
    def cambiar_turno(self):
        ''' Representa el cambio de turno. Normalmente representa la ultima accion del turno '''
        self.turno = not self.turno
        self.numeroDeTurno += 1
        
    def esta_ocupado(self, posX, posY):
        ''' Verifica si en la posicion de una casilla dada existe una ficha (sin importar su color)
        :param posX: Coordenada horizontal de la casilla a verificar
        :type posX: int
        :param posY: Coordenada vertical de la casilla a verificar
        :type posY: int
        :returns: True si hay una ficha de cualquier color en la casilla, false en otro caso
        :rtype: bool
        '''
        return self.mundo[posX][posY] != 0
    
    def cantidad_fichas(self):
        ''' Cuenta la cantidad de fichas en el tablero
        :returns: La cantidad de fichas de ambos jugadores en el tablero como vector donde x = jugador 1, y = jugador 2
        :rtype: PVector 
        '''
        contador = PVector()
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.mundo[i][j] == 1:
                    contador.x = contador.x + 1
                if self.mundo[i][j] == 2:
                    contador.y = contador.y + 1
        return contador
                
    def fichas_rodeadas_aux(self, x, y, sx, sy, turno):
        l = []
        i, j = x, y
        contrario = 2 if turno else 1
        actual = 1 if turno else 2
        while i >= 0 and i < self.dimension and j >= 0 and \
            j < self.dimension and self.mundo[i][j] == contrario:   
            l.append((i,j))
            i += sx
            j += sy
        if i >= 0 and j >= 0 and i < self.dimension and j < self.dimension\
            and not (i == x and j == y) and self.mundo[i][j] == actual:
            return l
        return []
        
    def fichas_rodeadas(self, x, y, turno):
        fichas = []
        fichas += self.fichas_rodeadas_aux(x - 1, y - 1, -1, -1, turno)
        fichas += self.fichas_rodeadas_aux(x - 1, y, -1, 0, turno)
        fichas += self.fichas_rodeadas_aux(x - 1, y + 1, -1, 1, turno)
        fichas += self.fichas_rodeadas_aux(x, y + 1, 0, 1, turno)
        fichas += self.fichas_rodeadas_aux(x + 1, y + 1, 1, 1, turno)
        fichas += self.fichas_rodeadas_aux(x + 1, y, 1, 0, turno)
        fichas += self.fichas_rodeadas_aux(x + 1, y - 1, 1, -1, turno)
        fichas += self.fichas_rodeadas_aux(x, y - 1, 0, -1, turno)
        return set(fichas)
    
    def invertir_fichas(self, fichas, turno):
        actual = 1 if turno else 2
        for x in fichas:
            self.mundo[x[0]][x[1]] = actual
            
    def jugadas_posibles(self, turno):
        l = []
        for x in range(self.dimension):
            for y in range(self.dimension):
                if not self.esta_ocupado(x, y) and \
                    len(self.fichas_rodeadas(x, y, turno)) > 0:
                    l.append((x,y))
        return l
    
    def numero_jugadas_posibles(self, turno):
        return len(self.jugadas_posibles(turno))    
    
    def heuristica_esquinas(self, turno):
        esquina1 = -1
        esquina2 = -1
        esquina3 = -1
        esquina4 = -1
        color = 1 if turno else 2
        
        if self.mundo[0][0] == color:
            esquina1 = 1 #Esquina capturada
        else:
            if self.mundo[2][0] == color or self.mundo[2][2] == color\
                or self.mundo[0][2] == color:
                esquina1 = 0 
        
        if self.mundo[0][7] == color:
            esquina2 = 1
        else:
            if self.mundo[0][5] == color or self.mundo[2][5] == color\
                or self.mundo[2][7] == color:
                esquina2 = 0

        if self.mundo[7][7] == color:
            esquina3 = 1
        else:
            if self.mundo[7][5] == color or self.mundo[5][5] == color\
                or self.mundo[5][7] == color:
                esquina3 = 0

        if self.mundo[7][0] == color:
            esquina4 = 1
        else:
            if self.mundo[5][0] == color or self.mundo[5][2] == color\
                or self.mundo[7][2] == color:
                esquina4 = 0     
        return esquina1 + esquina2 + esquina3 + esquina4
    
    def heuristica_estabilidad(self, turno):
        estable = []
        semiestable = []
        inestable = []
        color = 1 if turno else 2
        esquinas = [(0, 0), (0, 7), (7, 0), (7, 7)]
        
        for esquina in esquinas:
            if esquina == color:
                estable.append(esquina)
        lista_fichas_rodeables = []
        for x in range(self.dimension):
            for y in range(self.dimension):
                if not self.esta_ocupado(x, y):
                    lista_fichas_rodeables.append(\
                        self.fichas_rodeadas(x, y, not turno))
                    
        conjunto_fichas_rodeables = set().union(*lista_fichas_rodeables)
        for x in range(self.dimension):
            for  y in range(self.dimension):
                if self.mundo[x][y] == color and \
                    (x, y) in conjunto_fichas_rodeables:
                    inestable.append((x, y))
                else:
                    semiestable.append((x, y))
        
        return 3 * len(estable) + 2 * len(semiestable) + len(inestable) 
        
                
