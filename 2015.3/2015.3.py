morse = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f', '--.':'g', \
'....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',\
'.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w',\
'-..-':'x', '-.--':'y', '--..':'z'}

def luis(cadena):
    codigo = cadena.split(' ')

    letras = []
    for i in codigo:
        letras.append(morse.get(i))

    res = letras[0].upper()
    for i in range(1, len(letras)):
        res += letras[i]
    
    return(res)

def main():
    entrada = open("input.txt", "r")
    salida = open("output.txt", "w")

    T = int(entrada.readline())

    for i in range(T):
        codigo = entrada.readline().replace('\n','')

        respuesta = luis(codigo)

        salida.write("{}\n".format(respuesta))

    entrada.close()
    salida.close()

main()

# 20min