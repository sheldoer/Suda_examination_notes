import re
import time
def get_record(url):
    #读文件函数
    with open(url,'r')as fp:
        vlst=fp.read().split() #读取全部文件并分裂成列表
    fp.close()
    return vlst
def get_v(vlst):
    # 获取全部不同的ETC编号，构成集合
    vset=set()         #新建空集合
    for i in vlst:     #将每条记录的车辆加入集合中，利用集合的性质自动去重
        vset.add(i[:10])
    return vset
def count_v(vlst, vset):
    # 构造车辆进出校园次数的字典
    keys=vset          #将车辆列表设为关键词集合
    lst=[]
    for i in vlst:
        lst.append(i[:10])
    values=list(lst.count(i) for i in vset)   #根据每辆车出现的次数列表设为值表
    fre=dict(zip(keys,values))                 #根据关键词列表与值列表构成字典
    return fre
def count_t(vlst, vset):
    # 构造车辆累计停留时间的字典
    tlst=dict.fromkeys(vset,0)           #根据车辆列表建立关键词字典，且值都为0
    for i in vlst:
        sp=i.split('|')
        tim2=time.mktime(time.strptime(sp[2],'%Y-%m-%d#%H:%M:%S'))
        tim1=time.mktime(time.strptime(sp[1],'%Y-%m-%d#%H:%M:%S'))
        tlst[sp[0]]+=(tim2-tim1)           #计算每个记录的时间差，并累加
    return tlst
def write_to_file(vlst, fre, tlst, url):
    # 输出结果到文件中
    with open(url,'w')as fp:      #依次输出每行信息
        fp.write('记录条数：'+str(len(vlst))+'\n')
        fp.write('车辆数：'+str(len(tlst))+'\n')
        fp.write('进校次数最多的5辆车（单位：次）：\n')
        fri=sorted(fre.items(),key=lambda x:x[1],reverse=True) #根据车辆出现次数由高向低排序
        for i in range(5):
            fp.write(fri[i][0]+','+str(fri[i][1])+'\n')
        fp.write('累计停留时间最长的5辆车（单位：秒）：\n')
        inter=sorted(tlst.items(),key=lambda x:x[1],reverse=True) #根据停留时间由高向低排序
        for i in range(5):
            fp.write(inter[i][0]+','+str(inter[i][1])+'\n')
    fp.close()
            
        
def main():
    vehicle_lst = get_record("data.txt")			# 读文件，获取全部ETC记录，构成列表
    vehicle_set = get_v(vehicle_lst)				# 获取全部不同的ETC编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)		# 构造车辆进出校园次数的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)		# 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict, "report.txt")	# 输出结果到文件中
    return

main()	# 调用main函数
