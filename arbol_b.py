# arbol_b.py

from nodo_b import NodoB

class ArbolB:
    def __init__(self, grado):
        self.raiz = NodoB(True)
        self.grado = grado

    def buscar(self, dato, nodo=None):

        if nodo is None:
            nodo = self.raiz

        i = 0

        while i < len(nodo.claves) and dato > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and dato == nodo.claves[i]:
            return True

        if nodo.hoja:
            return False

        return self.buscar(dato, nodo.hijos[i])

    def insertar(self, dato):

        raiz = self.raiz

        if len(raiz.claves) == (2 * self.grado) - 1:

            nueva_raiz = NodoB(False)
            nueva_raiz.hijos.append(self.raiz)

            self.dividir_hijo(nueva_raiz, 0)

            i = 0

            if nueva_raiz.claves[0] < dato:
                i += 1

            self.insertar_no_lleno(nueva_raiz.hijos[i], dato)

            self.raiz = nueva_raiz

        else:
            self.insertar_no_lleno(raiz, dato)

    def insertar_no_lleno(self, nodo, dato):

        i = len(nodo.claves) - 1

        if nodo.hoja:

            nodo.claves.append(None)

            while i >= 0 and dato < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1

            nodo.claves[i + 1] = dato

        else:

            while i >= 0 and dato < nodo.claves[i]:
                i -= 1

            i += 1

            if len(nodo.hijos[i].claves) == (2 * self.grado) - 1:

                self.dividir_hijo(nodo, i)

                if dato > nodo.claves[i]:
                    i += 1

            self.insertar_no_lleno(nodo.hijos[i], dato)

    def dividir_hijo(self, padre, i):

        grado = self.grado

        y = padre.hijos[i]
        z = NodoB(y.hoja)

        padre.hijos.insert(i + 1, z)
        padre.claves.insert(i, y.claves[grado - 1])

        z.claves = y.claves[grado:(2 * grado) - 1]
        y.claves = y.claves[0:grado - 1]

        if not y.hoja:
            z.hijos = y.hijos[grado:(2 * grado)]
            y.hijos = y.hijos[0:grado]

    def eliminar(self, dato, nodo=None):

        if nodo is None:
            nodo = self.raiz

        if dato in nodo.claves:
            nodo.claves.remove(dato)
            return True

        if nodo.hoja:
            return False

        i = 0

        while i < len(nodo.claves) and dato > nodo.claves[i]:
            i += 1

        return self.eliminar(dato, nodo.hijos[i])

    def mostrar(self, nodo=None, nivel=0):

        if nodo is None:
            nodo = self.raiz

        print("Nivel", nivel, ":", nodo.claves)

        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)