letras_a_numeros = {"B":1, "C":2, "D":3, "F":4, "G":5, "H":6, "J":7, "K":8, "L":9, "M":10, "N":11, "P":12, "Q":13, \
"R":14, "S":15, "T":16, "V":17, "W":18, "X":19, "Y":20, "Z":21}

numeros_a_letras = dict(zip(letras_a_numeros.values(), letras_a_numeros.keys()))

def placa_codigo(placa):
    placa = placa.split(' ')
    codigo = []
    codigo.append(int(placa[0]))
    for i in range(3):
        letra = placa[1][i]
        letra_numero = letras_a_numeros.get(letra)
        codigo.append(letra_numero)
    return(codigo)

def codigo_placa(codigo):
    placa = ''
    if codigo[0] == 0:
        placa += '0000'
    else:
        placa += str(codigo[0])
    
    l1 = numeros_a_letras.get(codigo[1])
    l2 = numeros_a_letras.get(codigo[2])
    l3 = numeros_a_letras.get(codigo[3])

    placa += ' ' + l1 + l2 + l3

    return(placa)

def codigo_sig(codigo):
    codigo[0] += 1
    if codigo[0] == 10000:
        codigo[0] = 0

    if codigo[0] == 0:
        codigo[3] += 1
        if codigo[3] == 22:
            codigo[3] = 1
            codigo[2] += 1
            if codigo[2] == 22:
                codigo[2] = 1
                codigo[1] += 1
    return(codigo)

def placa_sig(placa):
    codigo = placa_codigo(placa)
    nuevo_codigo = codigo_sig(codigo)

    return(codigo_placa(nuevo_codigo))

def main():
    entrada = open("input.txt","r")
    salida = open("output.txt","w")

    caso = 0
    while(True):
        caso += 1
        placa = entrada.readline()
        if placa == '9999 ZZZ':
            salida.write("Caso #{}: FINAL".format(caso))
            break
        else:
            salida.write("Caso #{}: {}\n".format(caso, placa_sig(placa)))

    entrada.close()
    salida.close()
    
main()