import sys

try:
    import PIL
except ImportError:
    sys.exit("""You need PIL!
                install it from http://pypi.python.org/pypi/Pillow
                or run pip install Pillow.""")