import pdb
import re
with open("stockbook.txt","r+") as f:
    lines=f.readlines()
content_list=[]
for line in lines:
    groups=re.split("\s",line)
    score=groups[-2]
    if re.match(r"^\d.*\d$",score):
        fenshu=float(score.split("*")[0])
        markshu=float(score.split("*")[1])
        totalscore=fenshu*1.5/2.5+markshu*1/2.5
        content_list.append({'line':line,'totalscore':totalscore})
sorted_content_list=sorted(content_list,key=lambda x:x['totalscore'],reverse=True)
for item in sorted_content_list:
    with open("sorted_stock_book.txt","a+") as f:
        f.write(item['line'])

