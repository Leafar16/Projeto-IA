
class Veiculo:
 
 def __init__(self, local,tipo,carga_maxima,carga_transportada,tempo_viagem_atual,tempo_viagem_maximo, combustivel, combustivel_max):
    self.local=local
    self.tipo=tipo
    self.carga_maxima=carga_maxima
    self.carga_transportada=carga_transportada
    self.tempo_viagem_atual=tempo_viagem_atual
    self.tempo_viagem_maximo=tempo_viagem_maximo
    self.combustivel=combustivel
    self.combustivel_max=combustivel_max


 def abastecer(self):
    self.carga_transportada = self.carga_maxima
    self.combustivel = self.combustivel_max
    self.tempo_viagem_atual = 0

 def verifica_viagem(self,tempo_viagem):
    return self.tempo_viagem_atual-tempo_viagem<=0


 def viajar(self,tempo_viagem,local_novo):
    self.tempo_viagem_atual=-tempo_viagem
    self.local=local_novo