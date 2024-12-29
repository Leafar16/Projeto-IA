import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

from Node import Node




class Grafo:
    def __init__(self, directed=False):
        self.m_nodes = []  
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas


    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
            return out


    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
            else:
                return None


    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA


    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if (n1 not in self.m_nodes):
            n1_id = len(self.m_nodes)  # numeração sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []

        

        if (n2 not in self.m_nodes):
            n2_id = len(self.m_nodes)  # numeração sequencial
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []
        

        self.m_graph[node1].append((node2, weight))  


    def getNodes(self):
        return self.m_nodes


    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT


    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            #print(teste[i])
            i = i + 1
        return custo

   
    def procura_DFS(self, start, end, path=None, visited=None):
     if path is None:
            path = []
     if visited is None:
            visited = set() #marca o nodo como visitado

     path.append(start)
     visited.add(start)
    
     if(start==end): #se for um nodo que corresponde ao nodo desejado
        custoT=self.calcula_custo(path) #calcula o custo total
        return (path,custoT)
    #else
     for(adjacente,peso) in self.m_graph[start]:
        if adjacente not in visited:
            resultado=self.procura_DFS(adjacente,end,path,visited)
            if resultado is not None:
                return resultado
     
     path.pop()
     return None
    
    
    def procura_BFS(self, start, end):
        # Initialize the queue, visited set, and path list
            queue=[]
            visited=set()
            path=[]
            parent = {start: None}  # Dictionary to store parent pointers

            path.append(start)
            visited.add(start)
            
            if(start==end): #se for um nodo que corresponde ao nodo desejado
                 custoT=self.calcula_custo(path) #calcula o custo total
                 return (path,custoT)

            queue.append(start)

            while queue:
                m=queue.pop(0)
                #visited.add(m)

                for (adjacente,peso) in self.m_graph[m]:
                    if(adjacente not in visited):
                     visited.add(adjacente)
                     queue.append(adjacente)

                    if adjacente==end:
                            path.append(adjacente)
                            custoT=self.calcula_custo(path) #calcula o custo total
                            return (path,custoT)
            
            path.pop()
            return(path,0)
            



    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

   





