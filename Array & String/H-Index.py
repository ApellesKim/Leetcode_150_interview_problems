"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        #Day 1 approach
        """
        When calculating h-index, it's useful to follow these steps.
            1. List all of your published papers
            2. Count the number of citations for each paper
            3. Sort the papers by citation count
            4. Find the h-index
                - Start from the biggest citation.
                - Compare its citation number and its index.
                - If citation number is smaller than index, return that index as h-index
                - If greater, move to the next index and compare the same.
        Let's try writing this into a pseudocode
        """
        
        #lst = sort(citations)
        #h_index = 0
        #for i in range(n):
            


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        #Day 2 approach (Continaution of day 1)
        """
        When calculating h-index, it's useful to follow these steps.
            1. List all of your published papers
            2. Count the number of citations for each paper
                - It's already listed in the citations.
            3. Sort the papers by citation count
                - Let's use .sort() method. Here, we need to sort descendingly, so let's use reverse=True.
            4. Find the h-index
                - Start from the biggest citation.
                - Compare its citation number and its index.
                - If citation number is smaller than index, return that index as h-index
                - If greater, move to the next index and compare the same.
        Let's try writing this into a pseudocode
        """
        
        citations.sort(reverse=True) #sorting the list descendingly
        h_index = 0 #initializing h_index to 0
        n = len(citations)

        for i in range(n): #this will loop through the list
            if citations[i] >= i + 1: #Calcualte h_index from biggest number.
                h_index += 1
            else:
                break #If any i fails, doesn't need to check any further becuase the numbers are sorted descendingly.
        
        return h_index #After the loop breaks, just return h_index.