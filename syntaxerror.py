code_with_error = 'print("Hello, World!"'

try:
    exec(code_with_error)
except SyntaxError:
    print("A syntax error occurred in the program.")
