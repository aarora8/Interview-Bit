class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count_0 = 0
        count_1 = 0
        count_subarr = 0
        for val in A:
            if val == str(0):
                count_0 = count_0 + 1
            else:
                count_1 = count_1 + 1
            if count_0 == count_1:
                count_subarr = count_subarr + 1
                count_0 = 0
                count_1 = 0
        return count_subarr
