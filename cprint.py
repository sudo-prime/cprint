import sys

class Cin():
    def __init__(self):
        self.strval = ""
    def get(self):
        self.strval = input("")

    def __rshift__(self, rhs):
        if isinstance(rhs, str):
            self.get()
            return str(self.strval)
        else:
            return self

class Cout(str):
    def __init__(self):
        self.strval = ""

    def __lshift__(self, rhs):
        if isinstance(rhs, Cout):
            sys.stdout.write(self.strval)
            self.strval = ""
            return self
        elif isinstance(rhs, Cin):
            sys.stdout.write(self.strval)
            rhs.get()
            self.strval += rhs.strval
            return self
        elif isinstance(rhs, Endl):
            self.strval += rhs.strval
            return self
        else:
            self.strval += str(rhs)
            return self

class Endl(str):
    def __init__(self):
        self.strval = "\n"

class CType(object):
    def __init__(self, ptype):
        self.strval = ""
        self.val = ptype

cout = Cout()
endl = Endl()
cin = Cin()