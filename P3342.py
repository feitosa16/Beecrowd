N= int(input())
total=(N*N)
if (total%2==0):
  a=int((total)/2)
  b=int(a)
  print(a, 'casas brancas e', b, 'casas pretas')
else:
  a=int((total+1)/2)
  b=int(a-1)
  print(a, 'casas brancas e', b, 'casas pretas')