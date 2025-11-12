l1=[1,4,3,2,6,3,7,8,10,3,3]
l2=[x for x in l1 if x%2==0]
print(l2)
print(5 % 10 + 10 < 50 and 29 >= 29)
print(15 & 22)
print(7 ** 2 // 9 % 3)

with open(r"myfile1.txt",'w+') as a:
    a.write("hi\n hello \n")
    a.seek(0)
    c=a.readlines()
    print(len(c))
u=12
v=18
l = [i for i in range(1,u + 1) if u % i == 0]
m=[i for i in range(1,v + 1) if v % i == 0]
print('\n')
for i in l :
    if i in m:
        print(i)