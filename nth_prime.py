def prime(number):
    if number == 0: raise ValueError ("The operation is not possible")
    lista = [2]
    a = 0
    b = 2
    while len(lista) < number:
        for l in lista:
            if b % l == 0:
                a = True
                break 
        if a == False: 
            lista += [b]
        a = False
        b += 1
    return lista[-1]