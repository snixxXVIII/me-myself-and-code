a = int(input('Insira a área em m²: '))

T = a / 18

P = T * 80

import math 

print( math.ceil(T), 'Latas de Tinta')
print( math.ceil(P), 'reais')