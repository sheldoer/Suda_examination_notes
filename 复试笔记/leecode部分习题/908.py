def _908(lst,k):
    return max(max(lst) - min(lst) - 2*k, 0)
    lst=list(set(lst))
    if len(lst)<2:
        return 0
    mxa=max(lst)
    mna=min(lst)
    if mxa-mna<=2*k:
        return 0
    lst.remove(mxa)
    lst.remove(mna)
    lst.append(mxa-abs(k))
    lst.append(mna+abs(k))
    return max(lst)-min(lst)
if __name__=='__main__':
    A = [1]
    K = 0
    print(_908(A,K))
    
