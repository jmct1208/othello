''' Proyecto base para el juego de Othello/Reversi 
:author: Rodrigo Colin
'''
from Othello import *
import Busqueda as b
juego = Othello()
estado_actual = juego.inicial
accion_humano = False
accion_computadora = False
termino_dibujarse = False

def settings():
    ''' Metodo para establecer tamano de ventana al incluir variables '''
    size(estado_actual.tablero.dimension * estado_actual.tablero.tam_casilla,
         estado_actual.tablero.dimension * estado_actual.tablero.tam_casilla)

def setup():
    ''' Inicializaciones '''
    println("Proyecto base para el juego de mesa Othello")
    print("------------------------------------------------")
    estado_actual.display()

def draw():
    global estado_actual
    global termino_dibujarse
    ''' Ciclo de dibujado '''
    estado_actual.tablero.display()
    if not juego.terminal_test(estado_actual) and not estado_actual.turno and termino_dibujarse:
        accion_computadora = b.alphabeta_cutoff_search(estado_actual, juego)
        print("------------------------------------------------")
        print("Accion computadora: %s" % str(accion_computadora))
        estado_actual = juego.resultado(estado_actual, accion_computadora)
        print("------------------------------------------------")
        estado_actual.display()
    if juego.terminal_test(estado_actual):
        fichas_en_tablero = estado_actual.tablero.cantidad_fichas()
        fichas_negras = int(fichas_en_tablero.x)
        fichas_blancas = int(fichas_en_tablero.y)
        c_fichas_negras = len(fichas_negras)
        c_fichas_blancas = len(fichas_blancas)

        if c_fichas_negras < fichas_blancas:
            print("Ganó la computadora")
        elif c_fichas_negras > fichas_blancas:
            print("Ganó el humano")
        else:
            print("Empate")
    termino_dibujarse = True


def mousePressed():
    global estado_actual
    global accion_humano
    global termino_dibujarse
    termino_dibujarse = False
    if juego.terminal_test(estado_actual):
        print("El juego ha terminado.")
    else:
        if estado_actual.turno:
            x = mouseX / estado_actual.tablero.tam_casilla
            y = mouseY / estado_actual.tablero.tam_casilla
            print "Click en la casilla [%d, %d]" % (x, y)
            if len(estado_actual.movimientos) > 0:
                if (x, y) in estado_actual.movimientos:
                    accion_humano = (x, y)
                else:
                    print("Movimiento no valido.")
                    return
            elif len(estado_actual.movimientos) == 0:
                accion_humano = None
            else:
                return
            print("------------------------------------------------")
            print("Accion humano: %s" % str(accion_humano))
            estado_actual = juego.resultado(estado_actual, accion_humano)
            print("------------------------------------------------")
            estado_actual.display()
        else:
            print("No es tu turno")
