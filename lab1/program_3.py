
file = open("input.txt", "r")
lines = file.readlines()
file.close()

all_keyword = ['auto','double','int','struct', 'break','else',
    'long','switch', 'case','enum','register','typedef',
    'char','extern','return','union', 'continue','for',
    'signed','void', 'do','if','static','while', 'default',
    'goto','sizeof','volatile', 'const','float','short','unsigned']

for line in lines:
    for single_keyword in all_keyword:
        if single_keyword in line:
            print(single_keyword,'is found')
