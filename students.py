# Имена втудентов в текстовом файле написаны на английском, так как
# при написании их на русском Питон ругался на кодировку
with open('file.txt','r') as f:
    data = [l.strip() for l in f.readlines()]
students=0
math=0
rus=0
phys=0
for student in data:
    students+=1
    a=student.split(';')
    math+=int(a[1])
    rus+=int(a[2])
    phys+=int(a[3])
    marks=int(a[1])+int(a[2])+int(a[3])
    print(marks/3)
average=[str(math/students),str(rus/students),str(phys/students)]
print (' '.join(average))