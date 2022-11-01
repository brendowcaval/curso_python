#Isso é orientação a objeto

class personagem:
    nome = ""
    poder = ""
    def __init__(self,exemplo1,exemplo2):  # método construtor
        self.nome = exemplo1      # o self é como se fosse um this
        self.poder = exemplo2
    def exibir(self): #exibi valores
        print("nome : " + self.nome)
        print("poder: " + self.poder)
    


x1 = personagem("Ryu","hadouken") # valores que sao inseridos nos parametros exemplo1 e exemplo2
x2 = personagem("Ken","Shoryuken")


#chamando a funcao
x1.exibir()
x2.exibir()
