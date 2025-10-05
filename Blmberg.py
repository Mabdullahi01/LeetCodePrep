'''Maximum Nesting Depth of the Parentheses'''

# def maxDepth(s):
#     ans = 0
#     stack = []
#
#     for c in s:
#         if c == '(':
#             stack.append(c)
#         elif c == ')':
#             stack.pop()
#         ans = max(ans, len(stack))
#     return ans
#
# print(maxDepth('(1+(2*3)+((8)/4))+1'))
# #Time: O(n)
# #Space: O(n)

# def maxDepth(s):
#     ans = 0
#     openBrackets = 0
#
#     for c in s:
#         if c == '(':
#             openBrackets += 1
#         elif c == ')':
#             openBrackets -= 1
#
#         ans = max(ans, openBrackets)
#     return ans
# print(maxDepth('(1+(2*3)+((8)/4))+1'))

#Time comolexity is O(n) as we are iterating over each character in string s
#Space: O(1), we only required varaibles like ans and openBrackets

'''Two Sum'''
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

'''
#nums = [2,7,11,15], target = 9
#output = [0, 1]
# Using Brute Force
# def TwoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
# print(TwoSum([2, 7, 11, 15], 9))


#Using Hashmap
#nums = [2,7,11,15], target = 9
# nums[i] + complement = target
#compliment = target - nums[i]
# def TwoSum(nums, target):
#     hashmap = {}
#     for i in range(len(nums)):
#         compliment = target - nums[i]
#         if compliment in hashmap:
#             return [i, hashmap[compliment]]
#         hashmap[nums[i]] = i
#     return []
#
# print(TwoSum([2, 7, 11, 15], 9))




'''Given a string s, return true if it is a palindrome, false otherwise'''

#A string is a palindrome if it reads the same forward as backward
# s = aceca
# def ifpalindrom(s):
#     right = len(s) - 1
#     left = 0
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
#
# print(ifpalindrom('aceba'))

'''Deeply Nested Substring'''
# s = "ab(cd[]m){(ef)g}"
# def deepestSubstrings(s):
#     stack = []
#     current_depth = 0
#     max_depth = 0
#     dpest_substring = []
#
#     for i, c in enumerate(s):
#         if c in "{[(":
#             stack.append((i, c))
#             current_depth += 1
#             max_depth = max(max_depth, current_depth)
#
#         elif c in "}])":
#             if stack:
#                 indx, value = stack.pop()
#                 current_depth -= 1
#                 if current_depth + 1 == max_depth:
#                     dpest_substring.append(s[indx + 1:i])
#
#             #current_depth -= 1
#     return dpest_substring
#
# print(deepestSubstrings("ab(cd[]m){(ef)g}"))

'''Valid Parenthesis'''
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid'''

#s = "()[]{}"

# def isValid(s):
#     hashmap = {'(': ')', '[': ']', '{': '}'}
#     stack = []
#     for i in s:
#         if i in hashmap:
#             stack.append(i)
#         else:
#             if stack and hashmap[stack[-1]] == i:
#                 stack.pop()
#     return len(stack) == 0
#
# print(isValid("((()"))
# Time complexity is O(n)
# Space complexity is O(n)


'''Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0'''

'''Brute Force Solution'''

# def maxProfit(prices):
#     max_profit = 0
#
#     for i in range(len(prices) - 1):
#         for j in range(i + 1, len(prices)):
#             current_profit = prices[j] - prices[i]
#
#             if current_profit > max_profit:
#                 max_profit = current_profit
#     return max_profit
#
# print(maxProfit([7, 1, 5, 3, 6, 4]))


'''One pass'''
# def maxProfit(prices):
#     min_price = float('inf')
#     max_profit = 0
#
#     for price in prices:
#         if price < min_price:
#             min_price = price
#         profit = price - min_price
#         max_profit = max(max_profit, profit)
#     return max_profit
# print(maxProfit([7, 1, 5, 3, 6, 4]))

# Time complexity is O(n)
# Space complexity is O(1)  Only two variables are used


'Reverse Linked List'
'0-->1-->2-->3'
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def ReverseList(head):
#     curr = head
#     prev = None
#     while curr:
#         Nextnode = curr.next
#         curr.next = prev
#         prev = curr
#         curr = Nextnode
#     return prev
#
# node3 = ListNode(3)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)
# node0 = ListNode(0, node1)
#
# new_head = ReverseList(node0)
# while(new_head):
#     print(new_head.val, end='-->')
#     new_head = new_head.next





'Merge Two Sorted List'
'You are given the heads of two sorted linked lists list1 and list2.'
'Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists'

