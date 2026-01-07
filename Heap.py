from heapq import *


heap = []

heappush(heap, 1)
heappush(heap, 2)
heappush(heap, 3)

heap[0], # outputs 1, as python implements min heap by default
heappop(heap) # pop the min

len(heap) # length of heap

import heapq
nums = [43, 2, 13, 634, 120]
heapq.heapify(nums)
# print(nums)
# print(nums[0])

heap = [67, 341, 234, -67, 12, -976]
heapq.heapify(heap)
heapq.heappush(heap, 7451)
heapq.heappush(heap, -5352)
# print(heap)

# while heap:
    #print(heapq.heappop(heap))

'''Last Stone Weight'''
'''You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y'''

'''Array Based Simulation, Only good for when N < 30'''
def lastStoneWeight(stones):

    def remove_largest():
        index_of_largest = stones.index(max(stones))
        return stones.pop(index_of_largest)

    while len(stones) > 1:
        stone1 = remove_largest()
        stone2 = remove_largest()
        if stone1 != stone2:
            stones.append(stone1 - stone2)
    return stones[0] if stones else 0
# Time complexity is O(N^2)
# Space complexity is O(1)




'''Heap based simulation'''
import heapq

def lastStoneWeight(stones):

    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = abs(heapq.heappop(stones))
        second = abs(heapq.heappop(stones))
        if first != second:
            heapq.heappush(stones, -abs(first - second))

    return -stones[0] if stones else 0

# Time complexity: O(NlogN) converting the array into heap O(N) and doing two remmoves and one add on the heap takes O(logN)
# Space complexity: O(N), heapq.heapify() is an in place operation, but the heap still stores n elements



'''Minimum Operations to Halve Array sum'''
'''You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. 
Return the minimum number of operations to reduce the sum of nums by at least half..'''
# nums = [5, 19, 8, 1]
import heapq

def halveArray(nums):
    target = sum(nums) / 2
    ans = 0
    nums = [-num for num in nums]
    heapq.heapify(nums)

    while target > 0:
        ans += 1
        x = heapq.heappop(nums)
        target -= abs(x / 2)
        heapq.heappush(nums, x / 2)

    return ans

# Time complexity: O(NlogN)
# Space complexity: O(N)

























'''NeetCode5'''
'''Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

#Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#Output: [1,2]