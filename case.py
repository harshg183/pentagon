#upper
a=input("enter a string")
b=""
for i in range(len(a)):
    z=ord(a[i])
    if (z>64 and z<91):
        b=b+chr(z+32)
    else:
        b=b+a[i]
print(b)
#lower
c=input("enter a string")
d=""
for i in range(len(c)):
    w=ord(c[i])
    if (w>96 and w<112):
        d=d+chr(w-32)
    else:
        d=d+c[i]
print(d)
#swap case
p=input("enter a string")
q=""
for i in range(len(p)):
    y=ord(p[i])
    if (y>96 and y<112):
        q=q+chr(y-32)
    else:
        q=q+chr(y+32)
print(q)
print('inside the new branch')
