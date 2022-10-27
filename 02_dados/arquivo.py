import random


a = 50 #int
b = "Death Note" #String
c = 10.1 #float
d = True #bool
e = False #bool

print(type(e))  # type() diz o tipo de dado


# operação de casting
# str() é string  
x = 50
nome = "Manuel"

print("meu número é : " + str(x) + " e meu nome é " + nome)

# converter float para int
valorT = int(50.50) 
print(valorT)


#gerar numeros aleatorios
numeroAleatorio = random.randrange(1,10) #retorna entre 1 e 9

print(numeroAleatorio)