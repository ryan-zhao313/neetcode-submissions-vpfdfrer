class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = Counter(s1)
        l = 0
        matches = 0
        k = len(s1)

        for r in range(len(s2)):
            char = s2[r]
            
            # character matches
            if char in pattern:
                pattern[char] -= 1
                if pattern[char] == 0:
                    matches += 1

            if r - l + 1 > k:
                l_char = s2[l]
                if l_char in pattern:
                    if pattern[l_char] == 0:
                        matches -= 1
                    pattern[l_char] += 1
                l += 1

            if matches == len(pattern):
                return True

        return False