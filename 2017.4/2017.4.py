def Roller_coasters(vueltas, limite, pasajeros):
    dinero = 0
    for i in range(vueltas):
        carro = []

        for j in pasajeros:
            if (sum(carro) + j) <= limite:
                carro.append(j)
            else:
                break

        pasajeros = pasajeros[len(carro):len(pasajeros)]

        for c in carro:
            pasajeros.append(c)

        dinero += sum(carro)

    return(dinero)

#15min

def main():
    entrada = open("input.txt", 'r')
    salida = open("output.txt", 'w')

    T = int(entrada.readline())

    for i in range(T):
        entradai = entrada.readline().replace('\n', '').split(' ')
        
        vueltas = int(entradai[0])
        limite = int(entradai[1])

        pasajeros_str = entrada.readline().replace('\n','').split(' ')
        pasajeros = []
        for j in pasajeros_str:
            pasajeros.append(int(j))
        
        dinero_ganado = Roller_coasters(vueltas, limite, pasajeros)

        salida.write("Caso #{}: {}\n".format(i + 1, dinero_ganado))
        
    
    entrada.close()
    salida.close()

main()

#10min
#total 25min