# Classe grafo para representaçao de grafos,
import math
from queue import Queue
import threading
import time
import random


import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem

from Weather import Weather
from Veiculo import *
from Node import Node
from Geografia import Geografia


# Constructor
# Number of edges
# Adjacancy matrix, adjacency list, list of edges

# Methods for adding edges

# Methods for removing edges

# Methods for searching a graph
# BFS, DFS, A*, Greedy


# Other interesting methods


class Graph:
    # def __init__(self, num_of_nodes, directed=False):
    def __init__(self, directed=False):
        self.m_nodes = []  
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para posterirmente armazenar as heuristicas para cada nodo -> pesquisa informada

    #############
    #    escrever o grafo como string
    #############
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    ################################
    #   encontrar nodo pelo nome
    ################################

    def get_node_by_name(self, name):
        search_node = Node(name)
        for node in self.m_nodes:
            if node == search_node:
                return node
          
        return None

    ################################
    #   imprimir arestas
    ################################

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo,peso,geo,met) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + " Geo: " + geo.value + " Met: " + met.name + "\n"
        return listaA

    ################
    #   adicionar   aresta no grafo
    ######################

    def add_edge(self, node1, node2, weight, geografia):
        if not isinstance(geografia, Geografia):
            raise ValueError("geografia must be an instance of Geografia Enum")

        n1 = Node(node1)
        n2 = Node(node2)
        if n1 not in self.m_nodes:
            n1_id = len(self.m_nodes)  # numeração sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []
        else:
            n1 = self.get_node_by_name(node1)

        if n2 not in self.m_nodes:
            n2_id = len(self.m_nodes)  # numeração sequencial
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []
        else:
            n2 = self.get_node_by_name(node2)

        weather = random.choices(
            [Weather.CLEAR, Weather.RAIN, Weather.STORM,Weather.BLOCKED],
            weights=[50, 30, 15,5],
            k=1
        )[0]
        weather_multiplier = weather.value
        total_cost = weight * weather_multiplier        
        total_cost = int(total_cost)
        self.m_graph[node1].append((node2, total_cost, weight, geografia,weather)) 

        if not self.m_directed:
            self.m_graph[node2].append((node1, total_cost, weight, geografia,weather))

    #############################
    # devolver nodos
    ##########################

    def getNodes(self):
        return self.m_nodes

    #######################
    #    devolver o custo de uma aresta
    #######################

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo,custo,weight,geografia,meteorologia) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    ##############################
    #  dado um caminho calcula o seu custo
    ###############################

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

    ################################################################################
    #     procura DFS->com restricoes de veiculo
    ####################################################################################

    def procura_DFS(self,start,end,veiculo, path=[], visited=set()):
    
        path.append(start)
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, total_cost, weight, geografia,meteorologia) in self.m_graph[start]:
            if adjacente not in visited and self.pode_atravessar(veiculo,geografia,meteorologia):
                resultado = self.procura_DFS(adjacente,end,veiculo, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho
        return None

    #####################################################
    # Procura BFS->com restricoes de veiculo
    ######################################################

    def procura_BFS(self, start,end,veiculo):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, total_cost, weight, geografia, meteorologia) in self.m_graph[nodo_atual]:
                    if adjacente not in visited and self.pode_atravessar(veiculo,geografia,meteorologia):
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        # reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)

    ####################
    # funçãop  getneighbours, devolve vizinhos de um nó
    ##############################

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, total_cost, weight, geografia,met) in self.m_graph[nodo]:
            lista.append((adjacente, total_cost, weight, geografia,met))
        return lista

    ###########################
    # desenha grafo  modo grafico
    #########################

    def desenha(self):
        ##criar lista de vertices
        lista_v = self.m_nodes
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso,weight,geografia,met) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    ####################################33
    #    add_heuristica   -> define heuristica para cada nodo 1 por defeito....
    ################################3

    def add_heuristica(self, n, estima): #posso dar so o no,e as cidades,ele vai as cidades e calcula a heuristica com base nos atributos da cidade
        n1 = Node(n)
        if n1 in self.m_nodes:
            self.m_h[n] = estima

    ##########################################
    #    A*
    ##########################################

    def procura_aStar(self, start, end,veiculo):
        # open_list é uma lista de nós que foram visitados, mas cujos vizinhos não foram inspeccionados, começa com o nó inicial
        # closed_list é uma lista de nós que foram visitados e cujos os vizinhos foram inspeccionados
        open_list = {start}
        closed_list = set([])

        # g contém as distâncias atuais de start_node para todos os outros nós
        g = {}  

        g[start] = 0

        # parents contém um mapa de adjacência de todos os nós
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # encontrar um nó com o valor mais baixo de f() - função de avaliação
            for v in open_list:
                if n == None or g[v] + self.getH(v) < g[n] + self.getH(n):  
                    n = v
            if n == None:
                print('Path does not exist!')
                return None

            # se o nó atual for o stop_node, então começamos a reconstruir o caminho do mesmo até ao start_node
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))

            # para todos os vizinhos do nó atual
            for (m, total_cost,weight, geografia,met) in self.getNeighbours(n):  
                # se o nó atual não estiver em open_list e closed_list, adicione-se a open_list 
               if self.pode_atravessar(veiculo,geografia,met):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + total_cost

                else:
                    if g[m] > g[n] + total_cost:
                        g[m] = g[n] + total_cost
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remova n da open_list e adicione-o close_list porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

    ###################################3
    # devolve heuristica do nodo
    ####################################

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])


    ##########################################
    #   Greedy
    ##########################################


    def greedy(self, start, end,veiculo):
        
        open_list = set([start])
        closed_list = set([])

        # parents é um dicionário que mantém o antecessor de um nodo
        # começa com start
        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            # encontra nodo com a menor heuristica
            for v in open_list:
                if n == None or self.m_h[v] < self.m_h[n]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # se o nodo corrente é o destino
            # reconstruir o caminho a partir desse nodo até ao start
            # seguindo o antecessor
            if n == end:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()

                return (reconst_path, self.calcula_custo(reconst_path))
            # para todos os vizinhos  do nodo corrente
            
            for (m, total_cost, weight, geografia, met) in self.getNeighbours(n):
                # Se o nodo corrente nao esta na open nem na closed list
                # adiciona-lo à open_list e marcar o antecessor
             if self.pode_atravessar(veiculo,geografia,met):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n


            # remover n da open_list e adiciona-lo à closed_list
            # porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None



    ##########################################
    #   Escolhe a melhor algoritmo
    ##########################################
    def melhor_algoritmo(self,end,veiculo):
        start=veiculo.local
        #BFS    
        (bfs_path,bfs_cost) = self.procura_BFS(start,end,veiculo)
        #DFS
        dfs_result = self.procura_DFS(start, end,veiculo)
        if dfs_result is None:
            dfs_path, dfs_cost = [], float('inf')
        else:
            dfs_path, dfs_cost = dfs_result
        #A*
        a_star_result = self.procura_aStar(start, end,veiculo)
        if a_star_result is None:
            a_star_path, a_star_cost = [], float('inf')
        else:
            a_star_path, a_star_cost = a_star_result
        #greedy
        greedy_result = self.greedy(start, end,veiculo)
        if greedy_result is None:
            greedy_path, greedy_cost = [], float('inf')
        else:
            greedy_path, greedy_cost = greedy_result
        #escolher o melhor algoritmo
        if min(bfs_cost, dfs_cost, a_star_cost) == bfs_cost:
            return (bfs_path, bfs_cost)
        elif min(bfs_cost, dfs_cost, a_star_cost) == dfs_cost:
            return (dfs_path, dfs_cost)
        else:
            return (a_star_path, a_star_cost)



    ##########################################
    #   Escolhe o melhor veiculo
    ##########################################
    def melhor_veiculo(self, veiculos, cidade):
        (melhor_caminho, melhor_custo, melhor_veiculo) = ([], float('inf'), None)
        for veiculo in veiculos:

            (caminho, custo) = self.melhor_algoritmo(cidade,veiculo)
            

            if(custo>veiculo.km_atual or veiculo.carga_transportada==0):#se o veiculo nao tiver combustivel suficiente nao avanca
                continue

            if custo < melhor_custo:
                melhor_caminho = caminho
                melhor_custo = custo
                melhor_veiculo = veiculo

        if melhor_veiculo:
            melhor_veiculo.local = cidade
            melhor_veiculo.km_atual -= melhor_custo

            for i in range(len(veiculos)):
                if veiculos[i].id == melhor_veiculo.id:
                    veiculos[i] = melhor_veiculo
                    break
        return melhor_caminho, melhor_custo, melhor_veiculo


    ##########################################
    #   Escolhe o melhor caminho
    ##########################################
    def melhor_caminho(self, cidades, veiculos):
     caminho = []
     custo = 0
     while(cidades and veiculos_sem_carga(veiculos)):
        for cidade in cidades:
            if cidade.necessidades==0:
                cidades.remove(cidade)
                continue
            
            path, cost, veiculo = self.melhor_veiculo(veiculos, cidade.nome)
            
            if veiculo is None:
                continue
            deposito=veiculo.depositar(cidade.necessidades)
            cidade.decrementa_necessidades(deposito)
            
            if cidade.verifica_necessidades==0:
                cidades.remove(cidade)
            caminho.append((path, veiculo.id,veiculo.km_atual,veiculo.carga_transportada))
            custo += cost
            custo_cidade=self.calcula_custo_com_risco(path, cidades)
            custo+=custo_cidade

        
     return self.organiza_caminho_por_veiculo(caminho, custo)

    def calcula_custo_com_risco(self, caminho, cidades):
                    custo = self.calcula_custo(caminho)
                    for cidade_nome in caminho:
                        cidade = next((c for c in cidades if c.nome == cidade_nome), None)
                        if cidade and cidade.nivel_risco > 0:
                            custo += cidade.nivel_risco * 20
                    return custo

    ##########################################
    #   Organiza caminho por tipo de veiculo
    ##########################################
    def organiza_caminho_por_veiculo(self, caminho, custo):
        veiculos = {}
        for (path, id, km_atual, carga_transportada) in caminho:
            if id not in veiculos:
                veiculos[id] = []
            veiculos[id].append((path, km_atual, carga_transportada))
        return veiculos, custo

    ##########################################################################
    #   Update edge weights
    ##########################################################################
    def update_edge_weights(self):
        while True:
            for node1 in self.m_graph:
                for i, (node2, _, weight,g,met) in enumerate(self.m_graph[node1]):
                    met_new = random.choices([Weather.CLEAR, Weather.RAIN, Weather.STORM],weights=[50, 35, 15],k=1)[0]
                    weather_multiplier = met_new.value
                    total_cost = weight * weather_multiplier
                    total_cost = int(total_cost)
                    self.m_graph[node1][i] = (node2, total_cost,weight,g,met_new)
                    if not self.m_directed:
                        for j, (n1, _,peso,geo,met) in enumerate(self.m_graph[node2]):
                            if n1 == node1:
                                self.m_graph[node2][j] = (node1, total_cost,peso,geo,met_new)
                                break
            print("Updated edge weights")
            time.sleep(20)


    def start_updating_weights(self):
        thread = threading.Thread(target=self.update_edge_weights)
        thread.daemon = True
        thread.start()

    #################################
    #   Verifica se um veículo pode atravessar uma aresta
    #################################
    def pode_atravessar(self,veiculo,geografia,meteorologia):
        if veiculo.tipo == "Carro" or veiculo.tipo == "Carrinha" or veiculo.tipo == "Camiao":
            if geografia == Geografia.RIO:
                return False
        if veiculo.tipo=="Helicoptero":
            if meteorologia == Weather.STORM:
                return False
        if meteorologia == Weather.BLOCKED:
            return False
        return True

    
    #########################
    # Heuristica
    #########################

    def calcula_heuristica(self,cidade):
        return cidade.nivel_risco*20

    def remove_heuristica(self, n):
        if n in self.m_h:
            del self.m_h[n]
    
    def update_heuristica(self, cidades):
        while True:
            for cidade in cidades:
                new_heuristica = self.calcula_heuristica(cidade)
                self.add_heuristica(cidade.nome, new_heuristica)
            time.sleep(1)
    
        
    def start_updating_heuristica(self, cidades):
        thread = threading.Thread(target=self.update_heuristica, args=(cidades,))
        thread.daemon = True
        thread.start()

    #########################
    # Risco
    #########################
    def update_risco(self, cidades):
        while True:
            for cidade in cidades:
                cidade.calcula_risco()

    def start_updating_risco(self, cidades):
        thread = threading.Thread(target=self.update_risco, args=(cidades,))
        thread.daemon = True
        thread.start()