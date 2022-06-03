N = int(input())
H = int(N/3600)
N = N-3600* H
M = int(N/60)
N = N-60*M
S = N
print('{}:{}:{}'.format(H,M,S))
