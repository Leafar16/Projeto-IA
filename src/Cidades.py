
class Cidade:

    def __init__(self, nome, populacao_necessitada, populacao_total, necessidades, tempo_critico):
        self.nome = nome
        self.nivel_risco = 0
        self.populacao_necessitada = populacao_necessitada
        self.necessidades = necessidades
        self.populacao_total = populacao_total
        self.tempo_critico = tempo_critico
        self.calcula_risco()

    def calcula_risco(self):
        ratio = self.populacao_necessitada / self.populacao_total
        if ratio == 0:
            self.nivel_risco = 0
        elif ratio < 0.2:
            self.nivel_risco = 1
        elif ratio < 0.5:
            self.nivel_risco = 2
        else:
            self.nivel_risco = 3

    def verifica_necessidades(self, necessidades):
         self.necessidades = necessidades
    
    def verifica_populacao(self, populacao_ajudada, populacao_necessitada):
        return self.populacao_total >= 0 and self.populacao_total >= populacao_ajudada and self.populacao_total >= populacao_necessitada
    
    def incrementa_tempo_critico(self):
        self.tempo_critico += 1

    def incrementa_necessitados(self, populacao_total):
        self.populacao_necessitada += 1 and self.populacao_necessitada <= populacao_total

    def decrementa_necessitados(self,populacao_ajudada):
        self.populacao_necessitada -= populacao_ajudada and self.populacao_necessitada >= 0
    
    def nivel_risco(self, populacao_necessitada, populacao_total, tempo_critico):
        self.nivel_risco = populacao_necessitada/populacao_total * tempo_critico
    
    def incrementa_tempo_decorrido(self):
        self.tempo_decorrido += 1

    def decrementa_necessidades(self, necessidades):
        if necessidades<0:
            return 0
        self.necessidades -= necessidades and self.necessidades >= 0

    

def organiza_cidades(cidades):
    cidades_organizadas = sorted(cidades, key=lambda x: x.nivel_risco, reverse=True)
    return cidades_organizadas