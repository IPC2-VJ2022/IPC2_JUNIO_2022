manf=open("abc.txt")

for linea in manf:
    if (linea.startswith('abc: ')):
        print(linea)