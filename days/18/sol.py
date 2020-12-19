input = open('input.txt').readlines()
input = [x.strip() for x in input]
"""
This is like recursive object orientation???
"""
import re
class ExpressionTree:
    reg = r'\(([^()]+)\)'
    def __init__(self, expression):
        self.expression = expression
    
    def evaluate(self):
        expression = self.expression
        # reduce anything inside brackets
        while '(' in expression:
            for pattern in re.findall(ExpressionTree.reg, expression):
                exp = ExpressionTree(pattern)
                result = exp.evaluate()
                expression = expression.replace(f'({pattern})', str(result))
        curr = 0
        op = ''
        for val in expression.split(' '):
            if val in '+*':
                op = val
            else:
                val = int(val)
                if op == '+':
                    curr += val
                elif op == '*':
                    curr *= val
                else:
                    curr = val
        return curr
        
class NewExpressionTree:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        reg2 = r'[^*]+\ \+\ [^*]+'
        expression = self.expression
        # reduce any brackets
        while '(' in expression:
            for pattern in re.findall(ExpressionTree.reg, expression):
                exp = NewExpressionTree(pattern)
                result = exp.evaluate()
                expression = expression.replace(f'({pattern})', str(result))
        # The main difference here is i reduce any addition operations first
        while '+' in expression and '*' in expression:
            patterns = re.findall(reg2, expression)
            for pattern in patterns:
                pattern = pattern.strip()
                exp = NewExpressionTree(pattern)
                res = exp.evaluate()
                expression = expression.replace(pattern, str(res))
        curr = 0
        op = ''
        for val in expression.split(' '):
            if val in '+*':
                op = val
            else:
                val = int(val)
                if op == '+':
                    curr += val
                elif op == '*':
                    curr *= val
                else:
                    curr = val
        return curr
    

print(f'Part 1: {sum([ExpressionTree(expr).evaluate() for expr in input])}')
print(f'Part 2: {sum([NewExpressionTree(expr).evaluate() for expr in input])}')
