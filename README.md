### *Tired of python's simple, short, elegant print statements?*

### *Used to program in c++ and find yourself struggling to remember python's print syntax?*

### *Do you prefer doing things the hard way even when there's an easy solution?*

### *Have I got the module for you!*

# cprint

A python module that makes c++ print syntax just work, for some reason.

## Usage

First, import the module like so:

```python
from cprint import *
```

After that, anything is possible!
*Just kidding - only one very specific and unhelpful thing is possible that wasn't possible before!*

You can now use the following syntax in python:

```python
cout << "Hello " << "World" << endl;
```

```
Hello World
```

There's a catch or two, though.

1. To actually print to the screen, `endl` must be called. For example:
```python
cout << "test";
```
This won't print anything.
However,
```python
cout << "test" << endl;
```
will print the string "test".
`endl` doesn't neet to be inline though.
```python
cout << "test";
cout << endl;
```
will also print the string "test".

2. The semicolon is not required, but encouraged. If you're going to take the time to import and use a module that is essentially useless, you should at least go the extra mile to make sure that your experience is as genuine and authentic as possible. The semicolon is the cherry on top.

## Installation

I still haven't figured out how to package and distribute python modules as of yet, so for now, just download or copy and paste the code into a file called cprint.py and import it as shown above.
