import sys
# lines = []
# for line in sys.stdin:
#     lines.append(line[:-1])

lines = ['{asdfdsf}ddd###']
lines = ['[][[[]]]()()()()']

string = lines.pop()
letters = ''
for letter in string:
    if letter in '(){}[]':
        letters += letter

mapping = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}

stack = []
def balance(brackets):
    if brackets == '':
        return True
    
    for bracket in brackets:        
        if bracket in '({[':
            stack.append(bracket)
        else:
            if stack and stack[-1] == mapping[bracket]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

value = balance(letters)
if value:
    print('true')
else:
    print('false')

