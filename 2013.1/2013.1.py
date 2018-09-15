def binario_dec(binario):
    binario = binario[::-1]

    decimal = 0
    for i in range(len(binario)):
        decimal += (2**i) * int(binario[i])
    
    return(decimal)

def ip(binario):
    IP = ''

    p1 = binario[0:8]
    p2 = binario[8:16]
    p3 = binario[16:24]
    p4 = binario[24:32]

    p1d = binario_dec(p1)
    p2d = binario_dec(p2)
    p3d = binario_dec(p3)
    p4d = binario_dec(p4)

    IP = str(p1d) + '.' + str(p2d) + '.' + str(p3d) + '.' + str(p4d)

    return(IP)

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    for i in range(T):
        binario = entrada.readline().replace('\n','')

        IP = ip(binario)

        salida.write("Caso #{}: {}\n".format(i + 1, IP))

    entrada.close()
    salida.close()

main()

# 10min