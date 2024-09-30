from sys import argv

def media(data):
    return sum(data)/len(data)
def dispersion(data):
    return (max(data)-min(data))/media(data)

"""
data = []
counter = 1
a = input('Introduce dato 1: ')
data.append(int(a))
while a != '':
    counter += 1
    a = input('Introduce dato {}: '.format(counter)
    data.append(int(a))

"""

n = int(input('Dame cuantos: '))

data = []
for i in range(n):
    dato = input('Dame el dato {} :'.format(i))
    dato = float(dato)
    data.append(dato)

print(dispersion(data))


print(media(data))
