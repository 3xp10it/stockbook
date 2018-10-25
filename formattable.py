import re
import pdb
with open("stockbook.txt","r+") as f:
    lines=f.readlines()
for line in lines:
    groups=re.split(r"\s+",line)
    line="|"+"|".join(groups)+"\n"
    with open("format_stock_book.md","a+") as f:
        f.write(line)
