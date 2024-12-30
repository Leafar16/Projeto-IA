
class Veiculo:
 
 def __init__(self,id,local,tipo,carga_maxima,carga_transportada,km_max,km_atual):
    self.id=id
    self.local=local
    self.tipo=tipo
    self.carga_maxima=carga_maxima
    self.carga_transportada=carga_transportada
    self.km_max=km_max
    self.km_atual=km_atual
     


 def abastecer(self):
    self.carga_transportada = self.carga_maxima
    self.km_atual = self.km_max

 def verifica_viagem(self,custo_viagem):
    return self.km_atual-custo_viagem<=0


 def viajar(self,tempo_viagem,local_novo):
    self.km_atual=-tempo_viagem
    self.local=local_novo

 def __str__(self):
    return f"Veiculo(tipo={self.tipo}, local={self.local}, carga_maxima={self.carga_maxima}, carga_transportada={self.carga_transportada}, km_max={self.km_max}, km_atual={self.km_atual})"