def _905(lst):
    onum=[x for x in lst if x%2==0]
    enum=[y for y in lst if y%2!=0]
    return onum+enum
print(_905([3,1,2,4]))
