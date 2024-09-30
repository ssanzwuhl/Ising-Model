from string import ascii_lowercase
from time import sleep
units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decades = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def translator(n):
    if n<10:
        return units[n-1]
    elif n>=10 and n<20:
        return tens[n%len(tens)]
    elif n>=20 and n<100:
        return decades[(n//10)%len(decades)] + units[(n-1)%10]
    else:
        return units[n//100] + "hundredand" + translator(n%100)

cont = 0
for i in range(1, 1000):
    sleep(0.1)
    print(translator(i))
    cont += len(translator(i))
print(cont)