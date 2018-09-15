import math

def nCk(n, k):
    res = (math.factorial(n))//(math.factorial(k) * math.factorial(n - k))
    return(res)

def coeficientes(n):
    lista_coeficientes = []
    for k in range(1, n):
        coef = nCk(n, k)

        lista_coeficientes.append(coef)

    return(lista_coeficientes)

def potencias(n):
    lista_potencias = []
    for k in range(1, n):
        lista_potencias.append([n - k, k])
    
    return(lista_potencias)

def binomioN(a, b, n):
    if n == 1:
        res = '1' + a
    else:
        res = '1' + a + '**' + str(n)

    coe = coeficientes(n)
    pot = potencias(n)

    for i in range(n - 1):
        res += ' + ' + str(coe[i])
        if pot[i][0] == 1:
            res += a
        else:
            res += a + '**' + str(pot[i][0])

        if pot[i][1] == 1:
            res += b
        else:
            res += b + '**' + str(pot[i][1])
    
    if n == 1:
        res += ' + ' + '1' + b
    else:
        res += ' + ' + '1' + b + '**' + str(n)

    return(res)

def entrada_dato(cadena):
    cadena = cadena.replace('(','')
    cadena = cadena.replace(')','')
    cadena = cadena.replace(' ','')
    cadena = cadena.replace('**','')
    cadena = cadena.replace('+','')

    return(cadena)

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    for i in range(T):
        binomio = entrada_dato(entrada.readline())
        A = binomio[0]
        binomio = binomio.replace(binomio[0], '')
        B = binomio[0]
        binomio = binomio.replace(binomio[0], '')
        N = int(binomio)

        respuesta = binomioN(A, B, N)

        salida.write("Caso #{}: {}\n".format(i + 1, respuesta))

    entrada.close()
    salida.close()

main()

#40min