f = open('student1.txt', 'r')
b=f.read()
m=1
i = 0
for i in (b) :
    if i=='\n':
        m+=1
print(m)
f.seek(0)
for i in range(m):
    c=f.readline()
    for j in c:
        if "delhi" in c:
            s=open('delhi.txt', 'r+')
            if c not in s:
                s.write(c)
        elif "shimla" in c:
            m=open('simla.txt', 'r+')
            if c not in m:
                m.write(c)
        else:
            k=open('other.txt', 'r+')
            if c not in k:
                k.write(c)
