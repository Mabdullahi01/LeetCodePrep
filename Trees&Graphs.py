
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

# def func(i, sum = 0):
#     if i == 0:
#         return sum
#     return func(i - 1, sum + i)


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

'''checking if a string is a palindrome'''

# def is_palindrome(s, i = 0):
#     n = len(s)
#     if i >= (n // 2):
#         return True
#     if s[i] != s[n - i - 1]:
#         return False
#     return is_palindrome(s, i + 1)

'''Multiple Recursion calls: Fibonacci'''

# def f(n):
#     if n <= 1:
#         return n
#     last = f(n - 1)
#     slast = f(n - 2)
#
#     return last + slast
# print(f(4))

# Time complexity is near 2^n

'''Level Order Traversal Implementation'''
# from collections import deque
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def level_order(root):
#     if not root:
#         return []
#
#     result = []
#     queue = deque([root])
#
#     while queue:
#         level = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             level.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         result.append(level)
#     return result
#
#
# root = TreeNode(1,
#         TreeNode(2, TreeNode(4), TreeNode(5)),
#         TreeNode(3, TreeNode(6), TreeNode(7)))
#
# print(level_order(root))

'''Pre-Order Traversal'''
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# def preorder(root):
#     if not root:
#         return
#     print(root.val)
#     preorder(root.left)
#     preorder(root.right)



'''Iterative Preorder'''
#
# # Root Left Right
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def preorder_iterative(root):
#     if not root:
#         return
#
#     stack = [root]
#
#     while stack:
#         node = stack.pop()
#         print(node.val, end=" ")
#
#         if node.right:
#             stack.append(node.right)
#
#         if node.left:
#             stack.append(node.left)
#
# root = TreeNode(1,
#         TreeNode(2, TreeNode(4), TreeNode(5)),
#         TreeNode(3, TreeNode(6), TreeNode(7)))
#
# preorder_iterative(root)

'''Iterative InOrder '''
#Left Root Right

# def inorder_iterative(root):
#     stack = []
#     curr = root
#
#     while True:
#         if curr is not None:
#             stack.append(curr)
#             curr = curr.left
#
#         else:
#             if not stack:
#                 break
#
#             curr = stack.pop()
#             print(curr.val, end=" ")
#
#             curr = curr.right

'''Iterative PostOrder'''

# Left Right Root
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def iterative_postorder(root):
#     stack = []
#     lastVisited = None
#     curr = root
#     result = []
#
#     while curr or stack:
#
#         while curr:
#             stack.append(curr)
#             curr = curr.left
#
#         peek = stack[-1]
#
#         if peek.right and lastVisited != peek.right:
#             curr = peek.right
#         else:
#             result.append(peek.val)
#             lastVisited = stack.pop()
#
#     return result
#
#
# root = TreeNode(1,
#         TreeNode(2, TreeNode(4), TreeNode(5)),
#         TreeNode(3))
#
# print(iterative_postorder(root))


'''Iterative In,Pre,Post Order Traversal, using a stack[(root, num)], where num can be 1 for pre, 2 for in, 3 for post'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def All_traversal(root):
    if not root:
        return [], [], []


    stack = [(root, 1)]
    pre_order = []
    in_order = []
    post_order = []

    while stack:
        node, state = stack.pop()

        if state == 1:
            pre_order.append(node.val)
            stack.append((node, 2))

            if node.left:
                stack.append((node.left, 1))


        elif state == 2:
            in_order.append(node.val)
            stack.append((node, 3))

            if node.right:
                stack.append((node.right, 1))

        else:
            post_order.append(node.val)

    return pre_order, in_order, post_order







'''Maximum depth of a binary Tree
Given the root of a binary tree, find the length of the longest path from the root to a leaf.'''

# Height will always be 1 + max(l, r)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if root is None:
        return 0
    lh = max_depth(root.left)
    rh = max_depth(root.right)

    return 1 + max(lh, rh)
# Time complexity O(N)
# Space complexity O(N)





'''Check for Balanced Binary Tree'''
'''This solution was built upon the maximum depth of binary tree solution, which enables us to keep a time complexity of O(N)'''

# The absolute Difference between left height and right height must be less or equal to 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    return balance_Check(root) != -1


def balance_Check(root):
    if root is None:
        return 0

    left_height = balance_Check(root.left)
    if left_height == -1: return -1

    right_height = balance_Check(root.right)
    if right_height == -1: return -1

    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)

root = TreeNode(1,
        TreeNode(2,
            TreeNode(3,
                TreeNode(4),
                None
            ),
            None
        ),
        TreeNode(5)
)

# Time complexity is O(N)
# Space complexity is O(N)





'''Diameter of a Binary Tree'''

'''Given the root of a binary tree, return the length of the diameter of the tree.'''
'''The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    This path may or may not pass through the root.'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def diameterOfBinaryTree(root):
    diameter = [0]  # using list as parameter
    height(root, diameter)
    return diameter[0]

def height(node, diameter):
    if node is None:
        return 0
    lh = height(node.left, diameter)
    rh = height(node.right, diameter)

    diameter[0] = max( diameter[0], lh + rh)

    return 1 + max(lh, rh)

'''OR using instance variable'''


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0  # Instance variable
        self.height(root)
        return self.diameter

    def height(self, node):
        if not node:
            return 0

        lh = self.height(node.left)
        rh = self.height(node.right)

        self.diameter = max(self.diameter, lh + rh)

        return 1 + max(lh, rh)


#Time complexity is O(N)
#Space complexity is O(h), where h is the height of the tree, in best case O(log n)












