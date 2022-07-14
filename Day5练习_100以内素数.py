#
#参考答案：https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/code/Day05/prime.py
#以下为个人解答
a=0
for i in range(2,101):
    for j in range(i,0,-1):
        if i%j==0:
            a+=j
    if a-1==i:
        print(i,end=" ")
    a=0