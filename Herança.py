class atleta:
    def __init__(self, aposentado, peso, aquecido, nome):
        self.aposentado = aposentado
        self._peso = peso #atributo protegido
        self.aquecido = aquecido
        self._nome = nome = nome


    #função para acessar o atributo protegidos
        
    def setNome(self, nome):
        self._nome = nome
        
    def getNome(self):
        return self._nome
        
    def setPeso(self, peso):
        self._peso = peso

    def getPeso (self):
        return self._peso

    def aposentar(self):
        self.aposentado = 'sim'

    def aquecer (self):
        self.aquecido = 'preparado'

        
class corredor(atleta):
    def __init__(self, altura, velMedia, aposentado, peso, aquecido, nome):
        atleta.__init__(self, aposentado, peso, aquecido, nome)
        self.altura = altura
        self.velMedia = velMedia
#Aplica uma velocidade no corredor
    def correr(self):
        self.velMedia = '15 km/h'

class nadador(atleta):
    def __init__(self, envergadura, especialidade, nadar, aposentado, peso, aquecido, nome):
        atleta.__init__(self, aposentado, peso, aquecido, nome)
        self.envegadura = envergadura
        self.especialidade = especialidade
        self.nadar = nadar

#Inicia a natação
    def nadar (self):
        self.nadar = 'nadando'

class ciclista(atleta):
    def __init__(self, distMax, bicicleta, aposentado, peso, aquecido, nome):
        atleta.__init__(self, aposentado, peso, aquecido, nome)
        self.distMax = distMax
        self.bicicleta = bicicleta
#Começa a pedalar
    def pedalar(self):
        self.bicicleta = 'em uso'


class TriAtleta(corredor, nadador, ciclista):
    def __init__(self, titulos, aposentado, peso, aquecido, nome, altura, velMedia, envergadura, especialidade, nadar, distMax, bicicleta):
        corredor.__init__(self, altura, velMedia, aposentado, peso, aquecido, nome)
        nadador.__init__(self, envergadura, especialidade, nadar, aposentado, peso, aquecido, nome)
        ciclista.__init__(self, distMax, bicicleta, aposentado, peso, aquecido, nome)
        self.titulos = titulos
#cria um atleta
print ('ATLETA')
A = atleta('nao', 60, 'nao', 'erick')
print (A.getNome())
#muda de 'e' para 'E'
A.setNome('Erick')
print (A.getNome())
#Verifica aposentadoria
print (A.aposentado)
A.aposentar()
#aposenta
print (A.aposentado)
print ('')
print ('TRIATLETA')

#cria o triatleta
TA = TriAtleta(1, 'nao', 65, 'nao', 'NOMEADO', 1.70, 13, 2, 'Natação rasa', 'nao', 20, 'parada')
#get nome no triatleta (função com elemento protegido da função atleta)
print (TA.getNome())
#aquece
TA.aquecer()
#corre
TA.correr()
#anda de bike
TA.pedalar()
#aposenta o triatleta
print(TA.aposentado)
TA.aposentar()
print (TA.aposentado)
