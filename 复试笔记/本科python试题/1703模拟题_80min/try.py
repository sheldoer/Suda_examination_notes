def del_():
    global lst
    lst=list(set(lst))
    print(lst)

lst=[1,2,3,4,2,3,4,5,1,2,3,4]
del_()
print(lst)
