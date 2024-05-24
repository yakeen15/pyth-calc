#implementation of calc.py with Expression objects
class Expression:
    def __init__(self, expression, precision=2):
        self.expression = expression
        self.precision = precision
        self.result = 0.0
        self.validate()

    def validate(self):
        if not isinstance(self.expression, str):
            raise TypeError("Expression must be in string format")
        valids = ['.', '*', '/', '+', '-', '(', ')']
        for i in range(10):
            valids.append(str(i))
        for char in self.expression:
            if char not in valids:
                raise ValueError(f"Unknown symbol: {char}")
        muls = ['*', '/']
        allops = muls
        for index, _ in enumerate(list(self.expression)):
            if index == len(self.expression) - 1:
                break
            if self.expression[index] in muls and self.expression[index+1] in allops:
                raise ValueError(f"Repeated appearance of opeators symbols at position: {index+1}")

    def get_expression(self):
        return self.expression 

    def eval_parenthesis(self):
        paren_count = 0
        pos = [0, 0]
        for char in self.expression:
            if char == '(':
                #if paren_count
                paren_count = paren_count + 1
        while paren_count > 0:
            for index, char in enumerate(list(self.expression)):
                if char == '(':
                    pos[0] = index
                elif char == ')':
                    pos[1] = index
                if pos[0] != 0 and pos[1] != 0:
                    break
            subexpression = Expression(self.expression[pos[0]+1:pos[1]])
            subexpression.evaluate()
            self.expression = self.expression[0:pos[0]] + str(subexpression.result) + self.expression[pos[1]+1:len(self.expression)]
            paren_count = paren_count - 1
            

    def eval_mul(self):
        string = list(self.expression)
        ops = ['*', '/']
        fullops = ['+', '-', '*', '/']
        index = 0
        while index < len(string):
            char = string[index]
            if char in ops:
                i = index - 1
                while i > -1:
                    if string[i] in fullops or i == 0:
                        break
                    i = i - 1
                temp = ''
                for tempchar in string[i:index]:
                    temp += tempchar
                num1 = float(temp)
                j = index + 1
                while j < len(string):
                    if string[j] in fullops or j == len(string) - 1:
                        j = j - 1 if string[j] in fullops else j
                        break
                    j = j + 1
                temp = ''
                for tempchar in string[index + 1:j + 1]:
                    temp += tempchar
                num2 = float(temp)
                if char == ops[0]:
                    result = num1 * num2
                else:
                    result = num1 / num2
                del string[i:j + 1]
                result = str(round(result, self.precision))
                for r_index, r_char in enumerate(list(result)):
                    string.insert(i + r_index, r_char)
            index += 1
        self.expression = ''.join(string)
        return self

    def op_adjacent(self):
        slist = list(self.expression)
        addops = ['+', '-']
        i = 0
        while i < len(slist) - 1:
            if slist[i] in addops and slist[i + 1] in addops:
                if slist[i] == slist[i + 1]:
                    slist[i] = '+'
                else:
                    slist[i] = '-'
                del slist[i + 1]
                i = 0
            i += 1
        self.expression = ''.join(slist)
        return self

    def separate_expression(self):
        ops = ['+', '-']
        oplist = []
        numlist = []
        lastpos = 0
        for index, char in enumerate(self.expression):
            if char in ops:
                oplist.append(char)
                numlist.append(self.expression[lastpos:index])
                lastpos = index + 1
        numlist.append(self.expression[lastpos:len(self.expression)])
        return oplist, numlist

    def eval_expr(self, ops, nums):
        n = len(nums)
        negcount = 0
        result = 0
        for _ in range(n - 1):
            num1, num2 = float(nums[0]), float(nums[1])
            op = ops[0]
            if op == '+':
                result = num1 + num2
            else:
                if num1 < num2:
                    negcount += 1
                    if len(ops) > 1:
                        ops[1] = '+' if ops[1] == '-' else '-'
                result = abs(num1 - num2)
            del ops[0]
            if len(nums) > 1:
                del nums[0]
                nums[0] = str(result)
        return (-1) ** negcount * (round(float(nums[0]), self.precision))

    def evaluate(self):
        self.expression = self.expression.replace('*+','*')
        self.expression = self.expression.replace('/+','/')
        self.eval_parenthesis()
        self.eval_mul()
        self.op_adjacent()
        self.expression = '0' + self.expression
        ops, nums = self.separate_expression()
        self.result = self.eval_expr(ops, nums)
        return self.result


if __name__ == "__main__":
    for _ in range(100):
        inputstring = input("Enter expression: ")
        if inputstring == 'x':
            break
        expr = Expression(inputstring)
        print(expr.evaluate())
