# main.py

import csv
from arbol_b import ArbolB
from graficador import GraficadorArbolB

def cargar_csv(arbol, archivo):

    with open(archivo, newline='') as csvfile:

        lector = csv.reader(csvfile)

        for fila in lector:

            try:
                dato = int(fila[0])
                arbol.insertar(dato)

            except:
                pass

def menu():

    grado = int(input("Ingrese el grado del Árbol B: "))

    arbol = ArbolB(grado)

    while True:

        print("\n--- MENU ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar CSV")
        print("5. Mostrar")
        print("6. Graficar")
        print("7. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":

            dato = int(input("Dato: "))
            arbol.insertar(dato)

        elif opcion == "2":

            dato = int(input("Dato: "))

            if arbol.buscar(dato):
                print("Dato encontrado")
            else:
                print("Dato no encontrado")

        elif opcion == "3":

            dato = int(input("Dato: "))

            if arbol.eliminar(dato):
                print("Dato eliminado")
            else:
                print("Dato no existe")

        elif opcion == "4":

            archivo = input("Ruta CSV: ")
            cargar_csv(arbol, archivo)

        elif opcion == "5":

            arbol.mostrar()

        elif opcion == "6":

            grafo = GraficadorArbolB(arbol)
            grafo.graficar()

        elif opcion == "7":
            break

menu()