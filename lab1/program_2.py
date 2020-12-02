file = open("input.txt", "r")
lines = file.readline()
file.close()

print("String is:  ", lines)

if lines.isnumeric():
    print('True')
else:
    print('False')
