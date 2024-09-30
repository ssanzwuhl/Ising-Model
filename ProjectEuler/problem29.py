top = 100
power_list = [a ** b for a in range(2, top+1) for b in range(2, top+1)]
print(len(set(power_list)))