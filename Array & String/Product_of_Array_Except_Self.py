"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #Day 1 approach (!8/24 testcases passed : time limit exceeded)
        """
        First thought about solution is to create list ans and to use double for loop to append products into the list.

        1. Initialize an empty list ans.
        2. Create a for loop which loops through all of the elements in the array nums.
            - Initialize product = 0. -> This should be fixed. Since 0 multiplies any number is 0, so I can't find the product of the elements. This can just be procut = 1.
        3. Create another for loop inside.
            - This for loop will also loop through all of the elements in the array nums.
            - Multiply every element except self everytime it loops and update product.
        4. After inner for loop is completed, append product to list ans.
        5. Return ans.

        The problem occurs here. [0,0]
        My condition of inner loop skips when nums[i] == nums[j]. When elements in the list are the same, it not only skips itself but other elements too. 
        So, I think that I should use another condition to skip itself.
        This can be solved by changing condition to i == j.

        Another problem occured. Time limit exceeded when nums's length is huge.
        I have no idea about this right now.
        Double for loop is O(n^2) in space complexity, so it might have problem when input is large. So, I better to use another algorithm to solve this problem.
        """
        ans = []
        n = len(nums)

        for i in range(n):
            product = 1
            for j in range(n):
                if j == i:
                    continue
                product = product * nums[j]
                
            ans.append(product)

        return ans
