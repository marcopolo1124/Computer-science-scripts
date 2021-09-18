def print_all(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(key, value)
