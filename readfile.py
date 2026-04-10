"""#reading file
from pathlib import Path
path=Path("textfile.py")
read=path.read_text()
s=read.rstrip()# r strip remove white space
s2=s.split()
for i in s2:
    print(i)
p=" "
for j in s2:
    p+=j
#print(p)
#print(len(p))
for i in s2:
    p+=i.rstrip()
print(f"{p[:32]}")
print(len(p))
f=input("Enter no.")
if f in s2:
    print("exist")
else:
    print("doesnt exist")
#writing a line in text file
w=path.write_text("Python programminng")
#writing multiple lines
w2="This is a cat.\n"
w2+="These are cats."
path.write_text(w2)
#Use try blocks when you think error may occur
try:
    print(2/0)
except ZeroDivisionError:
    print("you can't divide numbers with 0")
#example of try blocks
#1
print("Enter two no. to divide\n Enter 'q' to quite")
while True:
    num1=input("Enter a no.")
    if num1=='q':
        break
    num2=input("Enter 2nd no.")
    if num2=='q':
        break
    try:
        ans=int(num1)/int(num2)
    except ZeroDivisionError:
        print("cant divide by zero")
#2
from pathlib import Path
a=Path("Alice.text")
try:
    c=a.read_text()
except FileNotFoundError:
    print(f"{a}file not found")
#working with Text
from pathlib import Path
a=Path("poem.txt")
try:
    r=a.read_text(encoding="utf-8") 
except FileNotFoundError:
    print(f"{a} not found")
s=r.split()
print(len(s))
#working with multiple files
from pathlib import Path
def count(path):
    try:
        a=path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"{path} not found")
    else:
        a2=a.split()
        print(f"{path} has {len(a2)} no. of text") 

files=["textfile.py","para.txt","para2.txt","poem.txt"]
for i in files:
    path=Path(i)
    count(path)
#using try blocks and not letting user know that file doesnt exist
from pathlib import Path
fi=["textfile.py","para.txt","para2.txt","poem.txt","o.txt"]
def count(path):
    try:
        r=path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        s=r.split()
        print(f"{path} no. of text is {len(s)}")

for i in fi:
    path=Path(i)
    count(path)"""
#to remember no.s we use json.loads and to remember texts we use json.dumps



 

