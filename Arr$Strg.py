'''Given a string s, return true if it is a palindrome, false otherwise'''

#A string is a palindrome if it reads the same forward as backward

# def ifpalindrom(s):
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         if s[left] != s[right]:
#             return False
#
#         left += 1
#         right -= 1
#     return True
#
#
# print(ifpalindrom('aceba'))

'''Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).'''

# nums = [1, 2, 4, 6, 8, 9, 14, 15]
# target = 13
# def check_for_target(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left < right:
#         sum = nums[left] + nums[right]
#         if sum == target:
#             return True
#         if sum > target:
#             right -= 1
#         else:
#             left += 1
#     return False

'''Brute Force Solution,When the array is not sorted'''
#nums = [4, -2, 5, 0, 6, 3, 2, -1]
#target = -2
# def TwoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
# print(TwoSum([4, -2, 5, 0, 6, 3, 2, -1], -2))

'''Using Hashmap(Dictionaries)'''
# def TwoSum(nums, target):
#     hash = {}
#     for i in range(len(nums)):
#         num = nums[i]
#         complement = target - num
#         if complement in hash:
#             return [i, hash[complement]]
#
#         hash[num] = i
# print(TwoSum([4, -2, 5, 0, 6, 3, 2, -1], -2))
# Time: O(n)
# Space: O(n)


'''Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted'''
# arr1 = [1, 4, 7, 20]
# arr2 = [3, 5, 6]
# def Two_Sorted_Array(arr1, arr2):
#     arr = []
#     i = j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             arr.append(arr1[i])
#             i += 1
#         else:
#             arr.append(arr2[j])
#             j += 1
#     # If there are remaining element in arr1, append them
#     while i < len(arr1):
#         arr.append(arr1[i])
#         i += 1
#     #If there are remaining element in arr2, append them
#     while j < len(arr2):
#         arr.append(arr2[j])
#         j += 1
#     return arr
# print(Two_Sorted_Array([1, 2, 3, 7, 20], [3, 5, 6]))
# Time: O(n)
# Space: O(1)

#18th June
#Is Subsequence
#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# s = ace
# t = abcde
# def isSubsequence(s, t):
#     i = j = 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#
#     return i == len(s)
# print(isSubsequence('ace', 'abcde'))
# Time: O(n+m) where n is the length of s and m is the length of t
# Space: O(1)


#Write a function that reverses a string. The input string is given as an array of characters s.
#s = ["h", "e", "l", "l", "o"]

# def reverseString(s):
#     i = 0
#     j = len(s) - 1
#     while (i < j):
#         tmp = s[i]
#         s[i] = s[j]
#         s[j] = tmp
#         i += 1
#         j -= 1
#     return s
#
# print(reverseString(["H","a","n","n","a","h"]))


# def reverseString(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left, right = left + 1, right - 1
#     return s
#
# print(reverseString(["H","a","n","n","a","h"]))

'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order'''

# def sortedSquares(nums):
#     num = []
#     for i in nums:
#         num.append(i * i)
#     return sorted(num)
#
# print(sortedSquares([-4, -1, 0, 3, 10]))

# def sortedSquares(nums):
#     num = []
#     num = [i*i for i in nums]
#     return sorted(num)
# print(sortedSquares([-4, -1, 0, 3, 10]))


#Using two pointer
#nums = [-4, -1, 0, 3, 10]
# def sortedSquares(nums):
#     n = len(nums)
#     result = [0] * n
#     i = 0
#     j = n - 1
#     for k in range(n - 1, -1, -1):
#         if abs(nums[i]) > abs(nums[j]):
#             sqwr = nums[i]
#             i += 1
#         else:
#             sqwr = nums[j]
#             j -= 1
#         result[k] = sqwr * sqwr
#     return result
#
# print(sortedSquares([-4, -1, 0, 3, 10]))

#SLIDING WINDOW
#Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.


# def find_length(nums, k):
#     left = 0
#     curr = 0
#     ans = 0
#     for right in range(len(nums)):
#         curr += nums[right]
#         while curr > k:
#             curr -= nums[left]
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
#
# print(find_length([1, 2, 3, 4, 5], 7))

# Time : O(n)
# Space: O(1)


#You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

# def find_length(s):
#     left = curr = ans = 0
#     for right in range(len(s)):
#         if s[right] == "0":
#             curr += 1
#         while curr > 1:
#             if s[left] == "0":
#                 curr -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
#
# print(find_length("110101100"))

