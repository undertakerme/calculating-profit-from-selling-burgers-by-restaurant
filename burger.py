t=int(input("no. of test cases"))#burger
u=[]
for i in range(t):
    n=input()
    q=input()
    y=q.split()
    x=n.split()
    m=[]
    k=[]
    for j in range(len(x)):
        m.append(int(x[j]))
    for j in range(len(y)):
        k.append(int(y[j]))
    b=m[0]
    l=b//2
    p=m[1]
    f=m[2]
    m.pop(0)
    g=max(k)
    ii=k.index(g)
    gg=min(k)
    iii=k.index(gg)
    h=q[0]
    c=q[1]
    cost=0
    if(b<=1):
       u.append(0)
    elif(l>=(p+f)):
       s1=h*p
       s2=c*f
       cost=s1+s2
       u.append(cost)
    elif(l<(p+f)):
        if(ii==1):
           for j in range(m[ii]):
               cost=cost+g
           ii=l-f
           if(ii>0):
              for j in range(ii):
                  cost=cost+gg
           u.append(cost)
        elif(ii==0):
            for j in range(m[ii]):
                 cost=cost+gg
            ii=l-p
            if(ii>0):
               for j in range(ii):
                   cost=cost+g
            u.append(cost)
for i in range(len(u)):
    print(u[i])
