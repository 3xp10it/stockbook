import pdb
import os
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
        content_list.append({'line':line,'WR':WR})
sorted_content_list=sorted(content_list,key=lambda x:x['WR'],reverse=True)
for item in sorted_content_list:
    with open("sorted_stock_book.txt","a+") as f:
        f.write(item['line'])



with open("sorted_stock_book.txt","r+") as f:
    lines=f.readlines()
with open("format_stock_book.txt","a+") as f:
    f.write("|书名|链接|评分|\n")
for line in lines:
    groups=re.split(r"\s+",line)
    line="|"+"|".join(groups)+"\n"
    with open("format_stock_book.txt","a+") as f:
        f.write(line)
os.system("rm sorted_stock_book.txt")
print("format finished,please visit https://www.tablesgenerator.com/markdown_tables to paste the content of format_stock_book.txt")
choose=input("Open format_stock_book.txt? Y|n")
if choose not in ['n','N']:
    os.system("/Applications/MacVim.app/Contents/MacOS/Vim format_stock_book.txt")
os.system("rm format_stock_book.txt")
