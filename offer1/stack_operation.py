

class Solution:
    def validateStackSequences(self, pushed, popped):
        """验证入栈顺序与出闸三年顺序是否一致"""
        stack = []
        j = 0
        print(f"popped-->{popped}")
        for n in pushed:
            stack.append(n)
            print(f"pushed:{n}-->{stack}")
            while len(stack) > 0 and popped[j] == stack[-1]:
                print(f"pop:{popped[j]}-->{stack}-->{popped}")
                stack.pop()
                j += 1
        print(f"{stack}-->\n{popped}")
        return len(stack) == 0


if __name__ == "__main__":
    so = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    # pushed = [1, 2, 3, 4, 5]
    # popped = [4, 3, 5, 1, 2]
    # pushed = [0, 2, 1]
    # popped = [0, 1, 2]
    # pushed = [1, 0, 3, 2]
    # popped = [0, 1, 2, 3]
    # pushed = [4, 0, 1, 2, 3]
    # popped = [4, 2, 3, 0, 1]
    # pushed = [1, 9, 8, 3, 0, 2, 6, 7, 5, 4]
    # popped = [9, 8, 4, 7, 3, 2, 5, 1, 6, 0]
    res = so.validateStackSequences(pushed, popped)
    print(res)
