import re
import random
def is_prime(n):
    #判断n是否为素数
    if n<2:
        return False
    if n==2:
        return True
    top=int(n**0.5)+1
    for i in range(2,top):
        if n%i==0:
            return False
    return True

def get_and_print(s):
    nums=re.findall('\d+',s)
    print(nums)
    spec={'3','7'}     #包含3与7的集合
    res=[]         #用来存储符合输出的数字
    for i in nums:
        if spec&set(i) and is_prime(int(i)):    #找到包含3或是7的素数存储到目标列表里
            res.append(int(i))
    print(res)
    length=len(res)
    for i in range(0,length,2):   #以步长为2读取列表信息
        if i+1<length:
            print('{:>10}{:>10}'.format(res[i],res[i+1]))
    return res
def generate_points(res):
    #把表中素数构建二维坐标
    points=[]
    for i in range(len(res)-1):
        points.append([res[i],res[i+1]])
    return points
def count_point(points):
    #生成A点坐标，并计算欧式距离之和与平均距离
    x=random.randint(0,100)
    y=random.randint(0,100)
    print('(x,y):{:>10.2f}{:>10.2f}'.format(x,y))   #求欧式距离公式
    A=[x,y]
    f=lambda a,b:((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    sumdistance=0
    for i in points:
        sumdistance+=f(A,i)
    print('欧氏距离：{:10.2},平均距离：{:10.2}'.format(sumdistance,sumdistance/len(points)))
    
def main():
    s='Regular296expression913patterns465are280compiled102into510a122series48of563bytecodes1 6which366are262then773executed361by50a949matching556engine509writen126in45IC760F or379advanced982use201it502may282be66necessary566to63lpay199careful685attntion915t o814how577the455engine309will349executel78a341given17IRE279and52write744the69RE5 78in190a361certain466way726in969order667to310produce943bytecode760that203runs590fast er423Optimization723is787not458covered30in250this747document66because396it803requires 530that601you928have208a152good609understanding194of31the772matching17engine599int ernals806'
    res=get_and_print(s)
    points=generate_points(res)
    count_point(points)
    
if __name__=='__main__':
    main()
    
        
