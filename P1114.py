S,T,F=input().split()
S=int(S)
T=int(T)
F=int(F)

H=S+T+F
if 0<=H<24:
  print(H)
if H>=24:
  print(H-24)
elif H<0:
  print(24+H)