''' Proyecto base para el juego de Othello/Reversi 
:author: Rodrigo Colin
'''
from Tablero import *
tablero = Tablero()

def settings():
    ''' Metodo para establecer tamano de ventana al incluir variables '''
    size(tablero.dimension * tablero.tamCasilla, tablero.dimension * tablero.tamCasilla)

def setup():
    ''' Inicializaciones '''
    println("Proyecto base para el juego de mesa Othello")
            
def draw():
    ''' Ciclo de dibujado '''
    tablero.display()

def mousePressed():
    ''' Evento para detectar cuando el usuario da clic '''
    x = mouseX/tablero.tamCasilla
    y = mouseY/tablero.tamCasilla
    print "\nClick en la casilla [%d, %d]" % (x,y)
    fichas = tablero.fichasRodeadas(x, y)
    if not tablero.estaOcupado(x, y) and len(fichas) > 0:
        tablero.setFicha(x, y)
        tablero.invertirFichas(fichas)
        tablero.cambiarTurno()
        print '[Turno # {!s}] {} (Score {!s} - {!s})'.format(tablero.numeroDeTurno, 'jugo ficha blanca' if tablero.turno else 'jugo ficha negra', int(tablero.cantidadFichas().x), int(tablero.cantidadFichas().y))
        posibles = tablero.jugadasPosibles()
        print("Jugadas posibles: %s" % str(posibles))
        if len(posibles) == 0:
            print("No hay jugadas posibles, cambiando de turno")
            tablero.cambiarTurno()
        
