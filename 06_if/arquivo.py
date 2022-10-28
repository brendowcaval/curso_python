# operaçoes matematicas são : + - * /

x = True

if x: #se for True entra aqui
    print("entrou no campo TRUE")


nome = "joana"

if nome == "paulo": # == é igual , tem também o > < >= <=
    print("olá paulo!")
elif nome == "breno":
    print("olá breno")
elif nome == "joana":
    print("olá joana")
else: #se todos os anteriores derem False, ele cai aqui
    print("não conheço você!")


print("-----")

dinheiro = 202
dia = "Domingo"


# no comando and, todos precisam ser verdadeiro para entrar na condição
# no comando or, só um já é suficiente para entrar na condição

if dia == "Domingo" and dinheiro > 200:   # and = e   or = ou    
    print("eu vou para a praia.")
