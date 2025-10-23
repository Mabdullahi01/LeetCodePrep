# class TreeNode:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right



'''Revision on Recursion'''

# def func(x):
#     if x >= 3:
#         return
#
#     print(x)
#     x += 1
#     func(x)
# func(1)

#
# def F(n):
#     if n <= 1:
#         return n
#     return F(n-1) + F(n-2)



"How it moves back up/ Backtracking"
# def func(i):
#     if i > 3
#         return
#     print(i)
#     func(i + 1)
#     print(f"End of call where i = {i}")
#     return
# func(1)

# def func(i, n):
#     if i > n:
#         return
#     print("Going down:", i)
#     print("Alchemy")
#     func((i + 1), n)
#     print("Coming back up:", i)
#     return
#
# func(1, 3)

"Backtracking"
# def func(i, n):
#     if i < 1:
#         return
#     func((i - 1), n)
#     print(i)
#
# N = int(input("In what range do you want to print N?"))
# func(N, N)

# def func(i, n):
#     if i < 1:
#         return
#
#     print(i)
#     func((i - 1), n)
#
#     return
# N = int(input("In what range do you want to print N?"))
# func(N, N)



"Parameterised Recursion"
'''Sum of first n numbers '''
# def func(i, sum):
#     if i < 1:
#         print(sum)
#         return
#     func(i - 1, sum + i)
# N = int(input(f"Print the sum of the first N number?"))
# func(N, 0)


# def func(n):
#     if n < 1:
#         return 0
#     return n + func(n - 1)
#
#
# n = int(input(f"Print the sum of the first N number? "))
# print(func(n))

'''Factorial of a number'''
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
# n = int(input(f"Print the sum of the first N number? "))
# print(fact(n))


'''Reverse an Array using Recursion'''

# def func(arr, i = 0):
#     n = len(arr)
#     if i >= (n//2):
#         return arr
#
#     arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
#     return func(arr, i + 1)

#Time: O(n) Space: O(n)










