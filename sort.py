import pdb
import re
with open("stockbook.txt","r+") as f:
    lines=f.readlines()
content_list=[]
fenshu_list=[]
for line in lines:
    groups=re.split("\s",line)
    score=groups[-2]
    if re.match(r"^\d.*\d$",score):
        fenshu=float(score.split("*")[0])
        fenshu_list.append(fenshu)

C=sum(fenshu_list)/len(fenshu_list)
C=7.5

for line in lines:
    groups=re.split("\s",line)
    score=groups[-2]
    if re.match(r"^\d.*\d$",score):
        fenshu=float(score.split("*")[0])
        markshu=float(score.split("*")[1])
        R=fenshu
        v=markshu
        m=500
        WR=(v/(v+m))*R+(m/(v+m))*C
        if "贼巢" in line:
            print(1,WR)
            print(v,m,R,C)
        if "股票大作手操盘术" in line:
            print(2,WR)
            print(v,m,R,C)
        content_list.append({'line':line,'WR':WR})
sorted_content_list=sorted(content_list,key=lambda x:x['WR'],reverse=True)
for item in sorted_content_list:
    with open("sorted_stock_book.txt","a+") as f:
        f.write(item['line'])

