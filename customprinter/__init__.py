from .core import (
    CustomPrinter,
    print,
    success,
    error,
    warning,
    info,
    override_builtin_print
)

printer = CustomPrinter()

__all__ = [
    'CustomPrinter',
    'print',
    'success',
    'error',
    'warning',
    'info',
    'override_builtin_print',
    'printer'
]

__version__ = '1.0.0'
