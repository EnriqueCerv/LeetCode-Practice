# %% 380 insert delete get random
class RandomizedSet(object):

    def __init__(self):
        self.vals = []

    def valToIndex(self, val):
        if val in self.vals:
            return self.vals.index(val)
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.vals:
            self.vals.append(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.vals:
            index = self.valToIndex(val)
            self.vals.pop(index)
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        size = len(self.vals)
        import random
        index = random.randint(0,size-1)
        return self.vals[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSet(object):

    def __init__(self):
        self.vals = set()

    def insert(self, val):
        if val not in self.vals:
            self.vals.add(val)
            return True
        return False

    def remove(self, val):
        if val in self.vals:
            self.vals.remove(val)
            return True
        return False
    
    def getRandom(self):
        size = len(self.vals)
        import random
        idx = random.randint(0,size - 1)
        return list(self.vals)[idx]

