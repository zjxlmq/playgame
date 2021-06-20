import random
keep = random.randint(1,100)
print("…这是我搭建的游戏…")
lmq= int(input("输入你想要输入的值:"))
guess = int(lmq)
while guess !=int(keep):
    print("猜错了，重新猜")
    lmq = input("重新输入值:")
    guess=int(lmq)
    if guess ==int(keep):
        print("猜对了")
        print("猜对了，也没有奖励")
    else:
        if guess >int(keep):
            print("猜大了")
        else:
            print("猜小了")
print("游戏结束")       
