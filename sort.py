import pdb
import os
import re
import sys
import requests
def get_douban_book_score(link):
    rsp=requests.get(link)
    html=rsp.text
    try:
        rating_num=re.search(r'<strong class="ll rating_num " property="v:average"> (\S+) </strong>',html).group(1)
        rating_people=re.search(r'<a href="collections" class="rating_people"><span property="v:votes">(\d*)</span>人评价</a>',html).group(1)
    except:
        #print("get book score error,check the code")
        rating_num="7.0"
        rating_people="50"
    return rating_num,rating_people
    
filename=sys.argv[1]
with open(filename,"r+") as f:
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
    link=re.search(r"(http\S+)",line).group(1)
    fenshu,markshu=get_douban_book_score(link)
    groups=re.split("\s",line)
    R=float(fenshu)
    v=float(markshu)
    m=500
    WR=(v/(v+m))*R+(m/(v+m))*C
    line=groups[0]+"    "+link+"    "+fenshu+"*"+markshu+"\n"
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
