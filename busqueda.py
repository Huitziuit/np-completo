import random

#calcula el valor de todos los elementos
def suma_v(elementos):
    suma=0
    for elemento in elementos:
        suma+=valores[elemento]
    return suma

#calcula el peso de todos los elementos
def suma_p(elementos):
    suma=0
    for elemento in elementos:
        suma+=pesos[elemento]
    return suma

#elegir primer elemento
def inicio():
    return random.randint(0,len(decisiones)-1) 

#operaciones
def intercambiar(elementos):
    for elemento in elementos:
        for n in range(-radio_vecindario,radio_vecindario+1):#    radio=3  obj=5     n       
            esta_repetido=False                              # -3, -2, -1, 0, 1, 2, 3, 4
            if(elemento+n in elementos):
                esta_repetido=True
            if( elemento+n >=0 and elemento+n <= no_elementos -1 and esta_repetido==False):
                elemento_temporal=elemento+n
                elementos_temporales=elementos.copy()#[3,6,11],     [3,4,11]
                aux_index=elementos_temporales.index(elemento)           
                elementos_temporales[aux_index]=elemento_temporal
                print("elementos "+ str(elementos))
                print("elemento a variar "+ str(elemento))
                print("nueva combinacion "+ str(elementos_temporales))
                if(comparar(elementos_temporales)):
                    return True
    return False #retorna false si no se dio ningun intercambio

def agregar(elementos):
    for elemento in elementos:
        for n in range(-radio_vecindario,radio_vecindario+1):
            esta_repetido=False
            if(elemento+n in elementos):
                esta_repetido=True
            if (elemento+n >=0 and elemento+n <= no_elementos-1 and esta_repetido==False):
                elemento_temporal=elemento+n
                elementos_temporales=elementos.copy()
                elementos_temporales.append(elemento_temporal)
                print("mochila "+ str(elementos))
                print("elemento a variar en la mochila"+ str(elemento))
                print("nueva combinacion "+ str(elementos_temporales))
                if(comparar(elementos_temporales)):
                    return True
        return False #retorna false si no se dio ningun intercambio

                

#compara si el valor de los elemetos es mejor al valor actual
#de la busqueda y si no sobrepasa la capacidad 
def comparar(elementos):
    global mejor_valor_local
    global elementos_en_mochila
    peso_elemetos=suma_p(elementos)
    valor_elementos = suma_v(elementos)
    print ("Mejor Valor guardado ----------> "+str(mejor_valor_local))
    print("Valor de la nueva combinacion -> "+str(valor_elementos))
    if (peso_elemetos <= capacidad and valor_elementos > mejor_valor_local):
        mejor_valor_local = valor_elementos
        elementos_en_mochila = elementos
        print("La NUEVA combinacion es MEJOR -> "+ str(elementos_en_mochila)+"\n")
        return True
    else: 
        print("la nueva combinacion NO es mejor"+"\n")
        return False
        

#Variables  globales ----------------------------------------------
capacidad=0
no_elementos=0
pesos = []
valores = []
decisiones= []
peso_optimo=0
valor_optimo=0
radio_vecindario=3 # 3 vecinos a la izquierda y 3 a la derecha

elementos_en_mochila=[]
posibles_elementos=[]#posibles elementos a meter en la mochila 
mejor_valor_local=0

#Guardar datos en arreglos
archivo = open("knapsack/P08.txt","r")
lines=[]
primera_i=True
segunda_i=True
for line in archivo:
    if(primera_i==True):
        capacidad=int(line.rstrip('\n'))
        primera_i=False
    elif(segunda_i==True):
        no_elementos=int(line.rstrip('\n'))
        segunda_i=False
    else:
        linea_actual=line.strip('\n')
        objeto=linea_actual.split('\t')
        pesos.append(int(objeto[0]))
        valores.append(int(objeto[1]))
        decisiones.append(int(0))
#borrar ultimo elemento de los arreglos
peso_optimo=pesos[-1]
valor_optimo=valores[-1]
pesos.pop()
valores.pop()
decisiones.pop()

print(str(capacidad) + " " + str(no_elementos))
for n in range(len(pesos)):
    print(str(n) + ": p -> "+ str(pesos[n])+ " v-> " + str(valores[n]))

print("p_O  = " + str(peso_optimo)+ " v_O = "+str(valor_optimo))


#Comienzo de las combinaciones--------------------------------
posibles_elementos.append(inicio())
print("primer elemento -> "+str(posibles_elementos[0]) + " Valor -> " + str(valores[posibles_elementos[0]]))
comparar(posibles_elementos)



for i in range(30):
    if(intercambiar(elementos_en_mochila)==False):
        if(agregar(elementos_en_mochila)==False):
            print("No se puede optimizar mas")
    


print("\n\n\nResultados----------------------------------------")
print(str(elementos_en_mochila))
print("\nPESO OBTENIDO  ->\t" + str(suma_p(elementos_en_mochila)))
print("PESO OPTIMO  -> \t" + str(peso_optimo))


print("\nVALOR OBTENIDO  ->\t"+ str(mejor_valor_local))
print("VALOR OPTIMO  -> \t" + str(valor_optimo))

print("Proximidad al valor optimo: " +"%"+str((mejor_valor_local*100)/valor_optimo))
print("Proximidad al peso optimo: " +"%"+str((suma_p(elementos_en_mochila)*100)/peso_optimo))
