
first_file = open("input.txt", "r")
all_data=first_file.read()
first_file.close()

first_file = open("input.txt", "r")
all_line=first_file.readlines()
first_file.close()

second_file = open("output.txt", "w+")
for line in all_data:
    second_file.write(line)
second_file.close()

count_operator=[]
opertor=['+','-','*','/','%','=','<','>','!','&','|']

total=len(all_line)

print("total line:",total)
for opr in opertor:
    cou=all_data.count(opr)
    count_operator.append(cou)

print("operator = value")
for i in range(len(opertor)):
    print("    ",opertor[i],"     ",count_operator[i])


