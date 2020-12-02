"""
#single alpha & beta
left=input('Enter left part:')
string=input('Enter right part:')
right=string.replace(" ", "")
print("Equation:"+left+'->'+right)


if left==right[0]:
    print('left recurision')
    for i in range(1,len(right)):
        if right[i]=='/':
            print(left+' -> '+right[i+1:]+left+'-prime')
            print(left+'-prime'+' -> '+right[1:i]+left+'-prime'+'|'+'epsilon')
else:
    print('Not left recurision')

"""


#multiple alpha & beta
#E→E+T | E-T | t | s | k
input_string=input('Enter Equation:')
string=input_string.replace(" ", "");


alpha=[]
beta=[]

split_string=string[2:].split('|')

for i in range(len(split_string)):
    for j in split_string[i]:
        if j==string[0]:
            alpha.append(split_string[i].replace(string[0],""))
            break
        else:
            beta.append(split_string[i])
            break


print(string[0]+'→',end="")
for i in range(len(beta)):
    if i==len(beta)-1:
         print(beta[i]+string[0]+'-prime')
    else:
         print(beta[i]+string[0]+'-prime',end="/")


print('\n'+string[0]+'-prime'+'→',end="")
for i in range(len(alpha)):
    #print(string[0]+'-prime'+'→'+alpha[i]+string[0]+'-prime')
    print(alpha[i]+string[0]+'-prime',end="/")

print('epsilon')




