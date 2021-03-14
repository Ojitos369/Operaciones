#-----------  IMPORTACIONES ----------------
from time import sleep
from src.menus import pausar, limpiar
import src.menus as menus
from src.operaciones import main as operaciones

#-----------  FUNCIONES ----------------

def main():
    mostrar_menu = True
    hay_funcion = True
    no_decimales = 5
    funcion = '4^2+(3*6)-25/5'
    while mostrar_menu:
        opc = menus.principal()
        if opc != 4:
            if opc == 1:
                hay_funcion, funcion = menus.pedir_funcion()
            elif opc == 2:
                if hay_funcion:
                    limpiar()
                    resultado = operaciones(funcion)
                    resultado = round(resultado,no_decimales)
                    print(f'El resultado de {funcion} es: {resultado}')
                    pausar()
                else:
                    print('Porfavor Ingresa primero una funcion')
                    pausar()
            elif opc == 3:
                texto = '''Ingresa el nivel de decimales (Por defecto 5): '''
                no_decimales = menus.aproximacion(texto)
        else:
            mostrar_menu = False
            print('Adios')
            sleep(.5)

#-----------  MAIN ----------------

if __name__ == "__main__":
    main()