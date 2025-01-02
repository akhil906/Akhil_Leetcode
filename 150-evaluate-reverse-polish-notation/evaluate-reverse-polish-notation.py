# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:

#         stack = []

#         def eval(a,b,op):
#             if op == "+":
#                 return a+b
#             elif op == "-":
#                 return a-b
#             elif op == "*":
#                 return a*b
#             elif op == "/":
#                 return a/b
        
        
        
#         for i in tokens:
#             if i == '+' or  i == '-' or  i == '*' or  i == '/':
#                 b = stack.pop()
#                 a = stack.pop()

#                 stack.append(eval(int(a),int(b),i))
#             else:
#                 stack.append(i)
        
#         return int(stack[-1])

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            if i == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)+int(b))

            elif i == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)-int(b))
            
            elif i == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)*int(b))

            elif i == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)/int(b))
            
            else:
                stack.append(i)
            
        

        return int(stack[-1])
        