
#list

personagens = ["goku","vegeta"]

print(personagens)
print(personagens[0]) #retorna o primeiro elemento
print(personagens[-1]) #retorna o ultimo elemento

personagens[1] = "Trunks" #muda elemento de uma list
print(personagens)

print("------------------")

#outra list

filmes = ["missao impossivel", "avatar"]
filmes.append(50) # adiciona outro elemento
#filmes.remove(50)    isso remove o elemento
#filmes.pop()          isso remove o ultimo elemento da list
#filmes.clear()         isso limpa toda a list
print(filmes)

#uma lista receber outra
# filmes2 recebe todos os elementos da lista filmes
filmes2 = list(filmes)
print(filmes2)
