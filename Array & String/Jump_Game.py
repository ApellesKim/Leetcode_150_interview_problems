"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""

#My Solution
class Solution(object):
    def canJump(self, nums):
        furthest = 0 #tracks the furthest index that can be reached
        n = len(nums) #length of nums
            
        for i in range(n):
            if i > furthest: 
                return False #the current index is not reachable, and thus it is impossible to reach the last index
            furthest = max(furthest, i + nums[i]) #update furthest to the maximum of its current value and i + nums[i], which represents how far you can jump from index i
            if furthest >= n - 1:
                return True #means you can reach or surpass the last index of the array
                    
        return False #indicating that the last index is not reachable