class UF:
    def __init__(self, n:int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
    
    def find(self, node:int)->int:
        root = node
        while self.parent[root] != root:
            root = self.parent[root]
        
        
        while self.parent[node] != root:
            p = self.parent[node]
            self.parent[node] = root
            node = p
        
        return root
    
    
    def union(self, a:int, b:int)-> None:
        aroot = self.find(a)
        broot = self.find(b)
        
        if (aroot == broot):
            return
        
        if self.size[aroot] < self.size[broot]:
            self.size[broot] += self.size[aroot]
            self.parent[aroot] = broot
        else:
            self.size[aroot] += self.size[broot]
            self.parent[broot] = aroot
        
        self.n-=1
            
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key= lambda x: x[0])
        
        uf = UF(n)
        for log in logs:
            uf.union(log[1], log[2])
            if uf.n <= 1:
                return log[0]
        
        return -1
        
        
