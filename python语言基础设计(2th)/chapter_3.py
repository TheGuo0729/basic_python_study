'''
自己学习python的学习代码
书籍： 《python语言程序设计基础（第2版》 （高等教育出版社）
'''

#学习输出字符

str_1 = input("your favorite actor is :")

print("hahahaha")
print("the first character is {}".format(str_1[0]))
print("the last character is {}".format(str_1[-1]))
print(str_1[1:]) #第一个不输出
print(str_1[0:-1]) #最后一个不输出 等于是[]这个范围被python识别为 左开右闭

#数学运算
import math

print(math.pi), print(math.e)

foundation = 1
effect = 0.01
up = math.pow((foundation + effect), 365)
down = math.pow((foundation - effect), 365)
print("努力{:.8f} , 不努力{:.8f}".format(up, down))


#字符串
week = str("星期一星期二星期三星期四星期五星期六星期天")
num = eval(input("输入星期几（数字1-7）")) #要不然num是str
print(week[num*3 - 3:num*3])

#动态显示进度条
import time
scale = 10
done = "*"
undone = "."
print("——————start——————")
for i in range(scale + 1):
    rate = i * 10
    print(" %{:.0f} $$[{}->>>{}]$$".format(rate, done * i, undone * (scale - i)))
    time.sleep(0.1)
print("——————finish——————")

#现在把这个变成一行不断刷新
print("——————start——————")
for j in range(scale + 1):
    rate = j * 10
    print("\r  %{:.0f} $$[{}->>>{}]$$".format(rate, done * j, undone * (scale - j)), end = '')
    #后面添加 end = '' 前面添加 \r 进行转义
    # end  ='' 意思是每次输出不换行 这次输出完停留在这一行的行尾
    # \r  把光标从队尾移动到队头
time.sleep(0.05)
print("——————finish——————")