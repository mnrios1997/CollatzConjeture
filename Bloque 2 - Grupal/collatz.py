
steps = 0
c0 = int(input("Ingrese un numero para comprobar la Conjetura de Collatz: "))

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
        steps = steps +1
        print(c0)
        if c0 != 1:
            continue
    elif c0 % 2 != 0:
        c0 = int(c0 * 3 + 1)
        steps = steps + 1
        print(c0)
        if c0 != 1:
            continue
print("Pasos = ", pasos)
        
