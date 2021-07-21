

lista = [
    'elemento_1 con posicion o indice 0',
    'elemento_1 con posicion o indice 1',
    'elemento_n con posicion o indice n'
]

lista_materiales = [
    'Lapices',
    'Carton Piedra',
    'Recortes de Gatos',
    'Tijeras',
    'Pintura',
    'Pincel',
]

# Para agregar 
lista_materiales.append('Regla')

# Para obtener
elemento_posicion_2 = lista_materiales[2]
elementos_posicion_del_0_al_4 = lista_materiales[1:4]

# Para alterar
lista_materiales[3] = 'Corta Carton'

# Para eliminar
lista_materiales.remove('Pintura') # para cuando el argumento es el elemento
lista_materiales.pop(0) # para cuando el argumento es el index

print(lista_materiales)

