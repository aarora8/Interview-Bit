class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        output = []
        total = 0
        count = 0
        for budget in B:
            for price in A:
                if (total + price) < budget:
                    total = total + price
                    count = count + 1
                else:
                    break
            output.append(count)
            total = 0
            count = 0
        return output
