class Solution:
    def isValid(self, s: str) -> bool:

        parenthesis_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack[-1] != parenthesis_map[ch]:
                    return False
                stack.pop()
        
        return not stack
    