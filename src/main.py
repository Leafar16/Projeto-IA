from Graph import Graph
from Node import Node
from Cidades import *
from Veiculo import *
from Geografia import *
import copy


def main():

    # Definir as cidades
    Ancora = Cidade("Ancora", 2, 400, 1000, 200, 0)
    Pte_Lima = Cidade("Pte Lima", 1, 100, 2000, 10, 0)
    Braga = Cidade("Braga", 0, 0, 3000, 0, 0)
    P_Lanhoso = Cidade("P Lanhoso", 3, 1000, 1500, 500, 0)
    Barcelos = Cidade("Barcelos", 0, 0, 2500, 0, 0)
    Esposende = Cidade("Esposende", 2, 300, 1200, 150, 0)
    Famalicao = Cidade("Famalicao", 0, 0, 2200, 0, 0)
    Guimaraes = Cidade("Guimaraes", 1, 270, 2700, 135, 0)
    Viana_do_Castelo = Cidade("Viana do Castelo", 3, 1500, 1800, 750, 0)
    Povoa_de_Varzim = Cidade("Povoa de Varzim", 0, 0, 2000, 0, 0)
    Santo_Tirso = Cidade("Santo Tirso", 2, 500, 1500, 600, 0)
    Amarante = Cidade("Amarante", 1, 200, 1000, 350, 0)
    Maia = Cidade("Maia", 0, 0, 3000, 0, 0)
    Lousada = Cidade("Lousada", 3, 1000, 1500, 500, 0)
    Marco_de_Canaveses = Cidade("Marco de Canaveses", 0, 0, 2500, 0, 0)
    Porto = Cidade("Porto", 2, 300, 1200, 150, 0)
    Santa_Maria_da_Feira = Cidade("Santa Maria da Feira", 0, 0, 2200, 0, 0)
    Ovar = Cidade("Ovar", 1, 270, 2700, 135, 0)

    cidades=[Ancora, Pte_Lima, Braga, P_Lanhoso, Barcelos, 
    Esposende, Famalicao, Guimaraes, Viana_do_Castelo, 
    Povoa_de_Varzim, Santo_Tirso, Amarante, Maia, Lousada, 
    Marco_de_Canaveses, Porto, Santa_Maria_da_Feira, Ovar]

    cidades = organiza_cidades(cidades) #organiza as cidades por nivel de risco

    # Definir os veiculos
    Carro=Veiculo("Carro1","Braga","Carro",1000,1000,1000,1000,90)
    Carrinha=Veiculo("Carrinha1","Braga","Carrinha",2000,2000,2000,2000,70)
    Camiao=Veiculo("Camiao1","Braga","Camiao",5000,5000,5000,5000,60)
    Helicoptero=Veiculo("Helicoptero1","Braga","Helicoptero",1500,1500,1500,1500,100)

    veiculos=[Carro,Carrinha,Camiao]
    
    #definir o grafo
    graph = Graph(directed=False)
    graph.start_updating_weights()

    graph.add_edge("Povoa de Varzim", "Maia", 32, Geografia.PLANICIE)
    graph.add_edge("Maia", "Santo Tirso", 23, Geografia.PLANICIE)
    graph.add_edge("Santo Tirso", "Lousada", 32, Geografia.MONTANHA)
    graph.add_edge("Lousada", "Amarante", 27, Geografia.MONTANHA)
    graph.add_edge("Lousada", "Marco de Canaveses", 21, Geografia.RIO)
    graph.add_edge("Maia", "Porto", 11, Geografia.PLANICIE)
    graph.add_edge("Porto", "Santa Maria da Feira", 34, Geografia.PLANICIE)
    graph.add_edge("Santa Maria da Feira", "Ovar", 11, Geografia.PLANICIE)
    graph.add_edge("Ancora", "Viana do Castelo", 10, Geografia.PLANICIE)
    graph.add_edge("Viana do Castelo", "Pte Lima", 5, Geografia.RIO)
    graph.add_edge("Viana do Castelo", "Esposende", 15, Geografia.PLANICIE)
    graph.add_edge("Pte Lima", "Braga", 5, Geografia.MONTANHA)
    graph.add_edge("Braga", "P Lanhoso", 10, Geografia.MONTANHA)
    graph.add_edge("Braga", "Barcelos", 15, Geografia.RIO)
    graph.add_edge("Braga", "Guimaraes", 10, Geografia.PLANICIE)
    graph.add_edge("Guimaraes", "Famalicao", 5, Geografia.PLANICIE)
    graph.add_edge("Barcelos", "Esposende", 5, Geografia.PLANICIE)
    graph.add_edge("Braga", "Famalicao", 10, Geografia.PLANICIE)
    graph.add_edge("Esposende", "Povoa de Varzim", 15, Geografia.PLANICIE)
    graph.add_edge("Santo Tirso", "Famalicao", 10, Geografia.PLANICIE)
    graph.add_edge("Amarante", "Marco de Canaveses", 10, Geografia.RIO)
    graph.add_edge("Guimaraes", "Amarante", 25, Geografia.MONTANHA)

    #definir heuristica
    #graph.add_heuristica("Povoa de Varzim",calcula_heuristica("Povoa de Varzim",cidades))

    #menu
    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir  nodos de Grafo")
        print("4-Imprimir arestas de Grafo")
        print("5-DFS")
        print("6-BFS")
        print("7-A*")
        print("8-Gulosa")
        print("9-Melhor Algoritmo")
        print("10-Melhor Caminho")
        print("11-Melhor Caminho com veiculo")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("saindo.......")
        elif saida == 1:
            print(graph.m_graph)
            l = input("prima enter para continuar")
        elif saida == 2:
            graph.desenha()
        elif saida == 3:
            print(graph.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(graph.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            Helicoptero2 = copy.deepcopy(Helicoptero)
            print(graph.procura_DFS(inicio,fim,Helicoptero2, path=[], visited=set()))
            l = input("prima enter para continuar")
        elif saida == 6:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(graph.procura_BFS(inicio,fim,Carro))
            print(Carro.local)
            l = input("prima enter para continuar")
        elif saida == 7:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(graph.procura_aStar(inicio, fim,Carro))
            l = input("prima enter para continuar")
        elif saida == 8:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(graph.greedy(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 9:
            fim = input("Nodo final->")
            print(graph.melhor_algoritmo(fim,Carro))
            l = input("prima enter para continuar")
        elif saida == 10:
            veiculos_new = copy.deepcopy(veiculos)
            cidades_new = copy.deepcopy(cidades)
            (caminho, custo) = graph.melhor_caminho(cidades_new, veiculos_new)
            
            for tipo_veiculo, detalhes in caminho.items(): #imprimir os caminhos de cada veiculo
                print(f"Veiculo: {tipo_veiculo}")
                for detalhe in detalhes:
                    print(f"Caminho: {detalhe[0]}, KM Atual: {detalhe[1]}, Carga Transportada: {detalhe[2]}")
                print("\n")
            print(f"Custo Total: {custo}")

            l = input("prima enter para continuar")
        elif saida == 11:
            fim = input("Nodo final->")
            veiculos_new = copy.deepcopy(veiculos)
            print(graph.melhor_veiculo(veiculos,fim))
            l = input("prima enter para continuar")
        else:
            print("you didn't add anything")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()
