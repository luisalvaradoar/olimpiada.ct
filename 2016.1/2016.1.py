def solo(lista):
    a = lista
    ai = list(set(a))

    for i in ai:
        if a.count(i) == 1:
            return(i)

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    for i in range(T):
        cantidad = int(entrada.readline())

        lista_s = entrada.readline().split(' ')

        lista = []
        for j in lista_s:
            lista.append(int(j))
        
        res = solo(lista)

        #print(res)

        salida.write("Caso #{}: {}\n".format(i + 1, res))
    
    entrada.close()
    salida.close()

main()