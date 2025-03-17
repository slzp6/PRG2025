""" p1_23.py """

mat = []
for x in range(4):
    mat.append([])
    for y in range(3):
        mat[x].append(y * 2)
print(mat)

mat_lc = [[y * 2 for y in range(3)] for x in range(4)]
print(mat_lc)
