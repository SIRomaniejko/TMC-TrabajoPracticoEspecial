
import random

cuartil = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cuartilNave = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def insertarNave(perdidas, nave):
    iterar = 0
    esInsertado = False
    while iterar < 10 and esInsertado == False:
        if cuartil[iterar] < perdidas:
            pushRight(iterar)
            cuartil[iterar] = perdidas
            cuartilNave[iterar] = nave
            esInsertado = True
        iterar = iterar + 1

def probabilidadNave(nave_p):
    iteracionMK5 = 0
    naves = 0
    probabilidad = 0
    while iteracionMK5 < 10:
        if cuartilNave[iteracionMK5] == nave_p:
            naves = naves + 1
        iteracionMK5 = iteracionMK5 + 1
    if nave_p == "a":
        probabilidad = naves/10
    else:
        probabilidad = naves/15
    # print(probabilidad)
    return probabilidad

def enunciado1(probabilidad):
    iteracion = 0
    perdidasTotal = 0
    probabilidadIngresada = probabilidad
    while iteracion < 12: 
        perdida = 0
        perdidaMax = 0
        iteracion2 = 0
        while iteracion2 < 300:
            if random.random() < probabilidad:
                perdida = perdida + 1
            else:
                perdida = 0
            if perdida > perdidaMax:
                perdidaMax = perdida
            iteracion2 = iteracion2 + 1
        perdidasTotal = perdidasTotal + perdidaMax
        iteracion = iteracion + 1
    return perdidasTotal/12

def enunciado3(epsilon):
    print("probabilidad de despido nave c")
    print(probabilidadNaveC(epsilon))
    print("cuartil a despedir en la ultima prueba")
    printCuartil()


def enunciado2():
    print(probabilidadNaveC(0.25))
    print(probabilidadNaveC(0.1))
    print(probabilidadNaveC(0.001))
    
def probabilidadNaveC(epsilon):
    probabilidad = 0
    probabilidadAnterior = 0
    pruebas = 0
    naves = 0
    while epsilon < abs(probabilidad - probabilidadAnterior) or pruebas < 10:
        probabilidadAnterior = probabilidad
        limpiar()
        todo()
        naves = naves + probabilidadNave("c")
        pruebas = pruebas + 1
        probabilidad = naves/pruebas
    return probabilidad
        

def pushRight(pos):
    iteracionMK4 = 9
    while iteracionMK4 > pos:
        cuartil[iteracionMK4] = cuartil[iteracionMK4-1]
        cuartilNave[iteracionMK4] = cuartilNave[iteracionMK4-1]
        iteracionMK4 = iteracionMK4 - 1

def limpiar():
    iteracionPlusUltra = 0
    while iteracionPlusUltra < 9:
        cuartil[iteracionPlusUltra] = 0
        cuartilNave[iteracionPlusUltra] = 0
        iteracionPlusUltra = iteracionPlusUltra + 1


def todo():
    naveA()
    naveB()
    naveC()

def naveA():
    iteracion = 0
    while iteracion < 10: 
        perdida = 0
        perdidaMax = 0
        iteracion2 = 0
        while iteracion2 < 300:
            if random.random() < 0.1:

                perdida = perdida + 1
            else:
                perdida = 0
            if perdida > perdidaMax:
                perdidaMax = perdida
            iteracion2 = iteracion2 + 1
        insertarNave(perdidaMax, "a")
        iteracion = iteracion + 1

def naveB():
    iteracion = 0
    while iteracion < 15:
        perdida = 0
        perdidaMax = 0
        iteracion2 = 0
        while iteracion2 < 300:
            if random.random() < 0.05:
                perdida = perdida + 1
            else:
                perdida = 0
            if perdida > perdidaMax:
                perdidaMax = perdida
            iteracion2 = iteracion2 + 1
        insertarNave(perdidaMax, "b")
        iteracion = iteracion + 1

def naveC():
    iteracion = 0
    while iteracion < 15:
        perdida = 0
        perdidaMax = 0
        iteracion2 = 0
        while iteracion2 < 300:
            if random.random() < 0.1:
                perdida = perdida + 1
            else:
                perdida = 0
            if perdida > perdidaMax:
                perdidaMax = perdida
            iteracion2 = iteracion2 + 1
        insertarNave(perdidaMax, "c")
        iteracion = iteracion + 1

def printCuartil():
    iterarV3 = 0
    while iterarV3 < 10:
        print(cuartil[iterarV3])
        print(cuartilNave[iterarV3])
        iterarV3 = iterarV3 + 1


    