A,B,C=input().split()
L1=float(1)
L2=float(1)
L3=float(3)
A=float(A)
B=float(B)
C=float(C)

if A>=B and A>=C:
  L1=A
  if B>=C:
    L2=B
    L3=C
  else:
    L2=C
    L3=B
if (B>=A) and (B>=C):
  L1=B
  if A>=C:
    L2=A
    L3=C
  else:
    L2=C
    L3=A
if (C>=A) and (C>=B):
  L1=C
  if A>=B:
    L2=A
    L3=B
  else:
    L2=B
    L3=A
if (A==B) and (B==C):
  L1=A
  L2=B
  L3=C
A=L1
B=L2
C=L3

if(A>=B+C):
  print("NAO FORMA TRIANGULO")
elif(A**2==B**2+C**2):
  print('TRIANGULO RETANGULO')
elif(A**2>B**2+C**2):
  print('TRIANGULO OBTUSANGULO')
elif(A**2<B**2+C**2):
  print('TRIANGULO ACUTANGULO')
if(A==B==C):
  print('TRIANGULO EQUILATERO')
elif(A==B)or(C==B)or(A==C):
  print('TRIANGULO ISOSCELES')