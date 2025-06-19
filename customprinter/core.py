import sys
import builtins
from colorama import init, Fore, Back, Style

init()


class CustomPrinter:
    def __init__(self):
        self.colors = {
            'black': Fore.BLACK,
            'red': Fore.RED,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'blue': Fore.BLUE,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
        }

        self.bg_colors = {
            'black': Back.BLACK,
            'red': Back.RED,
            'green': Back.GREEN,
            'yellow': Back.YELLOW,
            'blue': Back.BLUE,
            'magenta': Back.MAGENTA,
            'cyan': Back.CYAN,
            'white': Back.WHITE,
        }

        self.styles = {
            'bold': Style.BRIGHT,
            'dim': Style.DIM,
            'normal': Style.NORMAL,
            'underline': '\033[4m',
            'italic': '\033[3m',
        }

    def print(self, *args, **kwargs):
        color = kwargs.pop('color', None)
        bg = kwargs.pop('bg', None)
        style = kwargs.pop('style', None)
        align = kwargs.pop('align', 'left')
        width = kwargs.pop('width', None)

        text = kwargs.pop('sep', ' ').join(str(arg) for arg in args)
        end = kwargs.pop('end', '\n')
        file = kwargs.pop('file', sys.stdout)
        flush = kwargs.pop('flush', False)

        if width is not None:
            text = self._align_text(text, align, width)

        format_parts = []
        if style in self.styles:
            format_parts.append(self.styles[style])
        if color in self.colors:
            format_parts.append(self.colors[color])
        if bg in self.bg_colors:
            format_parts.append(self.bg_colors[bg])

        formatted_text = f"{''.join(format_parts)}{text}{Style.RESET_ALL}"
        file.write(formatted_text + end)

        if flush:
            file.flush()

    def _align_text(self, text, align, width):
        if align == 'left':
            return text.ljust(width)
        elif align == 'right':
            return text.rjust(width)
        elif align == 'center':
            return text.center(width)
        return text


_printer = CustomPrinter()

_original_print = builtins.print

WELCOME_MESSAGE = """
╔═════════════════════════════════════════════╗
║ 🚀 New Tool 🚀                              ║
║                                             ║
║ Custom Printer Successfully Started!        ║
║ You can now use:                            ║
║                                             ║
║ - print() with colors and formatting        ║
║ - success() for success messages            ║
║ - error() for error messages                ║
║ - warning() for warnings                    ║
║ - info() for information                    ║
║                                             ║
╚═════════════════════════════════════════════╝
"""


def print(*args, **kwargs):
    return _printer.print(*args, **kwargs)


def override_builtin_print(printer=print):
    builtins.print = printer
    _printer.print(WELCOME_MESSAGE, color='cyan', style='bold', align='center')


def restore_builtin_print():
    builtins.print = _original_print


def success(*args, **kwargs):
    _printer.print(*args, color='green', style='bold', **kwargs)


def error(*args, **kwargs):
    _printer.print(*args, color='red', style='bold', **kwargs)


def warning(*args, **kwargs):
    _printer.print(*args, color='yellow', style='bold', **kwargs)


def info(*args, **kwargs):
    _printer.print(*args, color='blue', **kwargs)
