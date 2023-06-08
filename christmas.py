import os

with open("employees.txt", "r") as my_file:
    names = my_file.read().splitlines()

template = "template.txt"
with open(template, "r") as file:
    template = file.read()

for name in names:
    
    seperated = name.split()
    first_initial = seperated[0][0]
    first_initial =template.replace("NAME", names)
    print(first_initial)

with open(template, "w") as cards:
        cards.write(first_initial)

print(cards)
