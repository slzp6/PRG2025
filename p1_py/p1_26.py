""" p1_26.py """

nums = [8, 4, 3, 2, 1, 8, 4, 3, 2, 2]
g_nums = (i for i in nums if i % 2 == 0)

print(g_nums)
for j in g_nums:
    print(j, end=" ")
