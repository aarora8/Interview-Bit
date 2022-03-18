class Solution:

    def binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return (mid+1)
            elif arr[mid] < x and arr[mid+1] > x:
                return (mid+1)
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x) 
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return -1
            
    def solve(self, A, B):
        C = []
        output = []
        total = 0
        for price in A:
            total = total + price
            C.append(total)
        
        for budget in B:
            if C[len(C)-1] < budget:
                output.append(len(C))
            elif C[0] > budget:
                output.append(0)
            else:
                output.append(self.binary_search(C, 0, len(C)-1, budget))
        return output
    
 
