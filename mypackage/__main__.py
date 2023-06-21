"""Command line interface. This script will allow us to
execute commands of our library directly from the terminal
in a similar fashion as libraries like black or pytest.

References:
    https://realpython.com/command-line-interfaces-python-argparse/

Example:
    >>> vector 1 0
    Vector (1.0, 0.0) created!

    >>> vector 1 2 --save vector.pkl
    Vector (1.0, 2.0) created!
    Vector pickled in data/hey.pkl!

"""
from argparse import ArgumentParser

from .vector import Vector


def main():
    parser = ArgumentParser(  # this object parses the arguments given through command line
        prog="vector",  # name of our command
        description="Create a 2D vector.",
        epilog="Thanks for using %(prog)s! :)",
    )
    parser.add_argument(
        "coordinates",  # positional argument
        nargs=2,
        type=float,
        metavar=("x", "y"),
        help="take the Cartesian coordinates %(metavar)s",
    )
    parser.add_argument(
        "-s",  # optional argument
        "--save",  # flag can be given both in long or short fomat
        action="store",  # stores whatever goes after --save. This is the default value for action.
        type=str,
    )
    args = parser.parse_args()  # after parsing the arguments we can access them
    x, y = args.coordinates[0], args.coordinates[1]
    vector = Vector(x, y)

    print(f"Vector {vector} created!")

    if args.save:
        # Usually imports are at the top, but sometimes it is superflous to import them all
        import pickle
        from pathlib import Path

        Path("data/").mkdir(exist_ok=True)
        file_path = Path("data") / args.save

        with open(file_path, mode="wb") as f:
            pickle.dump(vector, f)

        print(f"Vector pickled in {file_path}!")


if __name__ == "__main__":
    main()
