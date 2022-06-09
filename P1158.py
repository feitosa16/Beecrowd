N=int(input())
for N in range(0,N):
  X,Y=input().split()
  X=int(X)
  Y=int(Y)
  S=0 
  I=1 
  while I<=Y:
    if X%2!=0:
      S=S+X
      X=X+1
      I=I+1
    if X%2==0:
      X=X+1
  print(S)