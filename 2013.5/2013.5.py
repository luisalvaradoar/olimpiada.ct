def palindromoQ(n):
    ns = str(n)
    if ns == ns[::-1]:
        return(True)

def palindromo_sig(n):
    i = n
    while True:
        i += 1
        if palindromoQ(i) == True:
            return(i)

def main():
    entrada = open("input.txt","r")
    salida = open("output.txt","w")

    T = int(entrada.readline())

    for i in range(T):
        numero = int(entrada.readline())

        palindromoS = palindromo_sig(numero)

        salida.write("Caso #{}: {} \n".format(i + 1, palindromoS))

    entrada.close()
    salida.close()

main()

# 15min