
# partition devuelve en una tupla
# solo separa en 3 valores
# ademas uno de estos es el separador
hora, separador, minutos ='09:15'.partition(':')


"""
print(f'''
hora {hora}
minutos {minutos}
''')
"""

# split dev
time = '14:56:27'
hour, minutes, seconds = time.split(':')

"""
print(f'''
hour: {hour}
minutes: {minutes}
seconds: {seconds}''')
"""