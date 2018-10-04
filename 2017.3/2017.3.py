from itertools import permutations

def botin(cofres, llaves):
    posibilidades = tuple(permutations(range(1, len(cofres) + 1)))

    sol = []
    for intento in posibilidades:
        llavero = []
        for i in llaves:
            llavero.append(i)
        cont = 0
        for i in intento:
            cofrei = cofres.get(i)
            if cofrei[0] in llavero:
                llavero.remove(cofrei[0])
                cont += 1
                if cont == len(cofres):
                    sol.append(intento)
                for n_llave in cofrei[1]:
                    llavero.append(n_llave)
            else:
                pass
    if len(sol) != 0:
        return(min(sol))
    else:
        return([])

#20min

def main():
    entrada = open('input.txt', 'r')
    salida = open('output.txt', 'w')

    T = int(entrada.readline())

    for t in range(T):
        llaves_cofres = entrada.readline().replace('\n', '').split(' ')
        cant_cofres = int(llaves_cofres[-1])

        llaves_str = entrada.readline().replace('\n', '').split(' ')
        llaves = []
        for l in llaves_str:
            llaves.append(int(l))

        cofres_desc = []
        for c in range(cant_cofres):
            cofre_c = entrada.readline().replace('\n', '').split(' ')
            if cofre_c[1] == 0:
                cofres_desc.append([int(cofre_c[0]),[0]])
            else:
                llaves_c = []
                cerradura = cofre_c[0]
                cofre_c.remove(cerradura)
                cofre_c.remove(cofre_c[0])
                for lc in cofre_c:
                    llaves_c.append(int(lc))
                
                cofres_desc.append([int(cerradura), llaves_c])
        
        cofres_indexados = dict(zip(range(1, cant_cofres + 1), cofres_desc))

        res = botin(cofres_indexados, llaves)

        if len(res) != 0:
            sl = ''
            cont = 0
            for i in res:
                cont += 1
                sl += str(i)
                if cont < len(res):
                    sl += ' '

            salida.write("Caso #{}: {}\n".format(t + 1, sl))
        else:
            salida.write("Caso #{}: IMPOSIBLE\n".format(t + 1))

    entrada.close()
    salida.close()

main()
#15min
#total 35min