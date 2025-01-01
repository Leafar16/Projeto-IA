
class Veiculo:
 
 def __init__(self,id,local,tipo,carga_maxima,carga_transportada,km_max,km_atual,velocidade_media):
    self.id=id
    self.local=local
    self.tipo=tipo
    self.carga_maxima=carga_maxima
    self.carga_transportada=carga_transportada
    self.km_max=km_max
    self.km_atual=km_atual
    self.velocidade_media=velocidade_media
     

 def abastecer(self):
    self.carga_transportada = self.carga_maxima
    self.km_atual = self.km_max

 def depositar(self,carga):
   if(carga<0 or self.carga_transportada==0):
      return 0

   if(carga>self.carga_transportada):
      carga_atual=self.carga_transportada
      self.carga_transportada=0
      return carga_atual

   self.carga_transportada-=carga
   return carga

 def verifica_viagem(self,custo_viagem):
    return self.km_atual-custo_viagem<=0


 def dim_tempo_gasto(self,km):
    return self.velocidade_media/km



 def __str__(self):
    return f"Veiculo(tipo={self.tipo}, local={self.local}, carga_maxima={self.carga_maxima}, carga_transportada={self.carga_transportada}, km_max={self.km_max}, km_atual={self.km_atual})"

def veiculos_sem_carga(veiculos):
    for veiculo in veiculos:
        if veiculo.carga_transportada!=0:
            return True
    return False

