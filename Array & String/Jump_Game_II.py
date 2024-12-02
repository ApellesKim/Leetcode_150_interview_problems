"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

#My Solution

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #I will use Greedy algorithm which make most efficient choice overall by making optimal choice every time.
        #Among possible index range of jump, choose the index which has the largest number(next index range of jump). In other words, choose the index which can jump farthest among options.

        """
        Day 1 approach
            1. Initialize variables which help me to simplify my code
            2. Handle special cases:
                - When length of array is 1, return 0 immediately.
                - When length of array is 2, return 1 immediately. (Since it's guaranteed that I can reach nums[n-1].)
            3. Find the farthest point which each index can reach.
            4. Loop thorugh indexs whithin range of farthest point and itself.
            5. Compare and set biggest number to l_max.
            6. Move the i's poisition by l_max because it can directly jump to that position.
            7. Then, add 1 to mj.(minimum jump variable)
            8. When reaching the last index of the array, return total mj. 
                 
        """
        

        f = 0 #furthest jump at each index
        n = len(nums)
        mj = 0 #mininum number of jumps
        point = 0
        l_max = 0

        if n == 1:
            return 0
        if n == 2:
            return 1

        for i in range(n):
            if i < point:
                continue
            if i == n:
                return mj

            f = nums[i]
            for j in range(f - 1):
                initial = nums[i]
                l_max = max(initial, nums[j] + 1)
                #print(l_max)
            point += l_max
            mj += 1
            

        return mj
