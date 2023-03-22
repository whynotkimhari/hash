import random

file = open("", "w")
values = []
m = int(input())
i = 0
while i < m:
    code = ""
    len = random.randint(1, 100)
    for j in range(len):
        code = code + str(random.randint(0, 1))
    if code not in values:
        values.append(code)
        file.write(code + "\n")
        i += 1

file.close()