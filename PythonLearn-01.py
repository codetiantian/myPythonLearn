import random

print('-----------PythonLearn--------------')

"""生成1-—100的随机数"""
secret = random.randint(1, 100)

temp = input("请输入你猜想的数字:")
guess = int(temp)

if guess == secret :
    print("恭喜，猜正确")

else :
    while guess != secret :
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
