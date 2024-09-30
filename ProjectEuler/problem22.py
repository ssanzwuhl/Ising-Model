from string import ascii_uppercase as ABC
names_score = []
def name_score(name):
    return sum([ABC.index(j) + 1 for j in name])
with open('./p022_names.txt') as openfile:
    names = sorted(openfile.read().replace('"', '').split(','))


print(sum([name_score(names[i]) * (i+1) for i in range(len(names))]))
