"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""


import random
class RandomizedSet(object):

    #Day 1 Approach (Although I passed all the test cases, average time complexity isn't O(1). I will find which part is causing it, and how can I fix it to be O(1) time complexity in average. However, it's great to pass all the test cases in one day!)
    """
    I have less understanding and experience of creating a class, attributes, methods. Through solving this problem, I will learn basics of Class and its applications.

    1. First, if a class is created, there is a constructor(_init_ for python). This initializes atrributes for instances(object). So, for this class, I need to create a set, which will be used for methods (insert, remove, and getRandom).
        - Set is appropriate for this problem because all other methods should works in average O(1) time complexity. Set.add or Set.remove functions work in O(1) time complexity.
    2. Then, initialize other methods step by step.
    3. insert() : This method insert value into the set if not present. Also, return true / false depending on presence of value.
        - Use if statement.
        - First, check whether the value is present in the set. 
        - If no, add the value into the set and return True.
        - If yes, return False.
    4. remove() : This method remove value from the set if present. Also, return true / false depending on presence of value.
        - Use if statement, too.
        - Check, if the value is in the set. 
        - If yes, remove the value and return True.
        - If no, return False immediately.
    5. getRandom() : This should randomly return a element from the set. (It's guaranteed that at least one element exists when this method is called.)
        - For now, I have no idea about how this function should be designed. First, let's try the other methods!
    """
    def __init__(self):
        self.apple = set([])

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.apple:
            return False
        else:
            self.apple.add(val)
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.apple:
            self.apple.remove(val)
            return True
        else:
            return False

        

    def getRandom(self):
        """
        :rtype: int
        """
        #This conversion of set to list is O(n) time complexity.
        return random.choice(list(self.apple))

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()