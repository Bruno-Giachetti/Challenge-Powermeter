import json

repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

#Parte 1

def borrarRepetidos(lista):
    '''
    En esta funcion primero convierto los datos a string porque es un tipo de dato mas generico que int con la funcion map,
    luego lo convierto a set para eliminar repeticiones, luego lo transformo nuevamente a lista porque se pedia devolver
    una lista y luego ordeno los datos con sorted (esto ultimo es un agregado para dejar todo mas limpio)
    '''
    return sorted(list(set(map(str,lista))))

#Prueba
print(borrarRepetidos(repetidos))

#Parte 2

def valoresComunes(lista1, lista2):
    #Esta funcion se fija los valores repetidos en tipo y valor para que el "5" por ejemplo salga como un valor comun
    return list(filter(lambda x: x in borrarRepetidos(lista1), borrarRepetidos(lista2)))

#Prueba
print(valoresComunes(r,repetidos))

#Parte 3
def transformarADiccionario(entrada):
    return json.loads(entrada)

#Prueba
print(transformarADiccionario(d_str))