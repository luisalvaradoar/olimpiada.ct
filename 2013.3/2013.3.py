def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)

def canonica(n, d):
    MCD = mcd(d,n)
    nd = d // MCD
    nn = n // MCD
    return(nn, nd)

def mixta(n, d):
    if n < d:
        return(n, d)
    else:
        mix = n // d
        res = n % d
        return(mix, res, d)

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    for i in range(T):
        frac = entrada.readline().split('/')
        N = int(frac[0])
        D = int(frac[1])
        res = ''

        if N < 0:
            res += '-'
        
        if abs(N) % D == 0:
            res += str(abs(N) // D)
        else:
            can = canonica(abs(N), D)

            mix = mixta(can[0], can[1])

            if len(mix) == 2:
                res += str(mix[0]) + '/' + str(mix[1])
            else:
                res += str(mix[0]) + ' ' + str(mix[1]) + '/' + str(mix[2])
        
        salida.write("Caso #{}: {}\n".format(i + 1, res))



    entrada.close()
    salida.close()

main()

# 20min