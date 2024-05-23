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
            i = index-1
            while i>-1:
                if string[i] in fullops or i==0:
                    break
                i = i-1
            temp = ''
            for tempchar in string[i:index]:
                temp = temp + tempchar
            num1 = float(str(temp))
            j = index+1
            while j<len(string):
                if string[j] in fullops or j==len(string)-1:
                    j = j - 1 if string[j] in fullops else j
                    break
                j = j+1
            temp = ''
            for tempchar in string[index+1:j+1]:
                temp = temp + tempchar
            num2 = float(str(temp))
            if char == ops[0]:
                result = num1*num2
            else:
                result = num1/num2
            del string[i:j+1]
            result = str(round(result, PREC))
            for r_index, r_char in enumerate(list(result)):
                string.insert(i+r_index, r_char)
        index = index + 1
    simpstring = ''
    for simpchar in string:
        simpstring = simpstring+simpchar
    return str(simpstring)

        

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


for i in range(100):
    inputstring = input("Enter expression: ")
    if inputstring == 'x':
        break
    inputstring = eval_mul(inputstring)
    mainstring = '0'+op_adjacent(inputstring)
    ops, nums = separate_expression(mainstring)
    print(eval_expr(ops, nums))
