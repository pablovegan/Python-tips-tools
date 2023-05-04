# Python tips and tools
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pablovegan.github.io/Python-tips-tools-Benasque/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Test](https://github.com/pablovegan/Python-tips-tools-Benasque/actions/workflows/tests.yml/badge.svg)](https://github.com/pablovegan/Python-tips-tools-Benasque/actions/workflows/tests.yml)



Howdy! I present you some notes meant as a companion to the Python tips and tools talk for the Superconducting Qubit Technology school at Benasque 2023.

Since there are abundant online resources to learn Python, this document is quite succint and schematic. I tried to keep the files simple enough so that the essence of a Python project can be understood, but rich enough so that you, hopefully, learn new things! (No, we are not going to print "hello world" or explain `for` loops).

## Getting started

### Conda

The first thing we should do when working on a new project is to create a conda environment that suits our third-party library needs (with their corresponding versions), unless we already have one. I suggest you use the light version of conda, [`miniconda`](https://docs.conda.io/en/latest/miniconda.html), which only installs the standard Python libraries. Then you can always install whatever you need in a new environment to keep it all clean and tidy.

So, we start by creating and **activating** a new environment

```console
conda create -n env_name python==3.10
conda activate env_name
```
*Note*: always remember to activate your conda environment before using Python or installing new libraries. Do not install third party libraries in the base environment!

### Pip and PyPI

Once Python is installed, we can use either `pip` or `conda` to install new libraries in our environment. `pip` downloads packages from the [PyPI repository](https://pypi.org/) (Python Package Index), which usually has more libraries than the Conda repository.


To simplify our life, we will install the third-party libraries we need from a .txt file named [`requirements-dev.txt`](requirements-dev.txt), which also installs the dependencies in the [`requirements.txt`](requirements.txt) file (intended just for users of the library, not developers).
```console
pip install -r requirements-dev.txt
```

### Jupyter notebooks

If we also want to run jupyter notebooks, we must install the package `ipykernel`: 
```console
pip install ipykernel
```

### Create a project and initialize git

Finally, we create our project folder and initialize [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) inside it
```console
mkdir my_project
cd my_project
git init
```

or, instead, we can clone this repository
```console
git clone https://github.com/pablovegan/Python-tips-tools-Benasque.git
```

*Note*: be sure to push and pull your changes to and from the cloud (i.e. [Github](https://github.com/) or [Gitlab](https://about.gitlab.com/)) when switching between different devices (for example, your desktop computer and your laptop). Otherwise, you can have merge conflicts and, trust me, you don't want that...

### Text editor or IDE

I'm a [Visual Studio Code](https://code.visualstudio.com/) (VSCode) enjoyer because it is free, lightweight and has lots of useful extensions, but you may also try other IDEs and editors like [PyCharm](), [Sublime](https://www.sublimetext.com/) or [Vim](https://www.vim.org/) (for the nostalgic).

Here are some of the extensions I use in VSCode:

* Python
* IntelliCode
* Jupyter
* Ruff
* Gitlens
* GitHub Pull requests and issues
* autoDocstring

One tip for VSCode: you can hide cache folders from the file explorer in `Settings -> Files: Exclude`.


## Python basics

### Code structure

Once we have a folder for our project, we equip it with the following structure:

``` text
├── README.md
├── pyproject.toml
├── requirements.txt
├── ... other files ...
├── mypackage
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

First, we find the README, which contains whatever useful information the author of the repository wants to transmit us. Usually it begins with a short description of the package, and follows with sections on how to install it, a quick usage guide, references, how to contribute and the license.

Next we find [`pyproject.toml`](pyproject.toml), a configuration file with metadata about our project and configuration options for the tools that we use during development (e.g. linters and formatters). Usually you can copy configuration files from other projects (like this one) and tweak them to fit your needs.

Third party dependencies for our package are specified in the [`requirements.txt`](requirements.txt) file, ideally with the version of each library to avoid conflicts with updates or older versions. The resting developer tools that we'd like to use are added in the [`requirements-dev.txt`](requirements-dev.txt) file.

After a bunch of other files, we find our main package, with all our Python code organized in folders. Sometimes the package can be found inside a source folder, `src`, in a similar way to other programming languajes (like Java), but in Python is not really necessary so we can skip it.

In the `tests` folder we store the code needed to assert that our library is working as intented to. This shouldn't be mixed with the `examples` folder; sometimes we tend to test our code in jupyter notebooks, but it is better to define a set of tests that we expect our library to pass every single time, and then just use it for whatever examples we want.

For the moment, we will not worry about the `docs` folder (files to create documentation) or the `.github` folder (contains workflows) found in this repository; we will get to it in the [advanced stuff](#bit-more-advanced-stuff) section.

### Packages or libraries

A [**package**](https://docs.python.org/3/reference/import.html#packages) or **library** is a collection of Python `.py` modules organized in directories. The main directory is the package and the subdirectories are its subpackages. Their names should follow the convention `lowercasenames`, without underscores.

As you may have noticed in the project structure, every folder inside our package has an `__init__.py` file. The code inside it will be called whenever we import the library. It usually justs contains imports of functions or classes from other `.py` files in our library.

The `tests` folder can also contain a `__init__.py` file, but we can leave it empty since we are not going to import the tests package.


### Modules

Simply, a module is a `.py` file consisting of Python code. A module can define functions, classes and variables... Python modules should more or less follow this structure:

1. Module docstrings should appear at the very beginning, just before the imports. 
2. Imports should follow this order: standard Python library, third party and local libraries, each group separated by one empty line. Also, one should not import from more than one library per line.
3. Module constants, separated from the imports by two empty lines. Constants should follow the `UPPER_CASE_WITH_UNDERSCORES` naming convention.
4. Functions, separated again by two empty lines. Function names should follow the `lower_case_with_underscores` convention.
5. Exception classes.
6. Normal classes. Classes names should stick to the `CapitalizedWords` convention.

There is no exact rule on how much code should be in each module, but, ideally, each module should have one purpose (as with functions). For example, the purpose of our modules are defining the `Vector` class and creating some linear transforms for those vectors with the `LinearMap` class and its subclasses.

### Objects and classes

Python is an object oriented language; everything in Python is an **object** (even packages!), i.e. everything can be assigned to a variable or be passed as an argument to a function (the definition of object in Python varies with respect to other languages; in Python not all objects have attributes or methods, neither all admit subclasses).

[Classes](https://docs.python.org/3/tutorial/classes.html) provide a means of bundling data and functionality together.

[class]()

When we create a new object of a certain class, the `__new__` method is called in the background, which creates a new empty object that is then initialized through the `__init__` method.

For an in-depth introduction to classes in Python have a look at [realpython.com](https://realpython.com/python-classes/).

FILL IN WITH METHODS AND ATTRIBUTES (also class attributes)

Magic methods in Python are the special methods that start and end with the double underscores. They are also called dunder methods. Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. For example, when you add two numbers using the + operator, internally, the `__add__()` method will be called.

Abstract classes: a basic example of an abstract class can be found in the [`linear_map.py`](mypackage/linearmap/linear_map.py) module of our library. Basically, abstract classes allow us to define abstract methods in a super class that we can later code explicitly in all its subclasses.

An important thing to be aware of when using Python is that objects fall into two categories: mutable or immutable. An immutable object is the one that cannot be changed after it is created; even when you think you are changing the object, you are really making new objects from old ones. Immutable objects include numbers, strings, and tuples. Almost everything else is mutable, including lists, dicts, and user-defined objects. Mutable means that the value has methods that can change the value in-place. To learn more about this check out the example notebook [`3-mutable-objects.ipynb`](examples/3-mutable-objects.ipynb).

Two important properties of python classes are inheritance and polymorphism. [Inheritance](https://www.programiz.com/python-programming/inheritance) allows us to create a subclass that can access the methods of the parent class or classes (in the case of [multiple inheritance](https://www.programiz.com/python-programming/multiple-inheritance)). [Polymorphism](https://www.programiz.com/python-programming/polymorphism) allows different classes to use a single type entity (method, operator or object) to represent different types in different scenarios; for example, the sum operator `+` implements the method `__add__()`, whose functionality changes if the summed objects are integers, strings, lists...

### Variables

A Python **variable** is a symbolic name that is a reference or pointer to an object. In Python, unlike other programming languages like C, different variables can point to the same object/memory address. Each object has a [counter](https://docs.python.org/3/extending/extending.html#reference-counts) that keeps track of how many variables (names) have been bound to this object. When an object runs out of references, it is no longer accessible and Python will reclaim the allocated memory so it can be used for something else.

In general, variable names and attributes should follow the `lower_case_with_underscores` naming convention (as with functions). Only constants defined on a module level should be written in `UPPER_CASE_WITH_UNDERSCORES`. Variable names should be readable and meaningful, avoiding undescriptive names like single letters or cryptic abbreviations.

And how are variables passed to functions? If you have heard about the _pass by reference_ and _pass by value_ paradigms, you may be wondering which one Python follows. Well, the truth is... neither! Python passes variables by [**assignment**](https://realpython.com/python-pass-by-reference/#passing-arguments-in-python); that is, when you call a Python function, each function argument becomes a variable to which the passed value is assigned.


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

Elaborate type hints such as `Callable` or `Sequence` can be found in the [`typing` library](https://docs.python.org/es/3/library/typing.html). Note that after Python 3.10 the operator `|` can be used as an "or" between different types (same use as `Union`). For example, this function accepts either a float or an integer and outputs an integer.

```Python
def float_to_int(variable: float | int) -> int:
    return int(variable)
```

### Docstrings

Docstrings should always be added to your modules and functions. The idea when coding is to make simple functions with just one purpose and document them clearly. Ideally, functions should be readable and should require little to no inline comments explaining what the function does.

To create these docstrings in a fast and easy way, I use the autoDocstrings extension for VSCode. Once our function is type annotated, we type `"""` and click in `Generate Docstrings`; it will automatically create the template using the annotated inputs and outputs of the function, as well as the exceptions raised.

These docstrings can follow different conventions; one of the most popular ones is the [Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). I personally like it because it is very clear and compact (Numpy style, in contrast, occupies more lines).

Lastly, remember that we learn better from the concrete, so adding examples to your documentation is always a good idea:
```python
"""
Examples:
    Use case of our library:

    >>> some executable code block
    the result
"""
```
An easy way to check if the code gives the expected result without jumping into a jupyter notebook to test it is the tool `doctest`, which is part of the standard library. Simply, from the command line, execute

````bash
python -m doctest mypackage/linearmap/linear_map.py
````
to see the mismatches, if any.


## Tools

### Testing

How do we know if the functions in our library work as they are supposed to? Sure, we can always have a bunch of jupyter notebooks lying around, but there is a better way: [unit testing](https://realpython.com/python-testing/). Unit testing is a method for testing software that looks at the smallest testable pieces of code, called units, which are tested for correct operation. Usually in Python, units are functions and class methods.

Testing is a world on its own, especially in the so-called _Test Driven Development_ (TDD), and we will barely touch the surface in this demo... but it is enough for the needs of most physicists. Just as a sneak peak: we can test how different units fit together (integration testing), test a whole application, test in different operating systems (system testing), etc.

The tool we will use for unit testing is `pytest`. To keep our code organized, outside our library we create another folder called [`tests`](tests). Inside it, we place different modules `test_*.py`; in our case, we have one for each subpackage: [`test_vector.py`](tests/test_vector.py) and [`test_linear_map.py`](tests/test_linear_map.py). Inside each of these, we test all the functions and methods in the module (don't forget to test the exceptions as well!). The syntax is really easy, you just need to use the `@pytest.mark.parametrize` decorator to tell the pytest which inputs and expected results you want to test. For example:

````python
@pytest.mark.parametrize(
    ("arg_1", "arg_2", "result"),
    (
        (1, 2, 3),
        (3.0, -1, 2.0),
    ),
)
def test_sum(arg_1, arg_2, result):
    assert arg_1 + arg_2 == result
````

To run the tests inside the `tests` folder simply run from the command line
```bash
pytest tests
```

*Note*: In the workflows section we will see how to automate this.

### Debugging

How many times have you found yourself adding dozens of `print()` statements to your code to catch an error? You are not the only one... But turns out there is a much better way: use the debugger in your IDE. You can add breakpoints, execute single lines, see what value each variable has, step into the functions inside your library, see the call stack... 

A good idea is to debug your tests, since they, ideally, are the best tool to see if your code is really working.


### Timing

Even if our code runs without errors, it might not be very useful if it takes too long to do the task. To benchmark our code and find possible bottlenecks, we can use the library `timeit`, which executes a piece of code a number of times and returns the CPU time taken to run it. As an example, we can run the script [`7-timing.py`](examples/7-timing.py) to benchmark how long it takes to sum vectors two vectors:
```bash
cd examples
python 7-timing.py
```

Alternatively, we can use the magic function `%timeit` inside a jupyter notebook to benchmark our function. You can find an example in the [`5-jjit-compiler.ipynb`](examples/5-jit-compiler.ipynb) example, where we compare the speed of a determinant and its just-in-time compiled version.

### Profiling

Profiling allows you to disaggregate the time taken to run a function into its different components. For example, when adding two vectors, does it take longer to check the summand is a vector instance or to actually sum the two vectors? 

To profile our code we can write a simple script using the `Profiler` class from the `pyinstrument` library. To get a sense of how profiling works, you can run the script [`8-profiling.py`](examples/8-profiling.py):
```bash
cd examples
python 8-profiling.py
```

### Linters


Linters like `Flake8`, `Pylint` or `Ruff` (Ruff is very very fast and implements a lot of checks) help us find mismatches between our code and the conventions stablished by the python community in the [PEP8 guidelines](https://peps.python.org/pep-0008/). In summary, an indispensable tool for a programmer.

`Ruff` can be easily run from the command line to highlight all the errors of our library
```console
ruff check .
```
We can also lint one specific file 
```console
ruff check mypackage/vector/vector.py
```

`Ruff`, unlike other linters, also has the option to fix some of the problems encountered in the code
```console
ruff check --fix mypackage/vector/vector.py
```
Unless we are one of those old school programmers that read their email on the terminal, we can avoid using the command line by installing the Ruff extension for VSCode (or whatever tool your IDE provides).

### Formatters

Keeping track of all the errors and fixing them can be painful... This is where automatic tools to format the code enter. The two most popular are `autopep8` and `black`. I prefer `black` because it requires less configuration. To format our library simply type in the command line
```console
black mypackage
```
Black by default allows a maximum line length of 80. We can tweak this by adding an option:
```console
black --line-length 120 mypackage
```

Formatting can be done very simply in VSCode, just add this code to a `settings.json` file inside a `.vscode` folder in the main directory
```json
{
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "120"
    ],
    "[python]": {
        "editor.defaultFormatter": null,
        "editor.insertSpaces": true,
        "editor.tabSize": 4,
        "editor.formatOnSave": true
    },
}
```

### Type checker

The most popular type checker is `mypy`. Provided that we type hinted our functions and variables, this tool checks any mismatches between the expected inputs and outputs and the real ones. It can also highlight deeper errors in your code structure, like violations of Liskov substitution principle.

```console
mypy mypackage
```
Note that sometimes it complaints too much so you may just turn it off...


## Bit more advanced stuff

### Code acceleration

Python is an interpreted language, which means the source code is executed directly without compiling the program into machine code. Thus, Python relies on an interpreter, the most common being CPython (which is programmed in C and not to be confused with Cython).

One disadvantage of interpreted languages over compiled ones is that they are generally slower. In the recent years many tools have emerged to accelerate python code; to name some of them:

- Just in time compilers: Numba, JAX and PyPy.
- Parallelization with `pathos.multiprocessing` and `mpi4py` (Message Passing Interface for Python).
- Extend Python with C code: Cython (the `cythonbuilder` library makes our life easier).


### Installing the library

Before we install our local library, we need to specify some metadata and configuration settings; this is done in the [`pyproject.toml`](pyproject.toml) file (check out the [setuptools documentation](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)). Then we can use the command `pip install` with the editable option, `-e`, over the current folder, `.`, to install our library:
```console
pip install -e .
```
The advantage of installing the local package in editable mode is that when we make any change, the installed library is updated without reinstalling it.


### Creating documentation

If you want to create nice looking documentation and then upload it to a website (for free in Github Pages) you can follow [this tutorial](https://realpython.com/python-project-documentation-with-mkdocs/) using `mkdocs`. As a quick no-brainer guide:

1. Create a config file `mkdocs.yml`. You can simply copy the file in this repo and change the basic info like the site's name or URL.

2. Add a [`docs`](docs) folder. Usually, it contains an [`index.md`](docs/index.md) markdown file that copies whatever you have in the `README.md` and displays it as the main page of the documentation website. It also contains additional markdown files that we want to display as pages in our site. To create the documentation for our package using the docstrings, we use the script [`gen_ref_nav.py`](docs/scripts/gen_ref_nav.py). Inside the script, you only need to change the name of the folder containing your library in the `PATH_LIBRARY` variable. Again, you can simply copy the docs folder in this repo and modify the script.

3. Add a Github workflow to build and deploy the website in Github Pages. You can just copy the workflow in [`.github/workflows/documentation.yml`](.github/workflows/documentation.yml) (more on workflows later on). Whenever you push changes to Github, the documentation will be updated.

This repository's documentation can be found in https://pablovegan.github.io/Python-tips-tools-Benasque/.


### Building and uploading to PyPI

When we install packages using `pip` we are actually downloading them from the [PyPI repository](https://pypi.org/) (Python Package Index). Anyone can upload packages to PyPI... but be careful, since the package will stay forever in the repository. If you want to play with the uploading process you should always upload the package to https://test.pypi.org/.

To upload our library we use the Python package `twine`. Here is a [short guide](https://twine.readthedocs.io/en/stable/) on how to build and upload our library:

1. Build our library using `setuptools` and the [`pyproject.toml`](pyproject.toml) configuration file:
```bash
python -m build
```
2. Upload the built library to [TestPyPI](https://test.pypi.org/). You will need to enter the user and password of your TestPyPI account (different from your PyPI account)
```bash
twine upload -r testpypi dist/*
```
3. Once you are confident that you want to upload your package to PyPI, use the command
```bash
twine upload dist/*
```

Once the package is in PyIP, you can install it in your environment:
```bash
pip install python-tips-tools-benasque
```
(I only [uploaded my package](https://test.pypi.org/project/python-tips-tools-benasque/) to TestPyPI, since it is not very usefull as a standalone library).

*Note*: the process of uploading the package to PyPI can be automated with a [workflow](https://github.com/marketplace/actions/pypi-publish).

### Automating boring tasks with Github workflows

Ordinary tasks in a developers day such as testing (in multiple operating systems and Python versions), releasing packages and uploading them to PyPI, updating the documentation in a website, etc., can all be automated using workflows. Most cloud repositories like Github or Gitlab have them available and are really easy to use (at least the basic ones).

In this repo, I added two Github workflows: one to test our library in a linux machine (provided by Github) with Python version 3.10, and another to upload the documentation to Github Pages. The workflows can be found under the folder `.github/workflows` in `*.yml` files. As an example, the structure of the [`test.yml`](.github/workflows/tests.yml) file is:

1. Apply the action when we git push to or pull from the repository.
2. Create an Ubuntu Linux machine with python 3.10 installed.
3. Install `pytest` as well as the dependencies under the [`requirements.txt`](requirements.txt) file.
4. Run the tests inside the `tests` folder using `pytest`.

The green tick near the commits shows that the workflows were successful.

![Github workflows](https://raw.githubusercontent.com/pablovegan/Python-tips-tools-Benasque/master/docs/images/github_workflows.png)

*Cool tip*: we can add a badge at the beginning of our readme to show that the tests either passed or failed (this is updated automatically each time the tests are run).


## Other things to look into
- [List comprehensions](https://www.programiz.com/python-programming/list-comprehension), lambda functions and the functions `map()` and `filter()`.
- [Exception handling](https://www.programiz.com/python-programming/exception-handling): `try-except` statements. They work very well with custom error classes. An example can be found in the [`4-exceptions.ipynb`](examples/4-exceptions.ipynb) notebook inside the `examples` folder.
- [Iterators and generators](https://www.datacamp.com/tutorial/python-iterators-generators-tutorial): look up the functions `iter()` and `next()`, and the keyword `yield`.
- [Function and class decorators](https://www.programiz.com/python-programming/decorator): decorators are a simple sintax to transform certain functions or classes.
- [Pre-commits](https://pre-commit.com/): pre-commit hooks allow us to do certain actions before commiting changes with git. For example, we can lint our code with Ruff and fix it with Black if it doesn't whenever we make a commit.


## Online resources

Most of the material in this repo is covered in the excelent course [Python: Coding Guidelines, Tools, Tests and Packages](https://www.udemy.com/course/python-coding-guidelines-tooling-testing-and-packaging/?couponCode=FRANNECK_APR_2023).

Of course, free online resources are abundant; to name a few I use frequently:
- [Programiz](https://www.programiz.com/python-programming)
- [Real Python](https://realpython.com/)
- [Machine learning mastery](https://machinelearningmastery.com)
- Libraries' documentation