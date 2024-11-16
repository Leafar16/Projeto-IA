 
def Veiculo(java):
 
 def __init_(local,tipo,carga_maxima,carga_transportada,tempo_viagem_atual,tempo_viagem_maximo,nr_meds,nr_meds_maximo,nr_comida,nr_comida_max,nr_agua,nr_agua_maximo):
    self.local=local
    self.tipo=tipo
    self.carga_maxima=carga_maxima
    self.carga_transportada=carga_transportada
    self.tempo_viagem_atual=tempo_viagem_atual
    self.tempo_viagem_maximo=tempo_viagem_maximo
    self.nr_meds=nr_meds
    self.nr_meds_maximo=nr_meds_maximo
    self.nr_comida=nr_comida
    self.nr_comida_max=nr_comida_max
    self.nr_agua=nr_agua
    self.nr_agua_maximo=nr_agua_maximo


 def abastecer(self):
    self.tempo_viagem_atual=self.tempo_viagem_maximo
    self.nr_meds=self.nr_meds_maximo
    self.nr_agua=self.nr_agua_maximo
    self.nr_comida=self.nr_comida_max

 def verifica_viagem(self,tempo_viagem):
    return self.tempo_viagem_atual-tempo_viagem<=0


 def viajar(self,tempo_viagem,local_novo):
    self.tempo_viagem_atual=-tempo_viagem
    self.local=local_novo

 def depositar_agua(self,agua):
    if(self.nr_agua<agua):
        return
    self.nr_agua-=agua

 def depositar_comida(self,comida):
    if(self.nr_comida<comida):
        return
    self.nr_comida-=comida

 def depositar_meds(self,meds):
    if(self.nr_meds<meds):
        return
    self.nr_meds-=meds