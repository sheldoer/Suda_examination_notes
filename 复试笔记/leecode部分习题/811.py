def count_nums(lst):
    if not lst:
        return []
    dic={}
    for case in lst:
         time,domain=case.split()
         length=len(domain.split('.'))
         for num in range(length):
             dm=domain.split('.',num)[-1]
             print(dm)
             dic[dm]=dic.get(dm,0)+int(time)
    return [str(v)+' '+k for k,v in dic.items()]
'''
         domain=num[1].split('.')
         print(domain)
         for j in domain:
             dic[j]=dic.get(j,0)+int(num[0])
    return [str(v)+' '+k for k,v in dic.items()]
    '''
if __name__=='__main__':
    lst=["900 google.mail.com"]
    print(count_nums(lst))      
    
                   
