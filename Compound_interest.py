l=list(map(int,input().split()))
p=l[0]
r=l[1]
t=l[2]
c=p*(1+r/100)**t
print(format(c,".2f"))