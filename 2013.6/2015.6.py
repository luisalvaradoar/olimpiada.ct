def transaccion(retiro, saldo):
    if retiro % 5 != 0:
        return(saldo)
    elif (saldo - retiro) < 0:
        return(saldo)
    elif saldo == retiro:
        return(saldo)
    else:
        return(saldo - retiro - 0.5)

def main():
    entrada = open("input.txt","r")
    salida = open("output.txt","w")

    T = int(entrada.readline())

    for i in range(T):
        tran = entrada.readline().split(' ')

        M = float(tran[0])
        S = float(tran[1])

        res = transaccion(M, S)

        salida.write("Caso #{}: {} \n".format(i + 1, res))
    
    entrada.close()
    salida.close()


main()
#15 min