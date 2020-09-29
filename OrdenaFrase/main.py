
texto_aux=["Este","es","un","programa","escrito","en","Python"]
contenido=""
def leerTxt():
    f=open("oracion.txt",'r')
    contenido=f.read()
    f.close()
    return  contenido


def buscarIndice(palabra):

    indice=-1
    for i in range(len(texto)):
       if palabra==texto[i]:
           indice=i
    return indice


contenido=leerTxt()
texto=contenido.split(" ")
print(texto)
posicion=0
for i in range(len(texto_aux)):
    if texto[i] != texto_aux[i]:

        posicion=buscarIndice(texto_aux[i])
        if posicion == -1:
            print("Alguna palabra no coinide")
            break
        aux=texto[posicion]
        texto[posicion]=texto[i]
        texto[i]=aux
        print(texto)















