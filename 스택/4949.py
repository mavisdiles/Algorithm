import sys

while(True):
    stack = [] 
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    flag = "yes"

    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) != 0:
                temp = stack.pop() 
                if i == ")":
                    if temp == "(":
                        continue
                elif i == "]":
                    if temp == "[":
                        continue
            flag = "no"
            break
    if len(stack) !=0:
        print("no")
    else:
        print(flag)