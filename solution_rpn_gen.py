#coding=utf-8

class Solution:
    def evalRPN(self, tokens):
        s = [ ]
        ops = ( '+', '-', '*', '/' )
        for t in tokens:
            if t in ops:
                if t == '+':
                    s.append(s.pop()+s.pop())
                elif t == '-':
                    s.append(-s.pop()+s.pop())
                elif t == '*':
                    s.append(s.pop()*s.pop())
                elif t == '/':
                    a, b = s.pop(), s.pop()
                    o = b/a
                    if o < 0 and b%a != 0:
                        o += 1
                    s.append(o)
            else:
                s.append(int(t))
        return s.pop()

# 老生常谈的堆栈表达式求值
# 感觉写起来怪怪的，还有
# Python 的负整数除法简直是个坑
# 统一 floor() ...
#
# 141230 PM

s = Solution()
print(s.evalRPN(['2', '1', '+', '3', '*']))
print(s.evalRPN(['4', '13', '5', '/', '+']))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

