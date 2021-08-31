

# Tipo de dato String

variable = 'Buenas tardes'
tipo_dato = type(variable)

print(tipo_dato)


# Tipos de dato int y float

variable = 5000
tipo_dato = type(variable)

print(tipo_dato)

variable = 0.005
tipo_dato = type(variable)

print(tipo_dato)


# Tipo de dato boolean

variable = True | False
tipo_dato = type(variable)

print(tipo_dato)


# Casting

str() # Para convertir a string
int() # Para convertir a entero
float() # Para convertir a decimal
bool() # Para convertir a booleano

promedio = "5.7"
promedio = float(promedio)
promedio_con_decimas = promedio + 0.3

print(promedio_con_decimas)
