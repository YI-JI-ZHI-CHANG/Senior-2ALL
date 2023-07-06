'''
实践操作（数据为整数）:
1. 创建含10个元素个数的数组a，存储9个数据的升序序列
2. 随机产生一个整数
3. 将该数插入到适当位置，使序列依然有序
'''
from random import randint

a=[0]*10
a[0]=randint(10,20)
for i in range(1,9):
    a[i]=a[i-1]+randint(3,10)
print("a：",a)

b=[i+randint(3,5) for i in range(1,100,10)]
print("b：",b)

x=randint(10,70)
print("x：",x)
#先查找位置，再移动数据
for i in range(len(a)):
    if x<a[i]:
        break
for j in range(len(a)-1,i,-1):
    a[j]=a[j-1]
a[i]=x   # a[j+1]=x

'''
#边查找位置，边移动数据：
#for 循环：
for i in range(len(a)-2,-1,-1):
    if x<a[i]:
        a[i+1]=a[i]
    else:
        a[i+1]=x
        break

#while 循环：
i=len(a)-2
while x<a[i]:
    a[i+1]=a[i]
    i-=1
a[i+1]=x

i=len(a)-1
while x<a[i-1]:
    a[i]=a[i-1]
    i-=1
a[i]=x
'''
print(a)