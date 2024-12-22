import pyfiglet
from pyfiglet import Figlet



def list_available_fonts():
    fonts = pyfiglet.FigletFont.getFonts()
    print("Available Fonts:")
    # for font in fonts:
    #     print(font)
    return fonts

def create_ascii_art(text, font='slant', width=80, justify='left'):
    """
    Converts input text to customizable ASCII art using pyfiglet.

    :param text: The text string to convert.
    :param font: The font style to use for ASCII art. Default is 'standard'.
    :param width: The maximum width of the ASCII art. Default is 80 characters.
    :param justify: Text justification. Options include 'left', 'center', 'right'. Default is 'left'.
    :return: A string containing the customized ASCII art.
    """
    try:
        text = text.upper()
        figlet = Figlet(font=font, width=width, justify=justify)
        ascii_art = figlet.renderText(text)
        return ascii_art
    except pyfiglet.FontNotFound:
        return f"Error: The font '{font}' is not available. Please choose a valid font."

