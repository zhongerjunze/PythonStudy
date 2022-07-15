#
#参考答案：https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/code/Day05/perfect.py
#以下为个人答案
a=0
for i in range (1,10001):
    for j in range (i,0,-1):
        if i%j==0:
            a+=j
    if a-i==i:
        print(i)
    a=0