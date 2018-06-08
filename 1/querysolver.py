def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def div(a, b):
    r = a / b
    rr = a // b
    if abs(r - rr) < 0.01:
        return rr
    else:
        return r

class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, rpn):

        members = rpn.split(sep=' ')

        stack = list()
        operations = list();

        for i in members:
            if i == "+":
                operations.append("+")
            elif i == "-":
                operations.append("-")
            elif i == "*":
                operations.append("*")
            elif i == "/":
                operations.append("/")
            else:
                stack.append(num(i))

            if len(stack) >= 2 and len(operations) >= 1:
                i = operations.pop()
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(div(a,b))

        return stack.pop()
