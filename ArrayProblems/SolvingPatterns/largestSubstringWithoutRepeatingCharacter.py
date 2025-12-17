class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_of_characters = set()
        left = 0
        len_window = 0

        for right in range(len(s)):
            while s[right] in set_of_characters:
                set_of_characters.remove(s[left])
                left+=1
            
            set_of_characters.add(s[right])
            len_window = max(len_window, right - left + 1)

        return len_window


obj = Solution()
x = obj.lengthOfLongestSubstring("pwwkew")
print(x)