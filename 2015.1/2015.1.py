def fusion(ABClist, cadena):
    for i in ABClist:
        AB = i[0:2]
        if cadena.count(AB) == 1:
            return cadena.replace(AB, i[-1])
        elif cadena.count(AB[::-1]) == 1:
            return cadena.replace(AB[::-1], i[-1])
    
    return cadena

def fision(ABClist, cadena):
    for i in ABClist:
        A = i[0]
        B = i[1]
        if cadena.count(A) == 1 and cadena.count(B) == 1:
            Ai = cadena.index(A)
            Bi = cadena.index(B)
            if Ai < Bi:
                return(cadena.replace(cadena[Ai: Bi + 1], ''))
            else:
                return(cadena.replace(cadena[Bi: Ai + 1], ''))
    return cadena

def reactor(fusiones, fisiones, cadena):
    cadena_r = cadena[0]
    for i in range(len(cadena) - 1):
        cadena_r += cadena[i + 1]

        cadena_r = fusion(fusiones, cadena_r)

        cadena_r = fision(fisiones, cadena_r)
    
    return cadena_r

#20min

def main():
    entrada = open('input.txt', 'r')
    salida = open('output.txt', 'w')

    T = int(entrada.readline())

    for i in range(T):
        fusiones = []
        fisiones = []

        entradai = entrada.readline().replace('\n', '')
        entradai = entradai.split(' ')

        C = int(entradai[0])
        entradai.remove(str(C))
        if C != 0:
            for j in range(C):
                f = entradai[0]
                entradai.remove(f)
                fusiones.append(f)
        
        D = int(entradai[0])
        entradai.remove(str(D))
        if D != 0:
            for j in range(D):
                f = entradai[0]
                entradai.remove(f)
                fisiones.append(f)
        
        elemento = entradai[-1]
        
        elemento2 = reactor(fusiones, fisiones, elemento)

        lista = []
        for j in range(len(elemento2)):
            lista.append(elemento2[j])
        
        salida.write("Caso #{}: [".format(i +1))

        if len(lista) == 0:
            salida.write("]\n")
        else:
            coma = 0
            for e in lista:
                salida.write(e)
                coma += 1
                if coma < len(lista):
                    salida.write(',')
                else:
                    salida.write(']\n')

    
    entrada.close()
    salida.close()

main()
#20min
#total 40min