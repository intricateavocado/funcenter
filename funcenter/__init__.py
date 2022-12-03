__version__ = '1.01'
import time

def uncharsplit(list):
    return ''.join(list)


def charsplit(str):
    x = []
    for char in str:
        x.append(char)
    return x


def check_similarity(test, check, rating, debug = False):
    # SETUP
    score = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    x = []
    for letter in test:
        x.append(letter)
    test = x
    x = []
    for letter in check:
        x.append(letter)
    check = x

    # SECTION MATCH METHOD
    char_count = len(test)
    longest_count = len(check)
    if char_count > len(check):
        char_count = len(check)
        longest_count = len(test)
    if longest_count < 15:
        test_sections = []
        w = 0
        while w != (len(test)-2):
            prev = ''
            for i in test[w:]:
                if prev:
                    prev += i
                    test_sections.append(prev)
                else:
                    prev = i
            w += 1
        check_sections = []
        w = 0
        while w != (len(check)-2):
            prev = ''
            for i in check[w:]:
                if prev:
                    prev += i
                    check_sections.append(prev)
                else:
                    prev = i
            w += 1
    matches = 0
    for string in test_sections:
        for compare in check_sections:
            if string == compare:
                matches += 1
    if matches >= 2/5*(len(check)):
        if matches >= 4/5*(len(check)):
            score += 2
        else:
            score += 1
        if debug:
            print("\033[0;32m" + "STR_MATCH({0}) ✓".format(matches) + "\033[0m")
    else:
        if debug:
            print("\033[0;32m" + "STR_MATCH({0}) ✖".format(matches) + "\033[0m")
    # END OF SECTION MATCH METHOD
    # BEGIN CONSONANT POSITION METHOD
    same_char = 0
    test_cons = []
    for char in test:
        if char not in vowels:
            test_cons.append(char)
    check_cons = []
    for char in check:
        if char not in vowels:
            check_cons.append(char)
    con_count = len(test_cons)
    if con_count > len(check_cons):
        con_count = len(check_cons)
    for i in range(con_count):
        if test_cons[i] == check_cons[i]:
            same_char += 1
    if same_char >= (char_count/2):
        if debug:
            print("\033[0;32m" + "CONS_POS ✓" + "\033[0m")
        score += 1
    else:
        if debug:
            print("\033[0;32m" + "CONS_POS ✖" + "\033[0m")
    # END CONSONANT POSITION METHOD
    # BEGIN CHARACTER POSITION METHOD
    same_char = 0
    for i in range(char_count):
        if test[i] == check[i]:
            same_char += 1
    if same_char >= (char_count/2):
        if debug:
            print("\033[0;32m" + "CHAR_POS ✓" + "\033[0m")
        score += 1
    else:
        if debug:
            print("\033[0;32m" + "CHAR_POS ✖" + "\033[0m")
    # END CHARACTER POSITION METHOD
    # BEGIN UNIQUENESS METHOD
    test_unique = []
    check_unique = []
    for char in test:
        if char not in test_unique:
            test_unique.append(char)
    for char in check:
        if char not in check_unique:
            check_unique.append(char)
    if test_unique == check_unique:
        if debug:
            print("\033[0;32m" + "UNIQUE ✓" + "\033[0m")
        score += 2
    else:
        if debug:
            print("\033[0;32m" + "UNIQUE ✖" + "\033[0m")
    # END UNIQUENESS METHOD
    # BEGIN LAST3-UNIQUENESS METHOD
    test_unique = []
    check_unique = []
    last3 = 0
    for char in test[:]:
        if char not in test_unique:
            test_unique.append(char)
    for char in check[:3]:
        if char not in check_unique:
            check_unique.append(char)
    for char in test_unique:
        for char_ in check_unique:
            if char == char_:
                last3 += 1
    if last3 >= 2:
        if debug:
            print("\033[0;32m" + "LAST3_CHECK ✓" + "\033[0m")
            score += 1
    else:
        if debug:
            print("\033[0;32m" + "LAST3_CHECK ✖" + "\033[0m")
            score -= 1
    # END LAST3-UNIQUENESS METHOD
    # BEGIN LENGTH CHECK
    if (len(test) + 2) >= len(check):
        score -= 1
    elif (len(check) + 2) >= len(test):
        score -= 1
    # END LENGTH CHECK
    # RETURNS AND DEBUG
    if debug:
        print("\033[0;35m" + str(score) + "\033[0m")
    if score >= rating:
        return True
    else:
        return False


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


# PRINTING
def println(str, x = 1):
    print(str + ("\n"*x))


def printsln(str):
    print(str, end='')

 
def printx(str, x):
    for i in range(0, x):
        print(str)


