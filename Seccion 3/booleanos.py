verdad = True
noverdad = False
print(verdad or noverdad)
print(verdad and noverdad)
print((not verdad) or not noverdad)

if (verdad or noverdad):
    print("Alguno de los dos valores es verdadero")
else:
    print("no hubo valor alguno con valor de verdad TRUE")
