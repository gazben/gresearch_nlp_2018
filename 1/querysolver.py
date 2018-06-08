import pprint

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

class Expression:
    def eval(self):
        pass

class Operator(Expression):
    def eval(self):
        pass

class Constant(Expression):
    def eval(self):
        pass

class IntConstant(Constant):
    def __init__(self, i):
        self.i = i

    def eval(self):
        return self.i

class AddOperator(Operator):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def eval(self):
        pprint.pprint(self.lhs)
        pprint.pprint(self.rhs)
        return self.lhs.eval() + self.rhs.eval()

class SubOperator(Operator):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def eval(self):
        pprint.pprint(self.lhs)
        pprint.pprint(self.rhs)
        return self.lhs.eval() - self.rhs.eval()

class MulOperator(Operator):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def eval(self):
        pprint.pprint(self.lhs)
        pprint.pprint(self.rhs)
        return self.lhs.eval() * self.rhs.eval()

class DivOperator(Operator):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def eval(self):
        pprint.pprint(self.lhs)
        pprint.pprint(self.rhs)
        return self.lhs.eval() / self.rhs.eval()

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
        operations = list()

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
                stack.append(IntConstant(int(i)))

            if len(stack) >= 2 and len(operations) >= 1:
                i = operations.pop()
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(AddOperator(a, b))
                elif i == "-":
                    stack.append(SubOperator(a, b))
                elif i == "*":
                    stack.append(MulOperator(a, b))
                elif i == "/":
                    stack.append(DivOperator(a, b))

        return stack.pop().eval()
