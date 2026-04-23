class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}

        for word in strs:
            a.setdefault("".join(sorted(word)), []).append(word)

        return list(a.values())



        
        