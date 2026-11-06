
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def comb(start):
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)

                comb(i+1)

                path.pop()

        comb(1)

        return ans