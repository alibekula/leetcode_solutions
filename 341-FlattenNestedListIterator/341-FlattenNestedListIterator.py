# Last updated: 13.08.2025, 16:57:46
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # This will flatten the nestedList immediately upon initialization
        self.stack = []
        self.flatten(nestedList)
    
    def flatten(self, nestedList):
        # Recursively flatten the structure
        for item in nestedList:
            if item.isInteger():
                self.stack.append(item.getInteger())
            else:
                self.flatten(item.getList())
    
    def next(self) -> int:
        # Return the next element from the flattened list
        return self.stack.pop(0)
    
    def hasNext(self) -> bool:
        # Return True if there are still elements to return
        return len(self.stack) > 0
