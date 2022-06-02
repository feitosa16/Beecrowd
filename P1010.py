iten1= input().split()
c1= int(iten1[0]) 
n1= int(iten1[1])
v1= float(iten1[2])
total1= n1 * v1

iten2= input().split()
p2= int(iten2[0])
n2= int(iten2[1])
v2= float(iten2[2])
total2= n2 * v2
total= total1 + total2
print('VALOR A PAGAR: R$', '{:.2f}'.format(total))