lista = []
n=0
for x in range(10):
    n=int(input("Digite num número: "))
    lista.append(n)
maior = lista[0]
for x in lista:
        if x>maior:
            maior=x
indice =0
for x in range(len(lista)):
    if lista[x] ==maior:
        indice=x
print("O maior valor da lista é %d e seu indice será %d" %(maior,indice))

#exercicio

lista = []
somapar = 0
somapar2 = 0
for x in range(10):
    n = int(input("Digite um número %d: " % (x)))
    lista.append(n)
for x in lista:
    if x % 2 == 0:
        somapar = somapar + x
for x in range(len(lista)):
    if x % 2 == 0:
        somapar2 = lista[x] + somapar2

print("A soma dos números pares é: ", somapar)
print("A soma dos elementos de indice par é: ", somapar2)


#exercicio

lista = []

i=int(input("Digite o indice máximo da lista: "))
for x in range(i):
    n=int(input("Digite um número: "))
    lista.append(n)
x=len(lista) - 1
print("Lista: ",lista)
print("Inverso:")
while  x>=0:
    print(lista[x])
    x=x-1
    
#exercicio 

lista=[]
m=0
for x in range(10):
    n=int(input("Digite um número: "))
    lista.append(n)

print("Números: ",lista)

for x in range(2,len(lista)):
    if lista[x] > lista[x-1] + lista[x-2]:
        print(lista[x])

#exercicio

temp = [-10, -8, 0, 1, 2, 5, -2, -4]
min = temp[0]
max = temp[0]
soma = 0
for x in temp:
    soma = soma + x
    if x < min:
        min = x
    if x > max:
        max = x

print("Maior elemento: ", max)
print("Menor elemento: ", min)
media = soma / 8
print(media)