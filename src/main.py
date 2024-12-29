from Graph import Graph
from Node import Node
from Cidades import Cidade

def main():
    #g = Graph()

    # Ficha2
    Ancora = Cidade("Ancora", 2, 400, 1000, 200, 0)
    Pte_Lima = Cidade("Pte_Lima", 1, 100, 2000, 10, 0)
    Braga = Cidade("Braga", 0, 0, 3000, 0, 0)
    P_Lanhoso = Cidade("P_Lanhoso", 3, 1000, 1500, 500, 0)
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

    AncoraN = Node("Ancora")
    Pte_LimaN = Node("Pte_Lima")
    BragaN = Node("Braga")
    P_LanhosoN = Node("P_Lanhoso")
    BarcelosN = Node("Barcelos")
    EsposendeN = Node("Esposende")
    FamalicaoN = Node("Famalicao")
    GuimaraesN = Node("Guimaraes")
    Viana_do_CasteloN = Node("Viana do Castelo")
    Povoa_de_VarzimN = Node("Povoa de Varzim")
    Santo_TirsoN = Node("Santo Tirso")
    AmaranteN = Node("Amarante")
    MaiaN = Node("Maia")
    LousadaN = Node("Lousada")
    Marco_de_CanavesesN = Node("Marco de Canaveses")
    PortoN = Node("Porto")
    Santa_Maria_da_FeiraN = Node("Santa Maria da Feira")
    OvarN = Node("Ovar")

    nodes = [
        AncoraN,
        Pte_LimaN,
        BragaN,
        P_LanhosoN,
        BarcelosN,
        EsposendeN,
        FamalicaoN,
        GuimaraesN,
        Viana_do_CasteloN,
        Povoa_de_VarzimN,
        Santo_TirsoN,
        AmaranteN,
        MaiaN,
        LousadaN,
        Marco_de_CanavesesN,
        PortoN,
        Santa_Maria_da_FeiraN,
        OvarN
    ]
    graph = Graph(directed=False)

    # for node in nodes:
    #     graph.add_node(node)

    graph.add_edge(Povoa_de_VarzimN, MaiaN, 32)
    graph.add_edge(MaiaN, Santo_TirsoN, 23)
    graph.add_edge(Santo_TirsoN, LousadaN, 32)
    graph.add_edge(LousadaN, AmaranteN, 27)
    graph.add_edge(LousadaN, Marco_de_CanavesesN, 21)
    graph.add_edge(MaiaN, PortoN, 11)
    graph.add_edge(PortoN, Santa_Maria_da_FeiraN, 34)
    graph.add_edge(Santa_Maria_da_FeiraN, OvarN, 11)
    graph.add_edge(AncoraN, Viana_do_CasteloN, 10)
    graph.add_edge(Viana_do_CasteloN, Pte_LimaN, 5)
    graph.add_edge(Viana_do_CasteloN, EsposendeN, 15)
    graph.add_edge(Pte_LimaN, BragaN, 5)
    graph.add_edge(BragaN, P_LanhosoN, 10)
    graph.add_edge(BragaN, BarcelosN, 15)
    graph.add_edge(BragaN, GuimaraesN, 10)
    graph.add_edge(GuimaraesN, FamalicaoN, 5)
    graph.add_edge(BarcelosN, BragaN, 5)
    graph.add_edge(BarcelosN, EsposendeN, 5)

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
            print(g.imprime_aresta())
            l = input("prima enter para continuar")
        elif saida == 5:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(graph.procura_DFS(inicio, fim, path=[], visited=set()))
            l = input("prima enter para continuar")
        elif saida == 6:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(graph.procura_BFS(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 7:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(graph.procura_aStar(inicio, fim))
            l = input("prima enter para continuar")
        elif saida == 8:
            inicio = input("Nodo inicial->")
            fim = input("Nodo final->")
            print(graph.greedy(inicio, fim))
            l = input("prima enter para continuar")
        else:
            print("you didn't add anything")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()
