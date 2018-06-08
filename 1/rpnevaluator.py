def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

class RpnEvaluator(object):
    def __init__(self):
        pass

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""

        members = rpn.split(sep=' ')

        stack = list()

        for i in members:
            if i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                r = a / b
                rr = a // b
                if abs(r - rr) < 0.01:
                    stack.append(rr)
                else:
                    stack.append(r)
            else:
                stack.append(num(i))
        # TODO: add your code here
        return stack.pop()
