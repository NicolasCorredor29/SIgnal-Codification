
def cambiarEstado(estado):
    if estado=="par":
        return"impar"
    else:
        return "par"

def asignarSigno(signo):
    if signo=="-":
        return"+"
    else:
        return"-"

def cambiarindice(indice):
    if indice==3:
        indice=0
        return indice
    else:
        return (indice+1)
    
def hbd3(lista,indice,estado,signo):
 
    if((estado=="impar")and(signo=="+")):
        lista[indice+3]="+1"
        estado=cambiarEstado(estado)
    elif((estado=="impar")and(signo=="-")):
        lista[indice+3]="-1"
        estado=cambiarEstado(estado)
    elif((estado=="par")and(signo=="+")):
        lista[indice]="-1"
        lista[indice+3]="-1"
        signo=asignarSigno(signo)
    else:
        lista[indice]="+1"
        lista[indice+3]="+1"
        signo=asignarSigno(signo)
    return lista,estado,signo

def funcion2B1Q(lista,signo,parBits):
    match signo:
        case "-":
            match parBits:
                case "00":
                    lista.append("-1")
                case "01":
                    lista.append("-3")
                case "10":
                    lista.append("+1")
                    signo=asignarSigno(signo)
                case "11":
                    lista.append("+3")
                    signo=asignarSigno(signo)
        case "+":
            match parBits:
                case "00":
                    lista.append("+1")
                case "01":
                    lista.append("+3")
                case "10":
                    lista.append("-1")
                    signo=asignarSigno(signo)
                case "11":
                    lista.append("-3")
                    signo=asignarSigno(signo)
    return lista,signo

def MLT3(lista,indice,señal,entrada):
    valoresMLT3=["1","0","-1","0"]
    if lista==[]:#Verifico que no este vacia mi lista auxiliar, si esta vacia le coloco el primer elemento de mi señal
        lista.append("+"+señal[0])
    else:
        if(entrada=="1"):
            indice=cambiarindice(indice)
            lista.append(valoresMLT3[indice])
        else:
            lista.append(valoresMLT3[indice])
    return lista,indice



señal=input("Ingrese su señal : \n")
aux=[]
contador0=0
contador1=0
#inicializo el estado en impar para simular la misma situación que dejó el profesor
estado="impar"
#inicializo el signo en - para simular el mismo ejercicio que dejó el profesor en la clase
signo="-"
j=0
decision=0

while decision!=4:
    decision=int(input("¿Que desea realizar?\n 1:codificación hdb3\n 2:Codificación 2B1Q\n 3:Codificación MLT3\n 4:Salir\n"))
    match decision:
        case 1:
            for i in señal:
                if i=="0":
                    aux.append(i)
                    contador0+=1
                    if(contador0==4):
                        aux,estado,signo=hbd3(aux,j-3,estado,signo)
                        contador0=0
                else:
                    estado=cambiarEstado(estado)
                    signo=asignarSigno(signo)
                    aux.append(signo+"1")
                j+=1
            print(aux)
        
        case 2:
            if (len(señal) & 1)==1: #verifico si la entrada es par, en caso de que no le quito el ultimo termino pa que sea par
                señal=señal[:-1] 
            for i in range(0, len(señal), 2):
                parBits=señal[i:i+2]
                aux,signo=funcion2B1Q(aux,signo,parBits)
            print(aux)
        case 3:
            if señal[0]=="0":
                j=3
            else:
                j=0
            for i in señal:
                aux,j=MLT3(aux,j,señal,i)
                if ((contador1 & 1) ==1):
                    signo=asignarSigno(signo)
            print(aux)

    contador1=0           
    aux=[]
    contador0=0
    j=0



