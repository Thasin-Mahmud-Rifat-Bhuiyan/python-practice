# *args example (multiple values)


def add(*args):
    total = 0
    for i in args:
        total = total + i
    return total


print(add(1, 2, 3))
print(add(5, 10))


# **kwargs example (key-value pairs)


def student_info(**kwargs):
    for key in kwargs:
        print(key, ":", kwargs[key])


student_info(name="Rahim", age=20, city="Dhaka")