def typewriter(str, speed = 1):
    if speed == 1:
        speed = 0.18
    elif speed == 2:
        speed = 0.1
    elif speed == 3:
        speed = 0.03
    for char in str:
        time.sleep(speed)
        print(char, end='', flush=True)
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
def format(color = ''):
    if color == 'bold' or var == 'b':
        print("\033[1m", end='')
    elif color == 'italic' or var == 'i':
        print("\033[3m", end='')
    elif color == 'underline' or var == 'underl' or var == 'ul':
        print("\033[4m", end='')
    elif color == 'black':
        print("\033[0;30m", end='')
    elif color == 'red':
        print("\033[0;31m", end='')
    elif color == 'green':
        print("\033[0;32m", end='')
    elif color == 'yellow':
        print("\033[0;33m", end='')
    elif color == 'blue':
        print("\033[0;34m", end='')
    elif color == 'magenta':
        print("\033[0;35m", end='')
    elif color == 'cyan':
        print("\033[0;36m", end='')
    elif color == 'white':
        print("\033[0;37m", end='')
    elif color == 'bright_black':
        print("\033[0;90m", end='')
    elif color == 'bright_red':
        print("\033[0;91m", end='')
    elif color == 'bright_green':
        print("\033[0;92m", end='')
    elif color == 'bright_yellow':
        print("\033[0;93m", end='')
    elif color == 'bright_blue':
        print("\033[0;94m", end='')
    elif color == 'bright_magenta':
        print("\033[0;95m", end='')
    elif color == 'bright_cyan':
        print("\033[0;96m", end='')
    elif color == 'bright_white':
        print("\033[0;97m", end='')
    elif color == 'clear':
        print("\033[0m", end='')
        
def clear():
    print("\033[0m", end='')
