import pdb
n=37
pdb.set_trace()
for i in range(2,n):
    if n%i==0:
        print('No')
        break
    else:
        print('Yes')
