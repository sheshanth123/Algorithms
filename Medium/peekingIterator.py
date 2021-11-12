# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._peekedValue = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        
        if self._peekedValue is None:
            if not self._iterator.hasNext():
                raise Exception
            self._peekedValue = self._iterator.next()
            
        return self._peekedValue
        

    def next(self):
        """
        :rtype: int
        """
        
        if self._peekedValue is not None:
            toReturn = self._peekedValue
            self._peekedValue = None 
            return toReturn
        
        if not self._iterator.hasNext():
            raise Exception
        
        return self._iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peekedValue is not None or self._iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
