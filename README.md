# Python tips and tools

Library description

## Getting started

The first thing we should do when working on a new project is creating a conda environment that suits our third party library needs (with their corresponding versions), unless we already have one. I suggest you use the light version of conda, `miniconda`, which only installs the standard Python libraries. Then you can always install whatever you need in a new environment.

So we start creating and activating our environment (if we didn't activate it, we would install libraries in the base environment, which is strongly discouraged)
```console
conda create -n env_name python==3.10
conda activate env_name
```


Once Python is installed, we can use either pip or conda to install new libraries in our environment. `pip` downloads packages from the PyPI (https://pypi.org/) repository, which usually has more libraries than the conda repository.


To simplify our life, we will install the third-party libraries we need from a .txt file named `requirements-dev.txt`, which also installs the dependencies in the `requirements.txt` file (intended just for users of the library, not developers).
```console
pip install -r requirements-dev.txt
```
If we also want to run jupyter notebooks, we must install ipykernel: 
```console
pip install ipykernel
```

Finally we create our project folder and initialize git inside it
```console
mkdir my_project
cd my_project
git init
```


## Code structure

Once we have a folder for our project, we equip it with the following structure:

``` text
├── setup.py
├── setup.cfg
├── pyproject.toml
├── ... other config files ...
├── my_library
│   ├── __init__.py
│   ├── vector.py
│   └── sub_library
|       ├── __init__.py
│       └── sub_library
│── tests
│   ├── __init__.py
│   └── test_vector.py
├── examples
│   └── example.ipynb
└── docs
```

Usually you can copy configuration files from other projects (like this one) and tweak them to fit your needs.

Note that sometimes libraries can be found inside a source folder, `src`, in a similar way to other programming languajes (like Java), but in Python is not really necessary so we can skip it.

## Libraries or packages

As you may have noticed in the project structure, every folder inside our library needs an `__init__.py` file, which will be called whenever we import our library. Usually this file will just import functions or classes from other files (modules) in our library.

## Modules
Simply, a module is a file consisting of Python code. A module can define functions, classes and variables... Python modules should more or less follow this structure:
1. Module docstrings should appear at the very beginning, just before the imports. 
2. After

Imports should 

## Objects and classes

Everything in Python is an object, _i.e._ a reference to a memory address (?????). When we create a new object of a certain class, the `__new__` method is called in the background, which creates a new empty object that is then initialized through the `__init__` method.

## Linting and formatting



## Documentation

Docstrings should always be added to your modules and functions. The idea when coding is to make simple functions with one single purpose, so 

https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

We use the autoDocstrings extension for VSCode to create Google style docstrings in a fast and easy way. Once our function is type annotated, we type """ or ''' and click in Generate Docstrings. It will automatically create the template using the annotated inputs and outputs of the function, as well as exceptions raised in the function.

If you want to create nice looking documentation and then upload it to a website (for free in Github Pages) you can follow this tutorial (uses `mkdocs`): https://realpython.com/python-project-documentation-with-mkdocs/.

## Uploading to PyPI

When we install packages using `pip` we are actually downloading them from the PyPI repository (https://pypi.org/). Anyone can upload packages to PyPI... but be careful, since the package will stay forever in the repository. If you want to play with the uploading process you should always upload the package to https://test.pypi.org/.

To upload our package we use a library named `twine`. You can find a short guide here: https://twine.readthedocs.io/en/stable/.


## Code acceleration

Python is an interpreted language, meaning that the code lines are executed sequentially and passed to an interpreter (the most common is CPython, which is programmed in C —and not to be confused with Cython) (?????). One disadvantage of interpreted languages over compiled ones is that they are much slower. In the recent years many tools have emerged to accelerate python code; to name some of them:
- Just in time compilers: Numba, JAX and PyPy.
- Using C or Fortran code in Python: Cython and F2PY.

## Automating boring tasks with Github workflows


## Advanced stuff to look into
- Abstract classes
- Class decorators
- Exception handling
- Code acceleration (JITs: Numba, JAX, PyPy; Cython, F2PY)
- Creating documentation with mkdocs or Sphynx
- Pre-commits