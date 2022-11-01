#loop while

x = 0

while x < 10 : #Quando é True, os comandos sao executados, se for False, não
    print(x)
    x += 1 # incrementando, aqui ele vai adicionando +1 e quando o x ficar igual a 10, ele dá false



print("fim desse loop")
print(" ---------")
print("próximo loop:")

z = 0

while z < 10:
    print(z)
    z += 1
    if z >= 6:
        break


print("fim desse loop")
print(" ---------")
print("próximo loop:")

#imprimindo uma list no while
myList = ["naruto","sasuke","sakura"]
tamanhoL = len(myList)  #tamanho da list
b = 0

while b < tamanhoL:
    print(myList[b])
    b += 1
    