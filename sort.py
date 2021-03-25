import pdb
import time
import os
import re
import sys
import requests
chrome_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
def get_douban_book_score(link):
    rsp=requests.get(link,headers=chrome_headers)
    html=rsp.text
    try:
        rating_num=re.search(r'<strong class="ll rating_num " property="v:average"> (\S+) </strong>',html).group(1)
        rating_people=re.search(r'class="rating_people"><span property="v:votes">(\d*)</span>人评价</a>',html).group(1)
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
    #这里不sleep会被ban
    time.sleep(3)
    fenshu,markshu=get_douban_book_score(link)
    groups=re.split("\s",line)
    R=float(fenshu)
    v=float(markshu)
    m=500
    WR=(v/(v+m))*R+(m/(v+m))*C
    line=groups[0]+"    "+link+"    "+fenshu+"*"+markshu+"\n"
    content_list.append({'line':line,'WR':WR})
sorted_content_list=sorted(content_list,key=lambda x:x['WR'],reverse=True)
_time_str=str(time.time())
sorted_stock_book="sorted_stock_book_%s" % _time_str
format_stock_book="format_stock_book_%s" % _time_str
for item in sorted_content_list:
    with open(sorted_stock_book,"a+") as f:
        f.write(item['line'])



with open(sorted_stock_book,"r+") as f:
    lines=f.readlines()
with open(format_stock_book,"a+") as f:
    f.write("|书名|链接|评分|\n")
for line in lines:
    groups=re.split(r"\s+",line)
    line="|"+"|".join(groups)+"\n"
    with open(format_stock_book,"a+") as f:
        f.write(line)
os.system("rm %s" % sorted_stock_book)
print("format finished,please visit https://www.tablesgenerator.com/markdown_tables to paste the content of %s" % format_stock_book)
choose=input("Open %s? Y|n" % format_stock_book)
if choose not in ['n','N']:
    os.system("/Applications/MacVim.app/Contents/MacOS/Vim %s" % format_stock_book)
os.system("rm %s" % format_stock_book)
