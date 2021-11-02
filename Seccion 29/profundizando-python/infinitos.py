import math
from decimal import Decimal
#infinito_positivo = float('inf')
#infinito_negativo = float('-inf')

#infinito_positivo = math.inf
#infinito_negativo = -math.inf

infinito_positivo = Decimal('Infinity')
infinito_negativo = Decimal('-Infinity')

print(infinito_positivo > 0)
print(infinito_negativo < 0)
print(math.isinf(infinito_positivo))
print(math.isinf(infinito_negativo))

