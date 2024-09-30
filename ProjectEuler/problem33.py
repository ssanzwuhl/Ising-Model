#Hay que escribir una función que pueda calcular la intersección entre dos listas
def intersection(number1, number2): #Inputs 2 numbers, as strings
    stripping = ''
    number1 = str(number1)
    number2 = str(number2)
    for i in number1:
        if i in number2:
            number2 = number2.replace(i, '', 1)
            stripping += i

    for i in stripping:
        number1 = number1.replace(i, '', 1)

    #return int(number1)/int(number2)
    if (number1 != '' or number2 != '') and number2 != '0' and stripping != '':
        return int(number1)/int(number2)
    else:
        return 0

multiply = 1

for den in range(10, 100):
    for num in range(10, den):
        if not num%10:
            continue
        if num/den == intersection(num, den):
            multiply *= num/den
print(multiply)


            




