'''
两正整数和为667，最小公倍数是最大公约数的120倍
求这两个正整数
'''

def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

for a in range(1,667):
    if gcd(a,667-a)*120 == lcm(a,667-a):
        print("x=",a,"y=",667-a)