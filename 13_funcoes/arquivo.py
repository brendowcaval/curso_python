#funcao é um bloco de codigo


def minhaFuncao():
    print("Curso de Python")

minhaFuncao() #chamando funcao
minhaFuncao()


print("----")
#com parametros
def insiraNome(nome,idade): # ele poderia tambem passar o parametro assim: nome = "Brendow", pois assim já estaria definido no parametro
    print("meu nome é " + nome)
    print("minha idade é " , idade)



insiraNome("Brendow",25)
insiraNome("Itamar",23)

print("----")
#arbitrarios
# posso inserir quantos parametros eu quiser
def textos(*exemplo):
    print(exemplo[0])
    print(exemplo[1])
    print(exemplo[2])

textos("python","js","java")