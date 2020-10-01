from stack import Stack
# Checks two incoming brackets to see if they are the same type
def matching(bracket1, bracket2):
    if bracket1 == "[" and bracket2 == "]":
        return True
    elif bracket1 == "{" and bracket2 == "}":
        return True
    elif bracket1 == "(" and bracket2 == ")":
        return True
    else:
        return False

def are_brackets_balanced(bracketString):
    s = Stack()
    index = 0
    balanced = True

# checks if character in string is a opening bracket and if so, is put onto the stack
# if not opening bracket, it is then checked against top of stack to see if matching
    while index < len(bracketString) and balanced:
        bracket = bracketString[index]
        if bracket in "{[(":
            s.push(bracket)
        else:
            if s.is_empty():
                balanced = False
            else:
                topBracket = s.pop()
                if not matching(topBracket, bracket):
                    balanced = False
        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False

## Enter String to be checked here:

print("String : ((({}))) is this balanced?")
print(are_brackets_balanced("((({})))"))

print("String : {{[[]]}) is this balanced?")
print(are_brackets_balanced("{{[[]]})"))