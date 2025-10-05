#LIFO Last in, first out
# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.pop()
# stack.pop()
# stack.pop()
#
# stack.append(-2)
# stack.append(0)
#
# if not stack:
#     print("Stack is empty")
# else:
#     print(f"Stack is not empty, top is : {stack[-1]}")

# VALID PARENTHESES
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# s = "()[]{}"

# def isValid(s):
#     stack = []
#     hashmap = {"(":")", "{":"}", "[":"]"}
#
#     for char in s:
#         if char in hashmap:
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             previous_check = stack.pop()
#             if hashmap[previous_check] != char:
#                 return False
#     return not stack
#
# print(isValid("()[]{}"))
#Time complexity is O(n)
#Space complexity is O(n) because the stack size can grow linearly with the input size

#REMOVE ALL ADJACENT DUPLICATE IN STRING
#s = "abbaca"

# def removeDuplicates(s):
#     stack = []
#     for char in s:
#         if stack and stack[-1] == char:
#             stack.pop()
#         else:
#             stack.append(char)
#     return "".join(stack)
# print(removeDuplicates("leelcode"))

# Time complexity is O(n)
# Space complexity is O(n)

#BACKSPACE STRING COMPARE
# example s = "ab#c" and t = "ad#c" # represents a backspace

# def backspaceCompare(s, t):
#     def build(s):
#         stack = []
#         for char in s:
#             if char != "#":
#                 stack.append(char)
#             elif stack:
#                 stack.pop()
#         return "".join(stack)
#
#     return build(s) == build(t)
#
# print(backspaceCompare("ab#c", "ad#c"))


#SIMPLIFY PATH
#path = "/home/user/Documents/../Pictures"
# def simplifyPath(path):
#     stack = []
#
#     for pth in path.split('/'):
#
#         if pth == "..":
#             if stack:
#                 stack.pop()
#         elif pth == "." or pth == '':
#             continue
#         else:
#             stack.append(pth)
#
#     return '/' + '/'.join(stack)
#
# print(simplifyPath("/home/user/Documents/../Pictures"))
# Time is O(n)
# Space is O(n)


# def simplifyPath(path):
#     stack = []
#
#     for pth in path.split('/'):
#         if pth not in ['', '.', '..']:
#             stack.append(pth)
#         elif stack and pth == '..':
#             stack.pop()
#     return '/' + '/'.join(stack)
#
# print(simplifyPath("/home/user/Documents/../Pictures"))



#MAKE THE STRING GREAT
'Using iteration'
#s = leEeetcode
# def makeGood(s):
#
#     while len(s) > 1:
#
#         find = False
#
#         for i in range(len(s) - 1):
#             curr_char, next_char = s[i], s[i + 1]
#             if abs(ord(curr_char) - ord(next_char)) == 32:
#                 s = s[:i] + s[i + 2:]
#                 find = True
#                 break
#         if not find:
#             break
#
#     return s
# print(makeGood("leEeetcode"))

# Time O(n^2)
# Space O(n) Because of the concatenation into a new string

'Using stack'

# def makeGood(s):
#     stack = []
#     if len(s) < 2:
#         return s
#     for char in s:
#         if stack and abs(ord(stack[-1]) - ord(char)) == 32:
#             stack.pop()
#         else:
#             stack.append(char)
#     return "".join(stack)
# print(makeGood("leEeetcode"))
#
#
# Time complexity: O(n)
# Space complexity: O(n)

"QUEUE"

# from collections import deque
# queue = deque()
#
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# while queue:
#     print(queue.popleft())
#
# if not queue:
#     print("Queue is empty")

# queue.popleft()
# queue.popleft()

"Number Of Recent Calls"

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)


























































