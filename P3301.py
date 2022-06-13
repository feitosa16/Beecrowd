H, Z, L = input().split(" ")

H = int(H)
Z = int(Z)
L = int(L)

if (H > L and H < Z) or (H > Z and H < L):
  print("huguinho")

elif (Z > H and Z < L) or (Z > L and Z < H):
  print("zezinho")

else:
  print("luisinho")