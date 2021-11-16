import pandas as pd
import random
SEPARADOR = ("x" * 20) + "\n"

#creacion de un dataframe a partir de un ciccionario
diccionario_notas_aleatorias = {\
    "Fernanda":[random.randrange(60,101) for x in range (7)], \
    "Blanca" : [80,100,57,90,80,10,80], "Arath" : [80,70,57,100,80,90,60], "Luis Angel" : [20,100,100,90,60,70,80],\
    "Ruben" : [100,100,100,100,60,70,80], "Erik" : [100,100,100,100,80,70,60], "Eduardo" : [70,80,90,100,90,80,90]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index =["Estadistica", "Base de Datos", "Contabilidad", "Estructura de BD",\
               "Liderazgo", "Creatividad", "Macroeconomia"]

notas.to_csv (r'Notas.csv', index=True, header=True)
print("¡Guardado!")
print(SEPARADOR)

notas = pd.read_csv("Notas.csv", index_col=0)
print(notas)
print(SEPARADOR)

def estadistica(notas_aleatorias):
    notas= pd.Series(notas_aleatorias)
    estadistica = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()],
                            index=['min', 'max', 'media', 'desviacion tipica'])
    return estadistica

notas1 = pd.read_csv("Notas.csv", index_col=0)
print(notas1)
print(SEPARADOR)
notasp = {"promedios":notas1.mean()}
print(notasp)
def estadistica_notas(notas2):
    notas2 = pd.Series(notas2)
    estadisticos = pd.Series([notasp["promedios"].min(), notasp["promedios"].max(), notas2["promedios"].mean(), notas2["promedios"].std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticos
print(estadistica_notas(notasp))

