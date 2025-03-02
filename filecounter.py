file = open('codingal.txt', 'r')
counter = 0
content = file.read()
CoList = content.split("\n")

for i in CoList:
    if i:
        counter += 1
print(counter)