from underthesea import pos_tag
import subprocess
import os
import re 

with open(r"C:\Users\Admin\Desktop\CRF++-0.58\1000_sentences.txt","r", encoding='utf-8') as file:
    sentence = file.read()
    list_line = sentence.replace(".","").replace("\n"," . ").replace(",,",",").replace(","," , ")
    #print(pos_tag(content))
    list_line1 = list_line.split(" ")
if os.path.exists("1000_sentences_after_pre.txt"):
    os.remove("1000_sentences_after_pre.txt")
with open("1000_sentences_after_pre.txt",'a',encoding='utf-8') as file:
    for i in list_line1:
        if len(i) != 0:
            sentence1 = str(pos_tag(i)[0])
            sentence1 = sentence1.replace("('","").replace("')","").replace("', '"," ")
            file.write(sentence1+"\n")
command = "crf_test -m model.sh 1000_sentences_after_pre.txt > final_output4.txt"

#Bằng cách thêm os.system(command) bên ngoài vòng lặp, bạn đảm bảo rằng lệnh crf_test sẽ được thực hiện sau khi mỗi dòng trong list_line1 được xử lý.
# Sử dụng subprocess để chạy lệnh
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
with open('final_output4.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
# Khai báo biến để lưu trữ chuỗi B-NP hoặc I-NP liên tiếp
current_phrase = []
output = []

list_word = ['C','V']
list_token = ['phía','phùng','lại','bậc','khuất','nhiên','vung','gập','góc','tầm','ngước','dang','bế','sau','một','cả','gì','đó','đang','đội','dưới','cằm','cả','ngoài','bên','trong','gáy','hông','chìa','khóa','lưng','điện','thoại']
list_token2 = ['có','phục','đến','khuyên','buộc','rẽ','và','niên','đứng','qua','đan','ghi','thanh','niên','dép','pha','học','sinh','trắng','dài','xách','chấm','cắt','kính','liền']
list_pos = ['M','A']
# Lặp qua từng dòng trong tệp tin
for line in lines:
    # Tách dòng thành các phần tử
    parts = line.strip().split('\t')
    if (len(parts) == 3):
        token, pos, label = parts
        token = token.lower()
        if pos in list_word:
            label = 'O' 
        if pos == 'N' or token== 'nam'or token in list_token2 or pos in list_pos:
            label = 'I-NP' 
        if token in list_token:
            label = 'O'    
        if pos != 'CH' and label =='O':
            token = ","
        if token != ".":
            current_phrase.append(token)
        else:
            current_phrase.append(token)
            current_phrase = " ".join(current_phrase)
            current_phrase = current_phrase.replace(" , , , , "," , ").replace(" , , , "," , ").replace(" , , "," , ")
            current_phrase = current_phrase.replace(" , ."," .").replace(" .", "")
            current_phrase = current_phrase.lower()
            output.append(current_phrase)
            current_phrase = []

# Kiểm tra xem có chuỗi cuối cùng không được thêm vào danh sách
if current_phrase:
    current_phrase = " ".join(current_phrase)
    current_phrase = current_phrase.replace(" , , , , "," , ").replace(" , , , "," , ").replace(" , , "," , ")
    current_phrase = current_phrase.replace(" , ."," .").replace(" .", "")
    current_phrase = current_phrase.lower()
    output.append(current_phrase)


list_np = ["áo","cổ","quần","váy","người","cô","cậu","chàng","ông","nữ","nam","em","anh" ,"bạn","bác",
        "giày" , "giầy" , "dép" , "tất" , "boot" , "bốt" , "chân" ,"gối" ,"tóc", "đầu","mũ", "nón","ba_lô", 
        "balo", "ví", "túi","khăn", "vai", "vòng", "tay","mặt","khẩu","kính"]            
output2 =[]
#Loại bỏ các danh từ có len = 1 vì nó không mang nhiều ý nghĩa
for text in output:
    text1 = text.strip().split(" , ")
    new_text1 = []
    remove_first = False
    for i in text1:
        j = i.split(" ")
        if not remove_first:
            remove_first = True
        elif len(j) == 1:
            continue
        new_text1.append(i.replace(", ",""))
    text = " , ".join(new_text1)
    output2.append(text)
if os.path.exists("run_project4.txt"):
    os.remove("run_project4.txt")
with open("run_project4.txt",'a',encoding='utf-8') as file:
    for phrase in output2:
        file.write(phrase+"\n")