class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        d = collections.defaultdict(int)
        for i in nums1:
            for j in nums2:
                d[i+j] += 1
                
        for k in nums3:
            for l in nums4:
                s = -(k+l)
                if s in d:
                    cnt += d[s]
        return cnt
