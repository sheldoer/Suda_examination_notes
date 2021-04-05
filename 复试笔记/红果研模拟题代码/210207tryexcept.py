a=input("请输入一个不小于100的数:")
try:
    x=int(a)
    if x>=100:
        print(x//100)
    else:
        print("请输入一个不小于100的数.")
except BaseException:
    print("输入错误")

