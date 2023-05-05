"""Script to time the addition of vectors.

Example:
    In the terminal, starting from the main project folder, we need
    to change directory to `examples` and from there run the script
    (if we have installed our library then there is no need to change
    folders or to append the path to our library).

    >>> conda activate env_name
    >>> cd examples
    >>> python 7-timing.py
    Standard lib timer implementation:
    Times: [1.62862, 1.62540, 1.62124], Mean computation time: 1.62509s
"""

import sys
from timeit import Timer

import numpy as np


NUM_RUNS = 3
NUM_LOOPS = 100_000


def time_addition() -> None:
    """Timing the addition of two vectors.

    Note:
        The code must be given in string format watching out for any indentations,
        since the string will be converted as is to Python code (yes, it looks ugly).
    """

    setup_str = """
import sys
from os.path import abspath

from pyinstrument import Profiler
from numpy.random import Generator, PCG64

module_path = abspath("..")
if module_path not in sys.path:
    sys.path.append(module_path)

from mypackage import Vector

rng = Generator(PCG64())  # random number generator
"""

    code_str = """
vector_1 = Vector(rng.integers(-10, 10), rng.integers(-10, 10))
vector_2 = Vector(rng.integers(-10, 10), rng.integers(-10, 10))
vector_sum = vector_1 + vector_2
"""

    timer = Timer(code_str, setup=setup_str)
    times = timer.repeat(repeat=NUM_RUNS, number=NUM_LOOPS)
    mean_time = np.mean(times)
    print(f"Times: {times}, Mean computation time: {mean_time}s")


def main() -> int:
    print("Standard library timer implementation: ")
    time_addition()
    return sys.exit(0)


if __name__ == "__main__":
    main()
