"""
con el :.5f indico el formato del parametro que caberá en dicho lugar
"""

dr = 'Dave'
vg = 'Kurt'
a = 100

description = 'Bateria -> {1}, Vocalista y guitarrista -> {2}, puntaje: {0:.5f}'.format(a,dr,vg)
description = 'Bateria -> {drum}, Vocalista y guitarrista -> {cant}, puntaje: {po:.5f}'.format(po=a,drum=dr,cant=vg)

print(description)


#
diccionario = {'nombre':'barcelona', 'pais':'españa', 'estado actual':'muerto'}

mensaje_nuevo = 'el club es {club[nombre]} se encuentra en {club[pais]} y está {club[estado actual]} '.format(club=diccionario)
print(mensaje_nuevo)