""" p1_8.py """

S = "Tokyo"
print(S)
print(type(S))

SE = S.encode()
print(SE)
print(type(SE))
# SE[0] = 97 はエラーとなる

print("---")
T = "Osaka"
TE = bytearray(T, "utf-8")
print(TE)
print(type(TE))
TE[0] = 97
print(TE)

print("---")
U = b"Japan"
UMV = memoryview(U)
print(bytes(UMV))
print(type(UMV))
print(bytes(UMV[2:5]))
print(UMV.tolist())
