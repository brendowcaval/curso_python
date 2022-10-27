# mudando variável
valor = 50
valor = "Bren"
valor = 50.0

print(valor)


#fazendo concatenação
nome = "João"
sobrenome = "Paulo"
print("meu nome é " + nome + " " + sobrenome)


# Como fazer comentário com muitas linhas

"""
um
comentário com muitas linhas
aqui
"""

#muitas variáveis com o mesmo valor

x1 = x2 = x3 = 10

# como fazer uma variável se tornar global e acessá-la de fora

def cd(): #função
    global personagem # deixando a variavel global e não local
    personagem = "Ryu"

cd() #chamando função
print(personagem) # printando a variavel