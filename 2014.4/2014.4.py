import itertools

def mejor_dis(jugadores):

    N = len(jugadores)

    total = sum(jugadores)
#el problema dice que la cantidad de jugadores puede diferir por uno, si es impar la cantidad de jugadores no hay de otra, pero si es par hay dos casos, donde se divide a la mitad los jugadores y cuando difiere por uno
    if N % 2 == 0:
        combinaciones1 = list(itertools.combinations(jugadores, N//2))
        #combinaciones2 = list(itertools.combinations(jugadores, N//2 + 1))
        combinaciones = list(combinaciones1)# + combinaciones2)
    else:
        combinaciones = list(itertools.combinations(jugadores, N//2))

    equipos = []
    for i in combinaciones:
        equipo1 = sum(i)
        equipo2 = total - equipo1
        dis = abs(equipo1 - equipo2)

        equipos.append([dis, equipo1, equipo2])
    
    return(min(equipos)[1:3])

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    for i in range(T):
        entrada.readline()
        
        cantidad = int(entrada.readline())

        jugadores = []
        for j in range(cantidad):
            jugadores.append(int(entrada.readline()))
        
        res = mejor_dis(jugadores)

        salida.write("Caso #{}: {} {}\n".format(i + 1, min(res), max(res)))
    
    entrada.close()
    salida.close()

main()