#coding:utf-8
#notas = [0,0,0]
#soma = 0
#x = 0
#while x < 3:
#    notas[x] = float(input("Prova %d: " % x))
#    soma = soma + notas[x]
#    x += 1
#x = 0
#while x < 3:
#    print ("Nota %d: %3.2f" % (x, notas[x]))
#    x = x + 1
#print ('Média: %d' % (soma/x))
#Versão 1

print "Versão 1"
notas = [0,0,0]
soma = 0
x = 0
while x < 3:
    notas[x] = float(input("Prova %d: " % (x+1)))
    soma = soma + notas[x]
    x += 1
x =0 
while x < 3:
    print ("Nota %d: %3.2f" % ((x + 1), notas[x]))
    x = x + 1
print ("Média: %3.2f" % (soma/x))
if (soma/x) >= 7:
    print ("Aprovado")
else:
    print("Reprovado")


#Versão 2
########################################
print "Versão 2"
soma = 0 
notas=[0, 0, 0]
for x, nota in enumerate(notas):
    notas[x] = float(input("Prova %d: " % (x + 1)))
    soma += notas[x]

for x, y in enumerate(notas):
    print("Nota %d: %3.2f" % ((x + 1), notas[x]))
 
print "Aprovado com %f" %(soma/3) if soma/3 >= 7 else "Reprovado com %f" %(soma/3)    
