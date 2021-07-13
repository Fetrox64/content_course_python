

pregunta_1 = 'manzana' == 'manzana'
pregunta_2 = 2 != 0

pregunta_3 = 4 < 10
pregunta_4 = 4 <= 10

pregunta_5 = 6 > 9
pregunta_6 = 6 >= 9

print('pregunta', 'respuesta')


hay_sol = True
son_las_doce = True

# Se probara el if variando los booleanos

if hay_sol:
    print('Es de dia')
elif not hay_sol and son_las_doce:
    print('Son las 12:00 AM')
else:
    print('Es de noche')


if hay_sol: print('Es de dia')


print('Es de dia') if hay_sol else print('Es de noche')

