from ast import parse
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


# Takes user input and checks if user input has balanced brackets
import argparse
parser = argparse.ArgumentParser(description="Check if string entered is balanced")
parser.add_argument("InputString", metavar="inputString", type=str, help="String to be checked if balanced")
args = parser.parse_args()

inputString = args.InputString
print("Are these brackets balanced?  "+inputString)
if(are_brackets_balanced(inputString)):
    print("The brackets are balanced")
else :
    print("The brackets are not balanced")
