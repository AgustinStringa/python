# cuando se usa \u se agregan 4 caracteres mas para indicar el valor unicode del caracter a insertar

print('HI\u0020WORLD')
ases = 4*'\u0041'
print(ases)

print('No se que saldra: \u2665')
print('No se que saldra: \u02AC')
print('No se que saldra: \u02A7')
print('No se que saldra: \U0001F605')
print('No se que saldra: \U0000267B')