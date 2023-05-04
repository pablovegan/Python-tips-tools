"""Script to profile the sum of two vectors.

Example:
    In the terminal, starting from the main project folder, we need
    to change directory to `examples` and from there run the script
    (if we have installed our library then there is no need to change
    folders or to append the path to our library).

    >>> conda activate env_name
    >>> cd examples
    >>> python 8-profiling.py
    2.033 profile_addition  8-profiling.py:49
    ├─ 0.963 Generator.integers  None
    │     [2 frames hidden]  ..
    ├─ 0.539 Vector.__init__  ../mypackage/vector/vector.py:61
    │  ├─ 0.413 Vector.norm  ../mypackage/vector/vector.py:155
    │  └─ 0.126 [self]  None
    ├─ 0.314 Vector.__add__  ../mypackage/vector/vector.py:100
    │  ├─ 0.221 Vector.__init__  ../mypackage/vector/vector.py:61
    │  │  ├─ 0.169 Vector.norm  ../mypackage/vector/vector.py:155
    │  │  └─ 0.052 [self]  None
    │  └─ 0.085 [self]  None
    └─ 0.217 [self]  None

    As we can see, the random integer generation and the vector initialization
    take up more time than actually summing the vectors.
"""

import sys
from os.path import abspath

from pyinstrument import Profiler
from numpy.random import Generator, PCG64

# Tell python to search for the files and modules starting from the working directory
module_path = abspath("..")
if module_path not in sys.path:
    sys.path.append(module_path)

from mypackage import Vector  # noqa


def profile_addition() -> None:
    """Profile the sum of two vectors 100000 times."""
    profiler = Profiler()
    profiler.start()

    rng = Generator(PCG64())  # random number generator

    for _ in range(100_000):
        vector_1 = Vector(rng.integers(-10, 10), rng.integers(-10, 10))
        vector_2 = Vector(rng.integers(-10, 10), rng.integers(-10, 10))
        vector_sum = vector_1 + vector_2  # noqa

    profiler.stop()
    profiler.print()


if __name__ == "__main__":
    profile_addition()
