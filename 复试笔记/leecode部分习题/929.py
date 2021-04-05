def to_email(lst):
    res=set()
    for i in lst:
        mail=i.split('@')   #根据@符号分割，第一项为本地名称，第二项为域名
        s=''
        for j in mail[0]:   #对本地名称进行.与+的符号操作
            if j=='.':
                continue
            elif j=='+':
                break
            else:
                s=s+j
        res.add(s+mail[1])  #对集合添加目标邮件地址
    return len(res)
if __name__=='__main__':
    lst=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","tes temail+david@lee.tcode.com"]
    print(to_email(lst))
