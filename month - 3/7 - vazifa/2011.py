class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        lenght = len(operations)
        for i in range(lenght):
            if(operations[i]=='++X'or operations[i]=='X++'):
                count += 1
            elif(operations[i]=='--X'or operations[i]=='X--'):
                count -= 1
        return count


