# gana X si TXXX o XXXX
# gana O si TOOO o OOOO
# no a terminado si '.' no es 0
# empate si '.' = 0 y no se da 1,2

def diagonales(juego):
    d1 = ''
    d2 = ''

    for i in range(len(juego)):
        d1 += juego[i][i]

    for i in range(len(juego)):
        d2 += ((juego[i])[::-1])[i]
    
    return(d1, d2)

def columnas(juego):
    cols = []
    for i in range(len(juego)):
        ci = juego[0][i] + juego[1][i] + juego[2][i] + juego[3][i]
        cols.append(ci)
    return(cols)

def juego_completo(juego):
    completo = juego

    diag = diagonales(juego)

    colm = columnas(juego)

    completo.append(diag[0])
    completo.append(diag[1])

    for i in colm:
        completo.append(i)

    return(completo)

def no_vacios(juego):
    cantidad = 0
    for i in juego:
        cantidad += i.count('.')
    
    return(cantidad)

def gana(juego):
    vacios = no_vacios(juego)
    juegoC = juego_completo(juego)

    for i in juegoC:
        if sorted(i) == ['T', 'X', 'X', 'X'] or sorted(i) == ['X', 'X', 'X', 'X']:
            return('X gano')
        elif sorted(i) == ['O', 'O', 'O','T'] or sorted(i) == ['O', 'O', 'O', 'O']:
            return('O gano')

    if vacios == 0:
        return('Draw')
    else:
        return('El juego no ha terminado')

# juego1 = ['XXXT','....','OO..','....']
# juego2 = ['XOXT','XXOO','OXOX','XXOO']
# juego3 = ['XOX.','OX..','....','....']
# juego4 = ['OOXX', 'OXXX','OX.T','O..O']
# juego5 = ['XXXO','..O.','.O..','T...']
# juego6 = ['OXXX','XO..','..O.','...O']
# 37min solucionar

def main():
    entrada = open("input.txt","r")
    salida = open("output.txt","w")

    casos = int(entrada.readline())

    for i in range(casos):
        juego = []
        for j in range(4):
            linea = entrada.readline().replace('\n','')

            juego.append(linea)

        entrada.readline()

        salida.write("Caso #{}: {} \n".format(i + 1, gana(juego)))

    entrada.close()
    salida.close()

main()


#40min