import json

class Test:
    def __init__(self):
        self.v1 = 1
        self.v2 = 2

s = json.dumps(Test())
print(s)