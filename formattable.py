import re
import pdb
with open("stockbook.txt","r+") as f:
    lines=f.readlines()
with open("format_stock_book.txt","a+") as f:
    f.write("|书名|链接|评分|\n")
for line in lines:
    groups=re.split(r"\s+",line)
    line="|"+"|".join(groups)+"\n"
    with open("format_stock_book.txt","a+") as f:
        f.write(line)
print("format finished,please visit https://www.tablesgenerator.com/markdown_tables to paste the content of format_stock_book.txt")
