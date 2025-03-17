""" p1_25.py """

nums = [8, 4, 3, 2, 1, 8, 4, 3, 2, 2]
s_nums = {i for i in nums if i % 2 == 0}
print(s_nums)
