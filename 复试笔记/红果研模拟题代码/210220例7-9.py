import pickle

f=open('sample.dat','rb')
n=pickle.load(f)
i=0
while i<n:
    x=pickle.load(f)
    print(x)
    i=i+1
f.close
