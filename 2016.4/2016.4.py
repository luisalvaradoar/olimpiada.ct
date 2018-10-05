def push(letra, pila):
    return pila.insert(0, letra)

def pop(pila):
    return pila.remove(pila[0])

def imprimir(pila, impreso):
    return(impreso.append(pila[0]))

def roland(nota_str):
    nota = []
    for j in range(len(nota_str)):
        nota.append(nota_str[j])

    impreso = []
    pila = [nota[0]]

    i = 0
    cont = 1
    while impreso != nota:
        letra_i = nota[i]
        if pila[0] != letra_i:
            if letra_i not in pila:
                cont += 2
                push(letra_i, pila)
                imprimir(pila, impreso)
                i += 1
            else:
                while pila.index(letra_i) != 0:
                    cont += 1
                    pop(pila)
                cont += 1
                imprimir(pila, impreso)
                i += 1
        else:
            cont += 1
            imprimir(pila, impreso)
            i += 1

    return(cont + len(pila))

#20min

def main():
    entrada = open("input.txt", 'r')
    salida = open("output.txt", 'w')

    T = int(entrada.readline())

    for t in range(T):
        nota = entrada.readline().replace('\n','')
        R = roland(nota)
        
        salida.write("Caso #{}: {}\n".format(t + 1, R))

    entrada.close()
    salida.close()

main()

#5min
#total 25min ~ 20min