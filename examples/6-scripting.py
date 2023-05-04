"""Simple python script that creates and prints a vector from two
arguments (given through the terminal when running the script).

Example:
    In the terminal, starting from the main project folder, we need
    to change directory to `examples` and from there run the script
    (if we have installed our library then there is no need to change
    folders or to append the path to our library):

    >>> conda activate env_name
    >>> cd examples
    >>> python 6-scripting.py 1 2
    The vector (1.0, 2.0) was created!

    If we inputed less than two arguments an IndexError would rise
    >>> python 6-scripting.py 1
    Error: At least two arguments required to create a vector.

"""
import sys
from os.path import abspath

# Tell python to search for the files and modules starting from the working directory
module_path = abspath("..")
if module_path not in sys.path:
    sys.path.append(module_path)

from mypackage import Vector  # noqa: E402 (ignore error for imports order)


if __name__ == "__main__":
    try:
        # Remember that sys.argv[0] is '6-scripting.py'
        x = float(sys.argv[1])  # arguments in terminal are given as a strings
        y = float(sys.argv[2])
        vector = Vector(x, y)
        print(f"The vector {vector} was created!")

    except IndexError:
        print("Error: At least two arguments required to create a vector.")
        sys.exit(1)
