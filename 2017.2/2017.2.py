def palindromoQ(n):
	ns = str(n)
	if ns == ns[::-1]:
		return True
	else:
		return False

def john(a,b):
	cont = 0
	for i in range(a, b + 1):
		raiz = i ** (0.5)
		disc = raiz - round(raiz)
		if disc == 0:
			if palindromoQ(i) == True and palindromoQ(int(raiz)) == True:
				cont += 1

	return(cont)

def main():
	entrada = open("input.txt", "r")
	salida = open("output.txt", "w")

	T = int(entrada.readline())

	for i in range(T):
		ab = entrada.readline().split(' ')
		a = int(ab[0])
		b = int(ab[1])

		res = john(a, b)

		salida.write("Caso #{}: {}\n".format(i + 1, res))

	entrada.close()
	salida.close()

main()
# 20min