import sys


def color_print(text, code=5):
    """
    Prints a piece of text in a fancy way. What fancy means depends on the 
    keyword argument code. Some possibilities are:

     0;1: bold text
     0;3: italics
     0;4: underline
     0;5: blinking text (only sane default)
     0;7: "inverted" text
    0;92: green
    0;93: yellow
    0;94: blue
    0;95: pink

    Though this is not done here, it is possible to combine
    these to get lovely things like flashing yellow text.
    """
    
    start_code = "\033[{}m".format(code)
    end_code = "\033[0m"
    
    print(start_code + text + end_code)

color_print("hei", code=sys.argv[1])
