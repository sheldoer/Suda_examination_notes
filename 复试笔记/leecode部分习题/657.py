def _657(s):
    if s.count('U')==s.count('D') and s.count('R')==s.count('L'):
        return True
    else:
        return False
if __name__=='__main__':
    s='UD'
    s='LL'
    print(_657(s))
