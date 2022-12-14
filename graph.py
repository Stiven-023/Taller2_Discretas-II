""" Una clase para representar grafos """

class Graph(object):

    def __init__(self, a_graph=None):
        """Inicializa el objeto Graph"""
        if not(a_graph):
            a_graph = {}
        self.graph = a_graph
    

    def set_type(self, a_type):
        """
        """
        GTYPE = {
            "GNMA":"Grafo no dirigido - Matriz de Adyacencia",
            "GNLA":"Grafo no dirigido - Lista de Adyacencia",
            "GNMI":"Grafo no dirigido - Matriz de Incidencia",
            "GDMA":"Grafo dirigido - Matriz de Adyacencia",
            "GDLA":"Grafo dirigido - Lista de Adyacencia",
            "GDMI":"Grafo dirigido - Matriz de Incidencia",
            "GPMA":"Grafo ponderado - Matriz de Adyacencia",
            "GPLA":"Grafo ponderado - Lista de Adyacencia",
            "GPMI":"Grafo ponderado - Matriz de Incidencia",
            "NNNN":"Grafo no identificado",
        }
        
        print(GTYPE.get(a_type))

        if not(a_type in GTYPE):
            self.gtype = GTYPE["NNNN"]
            self.type = "NNNN"
        self.gtype = GTYPE[a_type]
        self.type = a_type
        

    def parse(self, lines=[]):
        if self.type == "GNMA":
            for id, line in enumerate(lines): ## se obtiene el id del vertice
                self.add_vertex(id) ## se agregan todos los vertice al grafo
                for adjacent in line.split(" "): ## se obtienen los 1 de la MA
                    if adjacent == 1: ## se crea una arista donde es 1
                        self.add_vertex(adjacent) ## se agrega el vertice
                        self.add_edge(id, adjacent)
    
        if self.type == "GNLA":
                for id in range(len(lines)):
                    self.add_vertex(id) ## se agregan todos los vertice al grafo
                for id, line in enumerate(lines): ## Se obtiene el id del vertice
                    for link in line.split(" "): ## se obtiene la lista de enlaces
                        self.add_edge(id, link) ## se crea una arista entre el id y su adyacente

        if self.type == "GNMI":
            for id in range(len(lines)):
                self.add_vertex(id) ## se agregan todos los vertice al grafo
            

    def edges(self, vertex):
        """
        retorna las aristas vinculadas al vertice (vertex)
        param: vertex
        """
        return self.graph[vertex]

    def all_vertex(self):
        """
        retorna todas los vertices
        """
        return self.graph.keys()

    def add_vertex(self, vertex):
        """
        Agrega un vertice al grafo
        param: vertex
        """
        if not(vertex in self.graph):
            self.graph[vertex] = []
    
    def add_edge(self, start, end):
        adj = self.graph[start] ## se lee los vertices adyacentes
        adj.append(end) ### Se agrega un nuevo adyacente
        self.graph[start] = adj ### se asigna la nueva lista de adyacentes

