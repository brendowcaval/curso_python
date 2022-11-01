



personagens = {
    "personagem1" : "goku",   # chave : valor
    "personagem2" : "vegeta",
    "personagem3" : "picollo"

}

#personagens["personagem2"] = "trunks"           mudar valor
#personagens["personagem4"] = "goten"           adiciona outra chave e valor
#personagens.pop("personagem3")                   remover


print(personagens)
print(personagens["personagem1"]) #imprimi valor goku


#imprimi em um loop

for x in personagens:
    print(personagens[x] +" - " + x)   # personagens[x] imprimi os valores e x as chaves



print("--------------")

# possivel fazr um dictionary que contem outros dictionary


filmes = {
    "aventura" : {
        "filme1" : "senhor dos aneis",
        "filme2" : "harry potter"
    },
    "terror" : {
        "filme3" : "invocacao do mal",
        "filme4" : "a morte te da parabens"
    }
}

print(filmes["aventura"])
print(filmes["aventura"]["filme1"]) # imprimi senhor dos aneis