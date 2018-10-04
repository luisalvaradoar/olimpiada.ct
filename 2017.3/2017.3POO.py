from itertools import permutations

class Cofre():
    def __init__(self, cerradura, llaves = []):
        self.__cerradura = cerradura
        self.__llaves = llaves
    
    def getCerradura(self):
        return(self.__cerradura)
    
    def getLlaves(self):
        return(self.__llaves)
    
    def abrir(self, llaves):
        for l in llaves:
            if l == self.__cerradura:
                llaves.remove(l)
                for ln in self.getLlaves():
                    llaves.append(ln)

                return(True, llaves)
            else:
                return(False, [])
        return(False, [])

def soluciones(cofres, llaves_inicio):
    diccionario = dict(zip(range(len(cofres)), cofres))

    perm = list(permutations(range(len(cofres))))

    sol = []
    a = (llaves_inicio, 0)
    for intento in perm:
        llaves = a[0]
        cont = 0
        for j in intento:
            evento = diccionario.get(j).abrir(llaves)
            if evento[0]:
                llaves = evento[1]
                cont += 1
                if cont == len(cofres):
                    sol.append(intento)

    return(sol)

#40min

cofres = []
cofres.append(Cofre(1))
cofres.append(Cofre(1, [1, 3]))
cofres.append(Cofre(2))
cofres.append(Cofre(3, [2]))

print(soluciones(cofres, [1]))


def main():
    entrada = open("input.txt", 'r')
    salida = open("output.txt", 'w')

    T = int(entrada.readline())

    for t in range(T):
        N = int(entrada.readline().replace('\n', '').split(' ')[-1])

        llaves_str = entrada.readline().replace('\n', '').split(' ')
        llaves = []
        for i in llaves_str:
            llaves.append(int(i))

        for n in range(N):
            cerradura_cllaves_llaves = entrada.readline().replace('\n', '').split(' ')
            cerradura = int(cerradura_cllaves_llaves[0])
            cllaves = int(cerradura_cllaves_llaves[1])
            llaves_cofre = []
            if cllaves != 0:
                cerradura_cllaves_llaves.remove(cerradura)
                cerradura_cllaves_llaves.remove(cllaves)
                for ll in cerradura_cllaves_llaves:
                    llaves_cofre.append(int(ll))
        
        
    entrada.close()
    salida.close()

#main()