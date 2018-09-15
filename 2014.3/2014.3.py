def Fn(n):
    fib1 = 1
    fib2 = 1
    temp = 0
    
    if n == 1:
        return(1)
    
    if n == 2:
        return(1)

    else:
        n -= 2
        for i in range(n):
            temp = fib1 + fib2
            fib1 = fib2
            fib2 = temp

        return(temp)

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    saltos = 0
    for i in range(T):
        n = int(entrada.readline())

        salida.write("Caso #{}: {}".format(i + 1, Fn(n)))

        saltos += 1
        if saltos < T:
            salida.write("\n")
    
    entrada.close()
    salida.close()

main()

# 8min