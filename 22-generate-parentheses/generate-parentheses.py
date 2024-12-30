class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res= []

        def paranth(opc,cpc):

            if opc == cpc == n:
                res.append("".join(stack))
            
            if opc<n:
                stack.append('(')
                paranth(opc+1,cpc)
                stack.pop()
            
            if cpc<opc:
                stack.append(')')
                paranth(opc,cpc+1)
                stack.pop()
        
        paranth(0,0)

        return res
            