def criba(n):
    if n == 1:
        return(False)

    if n == 2:
        return(True)

    for i in range(2, int(round(n**0.5)) + 1):
        if n % i == 0:
            return(False)

    return(True)

def primos(A, B):
    lista = []
    for i in range(A, B + 1):
        if criba(i) == True:
            lista.append(i)

    return(lista)

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    cont_lblanco = 0
    for i in range(T):
        cont_lblanco += 1
        salida.write("Caso #{}:\n".format(i + 1))

        ab = entrada.readline().split(' ')
        a = int(ab[0])
        b = int(ab[1])

        lista = primos(a, b)

        for i in lista:
            salida.write("{}\n".format(i))
        
        if cont_lblanco < T:
            salida.write("\n")
    
    entrada.close()
    salida.close()

            
main()