heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros),"is the length of the list")

print(heros.append('black panther'))
print(heros)

heros.remove('black panther')
print(heros)
heros.insert(3,'black panther')
print(heros)

heros[3]="doctor strange"
print(heros)