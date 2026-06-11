class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch == ',':
                continue

            if ch != ')':
                stack.append(ch)
            else:
                vals = set()

                while stack[-1] != '(':
                    vals.add(stack.pop())

                stack.pop()
                op = stack.pop()

                if op == '!':
                    stack.append('t' if 'f' in vals else 'f')
                elif op == '&':
                    stack.append('f' if 'f' in vals else 't')
                else:  # '|'
                    stack.append('t' if 't' in vals else 'f')

        return stack[-1] == 't'