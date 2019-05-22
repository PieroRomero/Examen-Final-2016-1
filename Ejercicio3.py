n = int(input("Ingrese un numero:"))

if n >= 10000 : 
    print "el primer digito es:",str(n/10000)
elif n >= 1000 : 
    print "el primer digito es:",str(n/1000)
elif n >= 100 : 
    print "el primer digito es:",str(n/100)
else: 
    print "el numero es de un digito:", str(n)