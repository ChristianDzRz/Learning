from abc import ABCMeta ,abstractmethod

class Sequence(metaclass=ABCMeta):

    @abstractmethod
    def __len__(self):
        """"Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """ Return the element at the index j of the sequnce"""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
    
    def __eq__(self, other):
        if len(self) != len(other):
            return ValueError('Both sequence have to be the same length')
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
            else:
                return True
            
    def __lt__(self, other):
        if len(self) != len(other):
            return ValueError('Both sequence have to be the same length')
        for i in range(len(self)):
            if self[i] < other[i]:
                return True
        return False
    
    def index(self, val):
        """Return leftmost index at which val is found ( or raise ValueError)"""
        for j in range(len(self)):
            if self[j] == val:
                return
        raise ValueError('value not in sequence')
    
    def count(self, val):
        """Return the number of elements equal to given value"""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k+=1
            return k

class TestSequence(Sequence):
    def __init__(self, arr):
        self._sequence = arr

    def __len__(self):
        return(len(self._sequence))

    
    def __getitem__(self, j):
        return self._sequence[j]
        
        
if __name__ == "__main__":
    sequence1 = TestSequence(["a","b","c","d"])
    print(list(sequence1))
    print(sequence1 < ["a", "c", "c", "d"])




    
        
    