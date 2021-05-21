# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 15:43
# @Author  : Guoji
# @Email   : Guojinjia0729@Gmail.com
# @File    : chapter4.py

# break 和 continue 的区别

for s in 'ABCDEF':
    for i in range(3):
        print(s, end='')
        if s == 'D':
            break
        elif s == 'F':
            continue
# continue 会忽略掉这个循环中 continue 后面的所有内容
# continue 放在最后一行没有任何意义

for letter in 'Python':   # First Example
    if letter == 'h':
        continue
    print('Current Letter :', letter)

# continue 只能做到在一个大循环里面 特殊的几项比别人少些什么
# 就像 这个代码，h这一项少了一个 print
# 似乎做不到比别人多些什么
# 记住 ： print 的位置应该与 if 相持平 而不是与 continue 相持平

import random
x = random.random()
print(x)
y = random.randint(1, 10) # 左右都是闭区间
print(y)

# expect 和 else
try:
    num = eval(input('请输入一个整数'))
except NameError:
    print('整数啊！大哥！整数！！！')
except OverflowError:
    print('哥，小一点试试')
else:
    str_1 = 'abcdefghijklm'
    print(str_1[num])
finally:
    print('反正就结束了，爱咋咋把')

# 记住！ 把你要判断的句子写在 try 里面
# 剩下要执行的都写在 else 里面
# Error 也是有讲究的啊！！！



