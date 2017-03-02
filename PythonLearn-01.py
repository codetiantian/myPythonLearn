import random

print('-----------PythonLearn--------------')

"""浮点数转变整数"""
strNum = 5.99
num = int(strNum)
print(num)
"""浮点数转变整数时，Python会和PHP操作一致，采用截断操作"""

"""生成1-—100的随机数"""
secret = random.randint(1, 100)

temp = input("请输入你猜想的数字:")

"""isinstance来判断参数是否属于某一种类型，属于返回true，不属于返回false"""
if isinstance(temp, int) :
    guess = int(temp)
else :
    print("请输入1---100的整数")
    guess = 0

if guess == secret :
    print("恭喜，猜正确")
else :
    while guess != secret :
        if guess != 0 :
            if guess == secret :
                print("恭喜，猜正确")
            else :
                if guess > secret :
                    print("大了")
                else :
                    print("小了")
                    
        temp = input("请再次输入你猜想的数字:")
        guess = int(temp)

print("游戏结束，谢谢参与")
