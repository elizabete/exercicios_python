notas = [0,0,0]
soma = 0
x = 1
while x < 4:
    notas[x] = float(input("Nota %d: " % x))
    soma = soma + notas[x]
    x += 1
x = 1
while x < 4:
    print ("Nota %d: %5.2f" % (x, notas[x]))
    x = x + 1   

print ("Média: %d" % (soma/x)) 
