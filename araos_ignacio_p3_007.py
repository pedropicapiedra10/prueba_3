import numpy
import os
import msvcrt
import time

lista_ruts = []
lista_nombres = []
lista_nombres_mascotas = []
lista_filas = []
lista_columnas = []

def mostrar_menu():
    os.system('clear')
    print("""MENU
    1. GRABAR
    2. BUSCAR:
    3. RETIRARSE
    4. SALIR""")

def validar_opciones():
    while True:
        try:
            opc=int(input("INGRESE OPCION"))
            if opc in (1,2,3,4):
                return opc
            else:
                print("ERROR! DEBE INGRESAR UN NUMERO ENTERO") 
        except:
            print("ERROR! OPCION INCORRECTA")

def mostrar_hotel_mascota():
    os.system('clear')
print("\t HOTEL MASCOTAS\n")
contador = 1
for x in range(2):
    print(f"casillas para ") ()
    
def validar_rut():
    while True:
        try:
            rut=int(input("INGRESE RUT SIN PUNTOS NI DIGITO VERIFICADOR: "))
            if rut >= 1111111 and  99999999:
                return rut
            else:
                print("ERROR! DEBE INGRESAR ENTRE 7 O 8 DIGITOS")
        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO")

def validar_nombre_dueño():
    while True:
        try:
            nombre_dueño=int("INGRESE NOMBRE DEL DUEÑO")
            if nombre_dueño <= 1 and 333:
                return nombre_dueño
            else:
                print("ERROR! DEBE TENER MINIMO 3 LETRAS")
        except:
            print("ERROR! DEBE INGRESAR ")
#poner identificador unico
 
def validar_nombre_mascota():
    while True:
        try:
            nombre_mascota=int("INGRESE NOMBRE MASCOTA")
            if nombre_mascota <= 1 and 333:
                return nombre_mascota
            else:
                print("ERROR! EL NOMBRE DEBE TENER MINIMO 3 LETRAS")
        except:
            print("ERROR! ")

def validar_cantidad_dias():
    while True:
        try:
            cantidad_dias = int(input("INGRESE CANTIDAD DIAS"))