'Recursively'
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def mergeTwoLists(list1, list2):
#     if list1 is None:
#         return list2
#     elif list2 is None:
#         return list1
#     elif list1.val < list2.val:
#         list1.next = mergeTwoLists(list1.next, list2)
#         return list1
#     else:
#         list2.next = mergeTwoLists(list1, list2.next)
#         return list2
#
# node3 = ListNode(4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)
#
# node6 = ListNode(4)
# node5 = ListNode(3, node6)
# node4 = ListNode(1, node5)
#
# new_list = mergeTwoLists(node1, node4)
#
# while new_list:
#     print(new_list.val, end='-->')
#     new_list = new_list.next

# Time complexity is O(m + n)
# Space complexity is O(m + n) due to recursive stack, as each function call adds a new frame

'Iteratively'

# class ListNode:
#     def __init__(self, val=0, next = None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def mergeTwoLists(self, list1, list2):
#         dummy = ListNode()
#         current = dummy
#
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
#
#         current.next = list1 if list1 else list2
#
#         return dummy.next
#
# node3 = ListNode(4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)
#
# node6 = ListNode(4)
# node5 = ListNode(3, node6)
# node4 = ListNode(1, node5)
#
# solution = Solution()
# new_list = solution.mergeTwoLists(node1, node4)
#
# while new_list:
#     print(new_list.val, end='-->')
#     new_list = new_list.next

# Time complexity is O(m+n) The while loop runs for a number of iterations equal to the sum of the length of the two lists
# Space comolexity is O(1) The iterative approach only allocates a few pointers, so it has a constant overall memory footprint


'''Longest Substring Without Repeating Characters 
Given a string s, find the length of the longest substring without duplicate characters.'''

'Brute Force Solution'
# def lengthOfLongestSubstring(s):
#     max_length = 0
#     for i in range(len(s)):
#         unique_chars = set()
#         for j in range(i, len(s)):
#             if s[j] in unique_chars:
#                 break
#             unique_chars.add(s[j])
#             max_length = max(max_length, j - i + 1)
#
#     return max_length
# print(lengthOfLongestSubstring('abcabcbb'))

# Time complexity is O(n^2)
# Space complexity is O(n)


'Sliding Window Solution'
s = 'abcabcbb'
# from collections import defaultdict
#
# def lengthOfLongestSubstring(s):
#     left = ans = 0
#     hashmap = defaultdict(int)
#
#     for right in range(len(s)):
#         hashmap[s[right]] += 1
#         while hashmap[s[right]] > 1:
#             hashmap[s[left]] -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
#
# print(lengthOfLongestSubstring('abcabcbb'))
# Time complexity is O(2n) = O(n) The right pointer iterate through the string once, and the while loop moves the left pointer only when needed, meaning each character is visited at most twice
# Space complexity is O(min(n,k)), where n is the number of unique characters, k is 26

# 'Similar but using while instead of for loop'
# from collections import defaultdict
# def lengthOfLongestSubstring(s):
#     left = ans = right =  0
#     mp = defaultdict(int)
#     while right < len(s):
#         mp[s[right]] += 1
#
#         while mp[s[right]] > 1:
#             mp[s[left]] -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#         right += 1
#
#     return ans
# print(lengthOfLongestSubstring('abcabcbb'))

'''Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.'''
# nums = [1, 2, 3, 4, 5] k = 7
# def find_length(nums, k):
#     left = ans = curr = 0
#
#     for right in range(len(nums)):
#         curr += nums[right]
#         while (curr > k):
#             curr -= nums[left]
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
# print(find_length([1, 2, 3, 4, 5], 7))


'''You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". 
What is the length of the longest substring achievable that contains only "1"?'''
s = "1101100111"

# def find_length(s):
#     left = ans = 0
#     count = 0
#
#     for right in range(len(s)):
#         if s[right] == "0":
#             count += 1
#         while (count > 1):
#             if s[left] == "0":
#                 count -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
# print(find_length("1101100111"))

# Time : O(n) where n is the length of string s, as the workdone in each loop iteration is amortized constant
# space : O(1)

'''Given an array of positive integers nums and an integer k, 
return the number of subarrays where the product of all the elements in the subarray is strictly less than k.'''
#nums = [10, 5, 2, 6]  k = 100

# def numSubarrayProductLessThank(nums, k):
#     left = ans = 0
#     curr = 1
#
#     for right in range(len(nums)):
#         curr *= nums[right]
#         while curr >= k:
#             curr /= nums[left]
#             left += 1
#         ans += right - left + 1
#     return ans
# print(numSubarrayProductLessThank([10, 5, 2, 6], 100))

'''Valid Anagram'''
'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''
# s = "anagram", t = "nagaram"
'Hashmap Solution'
# from collections import defaultdict
# def isAnagram(s, t):
#     dict1 = defaultdict(int)
#     dict2 = defaultdict(int)
#     for i in s:
#         dict1[i] += 1
#     for j in t:
#         dict2[j] += 1
#     return dict1 == dict2
# print(isAnagram("anagram", "nagaram"))
# Time complexity is O(n), Two seperate loops for counting
# Space complexity is O(1), At most 26keys in dictionary

