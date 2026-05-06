class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            st1 = tuple(sorted(s))
            if st1 in res:
                res[st1].append(s)
            else:
                res[st1] = [s]

        return list(res.values())