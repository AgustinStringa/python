planetas = {'mercurio', 'venus', 'tierra', 'marte',
            'jupiter', 'saturno', 'urano', 'neptuno'}

print('Pluton' in planetas)
nuevo_elemento = 'pluton'

if(not(nuevo_elemento in planetas)):
    planetas.add(nuevo_elemento)

print(planetas)
# puede usarse la funcion .discard() en lugar de .remove()
# la ventaja de la primera es que no lanza un error en caso de no encontrar el elemento pasado por parametro
# remove si lo hace
planetas.remove('venus')
print(planetas)

planetas.clear()
print(planetas)

del planetas
