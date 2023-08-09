class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 :
            return 0
        
        if n == 1 :
            return 1
        
        v = []
        
        for i in range(0, n + 1) :
            if i == 0 :
                v.append(0)
                continue
            
            if i == 1 :
                v.append(1)
                continue
            
            if i % 2 == 0 :
                v.append(v[i//2]) 
                continue
            
            if i % 2 == 1 :
                v.append(v[i//2] + v[i//2 + 1])
                continue
        
        v.sort() 
        
        return v[len(v) - 1]      