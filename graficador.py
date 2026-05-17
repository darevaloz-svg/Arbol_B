from graphviz import Digraph

class GraficadorArbolB:

    def __init__(self, arbol):
        self.arbol = arbol
        self.grafo = Digraph()
        self.contador = 0

    def graficar(self):
        self._graficar_nodo(self.arbol.raiz)
        self.grafo.render('imagenes/arbol', format='png', cleanup=True)
        print("Imagen generada en imagenes/arbol.png")

    def _graficar_nodo(self, nodo):
        id_actual = str(self.contador)
        self.contador += 1

        etiqueta = " | ".join(map(str, nodo.claves))
        self.grafo.node(id_actual, etiqueta)

        for hijo in nodo.hijos:
            id_hijo = self._graficar_nodo(hijo)
            self.grafo.edge(id_actual, id_hijo)

        return id_actual
