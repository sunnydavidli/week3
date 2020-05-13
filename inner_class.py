# define a function firstly
def format_string(string, formatter=None):
    # inside the function, we define a class
    class DefaultFormatter:
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)


hello_string = "Hello, everyone, nice to meet you!"
print("input: " + hello_string)
print("output: " + format_string(hello_string))