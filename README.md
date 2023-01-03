# Funcenter

This is a simple package. You can use it however you want! Please let me know if there are any errors.

### Color/Text Formatting
This package offers some basic color and text formatting, in the form of:
- bold(`str`), b(`str`)
  - <span style="color:magenta">bold('str')</span> --> **str**
- italic(`str`), i(`str`)
 - <span style="color:magenta">italic('str')</span> --> *str*
- underline(`str`), underl(`str`), ul(`str`)
 - <span style="color:magenta">underline('str')</span> --> <u>str</u>
- format(`option`), color(`option`)
  - Sets the format or color.
- clear()
  - Clears all formatting.
- fprint(`option`, `str`), cprint(`option`, `str`)[^1]
  - Print `str` in the format of `option`.
  - <span style="color:magenta">fprint('bold, 'str')</span> --> **str**

### Printing
Some simple printing functions.
- println(`str`, `x`)
  - Prints *`x`* new lines after the `str` (default is 1).
- printsln(`str`)
  - Print the following print statement on the same line as `str`.
- printx(`str`, `x`)
  - Print `str` *`x`* times. <span style="color:magenta">`printx('str', 3)`</span> prints the following
  
    ```
    str
    str
    str
    ```
- typewriter(`str`, `speed`)[^1]
  - Print `str` character-by-character (typewriter-like effect) using `speed` *(from slowest to fastest: 1, 2, 3)*.
  - **<span style="color:red">`DO NOT USE WITH ESCAPE CHARACTERS`</span>**

### Math
Very very minimal and basic:
- is_decimal(`var`)
  - Returns <span style="color:blue">`True`</span> if `var` is a decimal.
- factorial(`num`)
  - Returns the factorial of `num`

### Other
- charsplit(`str`)
  - Returns a <span style="color:blue">list</span> of each character in `str`.
- uncharsplit(`list`)
  - Exactly what it sounds like. The reverse of the above; Returns a <span style="color:blue">string</span> of `list`. And yes I know how easy this is. I wanted it.

Any other functions not listed here are in development. Check back later.
  
[^1]: Work in progress. Use caution.