# Time : O(n) where n is the length of string s, as the workdone in each loop iteration is amortized constant
# space : O(1)



'''Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.'''
#nums = [10, 5, 2, 6]  k = 100
# def numSubarrayProductLessThanK(nums, k):
#     if k <= 1:
#         return 0
#     ans = left = 0
#     curr = 1
#     for right in range(len(nums)):
#         curr *= nums[right]
#         while curr >= k:
#             curr /= nums[left]
#             left += 1
#         ans += right - left + 1
#     return ans
#
# print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))

'''Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k'''

# def find_best_subarray(nums, k):
#     curr = 0
#     for i in range(k):
#         curr += nums[i]
#
#     ans = curr
#     for i in range(k, len(nums)):
#         curr += nums[i] - nums[i - k]
#         ans = max(ans, curr)
#
#     return ans
#
# print(find_best_subarray([1, 2, 3, 4, 5], 2))
# Time : O(n)
# Space: O(1)

'''You are given an integer array nums consisting of n elements, and an integer k, Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted'''


# nums = [1, 12, -5, -6, 50, 3]
# k = 4


# def findMaxAverage(nums, k):
#     curr = 0
#     for i in range(k):
#         curr += nums[i]
#         average = curr / k
#     ans = average
#     for i in range(k, len(nums)):
#         curr += nums[i]
#         curr -= nums[i - k]
#         average = curr / k
#         ans = max(ans, average)
#     return ans
# #We could just add return ans / k to the previous code and it's all solved
# print(findMaxAverage([5], 1))

'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.'''

#example nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

# def longestOnes(nums, k):
#     left = ans = curr = 0
#     for right in range(len(nums)):
#         if nums[right] == 0:
#             curr += 1
#         while curr > k:
#             if nums[left] == 0:
#                 curr -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
# print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

'''Prefix sum'''
#Sum of subarray from i to j, is prefix[j] - prefix[i - 1] or prefix[j] - prefix[i] + nums[i]

'''Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.'''

# def answer_queries(nums, queries, limit):
#     prefix = [nums[0]]
#
#     for i in range(1, len(nums)):
#         prefix.append(nums[i] + prefix[-1])
#
#     ans = []
#     for x, y in queries:
#         curr = prefix[y] - prefix[x - 1]
#         ans.append(curr < limit)
#     return ans
#
# print(answer_queries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13 ))

# Time : O(n+m) where n is the length of nums and m is the queries length
# Space : O(n) space for building the prefix sum, My question, What of the space for building the ans array?

'''Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.'''
# nums = [10, 4, -8, 7]
# def waysToSplitArray(nums):
#     prefix = [nums[0]]
#     n = len(nums)
#     for i in range(1, n):
#         prefix.append(nums[i] + prefix[-1])
#     ans = 0
#     for i in range(n - 1):
#         left_section = prefix[i]
#         right_section = prefix[-1] - prefix[i]
#         if left_section >= right_section:
#             ans += 1
#     return ans
# Time : O(n)
# Space: O(n)
#
# def waysToSplitArray(nums):
#     left_section = 0
#     total = sum(nums)
#     ans = 0
#
#     for i in range( len(nums) - 1):
#         left_section += nums[i]
#         right_section = total - left_section
#         if left_section >= right_section:
#             ans += 1
#     return ans
# Time : O(n)
# Space: O(1)

'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.'''

# def runningSum(nums):
#     running = [nums[0]]
#     for i in range(1, len(nums)):
#         running.append(nums[i] + running[-1])
#     return running
# print(runningSum([3,1,2,10,1]))


'''Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

'''

# nums = [-3, 2, -3, 4, 2]
# prefix_sum = [-3, -1, -4, 0, 2]

# def minStartValue(nums):
#     prefix = [nums[0]]
#     n = len(nums)
#     for i in range(1, n):
#         prefix.append(nums[i] + prefix[-1])
#
#     min_prefix = min(prefix)
#     startValue = 1 - min_prefix
#     return max(startValue, 1)
#
#
# print(minStartValue([1,-2,-3]))


# def minStartValue(nums):
#     min_sum = float('inf')  # Initialize to positive infinity
#     curr_sum = 0
#
#     for num in nums:
#         curr_sum += num
#         min_sum = min(min_sum, curr_sum)
#
#     startValue = 1 - min_sum
#     return max(1, startValue)



