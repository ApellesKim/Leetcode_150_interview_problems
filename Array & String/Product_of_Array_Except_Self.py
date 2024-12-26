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


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Day 2 Approach (Complete!)
        """
        In day 1, I wrote an algorithm that runs in O(n^2) time, and that caused a problem when nums had numerous elements. So, I should use another algorithm which runs in O(n) time.

        Let's use prefix/suffix product.

        1. Create two lists which will store products of prefix and suffix. 
            - Both with n elements, and all the elements are initialized to 1.
            - 1 is often the neutral element (multiplicative identity). Multiplying any number by 1 doesn't change its value, so this initialization makes sense for prefix products.
        2. Calculate prefix:
            - This will loop through index 1 to n (right before n).
            - Since it's i - 1, it excludes itself and updates prefix.
            - Example : nums[1, 2, 3, 4] / prefix[1, 1, 1, 1]
                prefix[0] = 1 because there's no number before index 0.
                when i = 1, prefix[1] = 1 * 1 = 1
                when i = 2, prefix[2] = 2 * 1 = 2
                when i = 3, prefix[3] = 3 * 2 = 6
                So, prefix[1, 1, 2, 6]
        3. Calculate suffix:
            - This will loop from second last index to 0 backwards.
            - It also excludes itself.
            - Example : nums[1, 2, 3, 4]
                suffix[3] = 1
                suffix[2] = 1 * 4 = 4
                suffix[1] = 4 * 3 = 12
                suffix[0] = 12 * 2 = 24
                So, suffix[24, 12, 4, 1]
        4. Multiply prefix and suffix to find product of array except i itself.
        """
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(n)]
        
        return answer

