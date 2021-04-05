def _476(n):
    num='0b'
    for i in bin(n)[2:]:
        if i=='0':
            num=num+'1'
        else:
            num=num+'0'
    return int(num,2)
if __name__=='__main__':
    print(_476(1))
