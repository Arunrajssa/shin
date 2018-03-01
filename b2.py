a=[]
i=0
n=(int(input("enter the no of elements")))
for i in range(i,n):
  b=input("enter number")
  a.append(b)
print(a)  
dupes = [x for n, x in enumerate(a) if x in a[:n]]
print(dupes)
b=sorted(dupes)
print(b)
