
'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''

# nums = [3, 0, 1] output = 2
# nums = [0, 1] output = 2
# nums = [9, 6, 4, 2, 3, 5, 7, 0, 1] output = 8

# def missingNumber(nums):
#     sum = 0
#     n = len(nums)
#     for num in nums:
#         sum += num
#     rangeSum = (n * (n + 1)) // 2
#
#     return rangeSum - sum
# print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
# Time and Space O(n)

'Using hashset'
# def missingNumber(nums):
#     set1 = set(nums)
#     n = len(nums) + 1
#     for number in range(n):
#         if number not in set1:
#             return number
# print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

'''Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 
If there are duplicates in arr, count them separately.'''
# arr = [1,2,3] output = 2
# arr = [1,1,3,3,5,5,7,7] output = 0

# def countElements(arr):
#     count = 0
#     for x in arr:
#         if x + 1 in arr:
#             count += 1
#     return count
# print(countElements([1,1,3,3,5,5,7,7]))
# time is O(n^2)
# space is O(1)

'Using Hashset'
# def countElements(arr):
#     hashset = set(arr)
#     count = 0
#     for x in arr:
#         if x + 1 in hashset:
#             count += 1
#     return count
# print(countElements([1,1,3,3,5,5,7,7]))
# Time and space  is O(n)


'''You are given a string s and an integer k. 
Find the length of the longest substring that contains at most k distinct characters.'''
# s = 'eceba' k = 2, return 3
# from collections import defaultdict
# def LongestSubstring(s, k):
#     map = defaultdict(int)
#     left = 0
#     ans = 0
#
#     for right in range(len(s)):
#         map[s[right]] += 1
#         while (len(map) > k):
#             map[s[left]] -= 1
#             if map[s[left]] == 0:
#                 del map[s[left]]
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
#
# print(LongestSubstring('eceba', 2))

'''Intersection of multiple arrays
Given a 2D array nums that contains n arrays of distinct integers, 
return a sorted array containing all the numbers that appear in all n arrays.'''

# nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]] output = [3, 4]

# from collections import defaultdict
#
# def ArrIntersect(nums):
#     count = defaultdict(int)
#     for arr in nums:
#         for num in arr:
#             count[num] += 1
#     n = len(nums)
#     ans = []
#     for key in count:
#         if count[key] == n:
#             ans.append(key)
#     return sorted(ans)
#
# print(ArrIntersect([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))

# Time complexity is O(nm + mlogm) if there are n lists and each list has an average of m elements
# Space complexity is O(nm)

'''Check If All characters have equal number of occurrences
Given a string s, determine if all characters have the same frequency.'''
# if s = abacbc return True
# from collections import defaultdict
# def charFrequency(s):
#     count = defaultdict(int)
#     for char in s:
#         count[char] += 1
#
#     unique_value = count.values()
#     return len(set(unique_value)) == 1
#
# print(charFrequency('abacbc'))

# Time complexity is O(n)
# space complelxity is O(k) where k is 26

'''Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)'''

'Recursive Approach'
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def swap_nodes(self, head):
#         if head is None or head.next is None:
#             return head
#         first_node = head
#         second_node = head.next
#
#         first_node.next = self.swap_nodes(second_node.next)
#         second_node.next = first_node
#
#         return second_node
#

'''Iterative Approach'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def swap_nodes(self, head):
#         dummy = ListNode(0)
#         dummy.next = head
#         pre_head = dummy
#         while pre_head.next and pre_head.next.next:
#             first_node = head
#             second_node = head.next
#
#             pre_head.next = second_node
#             first_node.next = second_node.next
#             second_node.next = first_node
#
#             pre_head = first_node
#             head = first_node.next
#
#         return dummy.next
#
# node6 = ListNode('F')
# node5 = ListNode('E', node6)
# node4 = ListNode('D', node5)
# node3 = ListNode('C', node4)
# node2 = ListNode('B', node3)
# node1 = ListNode('A', node2)
#
# def print_list(head):
#     current = head
#     while(current):
#         print(current.val, end='-->')
#         current = current.next
# new_head = ListNode().swap_nodes(node1)
# print_list(new_head)

'''Maximum Twin Sum of a linkedList'''
# head = [4, 2, 2, 3, 1, 5] output is 9
# half reversed = [4, 2, 2, 5, 1, 3]

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def Twin_Sum(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#
#         prev = None
#         while slow:
#             Next_node = slow.next
#             slow.next = prev
#             prev = slow
#             slow = Next_node
#
#         first_half = head
#         second_half = prev
#         max_sum = 0
#         while second_half:
#             max_sum = max(max_sum, first_half.val + second_half.val)
#             first_half = first_half.next
#             second_half = second_half.next
#         return max_sum
#
# node6 = ListNode(5)
# node5 = ListNode(1, node6)
# node4 = ListNode(3, node5)
# node3 = ListNode(2, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(4, node2)
#
# Insta = ListNode().Twin_Sum(node1)
# print(Insta)
#head = [4, 2, 2, 3, 1, 5]
'Using Array'
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def Twin_Sum(self, head):
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#
#         left = 0
#         right = len(arr) - 1
#         max_sum = 0
#         while left < right:
#             max_sum = max(max_sum, arr[right] + arr[left])
#             right -= 1
#             left += 1
#         return max_sum
# node6 = ListNode(5)
# node5 = ListNode(1, node6)
# node4 = ListNode(3, node5)
# node3 = ListNode(2, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(4, node2)
#
# Insta = ListNode().Twin_Sum(node1)
# print(Insta)























