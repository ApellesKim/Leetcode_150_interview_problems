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


class RandomizedSet(object):

    #Day 2 Approach (I realized that since set also uses hash table to store elements, we can use map instead of set. It's also O(1) time complexity. Using both map and list can be efficient in time complexity, in other words, it can run in O(1) time complexity.)
    """
    In day 1, insert and remove methods run in O(1) time complexity, but getRandom didn't. Random.choice() function can only be used in list, tuple, or string, which can directly access elements by index. So, in a process of converting set to list, the method ran in O(n) time complexity.

    So, today's goal is to fix getRandom function to run in O(1) time complexity.

    Possible solutions:
    1. Create a list and update it as well as set. Then, it might be able to use random.choice() function.
        - However, while checking val in list, I shouldn't use for loop since it becomes O(n).
            1) So, we can just follow as set does. (After checking though set, we can add for both set and list.)   
    Removing specific number from a list is running in O(n) time complexity. So, creating a list might not be a good idea.

    2. Create a map and list. 
        - Need a better understanding about method remove().
    
    """
    def __init__(self):
        self.d_map = {}
        self.d = [] 

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d_map: #checking dictionary is O(1) while checking array is O(n)
            return False
        
        self.d_map[val] = len(self.d) #key is val, and value is index of the new element 
        self.d.append(val) #Adding value to the list

        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.d_map:
            return False

        #moving last element in list to the position of element, which we will remove.
        last_elem = self.d[-1]
        remv_elem_i = self.d_map[val]

        self.d_map[last_elem] = remv_elem_i
        self.d[remv_elem_i] = last_elem 

        self.d[-1] = val

        self.d.pop()

        self.d_map.pop(val)
        return True
        

        

    def getRandom(self):
        """
        :rtype: int
        """
        #This conversion of set to list is O(n) time complexity.
        return random.choice(self.d)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class RandomizedSet(object):

    #Day 3 Approach 
    """
    1. Create a map and list. 
        1) method init()
            - Create an empty map and list which will be used through entire class.
        2) method insert()
            - We are inserting a value only if the value is not present in the map.
            - If the value is already present in the map, immediately return False.
            - Otherwise, we are going to insert the value into the map. (val is the key, and value is index + 1)
            - Also, add the value to the end of the list.
            - Then, return True.
        3) method remove()
            - Same as insert(), we can remove only when the value is present in the map.
            - Check and if the value is not present, return False immediately.
            - If the value is found in the map:
                - We are going to switch the position of target value with last value of the list. Then, pop the last value.
                - Initialize two variables: last_elem & i_remv_elem
                - Then swap last element and removable element.
        4) method getRandom()
            - random.choice() function can randomly pick a number from a list in O(1) time complexity.

    Therefore, every method in this class runs in O(1) time complexity. Hurray!

    
    """
    def __init__(self):
        self.d_map = {}
        self.d = [] 
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d_map: #checking dictionary is O(1) while checking array is O(n)
            return False
        
        self.d_map[val] = len(self.d)  
        self.d.append(val) 

        return True
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.d_map:
            return False
                                      # want to remove 4
        last_elem = self.d[-1]        # map [2:0, 4:1, 7:2, 1:3, 0:4] / list [2, 4, 7, 1, 0]
        i_remv_elem = self.d_map[val] # last_elem = 0 / i_remv_elem = 2

        self.d_map[last_elem] = i_remv_elem #d_map[0] = 2
        self.d[i_remv_elem] = last_elem     #d[2] = 0 -> [2, 0, 7, 1, 0]

        self.d[-1] = val                    #[2, 0, 7, 1, 4]

        self.d.pop()                        #remove 4 at the end.

        self.d_map.pop(val)                 #remove 4:2.
        return True

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.d)