# You are given a 0-indexed array nums of n integers, and an integer k.
#
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
#
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
#
# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
# nums = [7, 4, 3, 9, 1, 8, 5, 2, 6] k = 3
#PREFIX SUM SOLUTION
# prefixSum = [0, 7, 11, 14, 23, 24, 32, 37, 39, 45]
# def getAverages(nums, k):
#     n = len(nums)
#
#     avgs = [-1] * n
#     prefix = [0]
#
#     for i in range(n):
#         prefix.append(nums[i] + prefix[-1])
#
#     if k > n:
#         return -1
#     for i in range(k, n - k):
#         AvgSum = prefix[i + k + 1] - prefix[i - k]
#         avgs[i] = AvgSum // (2 * k + 1)
#     return avgs
# print(getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
# Time: O(n) two iterations of O(n) for the generation of both the prefix and avgs
# Space: O(n) output array avgs is not considered as an additional space, but the prefix array

#SLIDING WINDOW SOLUTION
# def getAverages(nums, k):
#     n = len(nums)
#     avgs = [-1] * n
#     window_sum = 0
#     window_size = 2 * k + 1
#
#     if window_size > n:
#         return avgs
#
#     for i in range(window_size):
#         window_sum += nums[i]
#     return window_sum
#
#     avgs[k] = window_sum // window_size
#
#     for i in range(k + 1, n - k):
#         window_sum += nums[i + k] - nums[i - k - 1]
#         avgs[i] = window_sum // window_size
#
#     return avgs
#
# nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
# k = 3
# print(getAverages(nums, k))
#
# Time: O(n)
# Space: O(1) avgs is not considered as extra space



#Bonus Problems
'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.'''
#s = "Let's take LeetCode contest"

# def reverseWords(s):
#     newstart = -1
#     ch_array = list(s)
#     n = len(s)
#
#     for i in range(n + 1):
#         if i == n or s[i] == " ":
#             start = newstart + 1
#             end = i - 1
#
#             while start < end:
#                 ch_array[start], ch_array[end] = ch_array[end], ch_array[start]
#                 start += 1
#                 end -= 1
#             newstart = i
#     return "".join(ch_array)
#
# s = "Let's take LeetCode contest"
# print(reverseWords(s))

#Bonus Problem
# Reverse Only Letters
'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.'''

#input: s = "ab-cd"
#output: "dc-ba"

# def ReverseOnlyLetters(s):
#     ans = []
#     j = len(s) - 1
#
#     for i, x in enumerate(s):
#         if x.isalpha():
#             while not s[j].isalpha():
#                 j -= 1
#             ans.append(s[j])
#             j -= 1
#         else:
#             ans.append(x)
#     return "".join(ans)
#
# print(ReverseOnlyLetters("Test1ng-Leet=code-Q!"))

'''Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
 If there is no common integer amongst nums1 and nums2, return -1.'''

# Input: nums1 = [1, 2, 3], nums2 = [2, 4]
# Output: 2
#BRUTE FORCE SOLUTION
# def getCommon(nums1, nums2):
#     for num1 in nums1:
#         for num2 in nums2:
#             if (num1 == num2):
#                 return num1
#     return -1
# print(getCommon([1, 2, 3, 4, 5], [1,3,5]))
#O(m * n) is the time complexity
#Space complexity is O(1)

#HASHSET solution

# def getCommon(nums1, nums2):
#     set1 = set(nums1)
#
#     for num in nums2:
#         if num in set1:
#             return num
#     return -1
# print(getCommon([2, 3, 4, 5], [1,3,5]))
#
# Time complexity: O(n + m), creating set1 takes O(n), checking elements in num2 takes O(m)
# Space complexity: O(n), initializing set1

# nums1 = [2, 4, 6, 8, 10]
# nums2 = [1, 1, 3, 4 , 10]
# def getCommon(nums1, nums2):
#     p = 0
#     q = 0
#     while(p < len(nums1) and q < len(nums2)):
#         if nums1[p] < nums2[q]:
#             p += 1
#         elif nums1[p] > nums2[q]:
#             q += 1
#         else:
#             return nums1[p]
#     return -1
# print(getCommon([2, 4, 6, 8, 10], [1, 1, 3, 4 , 10]))
#
# Time complexity: O(n + m)
# Space: O(1)














































