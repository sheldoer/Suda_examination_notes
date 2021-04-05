def kandy_split(lst):
    return min(len(set(lst)),int(len(lst)/2))
if __name__=='__main__':
    lst=[1,1,2,3]
    print(kandy_split(lst))
