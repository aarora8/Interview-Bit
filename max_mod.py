class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_mod = 0
        for i in A:
            for j in A:
                if (i%j) > max_mod:
                    max_mod = (i%j)
        return max_mod
