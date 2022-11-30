n=999

n=str(n)
global f
f=0
def s(q,p):
  global f
  if q>=p:
    return 0
  else:
    f+=int(n[q])
    s(q+1,p)
s(0,len(n))
print(f)
