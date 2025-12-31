class Solution:
    
    def build(self, s_t):
        stack = []
        for ch in s_t:
            if ch != "#":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
                

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.build(s) == self.build(t)