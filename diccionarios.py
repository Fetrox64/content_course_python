

diccionario = {
    'llave_1': 'valor_1',
    'llave_2': 'valor_2',
    'llave_n': 'valor_n'
}


promedio_notas = {
    'Lenguaje': 6.5,
    'Matematica': 2.0,
    'Historia': 5.0
}


# Para agregar 
promedio_notas['Artes'] = 6.5

# Para obtener
promedio_matematica = promedio_notas['Matematica']

# Para alterar
promedio_notas['Matematica'] = 6.0

# Para eliminar
promedio_notas.pop('Historia')


print(promedio_matematica)

