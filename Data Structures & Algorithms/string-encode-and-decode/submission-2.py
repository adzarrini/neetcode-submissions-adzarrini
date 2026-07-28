class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = [f"{len(w)}#{w}" for w in strs]
        return "".join(coded)

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0;
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            words.append(word)
            i = j + 1 + length
        return words