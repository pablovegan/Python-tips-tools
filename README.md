# Python tips and tools

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Test](https://github.com/pablovegan/Python-tips-tools-Benasque/actions/workflows/tests.yml/badge.svg)](https://github.com/pablovegan/Python-tips-tools-Benasque/actions/workflows/tests.yml)



Howdy! I present you some notes meant as a companion to the Python tips and tools talk for the Superconducting Qubit Technology school at Benasque 2023.

Since there are abundant online resources to learn Python, this document is quite succint and schematic. I tried to keep the files simple enough so that the essence of a Python project can be understood, but rich enough so that you, hopefully, learn new things! (No, we are not going to print "hello world" or explain for loops).

## Getting started

### Conda

The first thing we should do when working on a new project is to create a conda environment that suits our third party library needs (with their corresponding versions), unless we already have one. I suggest you use the light version of conda, `miniconda`, which only installs the standard Python libraries. Then you can always install whatever you need in a new environment to keep it all clean and tidy.

So, we start creating and _activating_ a new environment

```console
conda create -n env_name python==3.10
conda activate env_name
```
*Note*: always remember to activate your conda environment before using python or installing new libraries. Do not install third party libraries in the base environment!

### Pip and PyPI

Once Python is installed, we can use either `pip` or `conda` to install new libraries in our environment. `pip` downloads packages from the [PyPI repository](https://pypi.org/), which usually has more libraries than the Conda repository.


To simplify our life, we will install the third-party libraries we need from a .txt file named `requirements-dev.txt`, which also installs the dependencies in the `requirements.txt` file (intended just for users of the library, not developers).
```console
pip install -r requirements-dev.txt
```

### Jupyter notebooks

If we also want to run jupyter notebooks, we must install ipykernel: 
```console
pip install ipykernel
```

### Create a project and initialize git

Finally we create our project folder and initialize git inside it
```console
mkdir my_project
cd my_project
git init
```

or we can clone this repository
```console
git clone https://github.com/pablovegan/Python-tips-tools-Benasque.git
```

*Note*: be sure to push and pull your changes to the cloud when switching between different devices (for example your desktop computer and your laptop), if not you can have merge conflicts and, trust me, you don't want that...

### Text editor or IDE

I'm a [Visual Studio Code](https://code.visualstudio.com/) (VSCode) enjoyer because it is free, lightweight and has lots of useful extensions, but you may also try other IDEs and editors like [PyCharm](), [Sublime](https://www.sublimetext.com/) or [Vim](https://www.vim.org/) (for the nostalgic).

Here are some of the extensions I use in VSCode:
- Python
- IntelliCode
- Jupyter
- Flake8
- Black Formatter
- Mypy Type Checker
- Gitlens
- GitHub Pull requests and issues
- autoDocstring

One last tip: you can hide cache folders from the file explorer in `Settings -> Files: Exclude`.


## Python basics

### Code structure

Once we have a folder for our project, we equip it with the following structure:

``` text
├── setup.py
├── setup.cfg
├── pyproject.toml
├── requirements.txt
├── ... other config files ...
├── mylibrary
│   ├── __init__.py
│   ├── vector
│   │   ├── __init__.py
│   │   └── vector.py
│   └── linearmap
│       ├── __init__.py
│       └── linear_map.py
├── tests
│   ├── __init__.py
│   ├── test_linear_map.py
│   └── test_vector.py
└── examples
    └── example.ipynb
```

Folders in our library should have `lowercasenames` names, without underscores.

Usually you can copy configuration files from other projects (like this one) and tweak them to fit your needs. Both `pyproject.toml` and `setup.cfg` contain configuration options for the tools that we use, like `flake8` or `black`. `setup.cfg` also contains the metadata of our library, information like the author or version of the library; this is required when building our library to create an installable package (that we can upload to PyPI). When building the library, the script `setup.py` is used, but we don't need to bother with it at this moment.

Third party dependencies for our library are specified in the `requirements.txt` file, ideally with the version of each library to avoid conflicts with updates or older versions. The resting developer tools that we would like to use, like linters, are added in the `requirements-dev.txt` file.

Finally, note that sometimes the library can be found inside a source folder, `src`, in a similar way to other programming languajes (like Java), but in Python is not really necessary so we can skip it.

### Libraries or packages

As you may have noticed in the project structure, every folder inside our library needs an `__init__.py` file, which will be called whenever we import our library. Usually this file will just import functions or classes from other files (modules) in our library.

### Modules

Simply, a module is a `.py` file consisting of Python code. A module can define functions, classes and variables... Python modules should more or less follow this structure:
1. Module docstrings should appear at the very beginning, just before the imports. 
2. Imports should follow this order: standard Python library, third party and local libraries, each group separated by one empty line. Also, one should not import from more than one library per line.
3. Module constants, separated from the imports by two empty lines. Constants should follow the `UPPER_CASE_WITH_UNDERSCORES` naming convention.
4. Functions, separated again by two empty lines. Function names should follow the `lower_case_with_underscores` convention.
5. Exception classes.
6. Normal classes. Classes names should stick to the `CapitalizedWords` convention.

### Objects and classes

Everything in Python is an **object**, _i.e._ everything can be assigned to a variable or be passed as an argument to a function (the definition of object in Python varies with respect to other languages; in Python not all objects have attributes or methods, neither all admit subclasses).

When we create a new object of a certain class, the `__new__` method is called in the background, which creates a new empty object that is then initialized through the `__init__` method.

FILL IN WITH METHODS AND ATTRIBUTES (also class attributes)


An important thing to be aware of when using Python is that objects fall into two categories: mutable or immutable. An immutable object is the one that cannot be changed after it is created; even when you think you are changing the object, you are really making new objects from old ones. Immutable objects include numbers, strings, and tuples. Almost everything else is mutable, including lists, dicts, and user-defined objects. Mutable means that the value has methods that can change the value in-place. To learn more about this check out the example notebook [`3-mutable-objects.ipynb`](examples/3-mutable-objects.ipynb).

### Variables

A Python **variable** is a symbolic name that is a reference or pointer to an object. In Python, unlike other programming languages like C, different variables can point to the same object/memory address. 

When an object runs out of references, it is no longer accessible and Python will reclaim the allocated memory so it can be used for something else.

In general, variable names and attributes should follow the `lower_case_with_underscores` naming convention (as with functions). Only constants defined on a module level should be written in `UPPER_CASE_WITH_UNDERSCORES`. Variable names should be readable and meaningful, avoiding undescriptive names like single letters or cryptic abbreviations.


### Type hints
Python is both a **strongly typed** and a **dynamically typed** language. Strong typing means that variables do have a type and that the type matters when performing operations on a variable. Dynamic typing means that the type of the variable is determined only during runtime.

Due to dynamic typing, in Python the same variable can have a different type at different times during the execution. Dynamic typing allows for flexibility in programming, but with a price in performance.

Nonetheless, recent versions of Python allow one to add indicative type hints to our variables. For example

```Python
a: int = 3
b: float = 2.0

def shouting(text: str) -> str:
    return text.upper() + "!!"
```

They can be helpful to understand the code, create documentation or even catch errors using tools like `mypy`.

Elaborate type hints such as `Callable`, `Union` or `Optional` can be found in the [`typing` library](https://docs.python.org/es/3/library/typing.html).Note that after Python 3.10 the operator `|` can be used as an "or" between different types (same use as `Union`). For example, this function accepts either a float or an integer and outputs an integer.

```Python
def float_to_int(variable: float | int) -> int:
    return int(variable)
```

### Docstrings

Docstrings should always be added to your modules and functions. The idea when coding is to make simple functions with just one purpose and document them clearly. Ideally, functions should be readable and should require little to no inline comments explaining what the function does.

One of the most popular styles for docstrings is the [Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). I personally like it because it is very clear and compact (Numpy style for example occupies more code lines).


## Tools

### Tests

FILL IN WITH `PYTEST` STUFF

### Linters

Linters like `Ruff`, `Pylint` or `Flake8` (which is the one I use) help us find mismatches between our code and the conventions stablished by the python community in the [PEP8 guidelines](https://peps.python.org/pep-0008/). In summary, an indispensable tool for a programmer.

`Flake8` can be easily run from the command line to highlight all the errors of our library
```console
flake8 mylibrary
```
We can also lint one specific file 
```console
flake8 mylibrary/vector/vector.py
```

Or, even simpler, we can use the Flake8 extension for VSCode (or whatever tool your IDE provides).

### Formatters

Keeping track of all the errors and fixing them can be painful... This is where automatic tools to format the code enter. The two most popular are `autopep8` and `black`. I prefer `black` because it requires less configuration. To format our library simply type in the command line
```console
black mylibrary
```
or use the corresponding VSCode extension.

Black by default allows a maximum line length of 80. We can tweak this by adding an option:
```console
black --line-length 120 mylibrary
```

### Type checker

The most popular type checker is `mypy`. Provided that we type hinted our functions and variables, this tool checks any mismatches between the expected inputs and outputs and the real ones. It can also highlight deeper errors in your code structure, like violations of Liskov substitution principle.

```console
mypy mylibrary
```
Note that sometimes it complaints too much so you may just turn it off...

### Documentation

We use the autoDocstrings extension for VSCode to create Google style docstrings in a fast and easy way. Once our function is type annotated, we type """ or ''' and click in Generate Docstrings. It will automatically create the template using the annotated inputs and outputs of the function, as well as exceptions raised in the function.

If you want to create nice looking documentation and then upload it to a website (for free in Github Pages) you can follow [this tutorial](https://realpython.com/python-project-documentation-with-mkdocs/) using `mkdocs`.


## Bit more advanced stuff

### Uploading to PyPI

When we install packages using `pip` we are actually downloading them from the [PyPI repository](https://pypi.org/). Anyone can upload packages to PyPI... but be careful, since the package will stay forever in the repository. If you want to play with the uploading process you should always upload the package to https://test.pypi.org/.

To upload our library we use a Pythono package named `twine`. Here is a [short guide](https://twine.readthedocs.io/en/stable/) on how to build and upload our library.


### Code acceleration

Python is an interpreted language, which means the source code is executed directly without compiling the program into machine code. Thus, Python relies on an interpreter, the most common being CPython (which is programmed in C and not to be confused with Cython).

One disadvantage of interpreted languages over compiled ones is that they are generally slower. In the recent years many tools have emerged to accelerate python code; to name some of them:
- Just in time compilers: Numba, JAX and PyPy.
- Parallelization with `pathos.multiprocessing` and `mpi4py` (Message Passing Interface for Python).
- Extend Python with C code: Cython (the `cythonbuilder` library makes our life easier).

### Automating boring tasks with Github workflows

Ordinary tasks in a developers day such as testing (in multiple operating systems and Python versions), releasing packages and uploading them to PyPI, updating the documentation in a website, etc., can all be automated using workflows. Most cloud repositories like Github or Gitlab have them available and are really easy to use (at least the basic ones).

In this repo, I added a Github workflow to test our Python library in a linux machine (provided by Github) with Python version 3.10. The workflow can be found under the `.github/workflows` folder in a `test.yml` file. The basic structure of this file is:
1. Apply the action when we git push to or pull from the repository.
2. Create an ubuntu linux machine with python 3.10 installed.
3. Install `flake8` and `pytest`, as well as the dependencies under the `requirements.txt` file.
4. Lint with flake8 and stop if there are any errors.
5. Run the tests inside the `tests` folder using `pytest`.

The green tick near the commits show that the tests were successful.

![Github workflows](docs/github_tests_workflow.png)

Note: we can add a badge at the beginning of our readme to show that the tests either passed or failed (this is updated automatically each time the tests are run).

## Other things to look into
- Abstract classes: a basic example of an abstract class can be found in the `linear_map.py` module of our library. Basically, abstract classes allow us to define abstract methods in a super class that we can later code explicitly in all its subclasses.
- Exception handling: basically `try-except` statements. They work very well with custom error classes. An example can be found in the `3-exceptions.ipynb` notebook inside the `examples` folder.
- Iterators and generators: look up the functions `iter()` and `next()`, and the keyword `yield`.
- Function and class decorators: decorators are a simple sintax to transform certain functions or classes.
- Pre-commits: pre-commits allow us to do certain actions between commiting changes with git. For example, we can check that our code follows the PEP8 guidelines and fix it with black if it doesn't.