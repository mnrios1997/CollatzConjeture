
steps = 0
c0 = int(input("Ingrese un numero para comprobar la Conjetura de Collatz: "))

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
        steps +=1
        print 'Valor: {0} - Paso: {1} '.format(c0, steps)
        if c0 != 1:
            continue
    elif c0 % 2 != 0:
        c0 = int(c0 * 3 + 1)
        steps +=1
        print 'Valor: {0} - Paso: {1} '.format(c0, steps)
        if c0 != 1:
            continue
print 'Total de pasos: {0}.'.format(steps)
