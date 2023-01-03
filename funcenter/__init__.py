__version__ = "1.03.1"
import time


def uncharsplit(list):
    string = ""
    for element in list:
        string += str(element)
    return string


def charsplit(str):
    x = []
    for char in str:
        x.append(char)
    return x


def isdecimal(var):
    if var.is_integer():
        return False
    else:
        return True


def is_decimal(var):
    if var.is_integer():
        return False
    else:
        return True


def factorial(num):
    if num < 0:
        return False
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial


def mp(num):
    steps = 0
    while result >= 10:
        num = str(num)
        nums = list(num)
        x = len(nums)
        y = 1
        while x > 0:
            z = int(nums[x - 1])
            y = y * z
            x -= 1
        result = y
        steps += 1


# PRINTING
def println(str, x=1):
    print(str + ("\n" * x))


def printsln(str):
    print(str, end="")


def printx(str, x):
    for i in range(0, x):
        print(str)


def typewriter(str, speed=1):
    if speed == 1:
        speed = 0.18
    elif speed == 2:
        speed = 0.1
    elif speed == 3:
        speed = 0.03
    for char in str:
        time.sleep(speed)
        print(char, end="", flush=True)
    print()


# FORMATTING
def bold(str):
    output = "\033[1m" + str + "\033[0m"
    return output


def b(str):
    output = "\033[1m" + str + "\033[0m"
    return output


def italic(str):
    output = "\033[3m" + str + "\033[0m"
    return output


def i(str):
    output = "\033[3m" + str + "\033[0m"
    return output


def underline(str):
    output = "\033[4m" + str + "\033[0m"
    return output


def underl(str):
    output = "\033[4m" + str + "\033[0m"
    return output


def ul(str):
    output = "\033[4m" + str + "\033[0m"
    return output


def format(color=""):
    if color == "bold" or var == "b":
        print("\033[1m", end="")
    elif color == "italic" or var == "i":
        print("\033[3m", end="")
    elif color == "underline" or var == "underl" or var == "ul":
        print("\033[4m", end="")
    elif color == "black":
        print("\033[0;30m", end="")
    elif color == "red":
        print("\033[0;31m", end="")
    elif color == "green":
        print("\033[0;32m", end="")
    elif color == "yellow":
        print("\033[0;33m", end="")
    elif color == "blue":
        print("\033[0;34m", end="")
    elif color == "magenta":
        print("\033[0;35m", end="")
    elif color == "cyan":
        print("\033[0;36m", end="")
    elif color == "white":
        print("\033[0;37m", end="")
    elif color == "bright_black":
        print("\033[0;90m", end="")
    elif color == "bright_red":
        print("\033[0;91m", end="")
    elif color == "bright_green":
        print("\033[0;92m", end="")
    elif color == "bright_yellow":
        print("\033[0;93m", end="")
    elif color == "bright_blue":
        print("\033[0;94m", end="")
    elif color == "bright_magenta":
        print("\033[0;95m", end="")
    elif color == "bright_cyan":
        print("\033[0;96m", end="")
    elif color == "bright_white":
        print("\033[0;97m", end="")
    elif color == "clear":
        print("\033[0m", end="")


def clear():
    print("\033[0m", end="")


