#-----------  IMPORTACIONES ----------------
from src.extras import pausar,limpiar, convertir
from src.operaciones import validarFuncion
#-----------  FUNCIONES ----------------
def principal():
    incorrecto = True
    while incorrecto:
        limpiar()
        print('https://github.com/Ojitos369/operaciones.git')
        opc = input('''1.- Introducir ecuación
2.- Resolver
3.- Configurar numero de decimales
4.- Salir
Elige una opción: ''')
        opc = convertir(opc)
        if opc < 5 or opc > 0:
            incorrecto = False
        else:
            print('Opcion no valida. Intenta nuevamente. ')
            pausar()
    return opc

def pedir_funcion():
    permitidos = '/*0123456789+-^()'
    opc = ''
    incorrecto = True
    while incorrecto:
        incorrecto = False
        limpiar()
        opc = input('''Ingresa la operacion, ejemplo: 4^2+(3*6)-25/5\n''')
        
        for i in range (len(opc)):
            if opc[i] in permitidos:
                pass
            else:
                incorrecto = True
        #incorrecto = validarFuncion(opc)
        if incorrecto:
            print('No puedo resolver esa función de momento. Intenta con otra')
            pausar()
    return [True, opc]