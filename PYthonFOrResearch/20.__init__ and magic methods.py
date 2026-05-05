class Number:
    def __init__(self, value):
        self.value = value

    # magic method (dunder)
    def __str__(self):
        return f"Value is {self.value}"


n = Number(10)
print(n)