### COLORS
def black(str="", setColor=False):
    if str == "":
        print("\033[0;30m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;30m" + str
        else:
            output = "\033[0;30m" + str + "\033[0m"
    return output


def red(str="", setColor=False):
    if str == "":
        print("\033[0;31m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;31m" + str
        else:
            output = "\033[0;31m" + str + "\033[0m"
    return output


def green(str="", setColor=False):
    if str == "":
        print("\033[0;32m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;32m" + str
        else:
            output = "\033[0;32m" + str + "\033[0m"
    return output


def yellow(str="", setColor=False):
    if str == "":
        print("\033[0;33m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;33m" + str
        else:
            output = "\033[0;33m" + str + "\033[0m"
    return output


def blue(str="", setColor=False):
    if str == "":
        print("\033[0;34m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;34m" + str
        else:
            output = "\033[0;34m" + str + "\033[0m"
    return output


def magenta(str="", setColor=False):
    if str == "":
        print("\033[0;35m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;35m" + str
        else:
            output = "\033[0;35m" + str + "\033[0m"
    return output


def cyan(str="", setColor=False):
    if str == "":
        print("\033[0;36m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;36m" + str
        else:
            output = "\033[0;36m" + str + "\033[0m"
    return output


def white(str="", setColorColor=False):
    if str == "":
        print("\033[0;37m", end="")
        output = None
    else:
        if setColor:
            output = "\033[0;37m" + str
        else:
            output = "\033[0;37m" + str + "\033[0m"
    return output


def color(color="", str=""):
    if str == "":
        if color == "black":
            print("\033[0;30m", end="")
        elif color == "red":
            print("\033[0;31m", end="")
        elif color == "green":
            print("\033[0;32m", end="")
        elif color == "yellow":
            print("\033[0;33m", end="")
        elif color == "blue":
            print("\033[0;34m", end="")
        elif color == "magenta":
            print("\033[0;35m", end="")
        elif color == "cyan":
            print("\033[0;36m", end="")
        elif color == "white":
            print("\033[0;37m", end="")
        elif color == "bright_black":
            print("\033[0;90m", end="")
        elif color == "bright_red":
            print("\033[0;91m", end="")
        elif color == "bright_green":
            print("\033[0;92m", end="")
        elif color == "bright_yellow":
            print("\033[0;93m", end="")
        elif color == "bright_blue":
            print("\033[0;94m", end="")
        elif color == "bright_magenta":
            print("\033[0;95m", end="")
        elif color == "bright_cyan":
            print("\033[0;96m", end="")
        elif color == "bright_white":
            print("\033[0;97m", end="")
        elif color == "clear":
            print("\033[0m", end="")
    else:
        if color == "black":
            output = "\033[0;30m" + str + "\033[0m"
        elif color == "red":
            output = "\033[0;31m" + str + "\033[0m"
        elif color == "green":
            output = "\033[0;32m" + str + "\033[0m"
        elif color == "yellow":
            output = "\033[0;33m" + str + "\033[0m"
        elif color == "blue":
            output = "\033[0;34m" + str + "\033[0m"
        elif color == "magenta":
            output = "\033[0;35m" + str + "\033[0m"
        elif color == "cyan":
            output = "\033[0;36m" + str + "\033[0m"
        elif color == "white":
            output = "\033[0;37m" + str + "\033[0m"
        elif color == "bright_black":
            output = "\033[0;90m" + str + "\033[0m"
        elif color == "bright_red":
            output = "\033[0;91m" + str + "\033[0m"
        elif color == "bright_green":
            output = "\033[0;92m" + str + "\033[0m"
        elif color == "bright_yellow":
            output = "\033[0;93m" + str + "\033[0m"
        elif color == "bright_blue":
            output = "\033[0;94m" + str + "\033[0m"
        elif color == "bright_magenta":
            output = "\033[0;95m" + str + "\033[0m"
        elif color == "bright_cyan":
            output = "\033[0;96m" + str + "\033[0m"
        elif color == "bright_white":
            output = "\033[0;97m" + str + "\033[0m"
        else:
            output = None
        return output


def fprint(color, str):
    colors = [
        "bold",
        "b",
        "italic",
        "i",
        "underline",
        "underl",
        "ul",
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
        "bright_black",
        "bright_red",
        "bright_green",
        "bright_yellow",
        "bright_blue",
        "bright_magenta",
        "bright_cyan",
        "bright_white",
    ]
    if color in colors:
        if color == "bold" or color == "b":
            print("\033[1m" + str + "\033[0m")
        elif color == "italic" or color == "i":
            print("\033[3m" + str + "\033[0m")
        elif color == "underline" or color == "underl" or color == "ul":
            print("\033[4m" + str + "\033[0m")
        elif color == "black":
            print("\033[0;30m" + str + "\033[0m")
        elif color == "red":
            print("\033[0;31m" + str + "\033[0m")
        elif color == "green":
            print("\033[0;32m" + str + "\033[0m")
        elif color == "yellow":
            print("\033[0;33m" + str + "\033[0m")
        elif color == "blue":
            print("\033[0;34m" + str + "\033[0m")
        elif color == "magenta":
            print("\033[0;35m" + str + "\033[0m")
        elif color == "cyan":
            print("\033[0;36m" + str + "\033[0m")
        elif color == "white":
            print("\033[0;37m" + str + "\033[0m")
        elif color == "bright_black":
            print("\033[0;90m" + str + "\033[0m")
        elif color == "bright_red":
            print("\033[0;91m" + str + "\033[0m")
        elif color == "bright_green":
            print("\033[0;92m" + str + "\033[0m")
        elif color == "bright_yellow":
            print("\033[0;93m" + str + "\033[0m")
        elif color == "bright_blue":
            print("\033[0;94m" + str + "\033[0m")
        elif color == "bright_magenta":
            print("\033[0;95m" + str + "\033[0m")
        elif color == "bright_cyan":
            print("\033[0;96m" + str + "\033[0m")
        elif color == "bright_white":
            print("\033[0;97m" + str + "\033[0m")
        else:
            print(str)
    else:
        print(color)


def cprint(color, str):
    colors = [
        "bold",
        "b",
        "italic",
        "i",
        "underline",
        "underl",
        "ul",
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
        "bright_black",
        "bright_red",
        "bright_green",
        "bright_yellow",
        "bright_blue",
        "bright_magenta",
        "bright_cyan",
        "bright_white",
    ]
    if color in colors:
        if color == "bold" or color == "b":
            print("\033[1m" + str + "\033[0m")
        elif color == "italic" or color == "i":
            print("\033[3m" + str + "\033[0m")
        elif color == "underline" or color == "underl" or color == "ul":
            print("\033[4m" + str + "\033[0m")
        elif color == "black":
            print("\033[0;30m" + str + "\033[0m")
        elif color == "red":
            print("\033[0;31m" + str + "\033[0m")
        elif color == "green":
            print("\033[0;32m" + str + "\033[0m")
        elif color == "yellow":
            print("\033[0;33m" + str + "\033[0m")
        elif color == "blue":
            print("\033[0;34m" + str + "\033[0m")
        elif color == "magenta":
            print("\033[0;35m" + str + "\033[0m")
        elif color == "cyan":
            print("\033[0;36m" + str + "\033[0m")
        elif color == "white":
            print("\033[0;37m" + str + "\033[0m")
        elif color == "bright_black":
            print("\033[0;90m" + str + "\033[0m")
        elif color == "bright_red":
            print("\033[0;91m" + str + "\033[0m")
        elif color == "bright_green":
            print("\033[0;92m" + str + "\033[0m")
        elif color == "bright_yellow":
            print("\033[0;93m" + str + "\033[0m")
        elif color == "bright_blue":
            print("\033[0;94m" + str + "\033[0m")
        elif color == "bright_magenta":
            print("\033[0;95m" + str + "\033[0m")
        elif color == "bright_cyan":
            print("\033[0;96m" + str + "\033[0m")
        elif color == "bright_white":
            print("\033[0;97m" + str + "\033[0m")
        else:
            print(str)
    else:
        print(color)
