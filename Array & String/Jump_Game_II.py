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
        Day 1 approach  (30/110 test cases passed)
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


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Day 2 Approach (26/110 test cases passed)
            1. Initialize n to length of array nums and jumps to total number of jumps needed to reach the end of the array nums.
            2. Loop for all indexs in array nums. (Let's use while loop this time!)
                1) Check for each index's farthest reaching point.
                2) Compare all numbers within farthest point.
                3) Select biggest number to be next base point (where it will begin jump next time).
                4) Update i and total number of jumps.
            3. If the i reaches the end of the array, terminate the loop and return number of jumps.
        """

        # passed test cases: [2, 3, 1, 1, 4], [0], [1, 2], etc..
        # failing test case: [2, 3, 1]

        n = len(nums)
        jumps = 0
        i = 0

        if n <= 1:
            return 0
        elif n == 2:
            return 1

        while i < n:
            
            farthest = 0
            farthest += nums[i]  #i = 0 / nums[i] = 2 (First loop)
                                 #i = 1 / nums[i] = 3 (Second loop)
            
            if i + farthest + 1 > n:
                jumps += 1
                break

            if i + farthest + 1 == n:

                break 

            biggest_num = 0
            biggest_pos = 0
            for j in range(i + 1, i + farthest + 1): #1 ~ 3 (First loop) actual => 1 ~ 2
                                                     #2 ~ 5 (Second loop) actual => 2 ~ 4
                
                if nums[j] > biggest_num: #(First loop)when j = 1, biggest_num = 3 / pos = 1 #when j = 2, biggest_num = 3 / pos = 1
                                          #(Second loop)when j = 2, biggest_num = 1 / pos = 2 #When j = 3, biggest_num = 1 / pos = 2
                                                        #when j = 4, biggest_num = 4 / pos = 4 
                    biggest_num = nums[j] 
                    biggest_pos = j
            i += biggest_pos #(First loop) 0 + 1 = 1
                             #(Second loop) 1 + 4 = 5
            
            jumps += 1 #(First loop) 0 + 1 = 1
                       #(Second loop) 1 + 1 = 2
        return jumps
                


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Day 3 Approach
        Realized that my approach to this problem might be wrong. Let's plan and recheck my approach. 
            1. We need to know how far it can jump at index 0.
            2. Then, need to know all numbers from index 0 to farthest reaching point.
            3. Compare all and move to the index which has greatest jump range.
            4. Keep doing until we reach the last index or skip the last index. 
                - In step 2, we need to update starting index from 0 to next index where we will start jumping.
            5. We need to create several base cases which help us to handle special cases before we enter complex loop.
                - Such as when list are [0] or [1, 1], etc.

            * Should we use loop to compare all numbers within range of jump?
                - I can use max() and index() built-in function to find it, but it might be little complex.
                - Loop and max(), both are O(n) time complexity and are equal in efficiency.
            * 
        """