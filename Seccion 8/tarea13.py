monto = float(input('introduce el monto a pagar '))
interes = float(
    input('introduce el (porcentaje)% a aumentar el monto. (Ej: 20) '))


def calcular_total(pago_sin_impuesto, impuesto):
    total_pago = pago_sin_impuesto + (pago_sin_impuesto * impuesto / 100)
    return total_pago


print(
    f'Para un pago de {monto} y un impuesto del {interes} porciento, el total a pagar es {calcular_total(monto, interes)}')
