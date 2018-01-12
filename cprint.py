class helper(str):
    def __init__(self):
        self.strval = ""

    def __lshift__(self, input):
        if type(input) is helper:
            print(self.strval)
            self.strval = ""
            return self
        else:
            self.strval += str(input)
            return self

cout = helper()
endl = helper()
