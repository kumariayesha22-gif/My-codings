"""n=int(input("enter a no."))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
s=0
for i in range(1,11):
    s+=i
print(s)
n=int(input("enter a no."))
f=1
for i in range(1,n+1):
    f=f*i
    print(f)
for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()
x=0
for i in range(3):
    for j in range(4):
        x=x+1
        print(x,end=" ")
    print()
x=10
for i in range(3):
    for j in range(3):
        x=x-1
        print(j,end=" ")
    print()
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")


    
range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()
n=int(input("enter a no."))
for i in range(n,n+1):
t=0
a=int(input("no."))
b=int(input("no."))
t=a
a=b
b=t
print(a)
print(b)
a=int(input("enter ano."))
b=int(input("enter a no."))
if a>b:
    print(a)
else:
    print(b)
a=int(input("enter a no."))
b=int(input("enter a no."))
c=int(input("enter a no."))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
n=int(input("enter a no."))
for i in range (1,n+1):
    if n%i==0:
        print(i)
a="Hello" *3
print(a,end=" ")
is="heelo"
s2="z"+s[1: ]
print(s2
s="Heyy Ayesha"
c=0
z=0
for i in s:
    if i=="a" or i=="i" or i=="o" or i=="u" or i=="e" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        c+=1
        print(c,end=" ")
    
S=["my","name","is"]
t=" ".join(S)
print(t)
s="hii everybody"
t=s.split(s)
print(len(t))

a=[5,"apple",314,"grapes"]
t=" ".join([str(i) for i in a])
print(t)
a="Hii"
t=a.count(" ")-1
print(a)

a="Heyy Everybody"
t="".join(reversed(a))
print(t)

a="Hello String"
t=a[::-1]
print(t)
s="hello world"
t=s.replace("o","")
print(t)
import re
s="hello world"
t=re.sub("[aeiou]","",s)
print(t)

t=0
a=10
b=20
t=a
a=b
b=t
print(a)
s="my computer name is acer"
l=len(s.replace(" ",""))
print(l)
t="why are you running"
c=0
for i in t:
    if i!="":
        c+=1
print(c)
s="haaye haaye"
t=s.split()
m=[i for i in t if len(i)%2==0]
z=" ".join(m)
print(z)
l=[10,31,60,70]
l.sort(reverse=True)
print(l[1])
t=(20,30,129,29,98,94,62)
k=2
t2=sorted(t)
min=t2[:k]
max=t2[-k:]
print(min)
print(max)
a=[8,9,78,52]
r=[(n,n**3) for n in a]
print(r)
a=[9,8,7,6,5]
b=(88,22,78,98)
c=[1,5,6,2]
a.extend(b)
print(a)
d=b+tuple(c)
print(d)
t=(90,60,3279829,74979344839)
c=0
for i in t:
    c+=i
print("sum of list:",c)
l=[89,90,90,92,97]
t=0
p=1
for i in range(5):
    t+=l[i]
for i in range(5):
    p=t/5
print(" total no.",i+1,"=",l[i])
print(" total no.",t
      ," average no.",p)
l=[]
t=0
n=int(input("enter no. of subjects="))
for i in range(n):
    a=int(input("enter marks"))
    l.append(a)
    t=t+l[i]
for i in range(n):
    p=t/n
print("total no.",i+1,"=",l[i],
      "total marks=",t,
      "average marks=",p)
l=[]
n=int(input("enter size of the list"))
i=0
for i in range(n):
    a=int(input("enter no. of elements"))
    l.append(a)
print(l)
so=0
se=0
p=1
s=0
for i in range(n):
    if i%2==0:
        se+=l[i]
    else:
        so+=l[i]
    s+=l[i]
    p=p*l[i]
print("sum of even no.s=",se)
print("sum of odd no.s=",so)
print("product ofno.s=",p)
print("sum of no.s=",s)
l=[]
s=0
p=1
n=int(input("enter size of the list"))
for i in range(n):
    a=int(input("enter elements"))
    l.append(a)
print(l)
for i in range(n):
    if l[i]%5==0:
        s+=l[i]
        p=p*l[i]
print("enter sum of no. which is divisible by 5",s)
print("enter product of it",p)
l=[]
n=int(input("enter size"))
for i in range(n):
    a=int(input("enter element"))
    l.append(a)
print("original list",l)
for i in range(n):
    if l[i]%2==0:
        l[i]+=10
    else:
        l[i]+=5
print("changed list",l)
l=[]
n=int(input("enter size"))
for i in range(n):
    a=int(input("enter an element"))
    l.append(a)
print("original string",l)
for i in range(0,n-1,2):
    l[i+1],l[i]=l[i],l[i+1]
print("swapped ",l)
n=int(input("enter"))
for i in range(0,n-1,2):
    print(i)
a="hello world"
n=a[::-1]
print(n)
s = input("Enter a string: ")
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)
i=1
while i>6:
    print(i)
    i+=1
age = 28

# the test condition is always True
while age > 19:
    print('Infinite Loop'
b=input("enter a binary")
s=0
for i in range (len(b)):
    s+=2**i*int (b[i])
print(s)

b=int(input("enter no."))
s=0
for i in range (b):
    s+=2//i%int(b[i])
print(s)
# Easy program: binary to decimal using for loop

binary_str = input("Enter a binary number: ")

decimal_num = 0

# Loop through digits directly
for digit in binary_str:
    decimal_num = decimal_num * 2 + int(digit)

print("Decimal representation:", decimal_num)
binary = input("Enter a binary number: ")

decimal = 1

for bit in binary:
    decimal = decimal * 2 + int(bit)

print("Decimal value:", decimal)
i=2
while i<22:
    print(i)
    i+=2
a=int(input("enter starting no."))
b=int(input("enter ending no."))
for i in range(a,b+1):
   if i%2==0:
       print(i)
n=int(input("enter no."))
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        c+=i
print("total factors",c)
n=int(input("enter a no."))
sm=n
for i in range(1,11):
    n=int(input("enter a no."))
    if n<sm:
        sm=n
print("smallest no.",sm)
h=1
a=int(input("enter a no."))
b=int(input("enter ano."))
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        h=i
l=a*b/h
print("enter lcm=",l)
print("enter hcf",h)
n=int(input("enter a no."))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print("reversed no.",r)
a=int(input("enter a no."))
b=int(input("enter last no."))
for i in range(a,b+1):
    if i%2==0:
        print(i)
s=0
n=int(input("enter a no."))
for i in range(1,n+1):
    s=s+i
print("sum=",s)
p=1
n=int(input("enter a no."))
for i in range(1,n+1):
    p=p*i
print("factorial",p)
c=0
n=int(input("enter a no."))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        c+=1
print("enter sum of given factors",c
c=0
n=int(input("enter a no."))
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime no.")
else:
    print("composite no.")
sm=int(input("enter a no."))
for i in range (1,11):
    n=int(input("enter a no."))
    if n<sm:
        sm=n
print("smallest no.",sm)
a,b=0,0
c=int(input("enter a no."))
d=int(input("enter a no."))
for i in range(1,a+1):
    if c%i==0:
        a+=1
for i in range(1,b+1):
    if d%i==0:
        b+=1
if a==2 and b==2:
    if c-d==2 or d-c==2:
        print("yes they are twin prime no.")
    else:
        print("no, they are no twin prime no.")
else:
    print("not a prime no.")
s=0
n=int(input("enter a no."))
while n>0:
    d=n%10
    n=n//10
    s+=d
print(s
n=int(input("enter a no."))
m=n
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
if m==r:
    print("palindrome")
else:
    print("not")
n=int(input("enter a no."))
a=0
b=1
n=int(input("enter a number-"))
c=n
d=n
while n>0:


    e=n%10
    n=n//10
    a+=1
while c>0:
    f=c%10
    c=c//10
    g=f**a
    b+=g
if d==b:
    print("yes,it is an armstrong number")
else:
    print("no,it's not an armstrong number")
c=0
s=input("enter a string")
for i in s:
    if i>="A" and i<="Z":
        c+=1
print("no. of upper case",c)
C=0
S=input("ENTER A STRING")
for i in S:
    if i in "aeiouAEIOU":
        C+=1
print("no. of vowels",C)
n=" "
s=input("enter a string")
for i in s:
    if i>="a" and i<="z":
        n+=chr(ord(i)-32)
print("upper characters",n)
w=input("enter a strig")
a=w.upper()
print(a)
" "s=input("enter a string")
c="".join(reversed(s))
if c==s:
    print("palindrome")
else:
    print("no")
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n)
for i in range(1,101):
    prime(i)
s=input("enter your full name")
n=s[0]
for i in range(len(s)):
    if s[i]==" ":
        n+="."+s[i+1]
print("initials are",n)
c=1
s=input("enter a string")
n=len(s)
for i in s:
    if i==" ":
        c+=1
print("count it",c)
n=" "
s=input("enter a string")
for i in s:
    if i>="a" and i<="z":
        n+=chr(ord(i)-32)
    elif i>="A" and i<="Z":
        n+=chr(ord(i)+32)
print("swapped sentence",n)
s=input("enter a string")
c=len(s)
print("total no. of characters",c)
c=0
d=0
s=input("enter an element")
for i in s:
    if i.isalpha():
        c+=1
    else:
        d+=1
print("no. of alphabet",c)
print("no. of digits",d
u=0
l=0
n=input("Enter an element")
for i in n:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("no. of lower element",l)
print("no. of upper element",u)
s=input("enter a string")
u=s.upper()
l=s.lower()
print("lower cases=",l)
print("upper cases=",u
s=input("enter a string")
sp=0
di=0
for i in s:
    if i.isdigit():
        di+=1
    elif i.isspace():
        sp+=1
print("no. of digits",di)
print("no. of spaces",sp)
s=input("enter a sentenece")
s2=input("enter a word from the sentence")
i=s.count(s2)
print("no. of occurence",i)
s=input("enter a sentence")
s2=input("enter a word to replace")
s3=input("enter new word you want")
r=s.replace(s2,s3)
print("new word",r)
s= input("enter a string")
s2=input("enter word whose string you want")
f=s.find(s2)
print("enter index ",f)
s=input("enter a string")
t=s.title()
print("enter it in a title form",t)
s=input("enter a string")
r=s[::-1]
print("enter it in reverse form",r)
c=0
s=input("Enter a sentence")
s2=s.split()
for i in s2:
    if len(i)==4:
        c+=1
print("no. of words in 4 letter",c)
c=0
s=input("enter a string")
s2=s.split()
for i in s2:
    if i[0] in"aeiouAEIOU" or i[-1] in "aeiouAEIOU":
        print(i)
        c+=1
print("no. of words in which there is vowel",c)
s=input("emter a sentence")s=input("enter a sentence")
s2=s.split()
for i in s2:
    if len(s2)%2!=0:
        print(l[len(l)//2])
    elif len(s2)%2==0:
        print(l[len(l)//2-1],l[len(l)//2-1],end=" ")
s2=s.split()
for i in s2:
    if len(i)<6:
        print(i)
a=input("enter a sentence")
b=input("enter a word")
c=0
s=a.split()
for i in s:
    if i==b:
        c+=1
print("No. of times it occured",c)
s=input("enter a sentence")
s2=s.split()
l=s2[0]
for i in s2:
    if len(i)>len(l):
        i=l
print("longest word",l
s=input("enter a sentenece")
s2=s.split()
if len(s2)%2!=0:
    print(s2[len(s2)//2])
elif len(s2)%2==0:
    print(s2[len(s2)//2-1],s2[len(s2)//2],end=" ")
s=input("enter a string")
s2=s.split()
for i in s2:
    if i==i[::-1]:
        print(i)
s=input("enter a string")
s2=s.split()
print(s2[::-1])
s=input("enter a sentence")
s2=s.split()
for i in s2:
    print(s2[::-1]
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
for i in range(-1,-11,-1):
    print(l[i],end=",")
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
for i in l:
    if i%2==0:
        print(i)
c=0
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
for i in l:
    if i%2==0:
        c+=1
print("no. of even no.s",c)
s=0
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
for i in l:
    if i%2==0:
        s+=i
print("sum of even no.s",s)
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
for i in l:
    if i%2==0:
        print(i,end=",")
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
for i in range(5):
    temp=l[i]
    l[i]=l[9-i]
    l[9-i]=temp
print(l)
a=0
t=0
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
for i in l:
    if i%2!=0:
        t+=1
        a+=i
average=a/t
print("total sum of odd no.s",t)
print("average of odd no.s",average)
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
g=l[0]
s=l[0]
for i in range(10):
    if l[i]>g:
        g=l[i]
    elif l[i]<s:
        s=l[i]
print("enter smallest no.",s)
print("enter greatest no.",g)
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
print("before",l)
for i in range(10):
    if i%2==0:
        l[i]=l[i]//2
    else:
        l[i]=l[i]*2
print("after",l)
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
print("before=",l)
l=l[5:10]+l[0:5]
print("after=",l)
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
print("before",l)
for i in range(0,len(l),2):
    temp=l[i]
    l[i]=l[1+i]
    l[1+i]=temp
print("after",l)
l=[]
for i in range(10):
    n=int(input("enter values"))
    l.append(n)
g=l[0]
g2=l[0]
for i in range(10):
    if l[i]>g:
        g=g2
        g=l[i]
print("second largest no.",g2
s=0
c=0
l=[]
n=int(input("enter no. of values"))
for i in range(n):
    n2=int(input("enter values"))
    l.append(n2)
for i in l:
    c+=1
    s+=i
average=s/c
print("average no.=",average)
for i in range(n):
    if average<l[i]:
        print("no. greater than average",l[i])
l=[]
n=int(input("enter no. of integer values"))
for i in range(n):
    x=int(input("enter values"))
    l.append(x)
print("before sorting",l)
for i in range(n):
    p=i
    for j in range(1+i,n):
        if l[j]<l[p]:
            p=j
    l[i],l[p]=l[p],l[i]
print("after sorting",l)
l=[]
n=int(input("enter range"))
s=0
c=0
a=0
for i in range(n):
    n2=int(input("enter values"))
    l.append(n2)
for i in l:
    s+=i
    c+=1
average=s/c
for i in range(n):
    if l[i]>average:
        a+=l[i]
print("average",average)
print("sum of greater than average",a
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(n)
for i in range(1,101):
    prime(i)
n=int(input("enter range"))
l=[]
for i in range(n):
    s=int(input("enter value"))
    l.append(s)
for ch in l:
    c=0
    for i in range (l,ch+1):
        if ch%i==0:
            c+=1
    if c==2:
        print(ch)
l=[]
n=int(input("enter no. of values"))
for i in range(n):
    x=int(input("enter value"))
    l.append(x)
c=0
s=0
for ch in l:
    for i in range(ch):
        if ch%i==0:
            c+=1
    if c==1:
        s+=ch
print("sum",s)
se=0
so=0
t=eval(input("enter values creating bracket"))
for i in range (len(t)):
    if t[i]%2==0:
        se+=1
    else:
        so+=1
print("no. of even no.s",se)
print("no. of odd no.s",so)
t=eval(input("enter values in bracket"))
mx,mn=t[0],t[0]
for i in range(len(t)):
    if t[i]>mx:
        mx=t[i]
    elif t[i]<mn:
        mn=t[i]
print("enter smallest no.",mn)
print("enter greatest no.",mx)
t=eval(input("enter values in bracket"))
max_element=" "
max_length=t[0]
for i in t:
    if len(i)> max_length:
        max_length=len(i)
        i=max_element
print("maximum word",max_element)
t=eval(input("enter some values"))
for i in t:
    if i[0] in "aeiouAEIOU" or i[-1] in"aeiouAEIOU":
        print(i
t=eval(input("enter values"))
s=0
for i in range (len(t)):
    s+=t[i]
avg=s/len(t)
print("average",avg)
t=eval(input("enter values"))
for i in range(len(t)):
    print(t[i],len(t[i]))
t=eval(input("enter values"))
for i in range(len(t)):
    n=0
    n=len(t[i])
    if n>5:
        print(t[i]
d={}
n=int(input("enter range"))
for i in range(n):
    r=int(input("enter roll no."))
    nm=input("enter name")
    d[r]=nm
print(d)
d={}
n2=int(input("enter rannge"))
for i in range (n2):
    n=input("enter name")
    r=int(input("enter roll no."))
    p=int(input("enter percentage"))
    d[r]=[n,p]
s=0
for x in d:
    s+=d[x][1]
av=s/n2
print("average",av)
d={}
n=int(input("enter no. of products"))
for i in range(n):
    p=input("enter name of the product")
    s=int(input("enter sales"))
    d[p]=[s]
mx=max(d.values())
mn=min(d.values())
for j in d:
    if d[j]==mx:
        print("maximum",mx)
    elif d[j]==mn:
        print("minimum",mn)
for k in d:d
    print(k,d[k],end=" ")
d={}
n=int(input("enter no. of students"))
for i in range(n):
    name=input("enter name")
    r=int(input("enter %"))
    d[name]=r
c=0
for k in d:
    if  d[k]>=80:
        print(k)
        c+=1
print("no. of students who got above 80",c)
d={}
s=input("enter a string")
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    print(i,"it occured",d[i],"times")
d={}
n=int(input("enter range"))
for i in range(n):
    na=input("enter name")
    p=int(input("enter %"))
    adm=int(input("enter admission no."))
    d[na]=[adm,p]
for j in d:
    if d[j][1]>=80:
        print(d[j])
d={}
s=int(input("enter no. of entries"))
for i in range(s):
    nm=input("enter name")
    pn=int(input("enter phone no."))
    d[nm]=pn
a=input("enter name to be searched")
print(d.get(a,"npt  found"))
class student:
    name="karan"
s1=student()
print(s1.name)
s2=student()
print(s2.name)
s3=student()
print(s3.name)
class brand:
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        s=0
        for i in self.marks:
            s+=i
        print("hi",self.name,"your avg",s/3)
s1=student("tony",[90,98,78])
s1.get_avg
class account:
    def __init__(self,balance,acc):
        self.balance=balance
        self.account_no=acc
    def credit(self,amount):
        self.balance+=amount
        print("your account is credited with rs.",amount)
        print("total balance is rs.",self.balance())
    def debit(self,amount):
        self.balance-=amount
        print("your account is debited with rs.",amount)
        print("total balance is rs.",self.balance())
s1=account(10000,1234)
s1.credit(100)"""

