class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursion(temp,freq):
            if len(temp)==len(nums):
                ans.append(temp)
                return
        
            for i in range(len(freq)):
                if freq[i]==0:
                    freq[i]=1
                    recursion(temp+[nums[i]],freq)
                    freq[i]=0

        ans=[]
        freq=[0 for i in range(len(nums))]
        recursion([],freq)
        return ans