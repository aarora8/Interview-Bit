class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        output = 0
        for i in A:
            output = output + i
        return str(output)
