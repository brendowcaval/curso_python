

#imprimir uma list

numeros = [10,20,30]

for x in numeros:
    print(x)


#outra list
nomes = ['joao','joana','luana','marilia']


for x in nomes:
    print(x)
    if x == 'luana':
        print("eu conheço vc, luana.")

print("------")
#outra forma

for z in "Jesus":  # printa palavra por palavra
    print(z)


print("---")
#comando break

letras = ["a","b","c","d"]

for L in letras:
    print(L)
    if L == "c":  #ele printa o c e depois para
        break     # se o print(L) estivesse depois do if, o elemento c não seria printado
    