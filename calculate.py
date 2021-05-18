import re


def calculate(cadena):
    regex = re.compile(r'([\d]{1,}[+-][\d]{1,})')
    if regex.search(cadena):
        parenthesis_op = regex.search(cadena).group()

        parenthesis_result = (eval(parenthesis_op))

        string = cadena.replace('('+parenthesis_op+')', str(parenthesis_result))

    return eval(string)


if __name__ == "__main__":
    suma = calculate('(((2-1)-10+5))')
    print(suma)
        