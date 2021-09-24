songs = ['best of you', 'DOA', 'free me',
         'skin and bones', 'everlong', 'long road to ruin']
i = 0

for e in songs:
    e = i
    print(e)
    i += 1


print(f'''
Longitud de la lista: {len(songs)}''')
songs.append('wheels')
songs.insert(1, 'walk')

print(songs)
songs.remove('walk')
print(songs)
