# 1. Sum the Numbers
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(sum(nums))

# 2. Largest Number
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(max(nums))

# 3. Smallest Number
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(min(nums))

# 4. Even Numbers
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in nums:
#     if num % 2 == 0:
#         print(num)

# 5. Positive Numbers
# nums = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in nums:
#     if num > 0:
#         print(num)

# 6. Positive Numbers II
# nums1 = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums2 = list(filter(lambda x: (x > 0), nums1))

# print(nums2)

# 7. Multiply a list
# nums1 = [1, 2, 3, 4, 5]
# factor = 2

# for num in range(len(nums1)):
#     nums1[num] *= factor

# print(nums1)

# 8. Multiply Vectors
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]

# prod = [list1[i] * list2[i] for i in range(len(list1))]

# print(prod)

# 9. Matrix Addition
# x = [[1,5,5],[2,3,6]]
# y = [[6,9,3],[4,8,4]]

# r = []

# for i in range(len(x)):
#     n = []
#     for j in range(len(x)):
#         z = 0
#         for k in range(len(x)):
#             xx = x[k]
#             yy = y[j]
#             z += xx[j] + yy[k]
#         n.append(z)
#     r.append(n)

# print(r)

# 10. Matrix Addition II
# x = [[1,5,4],[2,3,6],[4,8,9]]
# y = [[2,9,3],[4,8,1],[5,7,6]]

# r = []

# for i in range(len(x)):
#     n = []
#     for j in range(len(x)):
#         z = 0
#         for k in range(len(x)):
#             xx = x[k]
#             yy = y[j]
#             z += xx[j] + yy[k]
#         n.append(z)
#     r.append(n)

# print(r)

# 11. De-dup
# my_numbers = [1, 2, 2, 3, 4, 5, 5, 6, 6, 7]
# my_numbers = list(dict.fromkeys(my_numbers))

# print(my_numbers)