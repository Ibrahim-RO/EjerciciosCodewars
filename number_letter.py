""" 
Tu tarea consiste en escribir una función que reciba como único argumento una cadena que contenga números delimitados por espacios. Cada número tiene una letra dentro.

Example : "24z6 1x23 y369 89a 900b"
Como se muestra arriba, esta letra del alfabeto puede aparecer en cualquier parte del número. Debe extraer las letras y ordenar los números según sus letras correspondientes.

Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246 (ordered according to the alphabet letter)
Aquí viene la parte difícil, ahora tienes que hacer una serie de cálculos sobre los números que has extraído.

La secuencia de cálculos es + - * /. Las reglas matemáticas básicas NO se aplican; debes realizar cada cálculo exactamente en este orden.
Esto tiene que funcionar para cualquier tamaño de números enviados (después de la división, volver a la suma, etc.).
En el caso de letras del alfabeto duplicadas, hay que ordenarlas según el número que apareció primero en la cadena de entrada.
Recuerde también redondear la respuesta final al número entero más cercano.
Examples :
"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299
"24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414
"10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60
"""
import operator
from itertools import cycle

# Diccionario que mapea símbolos a funciones reales
op_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def do_math(st) :
    operators = ['+', '-', '*', '/']
    st_list = st.split(" ")
    new_st_list = []
    for i in st_list:
        letter = ''.join([c for c in i if c.isalpha()])
        number = ''.join([c for c in i if not c.isalpha()])
        new_st_list.append([letter, number])
    new_st_list.sort(key=lambda x: x[0])
    
    operator_cycle = cycle(operators)
    total = int(new_st_list[0][1])
    
    for number in new_st_list[1::]:
        num = int(number[1])
        op_symbol = next(operator_cycle)
        func = op_map[op_symbol]
        total = func(total, num)

    return round(total)
    
string = "111a 222c 444y 777u 999a 888p"
print(do_math(string))