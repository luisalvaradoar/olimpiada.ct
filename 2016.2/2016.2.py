def prod_esc_min(V, W):
    producto = 0
    Vm = sorted(V)[::-1]
    WM = sorted(W)
    for i in range(len(Vm)):
        producto += Vm[i] * WM[i]
    return(producto)

def main():
    entrada = open("input.txt","r")
    salida = open("output.txt","w")

    T = int(entrada.readline())

    x = 0
    for i in range(T):
        dim = int(entrada.readline())

        vs = entrada.readline().split(' ')
        ws = entrada.readline().split(' ')

        v = []
        w = []
        for i in range(dim):
            v.append(int(vs[i]))
            w.append(int(ws[i]))
        
        escalar = prod_esc_min(v, w)

        x += 1
        salida.write("Caso #{}: {}\n".format(x, escalar))
    
    entrada.close()
    salida.close()

main()