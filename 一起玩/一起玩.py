import random

def main():
    """
    主函数
    """
    print("PlayTogether v0.7.1 RogoGames出品 开源项目\n")
    print("----------------------------------------------")
    print("这里有三种小游戏，\n按A，体验加法运算的快乐；\n按B，体验猜数字的美妙；\n按C，体验猜拳的激情\n*按下大写字母后请回车,Q退出")
    while True:
        print("----------------------------------------------")
        ans = input("Tell me:")
        if ans == "A":
            SA()
        elif ans == "B":
            SB()
        elif ans == "C":
            SC()
        elif ans =="Q":
            return
        else:
            print("Error!")
def SA():
    """
    加法运算
    """
    print("\n真是个爱数学的好孩子呢~来吧，接受制裁吧！")
    print("tips：一共5道题，回答时请务必只写数字！！！信心崩塌的话，按0退出")
    we=0
    for x in range(1,6):
        print("第"+str(x)+"题:")
        ae=random.randint(1,10000)
        be=random.randint(1,10000)
        wt=ae+be
        r=input(str(ae)+"+"+str(be)+"是多少哇：")
        if r=="":
            print("Error!自动跳题中")
        elif int( str(r) )==wt:
            print("你小子还真是个天才！再来！")
            we=we+1
        elif int(r)==0:
            return
        else:
            print("垃圾……这都不会")
    print("你小子才做对了"+str(we)+"道题，太逊了\n")
def SB():
    """
    猜数字
    """
    pass
def SC():
    """
    猜拳
    """
    pass

main()