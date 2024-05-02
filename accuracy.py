import math
with open(r"C:\Users\Admin\Desktop\CRF++-0.58\check_accuracy.txt","r",encoding ="utf-8") as file:
    lines = file.read()
    listline = lines.split("\n")
    listline = listline[:-1]
a=0
b=0
c=0
x=0
y=0
z=0
m=0
n=0
p=0
for i in listline:
    row = i.split("\t")
    if len(row) == 1:
        continue
    if row[2] == 'B-NP' and row[2]==row[3]:
        a+=1
    elif row[2] =='B-NP' and row[2]!=row[3]:
        b+=1
    elif row[2] !='B-NP' and row[3]=='B-NP':
        c+=1
        
    elif row[2] == 'I-NP' and row[2]==row[3]:
        x+=1
    elif row[2] =='I-NP' and row[2]!=row[3]:
        y+=1
    elif row[2] !='I-NP' and row[3]=='I-NP':
        z+=1
        
    if row[2] == 'O' and row[2]==row[3]:
        m+=1
    elif row[2] =='O' and row[2]!=row[3]:
        n+=1
    elif row[2] !='O' and row[3]=='O':
        p+=1
pre_B_NP = a/(a+c)
re_B_NP = a/(a+b)
f1_B_NP = 2*pre_B_NP*re_B_NP/(re_B_NP+pre_B_NP)
pre_I_NP = x/(x+z)
re_I_NP = x/(x+y)
f1_I_NP = 2*pre_I_NP*re_I_NP/(re_I_NP+pre_I_NP)
pre_O = m/(m+p)
re_O = m/(m+n)
f1_O = 2*pre_O*re_O/(re_O+pre_O)
print("Precision of B-NP: ", pre_B_NP)
print("Recall of B-NP: ", re_B_NP)
print("F1 of B-NP: ", f1_B_NP)
print("Precision of I-NP: ", pre_I_NP)
print("Recall of I-NP: ", re_I_NP)
print("F1 of I-NP: ", f1_I_NP)
print("Precision of O: ", pre_O)
print("Recall of O: ", re_O)
print("F1 of O: ", f1_O)
print("--------------------")
print("Recall:", (re_B_NP+re_I_NP+re_O)/3)
print("Precision:", (pre_B_NP+pre_I_NP+pre_O)/3)
print("F1:", (f1_B_NP+f1_I_NP+f1_O)/3)