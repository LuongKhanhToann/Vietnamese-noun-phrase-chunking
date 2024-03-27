import re
import os
def take(s):
    pattern = r"\(([^\(\)]+)\)"
    matches = re.findall(pattern, s)
    return matches
def check(s):
    char_open = s.count("(")
    char_close = s.count(")")
    return char_open - char_close
file_path = r"C:\Users\Admin\Desktop\CRF++-0.58\data_train.txt"
def check_O(s):
    if s.find("như")>=0 or s.find("và")>=0  or s.find("tại")>=0 or s.find("PUNCT")>=0:
        return True
    return False
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.split("\n")
line = []
for i in content:
    if i.find("(") >=0:
        line.append(i)
        continue
group_N = []
i = 0
while(i<len(line)):
    line[i] = line[i].replace("(S ","").replace("(S-SPL ","").replace("(SQ","").replace("(S-CMD ","").replace("(SBAR","").replace("(S-TTL","").replace("(S-TC ","").replace("(S-TPC ","").replace("(S-TH ","").replace("(S-PV ","").replace("(SQ ","").replace("(S-SUB","").replace("(SBAR-DOB","")
    N = [line[i]]
    # start 
    if line[i].find("NP")>=0:
        q = check(line[i])
        if q <= 0:
            group_N.append(N)
            i = i+1
            continue
        while(True):
            i = i+1
            q+=check(line[i])
            if q<=0:
                N.append(line[i])
                break
            N.append(line[i])
    group_N.append(N)
    i = i+1
result = []
for i in group_N:
    t = []
    for j in i:
        t.append(j.replace("\t",""))
    result.append(t)
final_result = []
for i in result:
    if i[0].find("NP")>=0:
        sequence = []
        for j in i:
            np = take(j)
            for t in np:
                sequence.append(t)
        final_result.append(sequence[0]+" B-NP")
        status = True
        for k in range(1,len(sequence)):
            if check_O(sequence[k]) == True:
                final_result.append(sequence[k]+" O")
                status = False
            elif status == True:
               final_result.append(sequence[k]+" I-NP")
            elif status == False:
                final_result.append(sequence[k]+" B-NP")
                status = True
    else:
        c = take(i[0])
        for j in c:
            j = j + " O"
            final_result.append(j)
# swap 
swap = []
for i in final_result:
    a = i.split(" ")
    s = ""
    for t in a[1:len(a)-1]:
        s+=str(t)
    c = s + " "+a[0] + " " + a[len(a)-1]
    swap.append(c)
file_path = 'data_after_preprocessing.txt'
with open(file_path, "w", encoding="utf-8") as file:
    for i in swap:
        file.write(i+"\n")
