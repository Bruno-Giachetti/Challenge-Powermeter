import json

repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

#Parte 1
lista_1 = list(set(map(str,repetidos)))
#Parte 2
lista_2 = list(set (repetidos) and set(r))
#Parte 3
diccionario = json.loads(d_str)

