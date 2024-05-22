def eval_mul(string):
    pass

def op_adjacent(string):
    slist = list(string)
    addops = ['+','-']
    i = 0
    while i < len(slist):
        if slist[i] in addops and slist[i+1] in addops:
            if slist[i]==slist[i+1]:
                slist[i] = '+'
            else:
                slist[i] = '-'
            del slist[i+1]
            i = 0
        i = i+1
    new_string = ''.join(slist)
    return new_string


def separate_expression(string):
    ops = ['+','-']
    oplist = []
    numlist = []
    lastpos = 0
    for index, char in enumerate(string):
        if char in ops:
            oplist.append(char)
            numlist.append(string[lastpos:index])
            lastpos = index+1
    numlist.append(string[lastpos:len(string)])
    return oplist, numlist

def eval_expr(ops, nums):
    n = len(nums)
    negcount = 0
    result = 0
    for _ in range(n-1):
        num1, num2 = float(nums[0]), float(nums[1])
        op = ops[0]
        if op=='+':
            result = num1 + num2
        else:
            if num1<num2:
                negcount = negcount + 1
                if len(ops)>1:
                    ops[1] = '+' if ops[1] == '-' else '-'
            result = abs(num1-num2)
        del ops[0]
        if len(nums)>1:
            del nums[0]
            nums[0] = str(result)
    return (-1)**negcount*(float(nums[0]))

for i in range(100):
    inputstring = input("Enter expression: ")
    if inputstring == 'x':
        break
    mainstring = '0'+op_adjacent(inputstring)
    ops, nums = separate_expression(mainstring)
    print(eval_expr(ops, nums))
