PREC = 2 #precision

def eval_mul(string):
    string = list(string)
    ops = ['*', '/']
    fullops = ['+', '-', '*', '/']
    num1 = 0
    num2 = 0
    index = 0
    while index < len(string):
        char = string[index]
        if char in ops:
            i = index
            while i>-1:
                if string[i] in fullops or i==0:
                    break
                i = i-1
            num1 = float(str(string[i:index]))
            j = index
            while j<len(string):
                if string[j] in fullops or j==len(string)-1:
                    break
                j = j+1
            num2 = float(str(string[index+1:j]))
            if char == ops[0]:
                result = num1*num2
            else:
                result = num1/num2
            string[i:j] = str(round(result, PREC))
        index = index + 1
    return str(string)

        

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
    return (-1)**negcount*(round(float(nums[0]), PREC))


inputstring = input("Enter expression: ")
print(eval_mul(inputstring))

#for i in range(100):
#    inputstring = input("Enter expression: ")
#    if inputstring == 'x':
#        break
#    mainstring = '0'+op_adjacent(inputstring)
#    ops, nums = separate_expression(mainstring)
#    print(eval_expr(ops, nums))
