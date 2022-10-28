
#verificar se tem uma palavra na string
texto = "Mello e Near"

resp = "Near" in texto
print(resp) #True

#verifica se não tem a palavra na string
resp2 = "Mello" not in texto
print(resp2) #False


#outra forma de concatenar dados
idade = 25
nome = "Brendow"
frase = "meu nome é {} e minha idade é {}"
print(frase.format(nome,idade))

print("meu nome é {} e minha idade é {}".format(nome,idade)) #ou assim também

print("meu nome é", nome) # ou com virgula


#quebrar linha
print("Estudando \nPython")

#colocar aspas dentro de string = pode ser \' ou \"
print(" \"Estudando Python\" ")


