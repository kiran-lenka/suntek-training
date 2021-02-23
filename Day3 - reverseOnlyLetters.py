class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        sLetters = []
        for i in S:
            o = ord(i)
            if (o>=65 and o<91) or (o>=97 and o<123):
                sLetters.append(i)
        
        S = list(S)
        for i in range(len(S)):
            o=ord(S[i])
            if (o>=65 and o<91) or (o>=97 and o<123):
                S[i] = sLetters.pop()
        return ''.join(S)
