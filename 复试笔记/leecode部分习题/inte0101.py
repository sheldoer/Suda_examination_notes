def inte0101(s):
    if len(s)==len(set(s)):
        return True
    else:
        return False
if __name__=='__main__':
    s="leetcode"
    print(inte0101(s))
