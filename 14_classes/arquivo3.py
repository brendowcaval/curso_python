# parte de herança : tudo que contem na classe pai, contem na classe filho


class Inimigo:
    def __init__(self,nome,hp,time):
        self.nome = nome
        self.hp = hp
        self.magia = 100 # esse ja esta como definido
        self.time = time

    def exibindo(self):
        print("nome:" , self.nome)
        print("hp:" , self.hp)
        print("magia:" , self.magia)
        print("time:" , self.time)
        print("----------")



class inimigo1(Inimigo): # aqui inimigo1 herda do Inimigo
    def __init__(self, nome, hp):
        self.time = 1
        super().__init__(nome,hp,self.time)   # super() é para invocar metodos da classe pai
    def exibindo2(self):
        super().exibindo()


class inimigo2(Inimigo):
    def __init__(self, nome, hp):
        self.time = 2
        super().__init__(nome, hp,self.time)
    def exibindo3(self):
        super().exibindo()


x1 = inimigo1("Bison",500)
x2 = inimigo1("Bar",200)
x3 = inimigo2("Klain",500)
x4 = inimigo2("Kun",200)


x1.exibindo2()
x2.exibindo2()
x3.exibindo3()
x4.exibindo3()
