

listLetter_minus = {chr(i+96):i for i in range(1,27)}
listLetter_majus = {chr(i+64):i for i in range(1,27)}

listLetter = dict()
for i in range(1,27):
     listLetter[i] = listLetter_minus.keys()
     print(listLetter)