'Using Fixed Array size'
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     arr = [0] * 26
#
#     for i in s:
#         arr[ord(i) - ord('a')] += 1
#     for i in t:
#         arr[ord(i) - ord('a')] -= 1
#         if arr[ord(i) - ord('a')] < 0:
#             return False
#     return True
# print(isAnagram("anagram", "nagaram"))
# Time complexity is O(n)
# Space complexity is O(1)

'''BackSpace String Compare
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.'''
#s = "ab#c", t = "ad#c" should return True

# def backspaceCompare(s, t):
#     def build(s):
#         stack = []
#         for i in s:
#             if i != '#':
#                 stack.append(i)
#             elif stack:
#                 stack.pop()
#         return stack
#     return build(s) == build(t)
# print(backspaceCompare("ab##", "c#d#"))

# def backspaceCompare(s, t):
#     def build(s):
#         stack = []
#         for char in s:
#             if char == '#':
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(char)
#         return stack
#     return build(s) == build(t)
# print(backspaceCompare("ab##", "c#d#"))
# print(backspaceCompare("a#c", "b"))
# print(backspaceCompare("abc#d", "abzz##d"))

# Time complexity is O(n+m) since we call build(s) and build(t)
# Space complexity is O(n+m) storing characters of string which result in O(n) usage for s and O(m) fo string t


# def backspaceCompare(s, t):
#     stacks = []
#     stackt = []
#     for i in range(len(s)):
#         if stacks and s[i] == '#':
#             stacks.pop()
#         else:
#             stacks.append(s[i])
#     for j in range(len(t)):
#         if stackt and t[j] == '#':
#             stackt.pop()
#         else:
#             stackt.append(t[j])
#     return stacks
# print(backspaceCompare("ab##", "c#d#"))
# print(backspaceCompare("a#c", "b"))
# print(backspaceCompare("abc#d", "abzz##d"))

#time complexity is O(n)
#Space complexity is O(n)

'''Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.'''
# x = 121 returns True

# def isPalindrome(x):
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False
#     revertedNumber = 0
#     while(revertedNumber < x):
#         revertedNumber = revertedNumber * 10 + x % 10
#         x //= 10
#
#     return x == revertedNumber or x == revertedNumber // 10
# print(isPalindrome(121))

# Time complexity is O(log n)
# Space complexity is O(1)

# def isPalindrome(x):
#     temp = x
#     y = 0
#
#     while(temp > 0):
#         quo = temp % 10
#         temp //= 10
#         y = y * 10 + quo
#
#     return y == x
# print(isPalindrome(121))
# Time complexity is O(log n)
# Space complexity is O(1)

'''Custom Sort String'''
# order = 'ecolt' s = 'leetcoded'
# output = 'eeecoltdd'
'Using Counter'
# from collections import Counter
# def customSortString(order, s):
#     count = Counter(s)
#     final = []
#
#     for char in order:
#         if char in count:
#             final.append(char * count.pop(char))
#             # del count[char]
#     for key, value in count.items():
#         final.append(key * value)
#     return ''.join(final)
#
# print(customSortString('ecolt','leetcoded'))

'Using hashmap'
# def customSortString(order, s):
#     from collections import defaultdict
#     map = defaultdict(int)
#     final = []
#
#     for char in s:
#         map[char] += 1
#
#     for char in order:
#         if char in map:
#             final.append(char * map[char])
#             del map[char]
#     for key, value in map.items():
#         final.append(key * value)
#     return ''.join(final)
#
# print(customSortString("bcafg",  "abcd"))

# Time compplexity is O(N), N is the length of string s, O(N+K) where K is the length of order
# Space complexity is O(N) A hashmap and a result string created


'''Sort Characters By Frequency
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.'''

'Hashmap and Sort Method'
# from collections import Counter
# def frequencySort(s):
#     count = Counter(s)
#     string = []
#
#     for char, value in count.most_common():
#         string.append(char * value)
#     return ''.join(string)
# print(frequencySort('tree'))
# Time complexity is O(n log n)
# Space complexity is O(n)

'Sort By Frequency'
# def frequencySort(s):
#     freq = [0 for _ in range(52)]
#     # freq = [0] * 52
#     temp = []
#     for c in s:
#         if 'a' <= c <= 'z':
#             freq[ord(c) - ord('a')] += 1
#         else:
#             freq[ord(c) - ord('A') + 26] += 1
#
#     for key, val in enumerate(freq):
#         if val > 0:
#             temp.append([val, key])
#     temp.sort(reverse=True)
#
#     res = ""
#     for key, val in temp:
#         if val < 26:
#             res += chr(ord('a') + val) * key
#         else:
#             res += chr(ord('A') + val - 26) * key
#     return res
# print(frequencySort('Aabb'))

# Time commplexity is O(n), Counting frequencies is O(n), sorting characters is O(52log 52) = O(1)
# Building string is O(n), so overall complexity is O(n)

# Space complexity is O(n), temporary list is O(52), frequency array is O(52), output string res is O(n)


















































