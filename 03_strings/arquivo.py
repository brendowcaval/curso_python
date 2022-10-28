#printando parte de uma string
# o espaço também conta
anime = "Dragon ball z"

print(anime[0]) # só printa a letra D por causa do index 0
print(anime[7]) # b
print(anime[0:6]) #Dragon


#como saber o tamanho de uma string
anime2 = "Naruto"
print(len(anime2))


#como remover espaço no inicio ou fim de string
nomeAqui = " Manuel "
print("-------")
print(nomeAqui) #com espaço
print(nomeAqui.strip()) #sem espaço
print("-------")

#converter string para minusculo junto com o strip
print(nomeAqui.lower().strip()) 
#converter string para maiusculo
print(nomeAqui.upper())

#mudar uma string por outra
nomeEmpresa = "Empresa X"
print(nomeEmpresa.replace("X","Z")) #muda X para Z
