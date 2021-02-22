f = open('student1.txt', 'r')
b=f.read()
count=1
for i in (b) :
    if i=='\n':
        count+=1
print(count)