### COLORS
def black(str = '', setColor = False):
    if str == '':
        print("\033[0;30m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;30m" + str
        else:
            output = "\033[0;30m" + str + "\033[0m"
    return output
def red(str = '', setColor = False):
    if str == '':
        print("\033[0;31m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;31m" + str
        else:
            output = "\033[0;31m" + str + "\033[0m"
    return output
def green(str = '', setColor = False):
    if str == '':
        print("\033[0;32m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;32m" + str
        else:
            output = "\033[0;32m" + str + "\033[0m"
    return output
def yellow(str = '', setColor = False):
    if str == '':
        print("\033[0;33m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;33m" + str
        else:
            output = "\033[0;33m" + str + "\033[0m"
    return output
def blue(str = '', setColor = False):
    if str == '':
        print("\033[0;34m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;34m" + str
        else:
            output = "\033[0;34m" + str + "\033[0m"
    return output
def magenta(str = '', setColor = False):
    if str == '':
        print("\033[0;35m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;35m" + str
        else:
            output = "\033[0;35m" + str + "\033[0m"
    return output
def cyan(str = '', setColor = False):
    if str == '':
        print("\033[0;36m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;36m" + str
        else:
            output = "\033[0;36m" + str + "\033[0m"
    return output
def white(str = '', setColorColor = False):
    if str == '':
        print("\033[0;37m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;37m" + str
        else:
            output = "\033[0;37m" + str + "\033[0m"
    return output
def color(color = '', str = ''):
    if str == '':
        if color == 'black':
            print("\033[0;30m", end='')
        elif color == 'red':
            print("\033[0;31m", end='')
        elif color == 'green':
            print("\033[0;32m", end='')
        elif color == 'yellow':
            print("\033[0;33m", end='')
        elif color == 'blue':
            print("\033[0;34m", end='')
        elif color == 'magenta':
            print("\033[0;35m", end='')
        elif color == 'cyan':
            print("\033[0;36m", end='')
        elif color == 'white':
            print("\033[0;37m", end='')
        elif color == 'bright_black':
            print("\033[0;90m", end='')
        elif color == 'bright_red':
            print("\033[0;91m", end='')
        elif color == 'bright_green':
            print("\033[0;92m", end='')
        elif color == 'bright_yellow':
            print("\033[0;93m", end='')
        elif color == 'bright_blue':
            print("\033[0;94m", end='')
        elif color == 'bright_magenta':
            print("\033[0;95m", end='')
        elif color == 'bright_cyan':
            print("\033[0;96m", end='')
        elif color == 'bright_white':
            print("\033[0;97m", end='')
        elif color == 'clear':
            print("\033[0m", end='')
    else:
        if color == 'black':
            output = "\033[0;30m" + str + "\033[0m"
        elif color == 'red':
            output = "\033[0;31m" + str + "\033[0m"
        elif color == 'green':
            output = "\033[0;32m" + str + "\033[0m"
        elif color == 'yellow':
            output = "\033[0;33m" + str + "\033[0m"
        elif color == 'blue':
            output = "\033[0;34m" + str + "\033[0m"
        elif color == 'magenta':
            output = "\033[0;35m" + str + "\033[0m"
        elif color == 'cyan':
            output = "\033[0;36m" + str + "\033[0m"
        elif color == 'white':
            output = "\033[0;37m" + str + "\033[0m"
        elif color == 'bright_black':
            output = "\033[0;90m" + str + "\033[0m"
        elif color == 'bright_red':
            output = "\033[0;91m" + str + "\033[0m"
        elif color == 'bright_green':
            output = "\033[0;92m" + str + "\033[0m"
        elif color == 'bright_yellow':
            output = "\033[0;93m" + str + "\033[0m"
        elif color == 'bright_blue':
            output = "\033[0;94m" + str + "\033[0m"
        elif color == 'bright_magenta':
            output = "\033[0;95m" + str + "\033[0m"
        elif color == 'bright_cyan':
            output = "\033[0;96m" + str + "\033[0m"
        elif color == 'bright_white':
            output = "\033[0;97m" + str + "\033[0m"
        else:
            output = None
        return output
def fprint(color, str):
    colors = ['bold', 'b', 'italic', 'i', 'underline', 'underl', 'ul', 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']
    if color in colors:
        if color == 'bold' or color == 'b':
            print("\033[1m" + str + '\033[0m')
        elif color == 'italic' or color == 'i':
            print("\033[3m" + str + '\033[0m')
        elif color == 'underline' or color == 'underl' or color == 'ul':
            print("\033[4m" + str + '\033[0m')
        elif color == 'black':
            print("\033[0;30m" + str + "\033[0m")
        elif color == 'red':
            print("\033[0;31m" + str + "\033[0m")
        elif color == 'green':
            print("\033[0;32m" + str + "\033[0m")
        elif color == 'yellow':
            print("\033[0;33m" + str + "\033[0m")
        elif color == 'blue':
            print("\033[0;34m" + str + "\033[0m")
        elif color == 'magenta':
            print("\033[0;35m" + str + "\033[0m")
        elif color == 'cyan':
            print("\033[0;36m" + str + "\033[0m")
        elif color == 'white':
            print("\033[0;37m" + str + "\033[0m")
        elif color == 'bright_black':
            print("\033[0;90m" + str + "\033[0m")
        elif color == 'bright_red':
            print("\033[0;91m" + str + "\033[0m")
        elif color == 'bright_green':
            print("\033[0;92m" + str + "\033[0m")
        elif color == 'bright_yellow':
            print("\033[0;93m" + str + "\033[0m")
        elif color == 'bright_blue':
            print("\033[0;94m" + str + "\033[0m")
        elif color == 'bright_magenta':
            print("\033[0;95m" + str + "\033[0m")
        elif color == 'bright_cyan':
            print("\033[0;96m" + str + "\033[0m")
        elif color == 'bright_white':
            print("\033[0;97m" + str + "\033[0m")
        else:
            print(str)
    else:
        print(color)
def cprint(color, str):
    colors = ['bold', 'b', 'italic', 'i', 'underline', 'underl', 'ul', 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']
    if color in colors:
        if color == 'bold' or color == 'b':
            print("\033[1m" + str + '\033[0m')
        elif color == 'italic' or color == 'i':
            print("\033[3m" + str + '\033[0m')
        elif color == 'underline' or color == 'underl' or color == 'ul':
            print("\033[4m" + str + '\033[0m')
        elif color == 'black':
            print("\033[0;30m" + str + "\033[0m")
        elif color == 'red':
            print("\033[0;31m" + str + "\033[0m")
        elif color == 'green':
            print("\033[0;32m" + str + "\033[0m")
        elif color == 'yellow':
            print("\033[0;33m" + str + "\033[0m")
        elif color == 'blue':
            print("\033[0;34m" + str + "\033[0m")
        elif color == 'magenta':
            print("\033[0;35m" + str + "\033[0m")
        elif color == 'cyan':
            print("\033[0;36m" + str + "\033[0m")
        elif color == 'white':
            print("\033[0;37m" + str + "\033[0m")
        elif color == 'bright_black':
            print("\033[0;90m" + str + "\033[0m")
        elif color == 'bright_red':
            print("\033[0;91m" + str + "\033[0m")
        elif color == 'bright_green':
            print("\033[0;92m" + str + "\033[0m")
        elif color == 'bright_yellow':
            print("\033[0;93m" + str + "\033[0m")
        elif color == 'bright_blue':
            print("\033[0;94m" + str + "\033[0m")
        elif color == 'bright_magenta':
            print("\033[0;95m" + str + "\033[0m")
        elif color == 'bright_cyan':
            print("\033[0;96m" + str + "\033[0m")
        elif color == 'bright_white':
            print("\033[0;97m" + str + "\033[0m")
        else:
            print(str)
    else:
        print(color)