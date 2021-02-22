class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u']
        sVowels = []
        for i in s:
            if i.lower() in vowels:
                sVowels.append(i)
        
        s = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s[i] = sVowels.pop()
        return ''.join(s)
