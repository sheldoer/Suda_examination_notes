filename='demo6.py'
with open(filename,'r')as fp:
    lines=fp.readlines()
lines=[line.rstrip()+''*(100-len(lines))+'#'+str(index)+'\n' for index,line
       in enumerate(lines)]
with open(filename[:-3]+'_new.py','w')as fp:
    fp.writelines(lines)
